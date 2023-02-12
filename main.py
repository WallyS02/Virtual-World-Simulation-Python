from PyQt5 import QtWidgets
import sys

import GUI


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = GUI.MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


main()
