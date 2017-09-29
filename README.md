# glTF converter

Based on the ideas of [2gltf2](https://github.com/ux3d/2gltf2). I wasn't able to get their repo working on MacOS and it was missing installation instructions.

Please note that the current version is highly experimental. Do not use this in your production workflow as of now. 

## General

Uses [Blender](https://www.blender.org/download/) and [glTF Blender Exporter](https://github.com/KhronosGroup/glTF-Blender-Exporter).

## General installation instructions
Installation instructions can be found on [glTF Blender Exporter Scripts](https://github.com/KhronosGroup/glTF-Blender-Exporter/tree/master/scripts).

## Specific installation instructions for Mac
Copy `io_scene_gltf2` from [glTF Blender Exporter Addons](https://github.com/KhronosGroup/glTF-Blender-Exporter/tree/master/scripts/addons).

Open Blender and see if it starts correctly. If you do these adjustments before opening Blender you will likely run into a verification hash issue that MacOS does on every install.

Select `Blender` and right click `show package contents -> Contents -> Resources -> 2.79 -> scripts -> addons`.

Place `io_scene_gltf2` in there. Open `Blender -> File -> User preferences -> Add-ons tab -> Toggle on Import-Export: glTF 2.0 format > Save user settings > Refresh`.

You should now be able to export scenes as glTF from the dropdown menu `File -> glTF 2.0 (.glb)` and `glTF 2.0 (.gltf)`.

## Exporting
Remove the default `cube` scene by following the [instructions](https://blender.stackexchange.com/questions/5574/how-to-remove-the-default-cube).

## Validate
To validate the exported `.gltf` and `.bin` select both and drag and drop them into the [glTF Viewer](https://gltf-viewer.donmccurdy.com/).
