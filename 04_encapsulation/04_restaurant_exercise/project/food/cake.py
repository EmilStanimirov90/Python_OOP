from project import Dessert


class Cake(Dessert):
    GRAMS = 25
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES )
