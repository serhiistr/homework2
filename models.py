import  json

class Toyota:
    file = "toyota.json"
    # name = "Toyota"

    def __init__(self, engine, color, shift_gir):
        # self.name = name
        self.engine = engine
        self.color = color
        self.shift_gir = shift_gir

    @classmethod
    def get_data(cls):
        file = open(cls.file)
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_cars(cls):
        data = cls.get_data()
        for car in data:
            print(car["engine"], car["color"], car["shift_gir"])

    def save(self):
        data = self.get_data()
        new_car = {"engine": self.engine, "color": self.color, "shift_gir": self.shift_gir}
        if len(data) > 0:
            new_car["id"] = data[-1]["id"] + 1
        else:
            new_car["id"] = 1
        data.append(new_car)
        file = open(self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)
