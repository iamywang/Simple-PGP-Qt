import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI import PGP_Main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = PGP_Main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addSystemTray()
    MainWindow.show()
    sys.exit(app.exec_())
