import sys
from PyQt5.QtWidgets import QApplication
from main.wpWindow import *

app = QApplication(sys.argv)
WordProcessor = EditorWindow()
sys.exit(app.exec())
