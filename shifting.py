from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt6.QtGui import QIcon
from random import choice
from sys import argv

class Shift(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shift")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(200,50)

        self.counter = 0

        self.main_button = QPushButton(str(self.counter),self)
        self.main_button.clicked.connect(self.changer)
        self.main_button.setStyleSheet(f"background-color:{choice(colors)};font-size:40px;font-weight:bold;color:grey;")

        self.setCentralWidget(self.main_button)

        self.show()

    def changer(self):
        self.counter += 1
        self.main_button.setText(str(self.counter))
        self.main_button.setStyleSheet(f"background-color:{choice(colors)};font-size:40px;font-weight:bold;color:grey;")

if __name__ == "__main__":
    application = QApplication(argv)
    colors_file = open("colors_file.txt")
    colors = colors_file.readlines()
    shift = Shift()
    colors_file.close()
    application.exec()