# Copyright 2021-2022 The glTF-Blender-IO-MSFS authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
import math

from io_scene_gltf2.io.com.gltf2_io import Node
from io_scene_gltf2.io.com.gltf2_io_extensions import Extension


class MSFSGizmo:
    bl_options = {"UNDO"}

    extension_name = "ASOBO_gizmo_object"

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("%s should not be instantiated" % cls)

    @staticmethod
    def create(gltf_scene, blender_scene, import_settings):
        """
        Create a "fake" node in the glTF scene to let the gizmo TRS get applied properly relative to the parent
        """
        nodes = gltf_scene.nodes
        for node_idx in nodes:
            node = import_settings.data.nodes[node_idx]
            # Check extensions in mesh
            if node.mesh is None:
                continue
            mesh = import_settings.data.meshes[node.mesh]
            extension = mesh.extensions.get(MSFSGizmo.extension_name)
            if extension is None:
                continue

            for gizmo_object in extension.get("gizmo_objects"):
                gizmo_type = gizmo_object.get("type")
                params = gizmo_object.get("params", {})

                scale = [1.0, 1.0, 1.0]
                if gizmo_type == "sphere":
                    scale[0] = params.get("radius")
                    scale[1] = params.get("radius")
                    scale[2] = params.get("radius")
                elif gizmo_type == "box":
                    scale[0] = params.get("length") / 2
                    scale[1] = params.get("width") / 2
                    scale[2] = params.get("height") / 2
                elif gizmo_type == "cylinder":
                    scale[0] = params.get("radius")
                    scale[1] = params.get("radius")
                    scale[2] = params.get("height")

                # Flip scale to convert from MSFS gizmo scale system
                scale = [scale[1], scale[2], scale[0]]

                placeholder_extension = {
                    "gizmo_blender_data": {
                        "road_collider": "Road"
                        in gizmo_object.get("extensions", {})
                        .get("ASOBO_tags", {})
                        .get("tags", {}),
                        "gizmo_type": gizmo_type,
                    }
                }

                # Create new placeholder node
                placeholder_node = Node(
                    camera=None,
                    children=None,
                    extensions=placeholder_extension,
                    extras=None,
                    matrix=None,
                    mesh=None,
                    name="Gizmo",
                    rotation=gizmo_object.get("rotation"),
                    scale=scale,
                    skin=None,
                    translation=gizmo_object.get("translation"),
                    weights=None,
                )

                import_settings.data.nodes.append(placeholder_node)
                if node.children is None:
                    node.children = []
                node.children.append(len(import_settings.data.nodes) - 1)

    @staticmethod
    def set_blender_data(gltf2_node, blender_object, import_settings):
        """
        Set proper gizmo properties on the blender object
        """
        if gltf2_node.extensions is None:
            return

        extension = gltf2_node.extensions.get("gizmo_blender_data")
        if extension is None:
            return

        blender_object.msfs_collision_is_road_collider = extension.get("road_collider")
        blender_object.msfs_gizmo_type = extension.get("gizmo_type")

        # Set name
        if blender_object.msfs_gizmo_type == "sphere":
            blender_object.name = "Sphere Collision"
        elif blender_object.msfs_gizmo_type == "box":
            blender_object.name = "Box Collision"
        elif blender_object.msfs_gizmo_type == "cylinder":
            blender_object.name = "Cylinder Collision"

        # The Khronos importer auto-calculates the empty display size, so we need to reset it to 1
        blender_object.empty_display_size = 1.0

    @staticmethod
    def export(nodes, blender_scene, export_settings):
        """
        Let the Khronos exporter gather the gizmo to calculate the proper TRS with the parent to make sure everything is correct,
        then remove the gizmo from the collected nodes and set the proper mesh extensions
        """
        for node in nodes:
            collisions = []  # TODO: make sure node is mesh?
            for child in list(node.children):
                blender_object = blender_scene.objects.get(
                    child.name
                )  # The glTF exporter will ALWAYS set the node name as the blender name

                if blender_object is None: # However, there are cases where the exporter creates fake nodes that don't exist in the scene
                    continue

                if (
                    blender_object.parent is None or blender_object.parent.type != "MESH"
                ):  # We only need the collision gizmos that are parented to a mesh
                    continue

                if blender_object.msfs_gizmo_type != "NONE":
                    result = {}
                    result["type"] = blender_object.msfs_gizmo_type
                    result["translation"] = child.translation
                    if child.rotation:
                        result["rotation"] = child.rotation

                    if child.scale is None: # If the scale is default, it will be exported as None which will raise an error here
                        child.scale = [1.0, 1.0, 1.0]

                    # Flip scale to match MSFS gizmo scale system
                    if export_settings["gltf_yup"]:
                        child.scale = [child.scale[2], child.scale[0], child.scale[1]]
                    else:
                        child.scale = [child.scale[1], child.scale[0], child.scale[2]]

                    # Calculate scale per gizmo type
                    scale = {}
                    if blender_object.msfs_gizmo_type == "sphere":
                        scale["radius"] = abs(child.scale[0] * child.scale[1] * child.scale[2])
                    elif blender_object.msfs_gizmo_type == "box":
                        scale["length"] = abs(child.scale[0]) * 2
                        scale["width"] = abs(child.scale[1]) * 2
                        scale["height"] = abs(child.scale[2]) * 2
                    elif blender_object.msfs_gizmo_type == "cylinder":
                        scale["radius"] = abs(child.scale[0] * child.scale[1])
                        scale["height"] = abs(child.scale[2])

                    result["params"] = scale

                    # Collision type
                    tags = ["Collision"]
                    if blender_object.msfs_collision_is_road_collider:
                        tags.append("Road")

                    result["extensions"] = {
                        "ASOBO_tags": Extension(
                            name="ASOBO_tags", extension={"tags": tags}, required=False
                        )
                    }

                    collisions.append(result)
                    node.children.remove(child)

            if collisions:
                node.mesh.extensions[MSFSGizmo.extension_name] = Extension(
                    name=MSFSGizmo.extension_name,
                    extension={"gizmo_objects": collisions},
                    required=False,
                )

            MSFSGizmo.export(node.children, blender_scene, export_settings)
