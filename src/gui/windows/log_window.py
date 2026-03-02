from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QComboBox, 
                             QPushButton, QProgressBar, QCheckBox, 
                             QMessageBox, QDialog, QTextEdit, QFileDialog, 
                             QLineEdit, QFrame, QStatusBar, QToolButton, QSpacerItem)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

class LogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rufus Log")
        self.resize(650, 450)
        layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Consolas", 9))
        self.log_text.setStyleSheet("background-color: white; border: 1px solid #ccc;")
        layout.addWidget(self.log_text)
        self.setLayout(layout)