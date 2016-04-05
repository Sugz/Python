#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar and a central widget.

author: Jan Bodnar
website: zetcode.com
last edited: August 2011
"""

import sys
from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)

        exit_action = QtGui.QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(self.close)

        # statusbar = self.statusBar()
        # statusbar.showMessage('Ready')
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main Window')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
