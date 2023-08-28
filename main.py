import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from Timer import Ui_MainWindow as Timer_Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Timer_Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.start_timer)
        self.ui.pause_btn.clicked.connect(self.pause_timer)
        self.ui.reset_btn.clicked.connect(self.reset_timer)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        self.minutes = 0
        self.seconds = 0
        self.pause = False
        self.user_time = 0

    def start_timer(self):
        text = self.ui.User_time.text()
        if text.isdigit():
            self.user_time = int(text)
            self.timer.start()

    def pause_timer(self):
        if self.pause:
            self.pause = False
            self.timer.start()
            self.ui.pause_btn.setText("Pause")
        else:
            self.pause = True
            self.timer.stop()
            self.ui.pause_btn.setText("Resume")

    def reset_timer(self):
        self.timer.stop()
        self.minutes = 0
        self.seconds = 0
        self.pause = False
        self.user_time = 0
        self.ui.Time.setText("00:00")
        self.ui.User_time.setText("")
        self.ui.User_time.setPlaceholderText("Enter the time")

    def update_timer(self):
        if self.pause:
            return

        if self.user_time == 0:
            self.timer.stop()
            return
        self.seconds += 1
        self.seconds = self.seconds % 60
        if self.seconds == 0:
            self.minutes += 1
        minute = str(self.minutes) if self.minutes > 9 else "0" + str(self.minutes)
        second = str(self.seconds) if self.seconds > 9 else "0" + str(self.seconds)
        self.ui.Time.setText(minute + ":" + second)
        if self.minutes == self.user_time:
            self.timer.stop()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
