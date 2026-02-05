import faulthandler
faulthandler.enable()

from SettingsWindow import *
import json


class AppSettings:
    def __init__(self):
        from data.fonts import font_regular, font_medium
        self.ui_settings = Ui_SettingsWindow()
        self.ui_settings.set_fonts(font_regular, font_medium)
        self.ui_settings.setupUi()
        self.ui_settings.past_styles()
    
    def run_app(self):
        self.ui_settings.SettingsWindow.show()

    def rewrite_settings(self):
        lang = "ru"
        if self.ui_settings.rb_en.isChecked():
            lang = "en"
        theme = "light"
        if self.ui_settings.rb_dark.isChecked():
            theme = "dark"
        settings = {"Theme":theme, "Language":lang}
        with open("data/settings.json", "w") as f:
            json.dump(settings, f)


if __name__ == "__main__":
    app_settings = AppSettings()
    app_settings.run_app()