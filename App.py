import os
import faulthandler
faulthandler.enable()

from App_mainwindow import *
from App_welcomewindow import *
from App_settingswindow import *
from App_calculator import *


class AppFileWorker:
    def __init__(self):
        
        pass

    def new_user(self):
        if os.path.exists("data/params.json"):
            return False
        return True
    
    def is_dark_mode(self):
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return value == 0
        except Exception:
            return False
    
    def create_settings_file(self):
        settings = {"Theme": "light", "language":"ru"}
        if self.is_dark_mode():
            settings = {"Theme": "dark", "language":"ru"}
        with open("data/settings.json", "w") as f:
            json.dump(settings, f)

    def create_food_progress_file(self):
        with open("data/food_progress.json", "w") as f:
            data = {"dates": [], "calories": [], "proteins": [], "fats": [], "carbs": []}
            json.dump(data, f)

    def create_todays_food_file(self, date):
        with open("data/todays_food.json", "w") as f:
            data = {"date": date, "calories": 0, "proteins": 0, "fats": 0, "carbs": 0}
            json.dump(data, f)


class App(AppFileWorker, Calculator):
    def __init__(self):
        AppFileWorker.__init__(self)
        Calculator.__init__(self)
        self.app = QtWidgets.QApplication(sys.argv)
        self.app_main = None
        self.app_welcome = None
        self.app_settings = None
    
    def run_app(self):
        if self.new_user():
            self.create_settings_file() ###############33 Добавить английский язык
            self.create_food_progress_file()
            self.create_todays_food_file(self.todays_date)
            self.show_welcome_window()
        else:
            self.show_main_window()
        
        sys.exit(self.app.exec_())

    def show_welcome_window(self):
        self.app_welcome = AppWelcome()
        self.app_welcome.ui_welcome.btn_finish.clicked.connect(self.show_main_window_after_welcome)
        self.app_welcome.run_app()

    def show_main_window_after_welcome(self):
        self.app_welcome.ui_welcome.get_sex_activity()
        self.app_welcome.ui_welcome.WelcomeWindow.close()
        self.show_main_window()

    def show_main_window(self):
        self.app_main = AppMain()
        self.app_main.ui_main.btn_open_window_settings.clicked.connect(self.show_settings_window)
        self.app_main.run_app()
        self.run_calculations()
        print(self.calories_need, self.proteins_need, self.fats_need, self.carbs_need)
        self.read_file_todays_food() ########################## вот тут проверка на то, чтобы вывести окно ввода веса
        self.past_data_on_main_window()

    def show_settings_window(self):
        self.app_settings = AppSettings()
        self.app_settings.ui_settings.btn_apply.clicked.connect(self.settings_apply)
        self.app_settings.run_app()

    def settings_apply(self):
        self.app_settings.rewrite_settings()
        self.app_main.ui_main.past_styles()
        self.app_settings.ui_settings.past_styles()
        self.app_settings.ui_settings.SettingsWindow.close()

    def past_data_on_main_window(self):
        self.app_main.ui_main.l_date.setText(self.todays_date)

        self.app_main.ui_main.l_amount_calories.setText(f"{self.calories} / {self.calories_need}")
        calories_percent = round(self.calories/self.calories_need)
        self.app_main.ui_main.l_percent_calories.setText(f"{calories_percent} %")

        self.app_main.ui_main.l_amount_protein.setText(f"{self.proteins} / {self.proteins_need}")
        proteins_percent = round(self.proteins/self.proteins_need)
        self.app_main.ui_main.l_percent_protein.setText(f"{proteins_percent} %")

        self.app_main.ui_main.l_amount_fats.setText(f"{self.fats} / {self.fats_need}")
        fats_percent = round(self.fats/self.fats_need)
        self.app_main.ui_main.l_percent_fats.setText(f"{fats_percent} %")

        self.app_main.ui_main.l_amount_carb.setText(f"{self.carb} / {self.carbs_need}")
        carb_percent = round(self.carb/self.carbs_need)
        self.app_main.ui_main.l_percent_carb.setText(f"{carb_percent} %")

        self.app_main.ui_main.l_amount_mass.setText(f"{self.mass}")


if __name__ == "__main__":
    app = App()
    app.run_app()