from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStatusBar
from .drive_section import DriveSection
from .format_section import FormatSection
from .status_section import StatusSection


class Rufus(QMainWindow):
    def __init__(self, usb_devices=None):
        super().__init__()

        self.usb_devices = usb_devices or {}

        self.setWindowTitle("Rufus")
        self.setFixedSize(640, 780)

        central = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(15, 10, 15, 10)

        self.drive_section = DriveSection(self, self.usb_devices)
        self.format_section = FormatSection(self)
        self.status_section = StatusSection(self)

        main_layout.addWidget(self.drive_section)
        main_layout.addWidget(self.format_section)
        main_layout.addWidget(self.status_section)
        main_layout.addStretch()

        central.setLayout(main_layout)
        self.setCentralWidget(central)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)