import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class BSWord(QMainWindow):
    def __init__(self):
        super(BSWord, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(25)
        self.font_size_box = QSpinBox()
        self.create_tool_bar()
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = QMenu('File', self)
        menu_bar.addMenu(file_menu)
        Edit_menu = QMenu('Edit', self)
        menu_bar.addMenu(Edit_menu)
        View_menu = QMenu('View', self)
        menu_bar.addMenu(View_menu)

        self.setMenuBar(menu_bar)

    def create_tool_bar(self):
        tool_bar = QToolBar()

        undo_action = QAction(QIcon('undo.png'), 'Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        redo_action = QAction(QIcon('redo.png'), 'redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        cut_action = QAction(QIcon('cut.png'), 'cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        copy_action = QAction(QIcon('copy.png'), 'copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        paste_action = QAction(QIcon('paste.png'), 'paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()



        self.font_size_box.setValue(20)
        self.font_size_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_size_box)

        self.addToolBar(tool_bar)

    def set_font_size(self):
        value = self.font_size_box.value()
        self.editor.setFontPointSize(value)

app = QApplication(sys.argv)
window = BSWord()
window.show()
sys.exit(app.exec_())
