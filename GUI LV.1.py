#PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(400, 400, 600, 400)#(x,y,weight,height)
        self.setWindowIcon(QIcon("icon.png"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",50))
        label.setGeometry(0,0,600,400)
        label.setStyleSheet("color:red;"
                            "background-color: green;"
                            "fron-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignCenter)# ตัวหนังสืออยูตรงกลาง
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignTop)#VERTICALLY TOP ตัวหนังสืออยู่ด้านบน
        #
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHcenter) #กลางบน
        #label.setAlignment(Qt.AlignVCenter) #กลางซ้าย
        # label.setAlignment(Qt.AlignLeft)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # อยู่กลางและอยู่ล่าง
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()