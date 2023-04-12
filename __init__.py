# Master Domain Corporation
# EdgeStore ~ This provides a way to store and recall the edge selection.
# Contributor(s): JRZ (masterjames@master-domain.net)
#

bl_info = {
    'name': 'Edge Store',
    'category': '3D View',
    'author': 'Master Domain Corp - Master James',
    'version': (1, 0),
    'blender': (3, 5, 0),
    'location': "View3D",
    'description': "Save and Restore/Set Selected Edges",
    'warning': "This will be solved in upcoming versions"
}

import bpy
from . import EdgeStore

def register():
    print("EdgeStore init")
    EdgeStore.register()


def unregister():
    print("EdgeStore Uninit")
    EdgeStore.unregister()


if __name__ == '__main__':
    register()
