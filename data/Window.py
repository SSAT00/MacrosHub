import ctypes
import json

import winreg

class Window:
    def __init__(self):
        self.font_medium = None
        self.font_regular = None

    def apply_dark_title_bar(self, fl, window):
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        hwnd = int(window.winId())
        value = ctypes.c_int(fl)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 
            ctypes.byref(value), ctypes.sizeof(value)
        )

    def read_theme(self):
        with open("data/settings.json", "r") as f:
            settings = json.load(f)
        return settings["Theme"]
        
    def set_fonts(self, regular, medium):
        self.font_medium = medium
        self.font_regular = regular