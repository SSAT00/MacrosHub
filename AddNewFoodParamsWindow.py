from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from data.Window import Window
from data.colors import *


class Ui_WindowAddNewMealParams(Window):
    def __init__(self):
        Window.__init__(self)
        self.WindowAddNewMealParams = QtWidgets.QWidget()
        self.icon_apple = QtGui.QIcon()
        self.icon_apple.addPixmap(QtGui.QPixmap("data/imgs/logo_apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout = QtWidgets.QGridLayout(self.WindowAddNewMealParams)
        self.l_fats_new_product = QtWidgets.QLabel(self.WindowAddNewMealParams)
        self.btn_add_new_food_params = QtWidgets.QPushButton(self.WindowAddNewMealParams)
        self.l_proteins_new_product = QtWidgets.QLabel(self.WindowAddNewMealParams)
        self.le_fats_new_product = QtWidgets.QLineEdit(self.WindowAddNewMealParams)
        self.l_calories_new_product = QtWidgets.QLabel(self.WindowAddNewMealParams)
        self.le_calories_new_product = QtWidgets.QLineEdit(self.WindowAddNewMealParams)
        self.le_carbs_new_product = QtWidgets.QLineEdit(self.WindowAddNewMealParams)
        self.l_carbs_new_product = QtWidgets.QLabel(self.WindowAddNewMealParams)
        self.le_proteins_new_product = QtWidgets.QLineEdit(self.WindowAddNewMealParams)
        self.le_name_new_product = QtWidgets.QLineEdit(self.WindowAddNewMealParams)
        self.l_name_new_product = QtWidgets.QLabel(self.WindowAddNewMealParams)
        regex_num_perc = QRegExp(r"^\d{1,2}\.\d{1}$")
        self.validator_num_perc = QRegExpValidator(regex_num_perc)
        regex_num_amount = QRegExp(r"^\d{1,4}\.\d{1}$")
        self.validator_num = QRegExpValidator(regex_num_amount)
        regex_let = QRegExp(r"^[a-zA-Zа-яА-ЯёЁ ]+$")
        self.validator_let = QRegExpValidator(regex_let)

    def setupUi(self):
        self.WindowAddNewMealParams.setObjectName("WindowAddNewMealParams")
        self.WindowAddNewMealParams.resize(569, 586)
        self.WindowAddNewMealParams.setWindowIcon(self.icon_apple)
        
        self.gridLayout.setContentsMargins(20, 40, 20, 40)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        
        self.l_fats_new_product.setMinimumSize(QtCore.QSize(0, 0))
        self.l_fats_new_product.setMaximumSize(QtCore.QSize(16777215, 30))
        self.font_regular.setPointSize(8)
        self.l_fats_new_product.setFont(self.font_regular)
        self.l_fats_new_product.setObjectName("l_fats_new_product")
        self.gridLayout.addWidget(self.l_fats_new_product, 6, 0, 1, 2)
        
        self.btn_add_new_food_params.setMinimumSize(QtCore.QSize(300, 60))
        self.font_medium.setPointSize(11)
        self.btn_add_new_food_params.setFont(self.font_medium)
        self.btn_add_new_food_params.setObjectName("btn_add_new_food_params")
        self.gridLayout.addWidget(self.btn_add_new_food_params, 9, 1, 1, 2)
        
        self.font_regular.setPointSize(8)
        self.l_proteins_new_product.setFont(self.font_regular)
        self.l_proteins_new_product.setObjectName("l_proteins_new_product")
        self.gridLayout.addWidget(self.l_proteins_new_product, 3, 2, 1, 1)
        
        self.le_fats_new_product.setMinimumSize(QtCore.QSize(0, 60))
        self.font_medium.setPointSize(9)
        self.le_fats_new_product.setFont(self.font_medium)
        self.le_fats_new_product.setObjectName("le_fats_new_product")
        self.gridLayout.addWidget(self.le_fats_new_product, 7, 0, 1, 2)
        self.le_fats_new_product.setValidator(self.validator_num_perc)
        
        self.l_calories_new_product.setMaximumSize(QtCore.QSize(16777215, 30))
        self.font_regular.setPointSize(8)
        self.l_calories_new_product.setFont(self.font_regular)
        self.l_calories_new_product.setObjectName("l_calories_new_product")
        self.gridLayout.addWidget(self.l_calories_new_product, 3, 0, 1, 2)
        
        self.le_calories_new_product.setMinimumSize(QtCore.QSize(0, 60))
        self.font_medium.setPointSize(9)
        self.le_calories_new_product.setFont(self.font_medium)
        self.le_calories_new_product.setObjectName("le_calories_new_product")
        self.gridLayout.addWidget(self.le_calories_new_product, 4, 0, 1, 2)
        self.le_calories_new_product.setValidator(self.validator_num)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 9, 3, 1, 1)
        
        self.le_carbs_new_product.setMinimumSize(QtCore.QSize(0, 60))
        self.font_medium.setPointSize(9)
        self.le_carbs_new_product.setFont(self.font_medium)
        self.le_carbs_new_product.setObjectName("le_carbs_new_product")
        self.gridLayout.addWidget(self.le_carbs_new_product, 7, 2, 1, 2)
        self.le_carbs_new_product.setValidator(self.validator_num_perc)
        
        self.font_regular.setPointSize(8)
        self.l_carbs_new_product.setFont(self.font_regular)
        self.l_carbs_new_product.setObjectName("l_carbs_new_product")
        self.gridLayout.addWidget(self.l_carbs_new_product, 6, 2, 1, 2)
        
        self.le_proteins_new_product.setMinimumSize(QtCore.QSize(0, 60))
        self.font_medium.setPointSize(9)
        self.le_proteins_new_product.setFont(self.font_medium)
        self.le_proteins_new_product.setObjectName("le_proteins_new_product")
        self.gridLayout.addWidget(self.le_proteins_new_product, 4, 2, 1, 2)
        self.le_proteins_new_product.setValidator(self.validator_num_perc)
        
        self.le_name_new_product.setMinimumSize(QtCore.QSize(0, 60))
        self.font_medium.setPointSize(9)
        self.le_name_new_product.setFont(self.font_medium)
        self.le_name_new_product.setObjectName("le_name_new_product")
        self.gridLayout.addWidget(self.le_name_new_product, 1, 0, 1, 4)
        self.le_name_new_product.setValidator(self.validator_let)
        
        self.l_name_new_product.setMaximumSize(QtCore.QSize(16777215, 30))
        self.font_regular.setPointSize(8)
        self.l_name_new_product.setFont(self.font_regular)
        self.l_name_new_product.setObjectName("l_name_new_product")
        self.gridLayout.addWidget(self.l_name_new_product, 0, 0, 1, 4)

        self.past_styles()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.WindowAddNewMealParams)

    def past_styles(self):
        theme = self.read_theme()

        c1, c3 = "", ""

        if theme == "light":
            c1 = light1
            c2 = light2
            c3 = dark2
            self.apply_dark_title_bar(0, self.WindowAddNewMealParams)
        else:
            c1 = dark1
            c2 = dark2
            c3 = light2
            self.apply_dark_title_bar(1, self.WindowAddNewMealParams)

        self.WindowAddNewMealParams.setStyleSheet("background-color:"+f"{c1}"+";")
        self.l_fats_new_product.setStyleSheet("padding-left:15px;color:"f"{c3}"+";")
        self.btn_add_new_food_params.setStyleSheet("QPushButton#btn_add_new_food_params{color:#fff;border-radius:30px;background-color:#7CC8FF;}\n"
                                                   "QPushButton#btn_add_new_food_params::hover{color:#fff;border-radius:30px;background-color:#52A9FF;}")
        self.l_proteins_new_product.setStyleSheet("padding-left:15px;color:"f"{c3}"+";")
        self.le_fats_new_product.setStyleSheet("QLineEdit#le_fats_new_product{background-color:"f"{c1}"+";border:4px solid #7CC8FF;\n"
                                               "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"+";}")
        self.l_calories_new_product.setStyleSheet("padding-left:15px;color:"f"{c3}"+";")
        self.le_calories_new_product.setStyleSheet("QLineEdit#le_calories_new_product{background-color:"f"{c1}"+";border:4px solid #7CC8FF;\n"
                                                   "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"+";}")
        self.le_carbs_new_product.setStyleSheet("QLineEdit#le_carbs_new_product{background-color:"f"{c1}"+";border:4px solid #7CC8FF;\n"
                                                "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"+";}")
        self.l_carbs_new_product.setStyleSheet("padding-left:15px;color:"f"{c3}"+";")
        self.le_proteins_new_product.setStyleSheet("QLineEdit#le_proteins_new_product{background-color:"f"{c1}"+";border:4px solid #7CC8FF;\n"
                                                   "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"+";}")
        self.le_name_new_product.setStyleSheet("QLineEdit#le_name_new_product{background-color:"f"{c1}"+";border:4px solid #7CC8FF;\n"
                                               "border-radius:30px;padding-left:30px;padding-right:30px;color:"f"{c3}"+";}")
        self.l_name_new_product.setStyleSheet("padding-left:15px;color:"f"{c3}"+";")
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.WindowAddNewMealParams.setWindowTitle(_translate("WindowAddNewMealParams", "КБЖУ нового продукта"))
        self.l_fats_new_product.setText(_translate("WindowAddNewMealParams", "Жиры на 100 гр"))
        self.btn_add_new_food_params.setText(_translate("WindowAddNewMealParams", "Добавить новый продукт"))
        self.l_proteins_new_product.setText(_translate("WindowAddNewMealParams", "Белки на 100 гр"))
        self.l_calories_new_product.setText(_translate("WindowAddNewMealParams", "Калории на 100 гр"))
        self.l_carbs_new_product.setText(_translate("WindowAddNewMealParams", "Углеводы на 100 гр"))
        self.l_name_new_product.setText(_translate("WindowAddNewMealParams", "Название нового продукта"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    from data.fonts import *
    ui = Ui_WindowAddNewMealParams()
    ui.set_fonts(font_regular, font_medium)
    ui.setupUi()
    ui.WindowAddNewMealParams.show()
    sys.exit(app.exec_())
