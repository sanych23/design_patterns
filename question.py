# есть фирма которая строит дома
# у этой фирмы есть типовые проекты домов
# для которых можно дозакказать доп.опции:

class House:
    def __init__(self) -> None:
        self.price = 1000000


class Terrace:
    price = 100000

    def __init__(self, house, terrace_type, volume) -> None:
        if volume and (terrace_type == "soft" or terrace_type == "hard"):
            house.terrace_type = [terrace_type, volume]
            house.price += self.price


class Porch:
    price = 50000
    
    def __init__(self, house, type_porch) -> None:
        if type_porch == "wood" or type_porch == "stone":
            house.type_porch = type_porch
            house.price += self.price


class Heating:
    price = 70000

    def __init__(self, house) -> None:
        house.heating_floor = True
        house.price += self.price


class Ventilation:
    price = 80000

    def __init__(self, house) -> None:
        house.ventilation = True
        house.price += self.price


house = House()
print(vars(house))

Terrace(house, "soft", 1000)
Porch(house, "wood")
Heating(house)
Ventilation(house)
print(vars(house))