from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QComboBox, 
                             QPushButton, QProgressBar, QCheckBox, 
                             QMessageBox, QDialog, QTextEdit, QFileDialog, 
                             QLineEdit, QFrame, QStatusBar, QToolButton, QSpacerItem)
from PyQt6.QtGui import QFont

class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.resize(650, 450)
        layout = QVBoxLayout()
        self.about_text = QTextEdit()
        self.about_text.setReadOnly(True)
        self.about_text.setFont(QFont("Consolas", 9))
        self.about_text.setStyleSheet("background-color: white; border: 1px solid #ccc;")
        layout.addWidget(self.about_text)
        self.setLayout(layout)
