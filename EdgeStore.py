import bpy, bmesh
from bpy.types import Scene

class ES_OT_edgestoresave(bpy.types.Operator):
    bl_label = 'Save/Store'
    bl_idname = 'object.edge_store_save'
    bl_space_type = 'VIEW_3D'
    bl_options = set(('REGISTER', 'UNDO'))
    bl_region_type = 'TOOLS'

    def draw(slf, ctx):
        lo = slf.layout
        lo.operator(ES_OT_edgestoresave.bl_idname)

    @classmethod
    def poll(cls, ctx):
        ao = ctx.active_object
        return (ctx.mode in {'OBJECT', 'EDIT_MESH'} and (ao is not None) and (ao.type == 'MESH'))

    def execute(slf, ctx):
        saveSetObjEdges(True, ctx)
        return {'FINISHED'}


class ES_OT_edgestoreset(bpy.types.Operator):
    bl_label = 'Set/Restore'
    bl_idname = 'object.edge_store_set'
    bl_space_type = 'VIEW_3D'
    bl_options = set(('REGISTER', 'UNDO'))
    bl_region_type = 'TOOLS'

    def draw(slf, ctx):
        lo = slf.layout
        lo.operator(ES_OT_edgestoreset.bl_idname)

    @classmethod
    def poll(cls, ctx):
        ao = ctx.active_object
        return (ctx.mode in {'OBJECT', 'EDIT_MESH'} and (ao is not None) and (ao.type == 'MESH'))

    def execute(slf, ctx):
        saveSetObjEdges(False, ctx)
        return {'FINISHED'}


def saveSetObjEdges(sav = True, ctx = bpy.context, selEdgz = None, atvEdg = None, obj = None, stor = None):
    opsObj = bpy.ops.object
    objz = ctx.view_layer.objects
    if(obj == None):
        obj = ctx.object
    if(obj == None):
        for ob in objz:
            print("No object selected, searching for first Mesh!?")
            if(ob.type == 'MESH'):
                obj = ob
                print("Found object:", obj)
                break
            else:
                print("Found object but not a mesh skipped:", ob)
    if(obj == None):
        print("No Mesh Objects found, create/select one first.")
    else:
        if(obj.type == 'MESH'):
            obj = ctx.object
            msh = bpy.ops.mesh
            if(stor == None):
                if(('edgStor' in obj) == False):
                    obj['edgStor'] = {'selEdgz': [], 'atvEdg':None}
                stor = obj['edgStor']
            if(selEdgz == None):
                if(('selEdgz' in stor) == False):
                    stor['selEdgz'] = []
                selEdgz = stor['selEdgz']
                selEdgz = selEdgz.to_list()
            if(atvEdg == None):
                if(('atvEdg' in stor) == False):
                    stor['atvEdg'] = None
                atvEdg = stor['atvEdg']
            strActv = obj
            obj.select_set(True)
            scn = ctx.scene
            selMod = tuple(scn.tool_settings.mesh_select_mode)
            selMod = {
                    (True, False, False): 'VERT', 
                    (False, True, False): 'EDGE', 
                    (False, False, True): 'FACE', 
                }[selMod]
            curMod = obj.mode
            if(curMod != 'EDIT' and selMod != 'EDGE' and sav == False):
                msh.primitive_cube_add(size = 0.1, location = (0, 0, 100) )
                swchBox = ctx.selected_objects[0]
                swchBox.name = 'swchModeBox'
                if(curMod != 'EDIT'):
                    opsObj.mode_set(mode = 'EDIT')
                msh.select_mode(type = 'EDGE')
                bpy.data.objects.remove(swchBox, do_unlink = True)
                objz.active = strActv
            else:
                curMod = obj.mode
                if(curMod != 'EDIT'):
                    opsObj.mode_set(mode = 'EDIT')
            oData = obj.data
            msh = bmesh.from_edit_mesh(oData)
            edgz = msh.edges
            if(sav == True):
                selEdgz.clear()
                for (idx, edg) in enumerate(edgz):
                    if(edg.select == True):
                        if((idx in selEdgz) == False):
                            selEdgz.append(idx)
                act = msh.select_history.active
                if(act != None):
                    atvEdg = act.index
                else:
                    atvEdg = None
                stor['selEdgz'] = selEdgz
                stor['atvEdg'] = atvEdg
                print(obj.name, "Stored Selected Edges:", selEdgz, "Active:", atvEdg)
            else:
                for ob in bpy.context.selected_objects:
                    ob.select_set(False)
                for (idx, edg) in enumerate(edgz):
                    if((idx in selEdgz) == True):
                        if(edg.select == False):
                            edg.select = True
                    else:
                        if(edg.select == True):
                            edg.select = False
                    if(atvEdg == idx):
                        msh.select_history.add(edg)
                print(obj.name, "Set Selected Edges:", selEdgz, "Active:", atvEdg)

            bmesh.update_edit_mesh(obj.data)
            if(objz.active != strActv):
                objz.active = strActv
            obj.select_set(True)
            if(selMod != 'EDGE'):
                if(obj.mode != 'EDIT'):
                    opsObj.mode_set(mode = 'EDIT')
                bpy.ops.mesh.select_mode(type = selMod)
            if(opsObj.mode != curMod):
                opsObj.mode_set(mode = curMod)


class ES_MT_EdgeStoreMenu(bpy.types.Menu):
    bl_label = "Edge Store"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(slf, ctx):
        lo = slf.layout
        lo.label(text="Edge Store", icon='WORLD_DATA')
        lo.operator(ES_OT_edgestoresave.bl_idname)
        lo.operator(ES_OT_edgestoreset.bl_idname)


def menuEdgeStore(self, context):
    #self.layout.label(text="Save Edges", icon='WORLD_DATA')
    lo = self.layout
    lo.menu(ES_MT_EdgeStoreMenu.bl_idname)


Scene.esClassez = [
    ES_MT_EdgeStoreMenu,
    ES_OT_edgestoresave,
    ES_OT_edgestoreset
]

def register():
    print("EdgeStore register")
    utls = bpy.utils
    for esCls in Scene.esClassez:
        utls.register_class(esCls)
    typs = bpy.types
    typs.VIEW3D_MT_object.append(menuEdgeStore)
    typs.VIEW3D_MT_edit_mesh_edges.append(menuEdgeStore)


def unregister():
    print("EdgeStore unregister")
    bpy.types.VIEW3D_MT_edit_mesh_edges.remove(menuEdgeStore)
    bpy.types.VIEW3D_MT_object.remove(menuEdgeStore)
    utls = bpy.utils
    for esCls in Scene.esClassez.__reversed__():
        utls.unregister_class(esCls)
