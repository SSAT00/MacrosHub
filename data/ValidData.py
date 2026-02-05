class ValidData:
    def __init__(self):
        weight_min = 30
        weight_max = 250

        tall_min = 100
        tall_max = 250

        name_min = 3
        name_max = 12

        age_min = 14
        age_max = 90

        self.err = {
            "weight": [
                [f"Bec должен быть в пределах от {weight_min} до {weight_max} кг !", "Введите вес"],
                weight_min, 
                weight_max],
            "tall": [
                [f"Рост должен быть в пределах от {tall_min} до {tall_max}см !", "Введите рост"],
                tall_min,
                tall_max],
            "age": [
                [f"Возраст должен быть в пределах от {age_min} до {age_max} лет !", "Введите возраст"],
                age_min, 
                age_max],
            "name": [
                f"Имя должно быть длиной от {name_min} до {name_max} букв",
                name_min,
                name_max]
        }

    def numbers_is_valid(self, fields, values):
        for field, value in zip(fields, values):
            if value != "":
                if self.err[field][1] > float(value) or float(value) > self.err[field][2]:
                    return self.err[field][0][0]
            else:
                return self.err[field][0][1]
        return "True"
    
    def string_is_valid(self, fields, values):
        for field, value in zip(fields, values):
            if self.err[field][1] > len(value) or len(value) > self.err[field][2]:
                return self.err[field][0]
        return "True"