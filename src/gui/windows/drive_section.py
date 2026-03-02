import webbrowser
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QComboBox, QPushButton
)
from .main_window_utils import create_header


class DriveSection(QWidget):
    def __init__(self, parent, usb_devices=None):
        super().__init__(parent)
        self.parent = parent
        self.usb_devices = usb_devices or {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)

        layout.addLayout(create_header("Drive Properties"))

        # Device
        lbl_device = QLabel("Device")
        self.combo_device = QComboBox()

        if self.usb_devices:
            for path, label in self.usb_devices.items():
                self.combo_device.addItem(f"{label} ({path})")
        else:
            self.combo_device.addItem("No USB devices found")

        device_layout = QVBoxLayout()
        device_layout.setSpacing(2)
        device_layout.addWidget(lbl_device)
        device_layout.addWidget(self.combo_device)
        layout.addLayout(device_layout)

        # Boot selection
        lbl_boot = QLabel("Boot selection")

        boot_row = QHBoxLayout()
        self.combo_boot = QComboBox()
        self.combo_boot.setEditable(True)
        self.combo_boot.lineEdit().setReadOnly(True)
        self.combo_boot.addItem("installationmedia.iso")

        lbl_check = QLabel("✓")

        btn_select = QPushButton("SELECT")
        btn_select.clicked.connect(self.parent.browse_file)

        boot_row.addWidget(self.combo_boot, 1)
        boot_row.addWidget(lbl_check)
        boot_row.addWidget(btn_select)

        boot_layout = QVBoxLayout()
        boot_layout.setSpacing(2)
        boot_layout.addWidget(lbl_boot)
        boot_layout.addLayout(boot_row)
        layout.addLayout(boot_layout)

        # Image option
        lbl_image = QLabel("Image option")
        self.combo_image_option = QComboBox()
        self.combo_image_option.addItems([
            "Standard Windows installation",
            "Windows To Go",
            "Windows To Go",
            "Standard Linux"
        ])
        self.combo_image_option.currentTextChanged.connect(
            self.parent.update_image_option
        )

        image_layout = QVBoxLayout()
        image_layout.setSpacing(2)
        image_layout.addWidget(lbl_image)
        image_layout.addWidget(self.combo_image_option)
        layout.addLayout(image_layout)

        # Partition grid
        grid = QGridLayout()

        lbl_part = QLabel("Partition scheme")
        self.combo_partition = QComboBox()
        self.combo_partition.addItems(["GPT", "MBR"])
        self.combo_partition.currentTextChanged.connect(
            self.parent.update_partition_scheme
        )

        lbl_target = QLabel("Target system")
        self.combo_target = QComboBox()
        self.combo_target.addItems(["UEFI (non CSM)", "BIOS (or UEFI-CSM)"])
        self.combo_target.currentTextChanged.connect(
            self.parent.update_target_system
        )

        grid.addWidget(lbl_part, 0, 0)
        grid.addWidget(self.combo_partition, 1, 0)
        grid.addWidget(lbl_target, 0, 2)
        grid.addWidget(self.combo_target, 1, 2)

        layout.addLayout(grid)

        self.setLayout(layout)