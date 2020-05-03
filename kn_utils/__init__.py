import bpy
from bpy.props import StringProperty

from . import filelocator

bl_info = {
    "name": "Basic Utility",
    "author": "KnIfER",
    "version": (0, 2, 1),
    "blender": (2, 67, 0),
    "location": "Properties > Render",
    "description": "A simple Texture Atlas for unwrapping many objects. It creates additional UV",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/UV/TextureAtlas",
    "category": "User",
}

def register():
    bpy.utils.register_class(filelocator.TE_SimpleFileLocator)

def unregister():
    bpy.utils.unregister_class(filelocator.TE_SimpleFileLocator)

if __name__ == "__main__":
    register()