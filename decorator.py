

class Car:
    def __init__(self) -> None:
        self.color = None
        self.value = 2
        self.dick_R = 13
        self.max_speed = 180
        self.privod = "front/all"
        self.transmission = "mechanical"
        self.kuzov = "sedan/hatchback/liftback"

    # conditioner = True
    # klimat_control = True
    # panoramic_roof = True
    # abs = True


class KlimatControl:
    def __init__(self, car, conditioner) -> None:
        self.car = car
        self.type_climat = conditioner
        self.car.type_climat = self.__setTypeKlimat(conditioner)

    def __setTypeKlimat(self, typeKlimat):
        if typeKlimat == "conditioner" or typeKlimat == "climat_control":
            return typeKlimat
        return None
    

class RoofPanoramic:
    def __init__(self, car, roof_panoramic) -> None:
        self.car = car
        self.roof_panoramic = roof_panoramic
        self.car.roof_panoramic = self.roof_panoramic


pegeout = Car()

KlimatControl(pegeout, "conditioner")
RoofPanoramic(pegeout, "panoramic")

print(vars(pegeout))
