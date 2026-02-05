import faulthandler
faulthandler.enable()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QMessageBox

from data.Window import Window, json

from data.colors import *
from data.ValidData import ValidData


class Ui_WelcomeWindow(Window):
    def __init__(self):
        Window.__init__(self)
        self.name = ""
        self.weight = 0.0
        self.tall = 0.0
        self.age = 0

        self.dv = ValidData()

        self.WelcomeWindow = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.WelcomeWindow)
        self.btn_next = QtWidgets.QPushButton(self.WelcomeWindow)
        self.btn_finish = QtWidgets.QPushButton(self.WelcomeWindow)
        self.btn_finish.hide()
        self.icon_redapple = QtGui.QIcon()
        self.icon_redapple.addPixmap(QtGui.QPixmap("data/imgs/logo_apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_content = QtWidgets.QFrame(self.WelcomeWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.f_content)
        self.f_UserName = QtWidgets.QFrame(self.f_content)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.f_UserName)
        self.l_UserName = QtWidgets.QLabel(self.f_UserName)
        self.le_UserName = QtWidgets.QLineEdit(self.f_UserName)
        self.f_UserWeight = QtWidgets.QFrame(self.f_content)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.f_UserWeight)
        self.le_UserWeight = QtWidgets.QLineEdit(self.f_UserWeight)
        self.l_UserWeight = QtWidgets.QLabel(self.f_UserWeight)
        self.f_UserTall = QtWidgets.QFrame(self.f_content)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.f_UserTall)
        self.l_UserTall = QtWidgets.QLabel(self.f_UserTall)
        self.le_UserTall = QtWidgets.QLineEdit(self.f_UserTall)
        self.f_UserAge = QtWidgets.QFrame(self.f_content)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.f_UserAge)
        self.l_UserAge = QtWidgets.QLabel(self.f_UserAge)
        self.le_UserAge = QtWidgets.QLineEdit(self.f_UserAge)
        self.l_Welcome = QtWidgets.QLabel(self.WelcomeWindow)

        regex_num = QRegExp(r"^\d{1,3}\.\d{1}$")
        self.validator_weight = QRegExpValidator(regex_num)
        self.le_UserWeight.setValidator(self.validator_weight)

        self.validator_tall = QRegExpValidator(regex_num)
        self.le_UserTall.setValidator(self.validator_tall)

        regex_let = QRegExp(r"^[a-zA-Zа-яА-ЯёЁ]+$")
        self.validator_name = QRegExpValidator(regex_let)
        self.le_UserName.setValidator(self.validator_name)

        self.f_content_2part = QtWidgets.QFrame(self.WelcomeWindow)
        self.gridLayout_2_ = QtWidgets.QGridLayout(self.f_content_2part)
        self.f_sex = QtWidgets.QFrame(self.f_content_2part)
        self.gridLayout_3_ = QtWidgets.QGridLayout(self.f_sex)
        self.rb_male = QtWidgets.QRadioButton(self.f_sex)
        self.rb_female = QtWidgets.QRadioButton(self.f_sex)
        self.f_activity = QtWidgets.QFrame(self.f_content_2part)
        self.gridLayout_4_ = QtWidgets.QGridLayout(self.f_activity)
        self.rb_activity2 = QtWidgets.QRadioButton(self.f_activity)
        self.rb_activity1 = QtWidgets.QRadioButton(self.f_activity)
        self.rb_activity3 = QtWidgets.QRadioButton(self.f_activity)
        self.rb_activity4 = QtWidgets.QRadioButton(self.f_activity)

        self.msg_err = QMessageBox()

    def setupUi1Page(self):
        self.WelcomeWindow.setObjectName("WelcomeWindow")
        self.WelcomeWindow.resize(612, 792)
        self.WelcomeWindow.setMinimumSize(QtCore.QSize(612, 792))
        self.WelcomeWindow.setMaximumSize(QtCore.QSize(612, 792))
        self.WelcomeWindow.setWindowIcon(self.icon_redapple)

        self.gridLayout.setContentsMargins(10, 50, 10, 50)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(70)
        self.gridLayout.setObjectName("gridLayout")

        self.btn_next.setMinimumSize(QtCore.QSize(260, 60))
        self.btn_next.setMaximumSize(QtCore.QSize(260, 60))
        self.font_medium.setPointSize(18)
        self.btn_next.setFont(self.font_medium)
        self.btn_next.setObjectName("btn_next")

        self.gridLayout.addWidget(self.btn_next, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        self.f_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content.setObjectName("f_content")
        self.f_content.setMaximumHeight(470)
        self.f_content.setMinimumHeight(470)

        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 15, 10, 15)

        self.f_UserName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_UserName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_UserName.setObjectName("f_UserName")

        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.font_regular.setPointSize(10)
        self.l_UserName.setFont(self.font_regular)
        self.l_UserName.setObjectName("l_UserName")
        self.gridLayout_3.addWidget(self.l_UserName, 0, 0, 1, 1)

        self.le_UserName.setMinimumSize(QtCore.QSize(400, 60))
        self.le_UserName.setMaximumSize(QtCore.QSize(400, 60))
        self.font_medium.setPointSize(12)
        self.le_UserName.setFont(self.font_medium)
        self.le_UserName.setObjectName("le_UserName")
        self.gridLayout_3.addWidget(self.le_UserName, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.f_UserName, 0, 0, 1, 1)

        self.f_UserWeight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_UserWeight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_UserWeight.setObjectName("f_UserWeight")

        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.le_UserWeight.setMinimumSize(QtCore.QSize(400, 60))
        self.le_UserWeight.setMaximumSize(QtCore.QSize(400, 60))
        self.font_medium.setPointSize(12)
        self.le_UserWeight.setFont(self.font_medium)
        self.le_UserWeight.setObjectName("le_UserWeight")
        self.gridLayout_4.addWidget(self.le_UserWeight, 1, 1, 1, 1)

        self.font_regular.setPointSize(10)
        self.l_UserWeight.setFont(self.font_regular)
        self.l_UserWeight.setObjectName("l_UserWeight")
        self.gridLayout_4.addWidget(self.l_UserWeight, 0, 1, 1, 1)

        self.gridLayout_2.addWidget(self.f_UserWeight, 1, 0, 1, 1)

        self.f_UserTall.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_UserTall.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_UserTall.setObjectName("f_UserTall")

        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.font_regular.setPointSize(10)
        self.l_UserTall.setFont(self.font_regular)
        self.l_UserTall.setObjectName("l_UserTall")
        self.gridLayout_5.addWidget(self.l_UserTall, 0, 0, 1, 1)

        self.le_UserTall.setMinimumSize(QtCore.QSize(400, 60))
        self.le_UserTall.setMaximumSize(QtCore.QSize(400, 60))
        self.font_medium.setPointSize(12)
        self.le_UserTall.setFont(self.font_medium)
        self.le_UserTall.setObjectName("le_UserTall")
        self.gridLayout_5.addWidget(self.le_UserTall, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.f_UserTall, 2, 0, 1, 1)

        self.f_UserAge.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_UserAge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_UserAge.setObjectName("f_UserAge")

        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.font_regular.setPointSize(10)
        self.l_UserAge.setFont(self.font_regular)
        self.l_UserAge.setObjectName("l_UserAge")
        self.gridLayout_6.addWidget(self.l_UserAge, 0, 0, 1, 1)

        self.le_UserAge.setMinimumSize(QtCore.QSize(400, 60))
        self.le_UserAge.setMaximumSize(QtCore.QSize(400, 60))
        self.font_medium.setPointSize(12)
        self.le_UserAge.setFont(self.font_medium)
        self.le_UserAge.setObjectName("le_UserAge")
        self.gridLayout_6.addWidget(self.le_UserAge, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.f_UserAge, 3, 0, 1, 1)
        
        self.gridLayout.addWidget(self.f_content, 1, 0, 1, 3)

        self.l_Welcome.setMinimumSize(QtCore.QSize(0, 64))
        self.l_Welcome.setMaximumSize(QtCore.QSize(16777215, 64))
        self.l_Welcome.setText("")
        self.l_Welcome.setObjectName("l_Welcome")
        self.gridLayout.addWidget(self.l_Welcome, 0, 0, 1, 3)

        self.msg_err.setFont(self.font_regular)
        self.msg_err.setWindowIcon(QtGui.QIcon("data/imgs/err_mark.png"))
        self.msg_err.setWindowTitle(" ")

        self.setupUi2Page()

        self.past_styles()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.WelcomeWindow)

    def setupUi2Page(self):
        self.f_content_2part.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_content_2part.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_content_2part.setObjectName("f_content_2part")
        self.f_content_2part.setMaximumHeight(400)
        self.f_content_2part.setMinimumHeight(400)
        
        self.gridLayout_2_.setContentsMargins(100, 30, 100, 30)
        self.gridLayout_2_.setObjectName("gridLayout_2")
        
        self.f_sex.setMinimumSize(QtCore.QSize(0, 120))
        self.f_sex.setMaximumSize(QtCore.QSize(16777215, 120))
        self.f_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_sex.setObjectName("f_sex")
        
        self.gridLayout_3_.setVerticalSpacing(2)
        self.gridLayout_3_.setObjectName("gridLayout_3")

        self.btn_finish.setMinimumSize(QtCore.QSize(260, 60))
        self.btn_finish.setMaximumSize(QtCore.QSize(260, 60))
        self.font_medium.setPointSize(18)
        self.btn_finish.setFont(self.font_medium)
        self.btn_finish.setObjectName("btn_finish")
        self.gridLayout.addWidget(self.btn_finish, 3, 1, 1, 1)
        
        self.font_regular.setPointSize(9)
        self.rb_male.setFont(self.font_regular)
        self.rb_male.setChecked(True)
        self.rb_male.setObjectName("rb_male")
        self.gridLayout_3_.addWidget(self.rb_male, 0, 0, 1, 1)
        
        self.rb_female.setFont(self.font_regular)
        self.rb_female.setObjectName("rb_female")
        self.gridLayout_3_.addWidget(self.rb_female, 0, 1, 1, 1)
        self.gridLayout_2_.addWidget(self.f_sex, 0, 0, 1, 1)
        
        self.f_activity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_activity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_activity.setObjectName("f_activity")
        
        self.gridLayout_4_.setVerticalSpacing(2)
        self.gridLayout_4_.setObjectName("gridLayout_4")
        
        self.rb_activity2.setFont(self.font_regular)
        self.rb_activity2.setObjectName("rb_activity2")
        self.gridLayout_4_.addWidget(self.rb_activity2, 1, 0, 1, 1)
        
        self.rb_activity1.setFont(self.font_regular)
        self.rb_activity1.setObjectName("rb_activity1")
        self.gridLayout_4_.addWidget(self.rb_activity1, 0, 0, 1, 1)
        
        self.rb_activity3.setFont(self.font_regular)
        self.rb_activity3.setChecked(True)
        self.rb_activity3.setObjectName("rb_activity3")
        self.gridLayout_4_.addWidget(self.rb_activity3, 2, 0, 1, 1)
        
        self.rb_activity4.setFont(self.font_regular)
        self.rb_activity4.setObjectName("rb_activity4")
        self.gridLayout_4_.addWidget(self.rb_activity4, 3, 0, 1, 1)
        self.gridLayout_2_.addWidget(self.f_activity, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.f_content_2part, 1, 0, 1, 3)
        self.f_content_2part.hide()

    def past_styles(self):
        theme = self.read_theme()

        c1, c3 = "", ""

        if theme == "light":
            c1 = light1
            c3 = dark2
            self.l_Welcome.setPixmap(QtGui.QPixmap("data/imgs/welcom_light.png"))
            self.apply_dark_title_bar(0, self.WelcomeWindow)
            self.apply_dark_title_bar(0, self.msg_err)
        else:
            c1 = dark1
            c3 = light2
            self.l_Welcome.setPixmap(QtGui.QPixmap("data/imgs/welcom_dark.png"))
            self.apply_dark_title_bar(1, self.WelcomeWindow)
            self.apply_dark_title_bar(1, self.msg_err)

        self.l_Welcome.setAlignment(QtCore.Qt.AlignCenter)
        
        self.WelcomeWindow.setStyleSheet("QWidget#WelcomeWindow{background-color:"+f"{c1};"+"}")
        self.btn_next.setStyleSheet("QPushButton#btn_next{color:#fff;border-radius:30px;background-color:#7CC8FF;}\n"
                                    "QPushButton#btn_next::hover{color:#fff;border-radius:30px;background-color:#52A9FF;}")
        self.btn_finish.setStyleSheet("QPushButton#btn_finish{color:#fff;border-radius:30px;background-color:#7CC8FF;}\n"
                                      "QPushButton#btn_finish::hover{color:#fff;border-radius:30px;background-color:#52A9FF;}")
        self.l_UserName.setStyleSheet("color:"+f"{c3};")
        self.le_UserName.setStyleSheet("QLineEdit#le_UserName{background-color:"+
                                       f"{c1};border:4px solid #7CC8FF;border-radius:30px;padding-left:30px;padding-right:30px;"+
                                       f"color:{c3};"+"}")
        self.l_UserWeight.setStyleSheet(f"color:{c3};")
        self.le_UserWeight.setStyleSheet("QLineEdit#le_UserWeight{background-color:"+
                                         f"{c1};border:4px solid #7CC8FF;border-radius:30px;padding-left:30px;padding-right:30px;"+
                                         f"color:{c3}"+";}")
        self.l_UserTall.setStyleSheet(f"color:{c3};")
        self.le_UserTall.setStyleSheet("QLineEdit#le_UserTall{background-color:"+
                                       f"{c1};border:4px solid #7CC8FF;border-radius:30px;padding-left:30px;padding-right:30px;"+
                                       f"color:{c3}"+";}")
        self.l_UserAge.setStyleSheet("color:"+f"{c3};")
        self.le_UserAge.setStyleSheet("QLineEdit#le_UserAge{background-color:"+
                                       f"{c1};border:4px solid #7CC8FF;border-radius:30px;padding-left:30px;padding-right:30px;"+
                                       f"color:{c3};"+"}")
        self.msg_err.setStyleSheet("QMessageBox {background-color:"+f"{c1};color:{c3}"+";}"
                                   "QPushButton {background-color:#7CBDFF;"+f"color:#FFF;"+"border-radius: 15px;width: 80px;height: 30px;}"
                                   "QMessageBox QLabel{"+f"color:{c3}"+";}")
        
        self.rb_male.setStyleSheet("QRadioButton#rb_male{color:"+f"{c3}"+";}\n"
                                   "QRadioButton#rb_male::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                   "QRadioButton#rb_male::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                   "QRadioButton#rb_male::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_female.setStyleSheet("QRadioButton#rb_female{color:"+f"{c3}"+";}\n"
                                     "QRadioButton#rb_female::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                     "QRadioButton#rb_female::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                     "QRadioButton#rb_female::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_activity2.setStyleSheet("QRadioButton#rb_activity2{color:"+f"{c3}"+";}\n"
                                        "QRadioButton#rb_activity2::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                        "QRadioButton#rb_activity2::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                        "QRadioButton#rb_activity2::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_activity2.setStyleSheet("QRadioButton#rb_activity2{color:"+f"{c3}"+";}\n"
                                        "QRadioButton#rb_activity2::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                        "QRadioButton#rb_activity2::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                        "QRadioButton#rb_activity2::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_activity1.setStyleSheet("QRadioButton#rb_activity1{color:"+f"{c3}"+";}\n"
                                        "QRadioButton#rb_activity1::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                        "QRadioButton#rb_activity1::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                        "QRadioButton#rb_activity1::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_activity3.setStyleSheet("QRadioButton#rb_activity3{color:"+f"{c3}"+";}\n"
                                        "QRadioButton#rb_activity3::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                        "QRadioButton#rb_activity3::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                        "QRadioButton#rb_activity3::indicator:checked{border:6px solid #7CC8FF;}")
        self.rb_activity4.setStyleSheet("QRadioButton#rb_activity4{color:"+f"{c3}"+";}\n"
                                        "QRadioButton#rb_activity4::indicator{background-color:"+f"{c1}"+";width:18px;height:18px;border-radius:15px;}\n"
                                        "QRadioButton#rb_activity4::indicator:unchecked{border:6px solid #D9D9D9;}\n"
                                        "QRadioButton#rb_activity4::indicator:checked{border:6px solid #7CC8FF;}")

    def check_data_valid(self):
        name = self.le_UserName.text()
        weight = self.le_UserWeight.text()
        tall = self.le_UserTall.text()
        age = self.le_UserAge.text()

        fields = ["name", "weight", "tall", "age"]
        values = [name, weight, tall, age]

        ans = self.dv.string_is_valid([fields[0]], [values[0]])
        
        if ans != "True":
            self.msg_err.setText(ans)
            self.msg_err.exec_()
            return False

        ans = self.dv.numbers_is_valid(fields[1::], values[1::])
        if ans != "True":
            self.msg_err.setText(ans)
            self.msg_err.exec_()
            return False
        
        self.name = name
        self.weight = float(weight)
        self.tall = float(tall)
        self.age = int(age)
        return True
    
    def past_next_page(self):
        self.f_content.close()
        self.f_content_2part.show()
        self.btn_next.hide()
        self.btn_finish.show()
        self.btn_finish.setText("Завершить")

    def get_sex_activity(self):
        sex = "male"
        if self.rb_female.isChecked():
            sex = "female"
        
        act = 1.2
        if self.rb_activity2.isChecked():
            act = 1.375
        elif self.rb_activity3.isChecked():
            act = 1.55
        elif self.rb_activity4.isChecked():
            act = 1.725

        with open("data/params.json", "w") as f:
            data = {"name": self.name, "age": self.age, "weight": self.weight, "tall": self.tall, "sex": sex, "activity": act}
            json.dump(data, f)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "MacrosHub"))
        self.btn_next.setText(_translate("WelcomeWindow", "Далее"))
        self.l_UserName.setText(_translate("WelcomeWindow", "     Имя"))
        self.l_UserWeight.setText(_translate("WelcomeWindow", "    Вес, кг"))
        self.l_UserTall.setText(_translate("WelcomeWindow", "    Рост, см"))
        self.l_UserAge.setText(_translate("WelcomeWindow", "    Возраст, лет"))

        self.rb_male.setText(_translate("WelcomeWindow", "Муж"))
        self.rb_female.setText(_translate("WelcomeWindow", "Жен"))
        self.rb_activity2.setText(_translate("WelcomeWindow", "Легкая активность"))
        self.rb_activity1.setText(_translate("WelcomeWindow", "Сиядчий образ жизни"))
        self.rb_activity3.setText(_translate("WelcomeWindow", "Средняя активность"))
        self.rb_activity4.setText(_translate("WelcomeWindow", "Высокая активность"))
