import sys
import json
import urllib.parse
import webbrowser
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QComboBox, 
                             QPushButton, QProgressBar, QCheckBox, 
                             QMessageBox, QDialog, QTextEdit, QFileDialog, 
                             QLineEdit, QFrame, QStatusBar, QToolButton, QSpacerItem)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
import states

def updateFS(self):
        states.currentFS = self.combo_fs.currentIndex()
        # print(f"Global state updated to: {states.currentFS}")
    
def update_image_option(self):
        states.image_option = self.combo_image_option.currentIndex()
        # print(f"Global state updated to: {states.image_option}")
    
def update_partition_scheme(self):
        states.partition_scheme = self.combo_partition.currentIndex()
        # print(f"Global state updated to: {states.partition_scheme}")

def update_target_system(self):
        states.target_system = self.combo_target.currentIndex()
        # print(f"Global state updated to: {states.target_system}")
    
def update_cluster_size(self):
        states.cluster_size = self.combo_cluster.currentIndex()
        # print(f"Global state updated to: {states.cluster_size}")

def update_QF(self):
        if self.chk_quick.isChecked():
            states.QF = 0
            # print(states.QF)
        else:
            states.QF = 1
            # print(states.QF)

def update_create_extended(self):
        if self.chk_extended.isChecked():
            states.create_extended = 0
            # print(states.create_extended)
        else:
            states.create_extended = 1
            # print(states.create_extended)

def update_check_bad(self):
        if self.chk_badblocks.isChecked():
            states.check_bad = 0
            # print(states.check_bad)
        else:
            states.check_bad = 1
            # print(states.check_bad)

def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Disk Image", "", "ISO Images (*.iso);;All Files (*)")
        if file_name:
            clean_name = file_name.split("/")[-1].split("\\")[-1]
            self.combo_boot.setItemText(0, clean_name)
            self.input_label.setText(clean_name.split('.')[0].upper())
            self.log_message(f"Selected image: {file_name}")

def show_log(self):
        self.log_window = LogWindow()
        self.log_window.show()

def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

def log_message(self, msg):
        if hasattr(self, 'log_window'):
            self.log_window.log_text.append(f"[INFO] {msg}")

def about_message(self, msg):
        if hasattr(self, 'about_window'):
            self.log_window.about_text.append(f"Rufus-Py is a disk image writer written in py for linux")

def start_process(self):
        self.btn_start.setEnabled(False)
        self.btn_cancel.setEnabled(True)
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("Formatting... 0%")
        self.simulate_write()

def cancel_process(self):
        reply = QMessageBox.question(self, "Cancel", "Are you sure you want to cancel?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.progress_bar.setValue(0)
            self.progress_bar.setFormat("")
            self.btn_start.setEnabled(True)
            self.btn_cancel.setEnabled(False)
            self.statusBar.showMessage("Ready", 0)

def simulate_write(self):
        self.timer = QTimer()
        self.progress = 86
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

def update_progress(self):
        self.progress += 1
        if self.progress > 100:
            self.progress = 0
        self.progress_bar.setValue(self.progress)
        self.progress_bar.setFormat(f"Copying ISO files: {self.progress}.0%")
        
        if self.progress >= 100:
            self.timer.stop()
            self.btn_start.setEnabled(True)
            self.btn_cancel.setEnabled(False)
            self.statusBar.showMessage("Ready", 0)