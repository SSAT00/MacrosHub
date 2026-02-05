from PyQt5.QtGui import QFontDatabase, QFont


font_id_regular = QFontDatabase.addApplicationFont("data/fonts/Montserrat-Regular.ttf")
font_regular = QFont(QFontDatabase.applicationFontFamilies(font_id_regular)[0])
font_id_medium = QFontDatabase.addApplicationFont("data/fonts/Montserrat-Medium.ttf")
font_medium = QFont(QFontDatabase.applicationFontFamilies(font_id_medium)[0])