import webbrowser
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QProgressBar, QToolButton
)
from .main_window_utils import create_header


class StatusSection(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addLayout(create_header("Status"))

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(86)
        self.progress_bar.setFormat("")
        layout.addWidget(self.progress_bar)

        bottom = QHBoxLayout()

        icons = QHBoxLayout()

        btn_icon1 = QToolButton()
        btn_icon1.setText("🌐")
        btn_icon1.clicked.connect(
            lambda: webbrowser.open(
                "http://www.github.com/hog185/rufus-py"
            )
        )

        btn_icon2 = QToolButton()
        btn_icon2.setText("ℹ")
        btn_icon2.clicked.connect(self.parent.show_about)

        btn_icon3 = QToolButton()
        btn_icon3.setText("⚙")

        btn_icon4 = QToolButton()
        btn_icon4.setText("📄")
        btn_icon4.clicked.connect(self.parent.show_log)

        icons.addWidget(btn_icon1)
        icons.addWidget(btn_icon2)
        icons.addWidget(btn_icon3)
        icons.addWidget(btn_icon4)
        icons.addStretch()

        self.btn_start = QPushButton("START")
        self.btn_start.setObjectName("btnStart")
        self.btn_cancel = QPushButton("CANCEL")

        buttons = QHBoxLayout()
        buttons.addWidget(self.btn_start)
        buttons.addWidget(self.btn_cancel)

        bottom.addLayout(icons, 1)
        bottom.addLayout(buttons)

        layout.addLayout(bottom)
        self.setLayout(layout)