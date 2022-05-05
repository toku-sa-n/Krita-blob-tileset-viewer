# Blob Tileset Viewer

Blob Tileset Viewer provides a way to check your 1x5 tileset is correctly arranged by converting it to a blob tileset and showing it in a docker.

## Requirements

You need to be able to run [`blob-tileset-generator`](https://github.com/toku-sa-n/blob-tileset-generator) on your terminal.

## Installation

Clone this project and copy the` blobtilesetviewer.desktop` and the `blobtilesetviewer` directory into the `pykrita` directory in your Krita resource folder. See [the documentation](https://docs.krita.org/en/reference_manual/resource_management.html#resource-management) for the location of the Krita resource folder.

## Usage

Open a 1x5 tileset image with Krita. If the image has the correct size, the viewer will convert your tileset and show the generated blob tileset in the viewer.

After editing your tileset image, click the `Update` button to update the blob tileset thumbnail.

When you want to open the generated blob tileset image, click the `Open` button. The viewer will open the blob tileset image, which the viewer saves in a temporary file, but you can still export it.

## License

All files are licensed under GNU General Public License v3.0. See [LICENSE](https://github.com/toku-sa-n/Krita-blob-tileset-viewer/blob/main/LICENSE).
