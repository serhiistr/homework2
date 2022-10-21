import json


class Toyota:
    file = "toyota.json"

    def __init__(self, name, engine, color, shift_gir):
        self.name = name
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
            print(car["id"], car["name"], car["engine"], car["color"], car["shift_gir"])


    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                if id == el["id"]:
                    for field in fields:
                        print(el[field])
                    break
                elif id != len(el):
                    print("Not found car ID")
                    break

    def save(self):
        data = self.get_data()
        new_car = {"name": self.name, "engine": self.engine, "color": self.color,
                   "shift_gir": self.shift_gir}
        if len(data) > 0:
            new_car["id"] = data[-1]["id"] + 1
        else:
            new_car["id"] = 1
        data.append(new_car)
        file = open(self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)


    @classmethod
    def change_color_car(cls):
        Toyota.get_all_cars()
        id_color = int(input("Enter ID car for change color: "))
        new_color = input("Enter new color car: ")
        data = cls.get_data()
        counter = 0
        for col in data:
            counter = counter + 1
            if id_color == counter:
                col["color"] = new_color
        file = open(cls.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def get_car_engine(cls):
        data = cls.get_data()
        choice_engine = input("Select engine your prefer (diesel or petrol): ")
        for col in data:
            if col["engine"] == choice_engine:
                print(col["id"], col["name"], col["engine"], col["color"], col["shift_gir"])
        id_choice = int(input("Enter the id of the car you like: "))
        for col in data:
            if col["id"] == id_choice:
                print("Your choice: ", col["id"], col["name"], col["engine"], col["color"], col["shift_gir"])

