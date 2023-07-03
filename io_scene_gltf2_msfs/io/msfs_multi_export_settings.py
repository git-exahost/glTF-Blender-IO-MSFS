# glTF-Blender-IO-MSFS
# Copyright 2018-2021 The glTF-Blender-IO authors
# Copyright 2022 The glTF-Blender-IO-MSFS authors
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


class MSFS_MultiExporterSettings(bpy.types.PropertyGroup):
    #### General Options
    ## keep original texture option Check
    export_keep_originals: bpy.props.BoolProperty(
        name="Manter original",
        description=(
            "Mantenha os arquivos de texturas originais, se possível. "
            "Aviso: se você usar mais de uma textura, "
            "Onde o padrão PBR requer apenas um, apenas uma textura será usada. "
            "Isso pode levar a resultados inesperados"
        ),
        default=False,
    )
    ## Texture directory path
    export_texture_dir: bpy.props.StringProperty(
        name="Texturas",
        description="Pasta para colocar arquivos de textura em. Em relação ao arquivo .gLTF",
        default="",
    )

    ## Copyright string UI
    export_copyright: bpy.props.StringProperty(
        name="Copyright",
        description="Direitos e condições legais para o modelo",
        default="",
    )
   
    ## Asobo Unique ID Check
    use_unique_id: bpy.props.BoolProperty(
        name='Use a extensão de identificação única do ASOBO',
        description='Use a extensão de identificação exclusiva do ASOBO',
        default=True
    )
    
    #### Include Options
    ## Export Visible Only Check - TODO : See if this works
    use_visible: bpy.props.BoolProperty(
        name="Objetos visíveis", description="Exportar objetos visíveis apenas", default=False
    )

    ## Export Renderable Objects Check
    use_renderable: bpy.props.BoolProperty(
        name="Objetos renderizáveis",
        description="exportarObjetosRenderizáveisApenas",
        default=False,
    )

    ## Export Active Collection Check
    use_active_collection: bpy.props.BoolProperty(
        name="Coleção ativa",
        description="Exportar objetos apenas na coleção ativa",
        default=False,
    )
    
    ## Export Custom Propreties Check
    export_extras: bpy.props.BoolProperty(
        name="Propriedades personalizadas",
        description="Exportar propriedades personalizadas como extras GLTF",
        default=False,
    )
    
    ## Export Camera Check
    export_cameras: bpy.props.BoolProperty(
        name="Cameras", description="Câmeras de exportação", default=False
    )

    ## Export Punctual Lights Check
    export_lights: bpy.props.BoolProperty(
        name="Luzes pontuais",
        description="Exportar luzes direcionais, pontuais e manchas. "
        'Uses "KHR_lights_punctual" glTF extension',
        default=True,
    )
        
    #### Transform Options
    ## Y Up Check
    export_yup: bpy.props.BoolProperty(
        name="+Y Up", description="Export using glTF convention, +Y up", default=True
    )

    #### Geometry options
    ## Export Apply Modifiers Check
    export_apply: bpy.props.BoolProperty(
        name="Aplique modificadores",
        description="Aplicar modificadores (excluindo armaduras) aos objetos de malha -"
        "Aviso: evita as chaves de forma de exportação",
        default=True,
    )
    
    ## Export UVs Check
    export_texcoords: bpy.props.BoolProperty(
        name="UVs",
        description="Exportar UVs (coordenadas de textura) com malhas",
        default=True,
    )

    ## Export normals Check
    export_normals: bpy.props.BoolProperty(
        name="Normals", description="Exportar normais de vértices com malhas", default=True
    )

    ## Export tangents Check
    export_tangents: bpy.props.BoolProperty(
        name="Tangents", description="Não funciona no MSFS, gerra erro de tangentes...", 
        default=False
    )

    ## Export Vertex Colors Check
    export_colors: bpy.props.BoolProperty(
        name="Cores de vértices",
        description="Exportar cores de vértices com malhas.",
        default=False,
    )
    
    ## Export Loose Edge Check
    use_mesh_edges: bpy.props.BoolProperty(
        name="Bordas soltas",
        description=(
            "Exportar bordas soltas como linhas, usando o material do primeiro slot de material"
        ),
        default=False,
    )
    
    ## Export Loose Points Check
    use_mesh_vertices: bpy.props.BoolProperty(
        name="Pontos soltos",
        description=(
            "Exportar pontos soltos como pontos GLTF, usando o material do primeiro slot de material"
        ),
        default=False,
    )
    
    ## Export materials option Check
    export_materials: bpy.props.EnumProperty(
        name="Materials",
        items=(
            ("EXPORT", "Export", "Exportar todos os materiais usados por objetos incluídos"),
            (
                "PLACEHOLDER",
                "Placeholder",
                "Não exporte materiais, mas escreva vários grupos primitivos por malha, mantendo as informações do slot do material",
            ),
            (
                "NONE",
                "No export",
                "Não exporte materiais e combine grupos primitivos de malha, perdendo informações de slot de material",
            ),
        ),
        description="Materiais de exportação ",
        default="EXPORT",
    )

    ## Export Image format UI (Auto/Jpeg/None)
    export_image_format: bpy.props.EnumProperty(
        name="Images",
        items=(
            (
                "AUTO",
                "Automatic",
                "Salve PNGs como PNGs e JPEGs como JPEGs. "" Se não, use png",
            ),
            (
                "JPEG",
                "JPEG Format (.jpg)",
                "Salve imagens como jpegs. (Imagens que precisam de alfa são salvas como PNGs.) "
                "Esteja ciente de uma possível perda de qualidade",
            ),
            ("NONE", "None", "Don't export images"),
        ),
        description=(
            "Formato de saída para imagens. O PNG é sem perdas e geralmente preferido, mas o JPEG pode ser preferível para a Web "
            "Aplicativos devido ao tamanho menor do arquivo.Alternativamente, eles podem ser omitidos se não forem necessários"
        ),
        default="AUTO",
    )

    #### Animation Options
    ## Use Current Frame Check
    export_current_frame: bpy.props.BoolProperty(
        name="Use o quadro atual",
        description="Exportar a cena no quadro de animação atual",
        default=False,
    )
    
    ##* Export Animation Options Check
    export_animations: bpy.props.BoolProperty(
        name="Animações",
        description="Exporta ações ativas e rastreia da NLA como animações GLTF",
        default=True,
    )

    ## Limit to Playback Range Check
    export_frame_range: bpy.props.BoolProperty(
        name="Limite para a faixa de reprodução",
        description="CLIPS Animações para a linha de reprodução selecionada",
        default=True,
    )

    ## Sampling Rate Slider (1-120)
    export_frame_step: bpy.props.IntProperty(
        name="Taxa de amostragem",
        description="Com que frequência avaliar valores animados (em quadros)",
        default=1,
        min=1,
        max=120,
    )

    ## Always Sample Animations Check
    export_force_sampling: bpy.props.BoolProperty(
        name="Sempre amostra de animações",
        description="Aplique amostragem a todas as animações",
        default=True,
    )

    ## Group by NLA Track Check
    export_nla_strips: bpy.props.BoolProperty(
        name="Group by NLA Track",
        description=(
            "Quando estão em várias ações, tornam -se parte da mesma animação GLTF se "
            "Eles são empurrados para as faixas da NLA com o mesmo nome. "
            "Quando está fora, todas as ações atualmente atribuídas se tornam uma animação GLTF"
        ),
        default=True,
    )

    ## Optimize Animation Size Check
    optimize_animation_size: bpy.props.BoolProperty(
        name="Otimize o tamanho da animação",
        description=(
            "Reduza o tamanho do arquivo de exportação removendo os quadros -chave duplicados"
            "Pode causar problemas com a animação escalonada"
        ),
        default=True,
    )
    
    ## Deformation Bones Only Check
    export_def_bones: bpy.props.BoolProperty(
        name="Exportar ossos de deformação apenas",
        description="Apenas ossos de deformação de exportação (e os ossos necessários para a hierarquia)",
        default=False,
    )

    ##* Skinning Option Check
    export_skins: bpy.props.BoolProperty(
        name="Skinning", description="Exportação de pele (armature) data", default=True
    )

    ## Export All Bone Influences Check
    export_all_influences: bpy.props.BoolProperty(
        name="Inclua todas as influências ósseas",
        description="ALlow> 4 influências conjuntas de vértice.Os modelos podem aparecer incorretamente em muitos espectadores",
        default=False,
    )

    export_displacement: bpy.props.BoolProperty(
        name="Texturas de deslocamento (EXPERIMENTAL)",
        description="EXPERIMENTAL: Export displacement textures. "
        'Uses incomplete "KHR_materials_displacement" glTF extension',
        default=False,
    )
    


class MSFS_PT_export_main(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = ""
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"HIDE_HEADER"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.prop(settings, "export_keep_originals")
        if settings.export_keep_originals is False:
            layout.prop(settings, "export_texture_dir", icon="FILE_FOLDER")

        layout.prop(settings, "export_copyright")
        layout.prop(settings, "use_unique_id")


class MSFS_PT_export_include(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Include"
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        col = layout.column(heading="Limit to", align=True)
        col.prop(settings, "use_visible")
        col.prop(settings, "use_renderable")
        col.prop(settings, "use_active_collection")

        col = layout.column(heading="Data", align=True)
        #col.prop(settings, "export_extras")
        col.prop(settings, "export_cameras")
        col.prop(settings, "export_lights")
 
 
class MSFS_PT_export_transform(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Transform"
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.prop(settings, "export_yup")


class MSFS_PT_export_geometry(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Geometry"
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.prop(settings, "export_apply")
        layout.prop(settings, "export_texcoords")
        layout.prop(settings, "export_normals")
        col = layout.column()
        col.active = settings.export_normals
        col.prop(settings, "export_tangents")
        layout.prop(settings, "export_colors")

        col = layout.column()
        col.prop(settings, "use_mesh_edges")
        col.prop(settings, "use_mesh_vertices")

        layout.prop(settings, "export_materials")
        col = layout.column()
        col.active = settings.export_materials == "EXPORT"
        col.prop(settings, "export_image_format")


class MSFS_PT_export_animation(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Animation"
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.prop(settings, "export_current_frame")


class MSFS_PT_export_animation_export(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Animation"
    bl_parent_id = "MSFS_PT_export_animation"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw_header(self, context):
        settings = context.scene.msfs_multi_exporter_settings
        self.layout.prop(settings, "export_animations", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.active = settings.export_animations

        layout.prop(settings, "export_frame_range")
        layout.prop(settings, "export_frame_step")
        layout.prop(settings, "export_force_sampling")
        layout.prop(settings, "export_nla_strips")
        layout.prop(settings, "optimize_animation_size")

        row = layout.row()
        row.active = settings.export_force_sampling
        row.prop(settings, "export_def_bones")
        if (
            settings.export_force_sampling is False
            and settings.export_def_bones is True
        ):
            layout.label(
                text="Export only deformation bones is not possible when not sampling animation"
            )


class MSFS_PT_export_animation_skinning(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Skinning"
    bl_parent_id = "MSFS_PT_export_animation"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw_header(self, context):
        settings = context.scene.msfs_multi_exporter_settings
        self.layout.prop(settings, "export_skins", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.active = settings.export_skins
        layout.prop(settings, "export_all_influences")


def register():
    bpy.types.Scene.msfs_multi_exporter_settings = bpy.props.PointerProperty(
        type=MSFS_MultiExporterSettings
    )
