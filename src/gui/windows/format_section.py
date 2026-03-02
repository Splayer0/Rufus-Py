from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QHBoxLayout,
    QLabel, QComboBox, QLineEdit, QCheckBox
)
from .main_window_utils import create_header


class FormatSection(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)

        layout.addLayout(create_header("Format Options"))

        # Volume label
        lbl_vol = QLabel("Volume label")
        self.input_label = QLineEdit("Volume label")

        vol_layout = QVBoxLayout()
        vol_layout.setSpacing(2)
        vol_layout.addWidget(lbl_vol)
        vol_layout.addWidget(self.input_label)
        layout.addLayout(vol_layout)

        # Grid
        grid = QGridLayout()

        lbl_fs = QLabel("File system")
        self.combo_fs = QComboBox()
        self.combo_fs.addItems(["NTFS", "FAT32", "exFAT", "ext4"])
        self.combo_fs.currentTextChanged.connect(self.parent.updateFS)

        lbl_cluster = QLabel("Cluster size")
        self.combo_cluster = QComboBox()
        self.combo_cluster.addItems(["4096 bytes (Default)", "8192 bytes"])
        self.combo_cluster.currentTextChanged.connect(
            self.parent.update_cluster_size
        )

        grid.addWidget(lbl_fs, 0, 0)
        grid.addWidget(self.combo_fs, 1, 0)
        grid.addWidget(lbl_cluster, 0, 2)
        grid.addWidget(self.combo_cluster, 1, 2)

        layout.addLayout(grid)

        # Checkboxes
        self.chk_quick = QCheckBox("Quick format")
        self.chk_quick.setChecked(True)
        self.chk_quick.stateChanged.connect(self.parent.update_QF)

        self.chk_extended = QCheckBox("Create extended label and icon files")
        self.chk_extended.setChecked(True)
        self.chk_extended.stateChanged.connect(
            self.parent.update_create_extended
        )

        bad_row = QHBoxLayout()
        self.chk_badblocks = QCheckBox("Check device for bad blocks")
        self.combo_badblocks = QComboBox()
        self.combo_badblocks.addItem("1 pass")
        self.combo_badblocks.setEnabled(False)
        self.chk_badblocks.stateChanged.connect(
            self.parent.update_check_bad
        )

        bad_row.addWidget(self.chk_badblocks)
        bad_row.addWidget(self.combo_badblocks)
        bad_row.addStretch()

        layout.addWidget(self.chk_quick)
        layout.addWidget(self.chk_extended)
        layout.addLayout(bad_row)

        self.setLayout(layout)