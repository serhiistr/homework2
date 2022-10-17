from models import Toyota

while True:
    print("1. Add engine, color and shift gir car")
    print("2. Oll cars Toyota in list: ")

    flag = int(input("Chose menu item: "))

    if flag == 1:
        engine = float(input("engine in cm3 (example - 1.5): "))
        color = input("Add color car: ")
        shift_gir = input("Add shit gir for car - automatic or manual: ")
        toyota = Toyota(engine, color, shift_gir)
        toyota.save()

    elif flag == 2:
        Toyota.get_all_cars()
