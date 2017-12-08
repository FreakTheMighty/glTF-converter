# Example usage
# blender -b -P gltf-converter.py -- example/bunny.obj example/bunny.gltf

import bpy
import os
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]
inputFile = argv[0]
outputFile = argv[1]
tempscene = '/tmp/temp.blend'

inputFilename, inputFileExtension = os.path.splitext(inputFile)

def convert(extension):
    if extension == ".blend":
        bpy.ops.wm.open_mainfile(filepath=inputFile)
    elif extension == ".dae":
        bpy.ops.wm.collada_import(filepath=inputFile)
    elif extension == ".fbx":
        bpy.ops.import_scene.fbx(filepath=inputFile)
    elif extension == ".obj":
        bpy.ops.import_scene.obj(filepath=inputFile)
    else:
        sys.exit('.blend, .dae, .fbx, .obj are supported')
    
    # Hack to deal with embedded FBX media not loading
    bpy.ops.wm.save_mainfile(filepath=tempscene)
    bpy.ops.wm.open_mainfile(filepath=tempscene)
    bpy.ops.export_scene.gltf(filepath=outputFile)

convert(inputFileExtension)
