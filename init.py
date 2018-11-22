import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui import pgp_gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = pgp_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addSystemTray()
    MainWindow.show()
    sys.exit(app.exec_())
