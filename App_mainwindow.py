import faulthandler
faulthandler.enable()

from MainWindow import *
from App_calculator import Calculator


class AppMain(Calculator):
    def __init__(self):
        Calculator.__init__(self)
        from data.fonts import font_regular, font_medium
        self.ui_main = Ui_MainWindow()
        self.ui_main.set_fonts(font_regular, font_medium)
        self.ui_main.setupUi()
        self.ui_main.past_styles()
    
    def run_app(self):
        self.ui_main.MainWindow.show()
        


if __name__ == "__main__":
    app_welcome = AppMain()
    app_welcome.run_app()