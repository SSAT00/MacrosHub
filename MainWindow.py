from PyQt5 import QtCore, QtGui, QtWidgets

from data.Window import Window, json
from data.colors import *


class Ui_MainWindow(Window):
    def __init__(self):
        Window.__init__(self)
        self.MainWindow = QtWidgets.QWidget()
        self.icon_apple = QtGui.QIcon()
        self.icon_apple.addPixmap(QtGui.QPixmap("data/imgs/logo_apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_settings = QtGui.QIcon()
        self.icon_settings.addPixmap(QtGui.QPixmap("data/imgs/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindow)
        self.f_header = QtWidgets.QFrame(self.MainWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.f_header)
        self.btn_open_window_my_params = QtWidgets.QPushButton(self.f_header)
        self.btn_open_window_settings = QtWidgets.QPushButton(self.f_header)
        self.f_side_menu = QtWidgets.QFrame(self.MainWindow)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.f_side_menu)
        self.f_fats = QtWidgets.QFrame(self.f_side_menu)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.f_fats)
        self.l_fats = QtWidgets.QLabel(self.f_fats)
        self.f_content_fats = QtWidgets.QFrame(self.f_fats)
        self.gridLayout_12 = QtWidgets.QGridLayout(self.f_content_fats)
        self.l_amount_fats = QtWidgets.QLabel(self.f_content_fats)
        self.l_percent_fats = QtWidgets.QLabel(self.f_content_fats)
        self.l_indicator_fats = QtWidgets.QLabel(self.f_content_fats)
        self.l_date = QtWidgets.QLabel(self.f_side_menu)
        self.btn_open_window_analysis = QtWidgets.QPushButton(self.f_side_menu)
        self.f_carb = QtWidgets.QFrame(self.f_side_menu)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.f_carb)
        self.l_carb = QtWidgets.QLabel(self.f_carb)
        self.f_content_carb = QtWidgets.QFrame(self.f_carb)
        self.gridLayout_13 = QtWidgets.QGridLayout(self.f_content_carb)
        self.l_amount_carb = QtWidgets.QLabel(self.f_content_carb)
        self.l_percent_carb = QtWidgets.QLabel(self.f_content_carb)
        self.l_indicator_carb = QtWidgets.QLabel(self.f_content_carb)
        self.f_mass = QtWidgets.QFrame(self.f_side_menu)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.f_mass)
        self.l_mass = QtWidgets.QLabel(self.f_mass)
        self.f_content_mass = QtWidgets.QFrame(self.f_mass)
        self.gridLayout_14 = QtWidgets.QGridLayout(self.f_content_mass)
        self.l_amount_mass = QtWidgets.QLabel(self.f_content_mass)
        self.l_indicator_mass = QtWidgets.QLabel(self.f_content_mass)
        self.f_protein = QtWidgets.QFrame(self.f_side_menu)
        self.gridLayout_7 = QtWidgets.QGridLayout(self.f_protein)
        self.l_protein = QtWidgets.QLabel(self.f_protein)
        self.f_content_protein = QtWidgets.QFrame(self.f_protein)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.f_content_protein)
        self.l_amount_protein = QtWidgets.QLabel(self.f_content_protein)
        self.l_percent_protein = QtWidgets.QLabel(self.f_content_protein)
        self.l_indicator_protein = QtWidgets.QLabel(self.f_content_protein)
        self.f_calories = QtWidgets.QFrame(self.f_side_menu)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.f_calories)
        self.l_calories = QtWidgets.QLabel(self.f_calories)
        self.f_content_calories = QtWidgets.QFrame(self.f_calories)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.f_content_calories)
        self.l_amount_calories = QtWidgets.QLabel(self.f_content_calories)
        self.l_percent_calories = QtWidgets.QLabel(self.f_content_calories)
        self.l_indicator_calories = QtWidgets.QLabel(self.f_content_calories)
        self.f_content = QtWidgets.QFrame(self.MainWindow)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.f_content)
        self.btn_open_window_add_meal = QtWidgets.QPushButton(self.f_content)
        self.btn_open_window_add_todays_weight = QtWidgets.QPushButton(self.f_content)

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1440, 900)
        self.MainWindow.setMinimumSize(QtCore.QSize(1440, 900))
        self.MainWindow.setMaximumSize(QtCore.QSize(1440, 900))
        self.MainWindow.setWindowIcon(self.icon_apple)
        
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        
        self.f_header.setMinimumSize(QtCore.QSize(0, 90))
        self.f_header.setMaximumSize(QtCore.QSize(16777215, 90))
        self.f_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_header.setObjectName("f_header")
        
        self.gridLayout_2.setContentsMargins(30, -1, 15, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.font_regular.setPointSize(10)
        self.btn_open_window_my_params.setFont(self.font_regular)
        self.btn_open_window_my_params.setObjectName("btn_open_window_my_params")
        self.gridLayout_2.addWidget(self.btn_open_window_my_params, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)

        self.btn_open_window_settings.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_open_window_settings.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_open_window_settings.setText("")
        self.btn_open_window_settings.setIcon(self.icon_settings)
        self.btn_open_window_settings.setIconSize(QtCore.QSize(40, 40))
        self.btn_open_window_settings.setObjectName("btn_open_window_settings")
        self.gridLayout_2.addWidget(self.btn_open_window_settings, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.f_header, 0, 0, 1, 2)
        
        self.f_side_menu.setMinimumSize(QtCore.QSize(500, 0))
        self.f_side_menu.setMaximumSize(QtCore.QSize(500, 16777215))
        self.f_side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_side_menu.setObjectName("f_side_menu")
        
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.f_fats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_fats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_fats.setObjectName("f_fats")
        
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        
        self.font_regular.setPointSize(9)
        self.l_fats.setFont(self.font_regular)
        self.l_fats.setStyleSheet("padding-left:20px;")
        self.l_fats.setObjectName("l_fats")
        self.gridLayout_8.addWidget(self.l_fats, 0, 0, 1, 1)
        
        self.f_content_fats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_fats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_fats.setObjectName("f_content_fats")
        
        self.gridLayout_12.setContentsMargins(20, 10, 10, 10)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        
        self.font_medium.setPointSize(9)
        self.l_amount_fats.setFont(self.font_medium)
        self.l_amount_fats.setObjectName("l_amount_fats")
        self.gridLayout_12.addWidget(self.l_amount_fats, 0, 0, 1, 1)
        
        self.font_regular.setPointSize(9)
        self.l_percent_fats.setFont(self.font_regular)
        self.l_percent_fats.setObjectName("l_percent_fats")
        self.gridLayout_12.addWidget(self.l_percent_fats, 0, 1, 1, 1)
        
        self.l_indicator_fats.setMinimumSize(QtCore.QSize(40, 40))
        self.l_indicator_fats.setMaximumSize(QtCore.QSize(40, 40))
        self.l_indicator_fats.setText("")
        self.l_indicator_fats.setObjectName("l_indicator_fats")
        self.gridLayout_12.addWidget(self.l_indicator_fats, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.f_content_fats, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.f_fats, 4, 0, 1, 3)
        
        self.font_regular.setPointSize(9)
        self.l_date.setFont(self.font_regular)
        self.l_date.setStyleSheet("padding-right:10px;")
        self.l_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_date.setObjectName("l_date")
        self.gridLayout_4.addWidget(self.l_date, 0, 0, 1, 3)
        
        self.btn_open_window_analysis.setMinimumSize(QtCore.QSize(255, 60))
        self.btn_open_window_analysis.setMaximumSize(QtCore.QSize(255, 60))
        self.font_medium.setPointSize(12)
        self.btn_open_window_analysis.setFont(self.font_medium)
        self.btn_open_window_analysis.setObjectName("btn_open_window_analysis")
        self.gridLayout_4.addWidget(self.btn_open_window_analysis, 8, 1, 1, 1)
        
        self.f_carb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_carb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_carb.setObjectName("f_carb")
        
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        
        self.font_regular.setPointSize(9)
        self.l_carb.setFont(self.font_regular)
        self.l_carb.setStyleSheet("padding-left:20px;")
        self.l_carb.setObjectName("l_carb")
        self.gridLayout_9.addWidget(self.l_carb, 0, 0, 1, 1)
        
        self.f_content_carb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_carb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_carb.setObjectName("f_content_carb")
        
        self.gridLayout_13.setContentsMargins(20, 10, 10, 10)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        
        self.font_medium.setPointSize(9)
        self.l_amount_carb.setFont(self.font_medium)
        self.l_amount_carb.setObjectName("l_amount_carb")
        self.gridLayout_13.addWidget(self.l_amount_carb, 0, 0, 1, 1)
        
        self.font_regular.setPointSize(9)
        self.l_percent_carb.setFont(self.font_regular)
        self.l_percent_carb.setObjectName("l_percent_carb")
        self.gridLayout_13.addWidget(self.l_percent_carb, 0, 1, 1, 1)
        
        self.l_indicator_carb.setMinimumSize(QtCore.QSize(40, 40))
        self.l_indicator_carb.setMaximumSize(QtCore.QSize(40, 40))
        self.l_indicator_carb.setText("")
        self.l_indicator_carb.setObjectName("l_indicator_carb")
        self.gridLayout_13.addWidget(self.l_indicator_carb, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.f_content_carb, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.f_carb, 5, 0, 1, 3)
        
        self.f_mass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_mass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_mass.setObjectName("f_mass")
        
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        
        self.font_regular.setPointSize(9)
        self.l_mass.setFont(self.font_regular)
        self.l_mass.setStyleSheet("padding-left:20px;")
        self.l_mass.setObjectName("l_mass")
        self.gridLayout_10.addWidget(self.l_mass, 0, 0, 1, 1)
        
        self.f_content_mass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_mass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_mass.setObjectName("f_content_mass")
        
        self.gridLayout_14.setContentsMargins(20, 10, 10, 10)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        
        self.font_medium.setPointSize(9)
        self.l_amount_mass.setFont(self.font_medium)
        self.l_amount_mass.setObjectName("l_amount_mass")
        self.gridLayout_14.addWidget(self.l_amount_mass, 0, 0, 1, 1)
        
        self.l_indicator_mass.setMinimumSize(QtCore.QSize(40, 40))
        self.l_indicator_mass.setMaximumSize(QtCore.QSize(40, 40))
        self.l_indicator_mass.setText("")
        self.l_indicator_mass.setObjectName("l_indicator_mass")
        self.gridLayout_14.addWidget(self.l_indicator_mass, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.f_content_mass, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.f_mass, 6, 0, 1, 3)
        
        self.f_protein.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_protein.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_protein.setObjectName("f_protein")
        
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        
        self.font_regular.setPointSize(9)
        self.l_protein.setFont(self.font_regular)
        self.l_protein.setStyleSheet("padding-left:20px;")
        self.l_protein.setObjectName("l_protein")
        self.gridLayout_7.addWidget(self.l_protein, 0, 0, 1, 1)
        
        self.f_content_protein.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_protein.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_protein.setObjectName("f_content_protein")
        
        self.gridLayout_11.setContentsMargins(20, 10, 10, 10)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        
        self.font_medium.setPointSize(9)
        self.l_amount_protein.setFont(self.font_medium)
        self.l_amount_protein.setObjectName("l_amount_protein")
        self.gridLayout_11.addWidget(self.l_amount_protein, 0, 0, 1, 1)
        
        self.font_regular.setPointSize(9)
        self.l_percent_protein.setFont(self.font_regular)
        self.l_percent_protein.setObjectName("l_percent_protein")
        self.gridLayout_11.addWidget(self.l_percent_protein, 0, 1, 1, 1)
        
        self.l_indicator_protein.setMinimumSize(QtCore.QSize(40, 40))
        self.l_indicator_protein.setMaximumSize(QtCore.QSize(40, 40))
        self.l_indicator_protein.setText("")
        self.l_indicator_protein.setObjectName("l_indicator_protein")
        self.gridLayout_11.addWidget(self.l_indicator_protein, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.f_content_protein, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.f_protein, 3, 0, 1, 3)
        
        self.f_calories.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_calories.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_calories.setObjectName("f_calories")
        
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.font_regular.setPointSize(9)
        self.l_calories.setFont(self.font_regular)
        self.l_calories.setStyleSheet("padding-left:20px;")
        self.l_calories.setObjectName("l_calories")
        self.gridLayout_5.addWidget(self.l_calories, 0, 0, 1, 1)
        
        self.f_content_calories.setMinimumSize(QtCore.QSize(0, 60))
        self.f_content_calories.setMaximumSize(QtCore.QSize(16777215, 60))
        self.f_content_calories.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_calories.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_calories.setObjectName("f_content_calories")
        
        self.gridLayout_6.setContentsMargins(20, 10, 10, 10)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.font_medium.setPointSize(9)
        self.l_amount_calories.setFont(self.font_medium)
        self.l_amount_calories.setObjectName("l_amount_calories")
        self.gridLayout_6.addWidget(self.l_amount_calories, 0, 0, 1, 1)
        
        self.font_regular.setPointSize(9)
        self.l_percent_calories.setFont(self.font_regular)
        self.l_percent_calories.setObjectName("l_percent_calories")
        self.gridLayout_6.addWidget(self.l_percent_calories, 0, 1, 1, 1)
        
        self.l_indicator_calories.setMinimumSize(QtCore.QSize(40, 40))
        self.l_indicator_calories.setMaximumSize(QtCore.QSize(40, 40))
        self.l_indicator_calories.setText("")
        self.l_indicator_calories.setObjectName("l_indicator_calories")
        self.gridLayout_6.addWidget(self.l_indicator_calories, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.f_content_calories, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.f_calories, 2, 0, 1, 3)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 8, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 7, 1, 1, 1)

        self.gridLayout.addWidget(self.f_side_menu, 1, 0, 1, 1)
        self.f_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content.setObjectName("f_content")
        
        self.gridLayout_3.setContentsMargins(10, 10, 10, 20)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.btn_open_window_add_meal.setMinimumSize(QtCore.QSize(300, 300))
        self.btn_open_window_add_meal.setMaximumSize(QtCore.QSize(300, 300))
        self.font_medium.setPointSize(12)
        self.btn_open_window_add_meal.setFont(self.font_medium)
        self.btn_open_window_add_meal.setObjectName("btn_open_window_add_meal")
        self.gridLayout_3.addWidget(self.btn_open_window_add_meal, 1, 0, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        
        self.btn_open_window_add_todays_weight.setMinimumSize(QtCore.QSize(300, 60))
        self.btn_open_window_add_todays_weight.setMaximumSize(QtCore.QSize(300, 60))
        self.font_medium.setPointSize(12)
        self.btn_open_window_add_todays_weight.setFont(self.font_medium)
        self.btn_open_window_add_todays_weight.setObjectName("btn_open_window_add_todays_weight")
        self.gridLayout_3.addWidget(self.btn_open_window_add_todays_weight, 3, 0, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.f_content, 1, 1, 1, 1)

        self.past_styles()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MacrosHub"))
        self.btn_open_window_my_params.setText(_translate("MainWindow", "Мои параметры"))
        self.l_fats.setText(_translate("MainWindow", "Жиры, г"))
        self.l_amount_fats.setText(_translate("MainWindow", "0 / 50"))
        self.l_percent_fats.setText(_translate("MainWindow", "0%"))
        self.l_date.setText(_translate("MainWindow", "01.01.2026"))
        self.btn_open_window_analysis.setText(_translate("MainWindow", "Анализ"))
        self.l_carb.setText(_translate("MainWindow", "Углеводы, г"))
        self.l_amount_carb.setText(_translate("MainWindow", "0 / 200"))
        self.l_percent_carb.setText(_translate("MainWindow", "0 %"))
        self.l_mass.setText(_translate("MainWindow", "Масса тела, кг"))
        self.l_amount_mass.setText(_translate("MainWindow", "55"))
        self.l_protein.setText(_translate("MainWindow", "Белки, г"))
        self.l_amount_protein.setText(_translate("MainWindow", "0 / 80"))
        self.l_percent_protein.setText(_translate("MainWindow", "0 %"))
        self.l_calories.setText(_translate("MainWindow", "Калории"))
        self.l_amount_calories.setText(_translate("MainWindow", "0 / 2000"))
        self.l_percent_calories.setText(_translate("MainWindow", "0 %"))
        self.btn_open_window_add_meal.setText(_translate("MainWindow", "Добавить\n""прием пищи"))
        self.btn_open_window_add_todays_weight.setText(_translate("MainWindow", "Добавить утренний вес"))

    def past_styles(self):
        theme = self.read_theme()

        c1, c3 = "", ""

        if theme == "light":
            c1 = light1
            c2 = light2
            c3 = dark2
            self.apply_dark_title_bar(0, self.MainWindow)
        else:
            c1 = dark1
            c2 = dark2
            c3 = light2
            self.apply_dark_title_bar(1, self.MainWindow)

        self.MainWindow.setStyleSheet("QWidget#MainWindow{background-color:"f"{c1}"";}")
        self.f_header.setStyleSheet("QFrame#f_header{background-color:"f"{c1}"";border: 1px solid "f"{c2}""; border-radius: 30px;}")
        self.btn_open_window_my_params.setStyleSheet("QPushButton#btn_open_window_my_params{background-color:"f"{c1}""; border:none;color:"f"{c3}"";}\n"
                                                     "QPushButton#btn_open_window_my_params::hover{text-decoration:underline;}")
        self.btn_open_window_settings.setStyleSheet("QPushButton#btn_open_window_settings{background-color:"f"{c1}""; border:3px solid #7CC8FF; border-radius: 30px;}\n"
                                                    "QPushButton#btn_open_window_settings::hover{ border:3px solid #52A9FF; border-radius: 30px;}")
        self.f_side_menu.setStyleSheet("QFrame#f_side_menu{background-color:"f"{c1}"";border: 1px solid "f"{c2}""; border-radius: 30px;}")
        self.f_content_fats.setStyleSheet("QFrame#f_content_fats{background-color:"f"{c1}"";border:1px solid "f"{c2}"";border-radius:30px;}")
        self.btn_open_window_analysis.setStyleSheet("QPushButton#btn_open_window_analysis{background-color:#7CC8FF; color:#fff; border-radius:30px;}\n"
                                                    "QPushButton#btn_open_window_analysis::hover{background-color:#52A9FF;}")
        self.f_content_carb.setStyleSheet("QFrame#f_content_carb{background-color:"f"{c1}"";border:1px solid "f"{c2}"";border-radius:30px;}")
        self.f_content_mass.setStyleSheet("QFrame#f_content_mass{background-color:"f"{c1}"";border:1px solid "f"{c2}"";border-radius:30px;}")
        self.f_content_protein.setStyleSheet("QFrame#f_content_protein{background-color:"f"{c1}"";border:1px solid "f"{c2}"";border-radius:30px;}")
        self.f_calories.setStyleSheet("QFrame#f_calories{background-color:"f"{c1}"";border:none;}")
        self.f_content_calories.setStyleSheet("QFrame#f_content_calories{background-color:"f"{c1}"";border:1px solid "f"{c2}"";border-radius:30px;}")
        self.f_content.setStyleSheet("QFrame#f_content{background-color:"f"{c1}"";border: 1px solid "f"{c2}""; border-radius: 30px;}")
        self.btn_open_window_add_meal.setStyleSheet("QPushButton#btn_open_window_add_meal{background-color:"f"{c1}"";border:10px solid #7CC8FF;border-radius:150px;color:"f"{c3}"";}"
                                                    "QPushButton#btn_open_window_add_meal::hover{text-decoration:underline;}")
        self.btn_open_window_add_todays_weight.setStyleSheet("QPushButton#btn_open_window_add_todays_weight{background-color:#7CC8FF; color:#fff; border-radius:30px;}\n"
                                                             "QPushButton#btn_open_window_add_todays_weight::hover{background-color:#52A9FF;}")
        self.l_date.setStyleSheet(f"color:{c3};")

        self.l_calories.setStyleSheet(f"color:{c3};padding-left:20px;")
        self.l_amount_calories.setStyleSheet(f"color:{c3};")
        self.l_percent_calories.setStyleSheet(f"color:{c3};")
        self.l_fats.setStyleSheet(f"color:{c3};padding-left:20px;")
        self.l_amount_fats.setStyleSheet(f"color:{c3};")
        self.l_percent_fats.setStyleSheet(f"color:{c3};")
        self.l_protein.setStyleSheet(f"color:{c3};padding-left:20px;")
        self.l_amount_protein.setStyleSheet(f"color:{c3};")
        self.l_percent_protein.setStyleSheet(f"color:{c3};")
        self.l_carb.setStyleSheet(f"color:{c3};padding-left:20px;")
        self.l_amount_carb.setStyleSheet(f"color:{c3};")
        self.l_percent_carb.setStyleSheet(f"color:{c3};")
        self.l_mass.setStyleSheet(f"color:{c3};padding-left:20px;")
        self.l_amount_mass.setStyleSheet(f"color:{c3};")


        self.l_indicator_fats.setStyleSheet("QLabel#l_indicator_fats{border-radius:20px;background-color:#FFA5A5;}")
        self.l_indicator_carb.setStyleSheet("QLabel#l_indicator_carb{border-radius:20px;background-color:#FFA5A5;}")
        self.l_indicator_mass.setStyleSheet("QLabel#l_indicator_mass{border-radius:20px;background-color:#C4FFA5;}")
        self.l_indicator_protein.setStyleSheet("QLabel#l_indicator_protein{border-radius:20px;background-color:#FFA5A5;}")
        self.l_indicator_calories.setStyleSheet("QLabel#l_indicator_calories{border-radius:20px;background-color:#FFA5A5;}")

