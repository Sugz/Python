#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

This program creates a menubar.

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
        exit_action = QtGui.QAction(QtGui.QIcon('Icons/Edit_Poly.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('MenuBar')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
