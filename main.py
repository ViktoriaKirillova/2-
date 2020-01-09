from piano_ui import Ui_Form
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3s()
        self.A.clicked.connect(self.player[0].play)
        self.B.clicked.connect(self.player[1].play)
        self.C.clicked.connect(self.player[2].play)
        self.D.clicked.connect(self.player[3].play)
        self.E.clicked.connect(self.player[4].play)
        self.F.clicked.connect(self.player[5].play)
        self.G.clicked.connect(self.player[6].play)

    def load_mp3s(self):
        media = [QtCore.QUrl.fromLocalFile(i) for i in
                 [t for t in os.listdir() if '.mp3' in t]]
        media.sort()
        content = [QtMultimedia.QMediaContent(i) for i in media]
        self.player = [QtMultimedia.QMediaPlayer() for _ in content]
        for i in range(len(content)):
            self.player[i].setMedia(content[i])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.player[2].play()
        elif event.key() == Qt.Key_F:
            self.player[3].play()
        elif event.key() == Qt.Key_G:
            self.player[4].play()
        elif event.key() == Qt.Key_H:
            self.player[5].play()
        elif event.key() == Qt.Key_J:
            self.player[6].play()
        elif event.key() == Qt.Key_K:
            self.player[0].play()
        elif event.key() == Qt.Key_L:
            self.player[1].play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
