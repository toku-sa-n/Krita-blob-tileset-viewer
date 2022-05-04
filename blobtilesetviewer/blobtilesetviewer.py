from krita import (DockWidget, Krita,
                   DockWidgetFactory, DockWidgetFactoryBase)


class BlobTilesetViewer(DockWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blob tileswet viewer")

    def canvasChanged(self, canvas):
        pass


Krita.instance().addDockWidgetFactory(DockWidgetFactory(
    "blobTilesetViewer", DockWidgetFactoryBase.DockRight, BlobTilesetViewer))
