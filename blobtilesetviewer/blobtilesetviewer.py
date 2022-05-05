import tempfile
import subprocess
from krita import (DockWidget, Krita,
                   DockWidgetFactory, DockWidgetFactoryBase, QImage, QPixmap,
                   QSize, InfoObject)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QLabel, QPushButton, QWidget)


class BlobTilesetViewer(DockWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blob tileswet viewer")

        self.image_label = QLabel('')
        self.image_label.setAlignment(Qt.AlignCenter)

        self.message_label = QLabel('')

        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_button_clicked)

        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_button_clicked)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.update_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setWidget(self.widget)

        # Krita opens a dialog to ask us how to save a PNG file
        # even if we specify the settings with `InfoObject`.
        # This is why we save the image as BMP.
        self.fp = tempfile.NamedTemporaryFile(suffix='.bmp')

    def __del__(self):
        self.fp.close()

    def canvasChanged(self, canvas):
        del canvas

        self.update_thumbnail()

    def open_button_clicked(self):
        doc = Krita.instance().openDocument(self.fp.name)
        Krita.instance().activeWindow().addView(doc)

    def update_button_clicked(self):
        self.update_thumbnail()

    def update_thumbnail(self):
        if Krita.instance().activeDocument() is None:
            return

        Krita.instance().activeDocument().exportImage(self.fp.name, InfoObject())
        result = subprocess.run(['blob-tileset-generator', '-o',
                                 self.fp.name, self.fp.name])
        if result.returncode != 0:
            self.image_label.clear()
            self.message_label.setText(
                'Failed to generate a blob tileset image.')
        else:
            self.message_label.clear()
            thumbnail = QImage(self.fp.name)
            thumbnail = thumbnail.scaled(
                QSize(200, 150), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(QPixmap.fromImage(thumbnail))


Krita.instance().addDockWidgetFactory(DockWidgetFactory(
    "blobTilesetViewer", DockWidgetFactoryBase.DockRight, BlobTilesetViewer))
