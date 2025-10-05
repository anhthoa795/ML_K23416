import sys, os
from PyQt6 import QtWidgets, QtGui
from MainWindow import Ui_MainWindow

class TestMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Fix đường dẫn ảnh ---
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images")

        # Tạo icon thủ công cho các nút
        self.ui.pushButtonNew.setIcon(QtGui.QIcon(os.path.join(img_dir, "ic_new.png")))
        self.ui.pushButtonInsert.setIcon(QtGui.QIcon(os.path.join(img_dir, "ic_save.png")))
        self.ui.pushButtonUpdate.setIcon(QtGui.QIcon(os.path.join(img_dir, "ic_update.png")))
        self.ui.pushButtonRemove.setIcon(QtGui.QIcon(os.path.join(img_dir, "ic_delete.png")))

        # Gán ảnh mặc định vào label Avatar
        self.ui.labelAvatar.setPixmap(QtGui.QPixmap(os.path.join(img_dir, "ic_no_avatar.png")))

        # (Tuỳ chọn) chỉnh tỷ lệ ảnh cho đẹp
        self.ui.labelAvatar.setScaledContents(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TestMainWindow()
    window.show()
    sys.exit(app.exec())
