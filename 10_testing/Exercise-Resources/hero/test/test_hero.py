from unittest import TestCase, main

from project.hero import Hero


class TestVehicle(TestCase):
    def setUp(self):
        self.hero = Hero("test", 1, 5.5, 5.5)
        self.hero2 = Hero("test2", 1, 5.5, 5.5)

    def test_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(5.5, self.hero.health)
        self.assertEqual(5.5, self.hero.damage)

    def test_battle_enemy_hero_name_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hp_lower_than_zero_raise_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(self.hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))

    def test_battle_enemy_hero_hp_zero_raise_error(self):
        self.hero2.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.hero2)
        self.assertEqual(f"You cannot fight test2. He needs to rest", str(ve.exception))

        self.hero2.health -= 0
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(self.hero2)
        self.assertEqual(f"You cannot fight test2. He needs to rest", str(ve2.exception))

    def test_battle_draw(self):
        expected_result = self.hero.battle(self.hero2)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.hero2.health)
        self.assertEqual("Draw", expected_result)
        self.assertEqual(self.hero.level, self.hero2.level)
        self.assertEqual(self.hero.damage, self.hero2.damage)

    def test_battle_hero_wins(self):
        enemy = Hero("loser", 1, 5.5, 1)
        expected_result = self.hero.battle(enemy)
        self.assertEqual(9.5, self.hero.health)
        self.assertEqual(0, enemy.health)
        self.assertEqual("You win", expected_result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(10.5, self.hero.damage)

    def test_battle_hero_loses(self):
        enemy = Hero("winner", 1, 50, 10)
        expected_result = self.hero.battle(enemy)
        self.assertEqual(-4.5, self.hero.health)
        self.assertEqual(49.5, enemy.health)
        self.assertEqual("You lose", expected_result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(15, enemy.damage)

    def test_str(self):
        expected_result = f"Hero test: 1 lvl\n" \
               f"Health: 5.5\n" \
               f"Damage: 5.5\n"
        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()
