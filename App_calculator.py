import json
import datetime

class TodaysFood:
    def __init__(self):
        self.date_from_file = ""
        self.todays_date = str(datetime.date.today())
        self.calories = 0
        self.proteins = 0
        self.fats = 0
        self.carb = 0
    
    def read_file_todays_food(self):
        with open("data/todays_food.json", "r") as f:
            data = json.load(f)
        
        if data["date"] == self.todays_date:
            self.past_data_cpft(data)
        else:
            self.past_tomorrows_food_on_file(data)

    def past_data_cpft(self, data):
        self.date_from_file = data["date"]
        self.calories = data["calories"]
        self.protins = data["proteins"]
        self.fats = data["fats"]
        self.carb = data["carbs"]

    def past_tomorrows_food_on_file(self, data):
        date_from_file = data["date"]
        calories = data["calories"]
        proteins = data["proteins"]
        fats = data["fats"]
        carb = data["carbs"]
        with open("data/food_progress.json", "r") as f:
            old_data = json.load(f)
        old_data["dates"].append(date_from_file)
        old_data["calories"].append(calories)
        old_data["proteins"].append(proteins)
        old_data["fats"].append(fats)
        old_data["carbs"].append(carb)
        with open("data/food_progress.json", "w") as f:
            json.dump(old_data, f)

        with open("data/todays_food.json", "w") as f:
            data_to_write = {"date": f"{self.todays_date}", "calories": 0, "proteins": 0, "fats": 0, "carbs": 0}
            json.dump(data_to_write, f)

    

class Calculator(TodaysFood):
    def __init__(self):
        TodaysFood.__init__(self)
        self.calories_need = 0
        self.proteins_need = 0
        self.fats_need = 0
        self.carbs_need = 0
        self.mass = 0
        
    def count_CPFC_male(self, weight, tall, age, activity):
        res = 10*weight+6.25*tall-5*age+5
        self.calories_need = int(res * activity)
        self.proteins_need = int(self.calories_need * 0.3 / 4)
        self.fats_need = int(self.calories_need * 0.3 / 9)
        self.carbs_need = int(self.calories_need * 0.4 / 4)

    def count_CPFC_female(self, weight, tall, age, activity):
        res = 10*weight+6.25*tall-5*age-161
        self.calories_need = int(res * activity)
        self.protein_need = int(self.calories_need * 0.3 / 4)
        self.fats_need = int(self.calories_need * 0.3 / 9)
        self.carbs_need = int(self.calories_need * 0.4 / 4)

    def run_calculations(self):
        with open("data/params.json", "r") as f:
            params = json.load(f)
        self.mass = params["weight"]
        if params["sex"] == "male":
            self.count_CPFC_male(params["weight"], params["tall"], params["age"], params["activity"])
        else:
            self.count_CPFC_female(params["weight"], params["tall"], params["age"], params["activity"])


if __name__ == "__main__":
    print(str(datetime.date.today()))