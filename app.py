import sys
from PyQt6.QtWidgets import QApplication
from ui.controller import ChatUI


def main():
    app = QApplication(sys.argv)
    window = ChatUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
