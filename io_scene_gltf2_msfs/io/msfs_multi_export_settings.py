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
        name="Keep original",
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
        name="Textures",
        description="Pasta para colocar arquivos de textura em. Em relação ao arquivo .gLTF",
        default="",
    )

    ## Copyright string UI
    export_copyright: bpy.props.StringProperty(
        name="Copyright",
        description="Direitos e condições legais para o modelo",
        default="",
    )

    ## Remember export settings check
    remember_export_settings: bpy.props.BoolProperty(
        name="Remember Export Settings",
        description="Armazene as configurações de exportação GLTF no projeto Blender.",
        default=False
    )

    ## MSFS extensions Check
    def msfs_enable_msfs_extension_update(self, context):
        props = bpy.context.scene.msfs_exporter_properties
        settings = context.scene.msfs_multi_exporter_settings
        props.enabled = settings.enable_msfs_extension

    enable_msfs_extension: bpy.props.BoolProperty(
        name='Use Microsoft Flight Simulator Extensions',
        description='Ativar extensões do simulador de vôo do Microsoft',
        default=True,
        update=msfs_enable_msfs_extension_update
    )

    ## Asobo Unique ID Check
    def msfs_use_unique_id_extension_update(self, context):
        props = bpy.context.scene.msfs_exporter_properties
        settings = context.scene.msfs_multi_exporter_settings
        props.use_unique_id = settings.use_unique_id
    
    use_unique_id: bpy.props.BoolProperty(
        name='Use ASOBO Unique ID Extension',
        description='Ativar extensão de identificação exclusiva do ASOBO',
        default=True,
        update=msfs_use_unique_id_extension_update
    )
    
    #### Include Options
    ## Export Selected Only Check - TODO : See if this works
    use_selected: bpy.props.BoolProperty(
        name="Selected Objects", 
        description= (
            "Exportar objetos selecionados apenas. "
            "Desativado para o uso do multiexporter (precisa ser sempre verificado)"
        ), 
        default=True
    )

    ## Export Visible Only Check - TODO : See if this works
    use_visible: bpy.props.BoolProperty(
        name="Visible Objects", 
        description="Exportar objetos visíveis apenas", 
        default=False
    )

    ## Export Renderable Objects Check
    use_renderable: bpy.props.BoolProperty(
        name="Renderable Objects",
        description="Apenas objetos renderizáveis de exportação",        
        default=False,
    )

    ## Export Active Collection Check
    use_active_collection: bpy.props.BoolProperty(
        name="Active Collection",
        description="Exportar objetos apenas na coleção ativa",
        default=False,
    )

    use_active_scene: bpy.props.BoolProperty(
        name="Active Scene",
        description="Exportar cena ativa apenas",
        default=False,
    )
    
    ## Export Custom Propreties Check
    export_extras: bpy.props.BoolProperty(
        name="Custom Properties",
        description="Exportar propriedades personalizadas como extras GLTF",
        default=False,
    )
    
    ## Export Camera Check
    export_cameras: bpy.props.BoolProperty(
        name="Cameras", 
        description="Câmeras de exportação", 
        default=False
    )

    ## Export Punctual Lights Check
    export_lights: bpy.props.BoolProperty(
        name="Punctual Lights",
        description= (
            "Exportar luzes direcionais, de ponto e ponto. "
            "Usa 'Khr_lights_punctual' GLTF Extensão"
        ),
        default=True,
    )
        
    #### Transform Options
    ## Y Up Check
    export_yup: bpy.props.BoolProperty(
        name="+Y Up", description="Exportar usando a Convenção GLTF, +Y para cima ", default=True
    )

    #### Geometry options
    ## Export Apply Modifiers Check
    export_apply: bpy.props.BoolProperty(
        name="Apply Modifiers",
        description=(
            "Aplique modificadores (excluindo armaduras) aos objetos de malha. "
            "AVISO: impede as chaves de forma de exportação"
        ),
        default=False,
    )
    
    ## Export UVs Check
    export_texcoords: bpy.props.BoolProperty(
        name="UVs",
        description="exportarUVs (coordenadasDeTextura)ComMalhas",
        default=True,
    )

    ## Export Normals Check
    export_normals: bpy.props.BoolProperty(
        name="Normals", description="Exportar normais de vértices com malhas", default=True
    )

    ## Export Tangents Check
    export_tangents: bpy.props.BoolProperty(
        name="Tangents", description="Exportar tangentes de vértices com malhas", default=False
    )

    ## Export Vertex Colors Check
    export_colors: bpy.props.BoolProperty(
        name="Vertex Colors",
        description="Exportar cores de vértices com malhas",
        default=True,
    )
    
    ## Export Loose Edge Check
    use_mesh_edges: bpy.props.BoolProperty(
        name="Loose Edges",
        description=(
            "Exportar bordas soltas como linhas, usando o material do primeiro slot de material"
        ),
        default=False,
    )
    
    ## Export Loose Points Check
    use_mesh_vertices: bpy.props.BoolProperty(
        name="Loose Points",
        description=(
            "Exportar pontos soltos como pontos GLTF, usando o material do primeiro material SLOt"
        ),
        default=False,
    )
    
    ## Export materials option Check
    export_materials: bpy.props.EnumProperty(
        name="Materials",
        items=(
            ("EXPORT", "Export", "Export all materials used by included objects"),
            (
                "PLACEHOLDER",
                "Placeholder",
                "Do not export materials, but write multiple primitive groups per mesh, keeping material slot information",
            ),
            (
                "NONE",
                "No export",
                "Não exporte materiais e combine grupos primitivos de malha, perdendo informações de slot de material",
            ),
        ),
        description="Materiais de exportação",
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

    ## Draco compression check 
    export_draco_mesh_compression_enable: bpy.props.BoolProperty(
        name='Draco mesh compression',
        description=(
            "Comprimir malha usando Draco. "
            "Aviso: a compressão Draco não é suportada no Microsoft Flight Simulator"
        ),
        default=False
    )

    ## Draco compression level
    export_draco_mesh_compression_level: bpy.props.IntProperty(
        name='Compression level',
        description='Nível de compressão (0 = a maioria da velocidade, 6 = mais compressão, valores mais altos atualmente não suportados)',
        default=6,
        min=0,
        max=10
    )

    ## Draco compression position quatization
    export_draco_position_quantization: bpy.props.IntProperty(
        name='Position quantization bits',
        description='Bits de quantização para valores de posição (0 = sem quantização)',
        default=14,
        min=0,
        max=30
    )

    ## Draco compression normal quatization
    export_draco_normal_quantization: bpy.props.IntProperty(
        name='Normal quantization bits',
        description='Bits de quantização para valores normais (0 = sem quantização)',
        default=10,
        min=0,
        max=30
    )

    ## Draco compression texture coordinate quatization
    export_draco_texcoord_quantization: bpy.props.IntProperty(
        name='Texcoord quantization bits',
        description='Bits de quantização para valores de coordenadas de textura (0 = sem quantização)',
        default=12,
        min=0,
        max=30
    )

    ## Draco compression vertex color quatization
    export_draco_color_quantization: bpy.props.IntProperty(
        name='Color quantization bits',
        description='Bits de quantização para valores de cor (0 = sem quantização)',
        default=10,
        min=0,
        max=30
    )

    ## Draco compression generic quatization
    export_draco_generic_quantization: bpy.props.IntProperty(
        name='Generic quantization bits',
        description='Bits de quantização para valores de coordenadas genéricas, como pesos ou articulações (0 = sem quantização)',
        default=12,
        min=0,
        max=30
    )

    #### Animation Options
    ## Use Current Frame Check
    export_current_frame: bpy.props.BoolProperty(
        name="Use Current Frame",
        description="Exportar a cena no quadro de animação atual",
        default=False,
    )
    
    ##* Export Animation Options Check
    export_animations: bpy.props.BoolProperty(
        name="Animations",
        description="Exporta ações ativas e rastreia da NLA como animações GLTF",
        default=True,
    )

    ## Limit to Playback Range Check
    export_frame_range: bpy.props.BoolProperty(
        name="Limit to Playback Range",
        description="CLIPS Animações para a linha de reprodução selecionada",
        default=True,
    )

    ## Sampling Rate Slider (1-120)
    export_frame_step: bpy.props.IntProperty(
        name="Sampling Rate",
        description="Com que frequência avaliar valores animados (em quadros)",
        default=1,
        min=1,
        max=120,
    )

    ## Always Sample Animations Check
    export_force_sampling: bpy.props.BoolProperty(
        name="Always Sample Animations",
        description="Aplique amostragem a todas as animações",
        default=False,
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

    ## Export NLA strips merged animation name
    export_nla_strips_merged_animation_name: bpy.props.StringProperty(
        name='Merged Animation Name',
        description=(
            "Nome da animação única GLTF a ser exportada"
        ),
        default='Animation'
    )

    ## Optimize Animation Size Check
    optimize_animation_size: bpy.props.BoolProperty(
        name="Optimize Animation Size",
        description=(
            "Reduza o tamanho do arquivo de exportação removendo os quadros -chave duplicados"
            "Pode causar problemas com a animação escalonada"
        ),
        default=True,
    )

    ## Export all armature actions check
    export_all_armature_actions: bpy.props.BoolProperty(
        name="Export all Armature Actions",
        description=(
            "Exportar todas as ações, ligadas a uma única armadura. "
            "AVISO: A opção não suporta exportações, incluindo várias armaduras"
        ),
        default=True
    )

    ## Export Shape Keys check
    export_morph: bpy.props.BoolProperty(
        name='Shape Keys',
        description=(
            "Chaves de forma de exportação (alvos morph). "
            "AVISO: Os alvos morph não são interpretados pelo Microsoft Flight Simulator."
        ),
        default=False
    )

    ## Export Shape Keys Normals check
    export_morph_normal: bpy.props.BoolProperty(
        name='Shape Key Normals',
        description=(
            "Exportar normais de vértices com teclas de forma (alvos morph). "
            "AVISO: Os alvos morph não são interpretados pelo Microsoft Flight Simulator."
        ),
        default=False
    )

    ## Export Shape Keys Tangent check
    export_morph_tangent: bpy.props.BoolProperty(
        name='Shape Key Tangents',
        description=(
            "Exportar tangentes de vértices com teclas de forma (alvos morph). "
            "Aviso: os alvos morph não são interpretados pelo Microsoft Flight Simulator."
        ),
        default=False
    )
    
    ##* Skinning Option Check
    export_skins: bpy.props.BoolProperty(
        name="Skinning", description="Exportar dados de pele (armadura)", default=True
    )

    ## Export All Bone Influences Check
    export_all_influences: bpy.props.BoolProperty(
        name="Include All Bone Influences",
        description="Permitir > 4 influências conjuntas de vértice. Os modelos podem aparecer incorretamente em muitos visualizadores. ",
        default=False,
    )

    ## Deformation Bones Only Check
    export_def_bones: bpy.props.BoolProperty(
        name="Export Deformation Bones Only",
        description="Exportar ossos de deformação apenas (e os ossos necessários para a hierarquia)",
        default=False,
    )

    ## Export displacement Check (works with Blender < 3.3 versions)
    export_displacement: bpy.props.BoolProperty(
        name="Displacement Textures (EXPERIMENTAL)",
        description=(
            "Experimental: texturasDeDeslocamentoDeExportação."
            "usaAExtensãoGltfIncompleta "'khrMaterialsDisplacement'". "
            "AVISO: funciona com Blender < 3.3 versions"
        ),
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
        layout.prop(settings, "remember_export_settings")
        

class MSFS_PT_MSFSExporterExtensionPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = ""
    bl_parent_id = "MSFS_PT_MultiExporter"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Microsoft Flight Simulator Extensions", icon='TOOL_SETTINGS')

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.prop(settings, 'enable_msfs_extension', text="Enabled")
        if settings.enable_msfs_extension:
            layout.prop(settings, 'use_unique_id', text="Enable ASOBO Unique ID extension")


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

        col1 = layout.column(heading="", align=True)
        col1.prop(settings, "use_selected") ## To use the MultiExporter panel, it's important to have use selected to True
        col1.enabled = False
        col2 = layout.column(heading="Limit to", align=True)
        col2.prop(settings, "use_visible")
        col2.prop(settings, "use_renderable")
        col2.prop(settings, "use_active_collection")
        col2.prop(settings, "use_active_scene")

        col2 = layout.column(heading="Data", align=True)
        col2.prop(settings, "export_extras")
        col2.prop(settings, "export_cameras")
        col2.prop(settings, "export_lights")
 
 
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

class MSFS_PT_export_geometry_compression(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Compression"
    bl_parent_id = "MSFS_PT_export_geometry"
    bl_options = {'DEFAULT_CLOSED'}

    def __init__(self):
        from io_scene_gltf2.io.com import gltf2_io_draco_compression_extension
        self.is_draco_available = gltf2_io_draco_compression_extension.dll_exists(quiet=True)

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw_header(self, context):
        settings = context.scene.msfs_multi_exporter_settings
        self.layout.prop(settings, "export_draco_mesh_compression_enable", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.active = settings.export_draco_mesh_compression_enable
        layout.prop(settings, 'export_draco_mesh_compression_level')

        col = layout.column(align=True)
        col.prop(settings, 'export_draco_position_quantization', text="Quantize Position")
        col.prop(settings, 'export_draco_normal_quantization', text="Normal")
        col.prop(settings, 'export_draco_texcoord_quantization', text="Tex Coord")
        col.prop(settings, 'export_draco_color_quantization', text="Color")
        col.prop(settings, 'export_draco_generic_quantization', text="Generic")

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
        if settings.export_nla_strips is False:
            layout.prop(settings, 'export_nla_strips_merged_animation_name')
        layout.prop(settings, "optimize_animation_size")
        if (bpy.app.version > (3, 3, 0)):
            layout.prop(settings, "export_all_armature_actions")
        else:
            layout.prop(settings, 'export_def_bones')


class MSFS_PT_export_animation_shapekeys(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Shape Keys"
    bl_parent_id = "MSFS_PT_export_animation"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.msfs_multi_exporter_current_tab == "SETTINGS"

    def draw_header(self, context):
        settings = context.scene.msfs_multi_exporter_settings
        self.layout.prop(settings, "export_morph", text="")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        settings = context.scene.msfs_multi_exporter_settings

        layout.active = settings.export_morph

        layout.prop(settings, 'export_morph_normal')
        col = layout.column()
        col.active = settings.export_morph_normal
        col.prop(settings, 'export_morph_tangent')


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

        if bpy.app.version > (3, 3, 0):
            row = layout.row()
            row.prop(settings, 'export_def_bones')
            row.active = settings.export_force_sampling
            if settings.export_force_sampling is False and settings.export_def_bones is True:
                layout.label(text="Export only deformation bones is not possible when not sampling animation")
        


def register():
    bpy.types.Scene.msfs_multi_exporter_settings = bpy.props.PointerProperty(
        type=MSFS_MultiExporterSettings
    )
