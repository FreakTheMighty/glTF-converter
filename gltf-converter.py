import bpy
import os
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]
inputFile = argv[1]
outputFile = argv[2]

inputFilename, inputFileExtension = os.path.splitext(inputFile)

def convert(extension):
    print(extension)
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
    
    bpy.ops.export_scene.gltf(filepath=outputFile)

convert(inputFileExtension)