from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

# import sau khi đã khởi QApplication
from retail_project.uis.LoginMainWindowEx import LoginMainWindowEx

login_ui = LoginMainWindowEx()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()
