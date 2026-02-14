from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from data.Window import Window
from data.colors import *


class Ui_WindowAddMeal(Window):
    def __init__(self):
        self.WindowAddMeal = QtWidgets.QWidget()
        Window.__init__(self)
        self.icon_apple = QtGui.QIcon()
        self.icon_apple.addPixmap(QtGui.QPixmap("data/imgs/logo_apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout = QtWidgets.QGridLayout(self.WindowAddMeal)
        self.btn_add_meal = QtWidgets.QPushButton(self.WindowAddMeal)
        self.btn_add_new_meal_params = QtWidgets.QPushButton(self.WindowAddMeal)
        self.f_name_product = QtWidgets.QFrame(self.WindowAddMeal)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.f_name_product)
        self.label = QtWidgets.QLabel(self.f_name_product)
        self.le_FoodName = QtWidgets.QLineEdit(self.f_name_product)
        self.f_weight_product = QtWidgets.QFrame(self.WindowAddMeal)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.f_weight_product)
        self.label_2 = QtWidgets.QLabel(self.f_weight_product)
        self.le_FoodWeight = QtWidgets.QLineEdit(self.f_weight_product)
        self.f_choise_product = QtWidgets.QFrame(self.WindowAddMeal)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.f_choise_product)
        self.btn_choise2 = QtWidgets.QPushButton(self.f_choise_product)
        self.btn_choise3 = QtWidgets.QPushButton(self.f_choise_product)
        self.btn_choise1 = QtWidgets.QPushButton(self.f_choise_product)

    def setupUi(self):
        self.WindowAddMeal.setObjectName("WindowAddMeal")
        self.WindowAddMeal.resize(612, 792)
        self.WindowAddMeal.setMinimumSize(QtCore.QSize(612, 792))
        self.WindowAddMeal.setMaximumSize(QtCore.QSize(612, 792))
        self.WindowAddMeal.setWindowIcon(self.icon_apple)
        
        self.gridLayout.setContentsMargins(10, 0, 10, 30)
        self.gridLayout.setObjectName("gridLayout")
        
        self.btn_add_meal.setMinimumSize(QtCore.QSize(300, 60))
        self.btn_add_meal.setMaximumSize(QtCore.QSize(300, 60))
        self.font_medium.setPointSize(13)
        self.btn_add_meal.setFont(self.font_medium)
        self.btn_add_meal.setObjectName("btn_add_meal")
        self.gridLayout.addWidget(self.btn_add_meal, 6, 1, 1, 1)

        self.btn_add_new_meal_params.setMinimumSize(QtCore.QSize(300, 60))
        self.btn_add_new_meal_params.setMaximumSize(QtCore.QSize(300, 60))
        self.font_medium.setPointSize(13)
        self.btn_add_new_meal_params.setFont(self.font_medium)
        self.btn_add_new_meal_params.setObjectName("btn_add_meal")
        self.gridLayout.addWidget(self.btn_add_new_meal_params, 4, 1, 1, 1)
        
        self.f_name_product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_name_product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_name_product.setObjectName("f_name_product")
        
        self.gridLayout_2.setContentsMargins(0, 100, 0, 0)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.font_regular.setPointSize(9)
        self.label.setFont(self.font_regular)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        
        self.le_FoodName.setMinimumSize(QtCore.QSize(460, 60))
        self.le_FoodName.setMaximumSize(QtCore.QSize(460, 60))
        self.font_medium.setPointSize(10)
        self.le_FoodName.setFont(self.font_medium)
        self.le_FoodName.setObjectName("le_FoodName")
        self.gridLayout_2.addWidget(self.le_FoodName, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.f_name_product, 0, 0, 1, 3)
        
        self.f_weight_product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_weight_product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_weight_product.setObjectName("f_weight_product")
        
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.font_regular.setPointSize(9)
        self.label_2.setFont(self.font_regular)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        
        self.le_FoodWeight.setMinimumSize(QtCore.QSize(460, 60))
        self.le_FoodWeight.setMaximumSize(QtCore.QSize(460, 60))
        regex_num = QRegExp(r"^\d{1,4}\.\d{1}$")
        self.validator_weight = QRegExpValidator(regex_num)
        self.le_FoodWeight.setValidator(self.validator_weight)
        self.font_medium.setPointSize(10)
        self.le_FoodWeight.setFont(self.font_medium)
        self.le_FoodWeight.setObjectName("le_FoodWeight")
        self.gridLayout_3.addWidget(self.le_FoodWeight, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.f_weight_product, 2, 0, 1, 3)
        
        self.f_choise_product.setMinimumSize(QtCore.QSize(0, 200))
        self.f_choise_product.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.f_choise_product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_choise_product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_choise_product.setObjectName("f_choise_product")
        
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.font_regular.setPointSize(8)
        self.btn_choise3.setFont(self.font_regular)
        self.btn_choise3.setObjectName("btn_choise3")
        self.gridLayout_4.addWidget(self.btn_choise3, 2, 0, 1, 1)
        
        self.font_regular.setPointSize(8)
        self.btn_choise2.setFont(self.font_regular)
        self.btn_choise2.setObjectName("btn_choise2")
        self.gridLayout_4.addWidget(self.btn_choise2, 1, 0, 1, 1)
        
        self.font_regular.setPointSize(8)
        self.btn_choise1.setFont(self.font_regular)
        self.btn_choise1.setObjectName("btn_choise1")
        self.gridLayout_4.addWidget(self.btn_choise1, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.f_choise_product, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 3)

        self.past_styles()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.WindowAddMeal)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.WindowAddMeal.setWindowTitle(_translate("WindowAddMeal", "MacrosHub - Добавить прием пищи"))
        self.btn_add_meal.setText(_translate("WindowAddMeal", "Добавить"))
        self.btn_add_new_meal_params.setText(_translate("WindowAddMeal", "Новый продукт"))
        self.label.setText(_translate("WindowAddMeal", "Название продукта"))
        self.label_2.setText(_translate("WindowAddMeal", "Вес продукта, г"))
        self.btn_choise3.setText(_translate("WindowAddMeal", ""))
        self.btn_choise2.setText(_translate("WindowAddMeal", ""))
        self.btn_choise1.setText(_translate("WindowAddMeal", ""))

    def past_styles(self):
        theme = self.read_theme()

        c1, c3 = "", ""

        if theme == "light":
            c1 = light1
            c2 = light2
            c3 = dark2
            self.apply_dark_title_bar(0, self.WindowAddMeal)
        else:
            c1 = dark1
            c2 = dark2
            c3 = light2
            self.apply_dark_title_bar(1, self.WindowAddMeal)
        
        self.WindowAddMeal.setStyleSheet("QWidget#WindowAddMeal{background-color:"f"{c1}"";}")
        self.btn_add_meal.setStyleSheet("QPushButton#btn_add_meal{color:#fff;border-radius:30px;background-color:#7CC8FF;}\n"
                                        "QPushButton#btn_add_meal::hover{color:#fff;border-radius:30px;background-color:#52A9FF;}")
        self.btn_add_new_meal_params.setStyleSheet("QPushButton#btn_add_meal{color:#fff;border-radius:30px;background-color:#7CC8FF;}\n"
                                        "QPushButton#btn_add_meal::hover{color:#fff;border-radius:30px;background-color:#52A9FF;}")
        self.label.setStyleSheet("color:"f"{c3}"";padding-left:15px;")
        self.le_FoodName.setStyleSheet("QLineEdit#le_FoodName{background-color:"f"{c1}"";border:4px solid #7CC8FF;"
                                       "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"";}")
        self.label_2.setStyleSheet("color:"f"{c3}"";padding-left:15px;")
        self.le_FoodWeight.setStyleSheet("QLineEdit#le_FoodWeight{background-color:"f"{c1}"";border:4px solid #7CC8FF;"
                                         "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"";}")
        self.btn_choise3.setStyleSheet("QPushButton#btn_choise3{background-color:"f"{c1}""; border:none;color:"f"{c3}"";}\n"
                                       "QPushButton#btn_choise3::hover{text-decoration:underline;}")
        self.btn_choise2.setStyleSheet("QPushButton#btn_choise2{background-color:"f"{c1}""; border:none;color:"f"{c3}"";}\n"
                                       "QPushButton#btn_choise2::hover{text-decoration:underline;}")
        self.btn_choise1.setStyleSheet("QPushButton#btn_choise1{background-color:"f"{c1}""; border:none;color:"f"{c3}"";}\n"
                                       "QPushButton#btn_choise1::hover{text-decoration:underline;}")
