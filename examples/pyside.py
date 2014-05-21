#!/usr/bin/env python

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.resize(200, 120)
window.setWindowTitle("My Application")

quit = QtGui.QPushButton("Quit", window)
quit.clicked.connect(app.quit)

window.show()
sys.exit(app.exec_())
