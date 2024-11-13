from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow  # Import the generated UI file

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Kết nối các nút bấm với các hàm
        self.pushButtonSHBT.clicked.connect(self.tinh_shbt)
        self.pushButtonKinhdoanh.clicked.connect(self.tinh_kinh_doanh)
        self.pushButtonSanxuat.clicked.connect(self.tinh_san_xuat)
        self.pushButtonTinhtiep.clicked.connect(self.tinh_tiep)
        self.pushButtonThoat.clicked.connect(self.close)
        self.pushButtonHuongdan.clicked.connect(self.huong_dan)

    def tinh_shbt(self):
        try:
            A = int(self.LineEditChisocu.text())
            B = int(self.LineEditChisomoi.text())
            C = float(self.LineEditSHBT.text())
            if B < A or C <= 0:
                raise ValueError

            dien_nang = B - A
            if dien_nang <= 50 * C:
                tong_tien = dien_nang * 1484
            elif dien_nang <= 100 * C:
                tong_tien = 50 * C * 1484 + (dien_nang - 50 * C) * 1533
            elif dien_nang <= 200 * C:
                tong_tien = 50 * C * 1484 + 50 * C * 1533 + (dien_nang - 100 * C) * 1786
            elif dien_nang <= 300 * C:
                tong_tien = 50 * C * 1484 + 50 * C * 1533 + 100 * C * 1786 + (dien_nang - 200 * C) * 2242
            elif dien_nang <= 400 * C:
                tong_tien = (50 * C * 1484 + 50 * C * 1533 + 100 * C * 1786 + 100 * C * 2242 +
                             (dien_nang - 300 * C) * 2503)
            else:
                tong_tien = (50 * C * 1484 + 50 * C * 1533 + 100 * C * 1786 + 100 * C * 2242 +
                             100 * C * 2503 + (dien_nang - 400 * C) * 2587)
            self.lineEditSotiensethu.setText(f"{tong_tien} VND")
        except ValueError:
            self.show_error("Thông tin nhập không hợp lệ!")

    def tinh_kinh_doanh(self):
        try:
            A = int(self.LineEditChisocu.text())
            B = int(self.LineEditChisomoi.text())
            if B < A:
                raise ValueError
            dien_nang = B - A
            tong_tien = dien_nang * 2320
            self.lineEditSotiensethu.setText(f"{tong_tien} VND")
        except ValueError:
            self.show_error("Thông tin nhập không hợp lệ!")

    def tinh_san_xuat(self):
        try:
            A = int(self.LineEditChisocu.text())
            B = int(self.LineEditChisomoi.text())
            if B < A:
                raise ValueError
            dien_nang = B - A
            tong_tien = dien_nang * 1518
            self.lineEditSotiensethu.setText(f"{tong_tien} VND")
        except ValueError:
            self.show_error("Thông tin nhập không hợp lệ!")

    def tinh_tiep(self):
        # Reset các trường nhập liệu
        self.LineEditChisocu.clear()
        self.LineEditChisomoi.clear()
        self.LineEditSHBT.clear()
        self.lineEditSotiensethu.clear()
        # Di chuyển con trỏ về ô chỉ số cũ
        self.LineEditChisocu.setFocus()

    def huong_dan(self):
        QMessageBox.information(self, "Hướng dẫn", "Sinh viên thực hiện: Bé meow meow ")

    def show_error(self, message):
        QMessageBox.critical(self, "Lỗi", message)


