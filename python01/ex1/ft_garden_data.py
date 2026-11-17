#!/usr/bin/env python3
class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(self.name, ":", self.height, "cm,", self.age, "days old")

def ft_garden_data():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()

ft_garden_data()