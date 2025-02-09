import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Bank')))
from BankClass import Bank
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

# დავაიმპორტედ ჩვენი ფაილი რომელიც დევს სხვა ფოლდერში

UserBank = Bank()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # შექმნა ცენტრალური ვიჯეტი და ვერტიკალური განლაგება
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # მომხმარებლის სახელის ლეიბლი და შეყვანის ველი
        self.username_label = QLabel("Username:")
        layout.addWidget(self.username_label)
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        # პაროლის ლეიბლი და შეყვანის ველი
        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # ელ.ფოსტის ლეიბლი და შეყვანის ველი
        self.email_label = QLabel("Email:")
        layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        # შესვლის ღილაკი
        self.login_button = QPushButton("Log In")
        layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()


def main():
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(100, 100, 300, 200)
    window.setWindowTitle("Bank Login")
    window.show()
    app.exec_()

main()