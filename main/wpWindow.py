from main.WordProcessor import Ui_WordProcessor
from main.spellchecker import spellcheck
from PyQt5 import QtWidgets

class EditorWindow(QtWidgets.QMainWindow,Ui_WordProcessor):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        '''File Menu'''

        self.actionNew_File.triggered.connect(self.newFile) 
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionExit.triggered.connect(self.exitWP)

        '''Edit Menu'''
        self.actionCopy.triggered.connect(self.copyText)
        self.actionCut.triggered.connect(self.cutText)
        self.actionPaste.triggered.connect(self.pasteText)

        '''Format Menu'''
        self.actionFont.triggered.connect(self.setTextFont)
        self.actionColor.triggered.connect(self.setColor)

        '''Buttons'''
        self.pushButton.clicked.connect(self.checkText)
        self.pushButton_2.clicked.connect(self.notAvailable)
        self.pushButton_5.clicked.connect(self.notAvailable)
        self.pushButton_6.clicked.connect(self.notAvailable)
        self.show()
    
    def newFile(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
    
    def openFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self,'open file')
        if name[0]:
            file = open(name[0],'r')
        with file:
            data = file.read()
            self.textEdit.setText(data)

    def saveFile(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save File')
        if filename[0]:
            file=open(filename[0],'w')
            with file:
                data = self.textEdit.toPlainText()
                file.write(data)

                QtWidgets.QMessageBox.about(self,'Save File',"File Saved Successfully")
    
    def exitWP(self):
        exit()
    
    def copyText(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
    
    def pasteText(self):
        self.textEdit.append(self.copiedText)
    
    def cutText(self): 
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.textEdit.cut()
    
    def setTextFont(self):
        font,flag =  QtWidgets.QFontDialog.getFont()
        if flag:
            self.textEdit.setCurrentFont(font)
            self.textEdit_2.setCurrentFont(font)
        

    def setColor(self):
        color = QtWidgets.QColorDialog.getColor()
        self.textEdit.setTextColor(color)
    spell=spellcheck()

    def checkText(self):
        self.textEdit_2.clear()
        text = self.textEdit.toPlainText()
        text = text.split('\n')
        cnt = 0
        for line in text:
            cnt+=1
            errors = self.spell.Scheck(line)
            if errors:
                self.textEdit_2.append('Line'+str(cnt)+' : '+', '.join(errors))


    def notAvailable(self):
        QtWidgets.QMessageBox.about(self,'Error','Function currently unavailable.')



'''
Future Work:

Implementation of suggestion for misspelled words.
Autorcorrect the lines 
Ignore the errors
Add to dictionary

'''
