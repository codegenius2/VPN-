import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider Example")
        self.setGeometry(100, 100, 400, 200)

        # ラベルを作成して配置
        self.label = QLabel(self)
        self.label.setGeometry(150, 80, 100, 40)

        # スライダーを作成して配置
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 50, 300, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(60)  # 秒数の範囲を設定

        # スライダーの値が変更されたときに、秒数を表示するスロットを接続
        self.slider.valueChanged.connect(self.showSeconds)

    def showSeconds(self, value):
        # スライダーの値をラベルに表示
        self.label.setText(str(value) + " 秒")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())