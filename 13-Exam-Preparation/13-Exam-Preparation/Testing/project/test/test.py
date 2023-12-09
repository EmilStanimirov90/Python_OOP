from project.second_hand_car import SecondHandCar

from unittest import TestCase, main

class TestSecondHandCar(TestCase):

    def setUp(self):
        car = SecondHandCar("testmodel", "test", 100, 10000)
