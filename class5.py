import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Class 5")
        self.setMinimumWidth(300)

        self.number = QSpinBox()
        self.number.setObjectName("number")
        self.number.setRange(0, 10000)
        self.number.setReadOnly(True)
        self.number.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.number.setStyleSheet("QSpinBox { background-color: blue; }")
        
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setObjectName("slider")
        self.slider.setRange(0, 255)

        self.slider_number = QSpinBox()
        self.slider_number.setObjectName("slider number")
        self.slider_number.setRange(0, 255)
        self.slider_number.setReadOnly(True)
        self.slider_number.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slider.valueChanged.connect(self.slider_methode)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timer_method)

        self.start_button = QPushButton("Start")
        self.start_button.setObjectName("start_button")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.stop_button)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.number)
        left_layout.addLayout(buttons_layout)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.slider)
        right_layout.addWidget(self.slider_number)

        self.empty_label = QLabel()
        self.empty_label.setObjectName("empty_label")
        self.empty_label.setMinimumSize(200, 200)

        layout = QHBoxLayout()
        layout.addLayout(left_layout)
        layout.addLayout(right_layout)
        layout.addWidget(self.empty_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def timer_method(self) -> None:
        self.number.setValue(self.number.value() + 1)
        if self.number.value() == self.number.maximum():
            self.stop()

    def slider_methode(self, value: int) -> None:
        self.slider_number.setValue(value)

    def start(self) -> None:
        if self.number.value() >= self.number.maximum():
            return
        self.timer.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop(self) -> None:
        self.timer.stop()
        self.start_button.setEnabled(True)
        if self.number.value() == self.number.maximum():
            self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
