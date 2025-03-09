import sys
import socket
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt


class PenTestToolkit(QWidget):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("💀 Penetration Testing Toolkit")
        self.setGeometry(100, 100, 500, 500)

        # Set Red Background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#8B0000"))  # Dark Red Color
        self.setPalette(palette)

        # Layout
        layout = QVBoxLayout()

        # Target Input Label
        self.label = QLabel("🎯 Enter Target (IP or URL):")
        self.label.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
        """)
        layout.addWidget(self.label)

        # Target Input Field
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText("example.com or IP Address")
        self.target_input.setStyleSheet("""
            padding: 10px;
            font-size: 15px;
            border: 2px solid #ff0000;
            border-radius: 5px;
            color: black;
        """)
        layout.addWidget(self.target_input)

        # Port Scanner Button
        self.scan_button = QPushButton("🔎 Run Port Scanner")
        self.scan_button.clicked.connect(self.run_port_scan)
        self.scan_button.setStyleSheet("""
            background-color: #b30000;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        """)
        self.scan_button.setCursor(Qt.PointingHandCursor)
        layout.addWidget(self.scan_button)

        # Brute Force Button
        self.brute_button = QPushButton("💀 Run Brute-Force Attack")
        self.brute_button.clicked.connect(self.run_brute_force)
        self.brute_button.setStyleSheet("""
            background-color: #800000;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        """)
        self.brute_button.setCursor(Qt.PointingHandCursor)
        layout.addWidget(self.brute_button)

        # Result Box
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("""
            background-color: #f0f0f0;
            color: black;
            font-size: 14px;
            border: 2px solid #ff0000;
            padding: 10px;
            border-radius: 5px;
        """)
        layout.addWidget(self.result_box)

        # Set Layout
        self.setLayout(layout)

    # ✅ Function to Run Port Scanner
    def run_port_scan(self):
        target = self.target_input.text().strip()
        if not target:
            QMessageBox.warning(self, "❌ Error", "Please enter a target (IP or URL).")
            return
        
        self.result_box.append(f"🚀 Scanning {target} for open ports...\n")
        open_ports = []
        for port in range(20, 1025):  # Scanning common ports
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except Exception as e:
                self.result_box.append(f"❌ Error scanning port {port}\n")
        
        if open_ports:
            self.result_box.append(f"✅ Open Ports Found: {open_ports}\n")
        else:
            self.result_box.append("❌ No open ports found.\n")

    # ✅ Function to Run Brute Force Attack
    def run_brute_force(self):
        target = self.target_input.text().strip()
        if not target.startswith("http"):
            QMessageBox.warning(self, "❌ Error", "Please enter a valid URL for brute-force testing.")
            return
        
        self.result_box.append(f"💣 Starting brute-force attack on {target}...\n")
        common_passwords = ["admin", "password", "123456", "qwerty", "letmein", "root"]

        for pwd in common_passwords:
            try:
                response = requests.post(target, data={
                    "username": "admin",
                    "password": pwd
                })
                if "incorrect" not in response.text.lower():
                    self.result_box.append(f"✅ Possible Password Found: {pwd}\n")
                    return
            except Exception as e:
                self.result_box.append("❌ Failed to connect to target URL.\n")
        
        self.result_box.append("❌ No password matched from the dictionary.\n")


# ✅ Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PenTestToolkit()
    window.show()
    sys.exit(app.exec_())
