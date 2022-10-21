from models import Toyota

while True:
    print()
    print("1. Add model, engine, color and shift gir car: ")
    print("2. All cars Toyota in list: ")
    print("3. Choose car by engine: ")
    print("4. Change color: ")
    print("5. Quit: ")

    flag = int(input("Chose menu item: "))

    if flag == 1:
        name = input("Car model: ")
        engine = input("Enter the engine (diesel or petrol): ")
        color = input("Add color car: ")
        shift_gir = input("Add shit gir for car - automatic or manual: ")
        toyota = Toyota(name, engine, color, shift_gir)
        toyota.save()

    elif flag == 2:
        Toyota.get_all_cars()

    elif flag == 3:
        Toyota.get_car_engine()

    elif flag == 4:
        Toyota.change_color_car()

    elif flag == 5:
        break


