import faulthandler
faulthandler.enable()

from WelcomeWindow import *
import sys
import winreg


class AppWelcome:
    def __init__(self):
        from data.fonts import font_regular, font_medium
        self.ui_welcome = Ui_WelcomeWindow()
        self.ui_welcome.set_fonts(font_regular, font_medium)
        self.ui_welcome.setupUi1Page()
        self.ui_welcome.past_styles()

        self.ui_welcome.btn_next.clicked.connect(self.go_next_step)

    def run_app(self):
        self.ui_welcome.WelcomeWindow.show()

    def go_next_step(self):
        if self.ui_welcome.check_data_valid():
            self.ui_welcome.past_next_page()
            self.ui_welcome.btn_next.clicked.connect(self.ui_welcome.get_sex_activity)

if __name__ == "__main__":
    app_welcome = AppWelcome()
    app_welcome.run_app()
