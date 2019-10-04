import sys
from PyQt5.QtWidgets import QApplication
from wpWindow import EditorWindow

app = QApplication(sys.argv)
WordProcessor = EditorWindow()
sys.exit(app.exec())
