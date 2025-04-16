import bpy
import json
import os

bl_info = {
    "name": "Export Vertices To THREE.JS",
    "author": "Class Outside",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Exports vertices to Vector3 in a JavaScript file.",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

class ExportVerticesOperator(bpy.types.Operator):
    bl_idname = "export.vertices_js"
    bl_label = "Export Vertices to JS"
    bl_description = "Export vertices as a JavaScript file"

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')
    filter_glob: bpy.props.StringProperty(default="*.js", options={'HIDDEN'})
    use_selection: bpy.props.BoolProperty(name="Export Selected", description="Export only selected objects", default=True)
    closed: bpy.props.BoolProperty(name="Closed Curve", description="Indicate if the curve is closed", default=False)

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def invoke(self, context, event):
        selected_objects = bpy.context.selected_objects
        if len(selected_objects) != 1:
            bpy.context.window_manager.popup_menu(draw_error_message, title="Export Error", icon='ERROR')
            return {'CANCELLED'}

        default_path = bpy.data.filepath
        if default_path:
            default_name = os.path.splitext(os.path.basename(default_path))[0] + ".js"
            self.filepath = os.path.join(os.path.dirname(default_path), default_name)
        else:
            self.filepath = ".js"
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        export_vertices(self.filepath, self.use_selection, self.closed)
        return {'FINISHED'}

def export_vertices(filepath, use_selection, closed):
    points = []

    selected_objects = bpy.context.selected_objects if use_selection else bpy.context.scene.objects

    for obj in selected_objects:
        if obj.type == 'MESH':
            for vertex in obj.data.vertices:
                x = vertex.co.x
                y = vertex.co.z 
                z = -vertex.co.y
                points.append(f"new THREE.Vector3({x}, {y}, {z})")

    js_content = "import * as THREE from 'three';\n"
    js_content += "export const curve = [\n"
    js_content += ",\n".join(f"    {p}" for p in points)
    js_content += "\n];\n"
    js_content += f"export const closed = {str(closed).lower()};\n"

    # Change the file extension to .js
    filepath = os.path.splitext(filepath)[0] + ".js"

    with open(filepath, 'w') as file:
        file.write(js_content)
def draw_error_message(self, context):
    self.layout.label(text="Please select only one object to export.")

def menu_func_export(self, context):
    self.layout.operator(ExportVerticesOperator.bl_idname, text="Export Vertices to JS")

def register():
    bpy.utils.register_class(ExportVerticesOperator)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportVerticesOperator)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
