import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


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
        self.number.setStyleSheet("QSpinBox { background-color: lightgray; }")

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

        layout = QVBoxLayout()
        layout.addWidget(self.number)
        layout.addLayout(buttons_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start(self) -> None:
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop(self) -> None:
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
