import sys 
from PyQt5.QtWidgets import (
    QApplication,  
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QWidget
)

class Cripedit(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cripedit")
        self.resize(1000, 650)

        title = QLabel("Cripedit",)
        title.setStyleSheet("""
                Qlabel {
                    font-size: 32px;
                    font-weight: bold;
            """)  

        subtitle = QLabel("free video editor",)

        open_button = QPushButton("Open video",)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(open_button)

        contral_widget = QWidget()

        self.setCentralWidget("container")

    def main():
        app = QApplication(sys.argv)
        window = Cripedit()
        window.show()
        sys.exit(app.exec_())

        if __name__ == "__main__":
            main()