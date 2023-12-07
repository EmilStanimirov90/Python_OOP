from unittest import TestCase, main


from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Cat", "Cats", "Meow")

    def test_correct_init(self):
        self.assertEqual("Cat", self.mammal.name)
        self.assertEqual("Cats", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_res = self.mammal.make_sound()
        self.assertEqual(f"Cat makes Meow", expected_res)

    def test_get_kingdom(self):
        expected_res = self.mammal.get_kingdom()
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Cat is of type Cats", self.mammal.info())

    if __name__ == "__main__":
        main()
