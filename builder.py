class Home:
    def __init__(self) -> None:
        self.color = "black"
        self.price = 2000000


class BuildHome:
    def __init__(self) -> None:
        self.home = Home()

    def fundament(self, fundament_type: str):
        self.home.fundament_type = fundament_type
        return self

    def one_floor(self, one_floor: bool):
        self.home.one_floor = one_floor
        return self

    def two_floor(self, two_floor: bool):
        self.home.two_floor = two_floor
        return self

    def roof(self, roof_type: str):
        self.home.roof_type = roof_type
        return self
    
    def build(self):
        return self.home


mihaHouse = BuildHome().fundament("lenta").one_floor(True).roof("ruberoid").build()

print(vars(mihaHouse))
