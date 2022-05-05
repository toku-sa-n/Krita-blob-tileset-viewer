import tempfile
from krita import (DockWidget, Krita,
                   DockWidgetFactory, DockWidgetFactoryBase)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QWidget)


class BlobTilesetViewer(DockWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blob tileswet viewer")

        self.image_label = QLabel('')
        self.image_label.setAlignment(Qt.AlignCenter)

        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_button_clicked)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.open_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setWidget(self.widget)

        self.fp = tempfile.NamedTemporaryFile()

    def __del__(self):
        self.fp.close()

    def canvasChanged(self, canvas):
        pass

    def open_button_clicked(self):
        pass


Krita.instance().addDockWidgetFactory(DockWidgetFactory(
    "blobTilesetViewer", DockWidgetFactoryBase.DockRight, BlobTilesetViewer))
