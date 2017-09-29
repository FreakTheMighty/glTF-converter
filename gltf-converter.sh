#!/bin/bash

# Example usage
# ./gltf-converter.sh example/bunny.obj example/bunny.gltf
# $0 <gltf-converter.sh>
# $1 <input> 
# $2 <output>

blender -b -P gltf-converter.py -- $0 $1 $2