from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from data.Window import Window
from data.colors import *


class Ui_SettingsWindow(Window):
    def __init__(self):
        Window.__init__(self)
        self.SettingsWindow = QtWidgets.QWidget()
        self.icon_apple = QtGui.QIcon()
        self.icon_apple.addPixmap(QtGui.QPixmap("data/imgs/logo_apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout = QtWidgets.QGridLayout(self.SettingsWindow)
        self.f_language = QtWidgets.QFrame(self.SettingsWindow)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.f_language)
        self.l_language = QtWidgets.QLabel(self.f_language)
        self.rb_ru = QtWidgets.QRadioButton(self.f_language)
        self.rb_en = QtWidgets.QRadioButton(self.f_language)
        self.btn_apply = QtWidgets.QPushButton(self.SettingsWindow)
        self.f_theme = QtWidgets.QFrame(self.SettingsWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.f_theme)
        self.l_theme = QtWidgets.QLabel(self.f_theme)
        self.rb_light = QtWidgets.QRadioButton(self.f_theme)
        self.rb_dark = QtWidgets.QRadioButton(self.f_theme)

    def setupUi(self):
        self.SettingsWindow.setObjectName("SettingsWindow")
        self.SettingsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.SettingsWindow.resize(600, 700)
        self.SettingsWindow.setMinimumSize(QtCore.QSize(600, 700))
        self.SettingsWindow.setMaximumSize(QtCore.QSize(600, 700))
        self.SettingsWindow.setWindowIcon(self.icon_apple)
        
        self.gridLayout.setContentsMargins(10, 10, 10, 30)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        self.f_language.setMinimumSize(QtCore.QSize(0, 100))
        self.f_language.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_language.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_language.setObjectName("f_language")
        
        self.gridLayout_3.setContentsMargins(100, -1, 100, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.font_medium.setPointSize(10)
        self.l_language.setFont(self.font_medium)
        self.l_language.setObjectName("l_language")
        self.gridLayout_3.addWidget(self.l_language, 0, 0, 1, 1)
        
        self.font_regular.setPointSize(8)
        self.rb_ru.setFont(self.font_regular)
        self.rb_ru.setChecked(True)
        self.rb_ru.setObjectName("rb_ru")
        self.gridLayout_3.addWidget(self.rb_ru, 1, 0, 1, 1)
        
        self.rb_en.setFont(self.font_regular)
        self.rb_en.setObjectName("rb_en")
        self.gridLayout_3.addWidget(self.rb_en, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.f_language, 2, 0, 1, 3)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)

        self.btn_apply.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_apply.setMaximumSize(QtCore.QSize(200, 50))
        self.font_medium.setPointSize(11)
        self.btn_apply.setFont(self.font_medium)
        self.btn_apply.setStyleSheet("QPushButton#btn_apply{color:#fff;border-radius:25px;background-color:#7CC8FF;}\n"
                                     "QPushButton#btn_apply::hover{color:#fff;border-radius:25px;background-color:#52A9FF;}")
        self.btn_apply.setObjectName("btn_apply")
        self.gridLayout.addWidget(self.btn_apply, 4, 1, 1, 1)
        
        self.f_theme.setMinimumSize(QtCore.QSize(0, 100))
        self.f_theme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_theme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_theme.setObjectName("f_theme")
        
        self.gridLayout_2.setContentsMargins(100, -1, 100, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.font_medium.setPointSize(10)
        self.l_theme.setFont(self.font_medium)
        self.l_theme.setObjectName("l_theme")
        self.gridLayout_2.addWidget(self.l_theme, 0, 0, 1, 1)
        
        self.rb_light.setFont(self.font_regular)
        self.rb_light.setChecked(True)
        self.rb_light.setObjectName("rb_light")
        self.gridLayout_2.addWidget(self.rb_light, 1, 0, 1, 1)
        
        self.rb_dark.setFont(self.font_regular)
        self.rb_dark.setObjectName("rb_dark")
        self.gridLayout_2.addWidget(self.rb_dark, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.f_theme, 1, 0, 1, 3)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)

        self.past_styles()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.SettingsWindow)

    def past_styles(self):
        theme = self.read_theme()

        c1, c3 = "", ""

        if theme == "light":
            c1 = light1
            c2 = light2
            c3 = dark2
            self.apply_dark_title_bar(0, self.SettingsWindow)
            self.rb_light.setChecked(True)
        else:
            c1 = dark1
            c2 = dark2
            c3 = light2
            self.apply_dark_title_bar(1, self.SettingsWindow)
            self.rb_dark.setChecked(True)

        self.SettingsWindow.setStyleSheet("QWidget#SettingsWindow{background-color:"f"{c1}"";}")
        self.l_language.setStyleSheet(f"color:{c3};")
        self.l_theme.setStyleSheet(f"color:{c3};")
        self.rb_ru.setStyleSheet("QRadioButton#rb_ru{color:"f"{c3}"";}\n"
                                 "QRadioButton#rb_ru::indicator{background-color:"f"{c1}"";width:18px;height:18px;border-radius:15px;}\n"
                                 "QRadioButton#rb_ru::indicator:unchecked{border:6px solid "f"{c2}"";}\n"
                                 "QRadioButton#rb_ru::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_en.setStyleSheet("QRadioButton#rb_en{color:"f"{c3}"";}\n"
                                 "QRadioButton#rb_en::indicator{background-color:"f"{c1}"";width:18px;height:18px;border-radius:15px;}\n"
                                 "QRadioButton#rb_en::indicator:unchecked{border:6px solid "f"{c2}"";}\n"
                                 "QRadioButton#rb_en::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_light.setStyleSheet("QRadioButton#rb_light{color:"f"{c3}"";}\n"
                                    "QRadioButton#rb_light::indicator{background-color:"f"{c1}"";width:18px;height:18px;border-radius:15px;}\n"
                                    "QRadioButton#rb_light::indicator:unchecked{border:6px solid "f"{c2}"";}\n"
                                    "QRadioButton#rb_light::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_dark.setStyleSheet("QRadioButton#rb_dark{color:"f"{c3}"";}\n"
                                   "QRadioButton#rb_dark::indicator{background-color:"f"{c1}"";width:18px;height:18px;border-radius:15px;}\n"
                                   "QRadioButton#rb_dark::indicator:unchecked{border:6px solid "f"{c2}"";}\n"
                                   "QRadioButton#rb_dark::indicator:checked{border:6px solid #7CC8FF;}")
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MacrosHub - Настройки"))
        self.l_language.setText(_translate("SettingsWindow", "Язык"))
        self.rb_ru.setText(_translate("SettingsWindow", "Русский"))
        self.rb_en.setText(_translate("SettingsWindow", "English"))
        self.btn_apply.setText(_translate("SettingsWindow", "Применить"))
        self.l_theme.setText(_translate("SettingsWindow", "Тема"))
        self.rb_light.setText(_translate("SettingsWindow", "Светлая"))
        self.rb_dark.setText(_translate("SettingsWindow", "Темная"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    from data.fonts import font_regular, font_medium
    ui = Ui_SettingsWindow()
    ui.set_fonts(font_regular, font_medium)
    ui.setupUi()
    ui.SettingsWindow.show()
    sys.exit(app.exec_())
