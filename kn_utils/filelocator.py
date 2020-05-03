import os
import bpy
from bpy.props import StringProperty
import subprocess

class TE_SimpleFileLocator(bpy.types.Operator):
    bl_idname = "file.simple_locator"
    bl_label = "Locate"
    
    var1 = StringProperty(default="")
    @classmethod
    def poll(cls, context): 
        return True#context.active_object is not None

    def execute(self, context):
        pathTL = self.var1
        if pathTL!="":
            print(pathTL)
            #if os.path.isfile(pathTL):
            #pathTL = os.path.dirname(pathTL)
            if os.path.exists(pathTL):
                #os.system("start explorer %s" % pathTL)
                subprocess.Popen(r'explorer /select,"%s"'%pathTL)
            else:
                print("Rorre - Dir Not Exist")
        else:
            print("Rorre - No File Parameter")
        return {'FINISHED'}

if __name__ == "__main__":
    register()

    # test call
    
    bpy.ops.file.simple_locator()