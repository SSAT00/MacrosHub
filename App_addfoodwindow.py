from AddFoodWindow import *
import json
import os

class AppAddFood:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        from data.fonts import font_regular as regular, font_medium as medium
        self.ui_add_food = Ui_WindowAddMeal()
        self.ui_add_food.set_fonts(regular, medium)
        self.ui_add_food.setupUi()
        self.products = {}
        self.names = []

    def run_app(self):
        self.read_products_file()
        self.ui_add_food.WindowAddMeal.show()
        self.ui_add_food.le_FoodName.textChanged.connect(self.search_field_changed)
        self.ui_add_food.btn_choise1.clicked.connect(lambda: self.set_text_from_btn(self.ui_add_food.btn_choise1.text()))
        self.ui_add_food.btn_choise2.clicked.connect(lambda: self.set_text_from_btn(self.ui_add_food.btn_choise2.text()))
        self.ui_add_food.btn_choise3.clicked.connect(lambda: self.set_text_from_btn(self.ui_add_food.btn_choise3.text()))
        sys.exit(self.app.exec_())

    def read_products_file(self):
        with open("data/products.json", "r", encoding="utf-8") as f:
            self.products = json.load(f)
        for name in self.products:
            self.names.append(name)

    def get_trigrams(self, text):
        text = text.lower()
        return [text[i:i+3] for i in range(len(text) - 2)]
        
    def smart_find(self, limit=3):
        query = self.ui_add_food.le_FoodName.text().lower()
        if query != "":
            if len(query) < 3:
                results = [name for name in self.names if query in name.lower()]
                return results[:limit]
            query_trigrams = set(self.get_trigrams(query))
            scored_results = []
            for name in self.names:
                name_lower = name.lower()
                name_trigrams = self.get_trigrams(name_lower)
                matches = sum(1 for tri in query_trigrams if tri in name_trigrams)
                if matches > 0:
                    scored_results.append((name, matches))
            scored_results.sort(key=lambda x: x[1], reverse=True)
            return [item[0] for item in scored_results[:limit]]
        else:
            return ['', '', '']
    
    def search_field_changed(self):
        variants = self.smart_find()
        while len(variants) < 3:
            variants.append("")
        self.ui_add_food.btn_choise1.setText(variants[0])
        self.ui_add_food.btn_choise2.setText(variants[1])
        self.ui_add_food.btn_choise3.setText(variants[2])

    def set_text_from_btn(self, txt):
        if txt != "":
            self.ui_add_food.le_FoodName.setText(txt)

    def add_todays_food(self):
        name = self.ui_add_food.le_FoodName.text()
        weight = self.ui_add_food.le_FoodWeight.text()

    def open_window_add_new_food_params():
        pass
        



if __name__ == "__main__":
    os.system('chcp 65001')
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    app = AppAddFood()
    app.run_app()