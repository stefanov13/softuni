from unittest import TestCase, main
from project.hero import Hero


class HeroTesting(TestCase):
    def setUp(self):
        self.hero = Hero("Penka", 4, 33.5, 7.5)
        self.enemy_hero = Hero("Lazer", 2, 20.5, 7.5)

    def test_class_attributes_for_correct_value_types(self):
        self.assertIs(str, type(self.hero.username))
        self.assertIs(float, type(self.hero.health))
        self.assertIs(float, type(self.hero.damage))
        self.assertIs(int, type(self.hero.level))

    def test_initialising_correctly(self):
        self.assertEqual("Penka", self.hero.username)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(33.5, self.hero.health)
        self.assertEqual(7.5, self.hero.damage)

    def test_battle_raise_exception_when_enemy_is_same_as_user(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_hero_health_raise_value_error(self):
        self.hero.health = 0 
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_zero_enemy_hero_health_raise_value_error(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight Lazer. He needs to rest", str(ve.exception))
    
    def test_battle_if_health_of_hero_and_enemy_hero_is_zero(self):
        self.hero.health = 15
        self.enemy_hero.health = 30
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_if_enemy_hero_health_got_zero_hero_won(self):
        self.enemy_hero.health = 30
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(23.5, self.hero.health)
        self.assertEqual(12.5, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_if_enemy_hero_won_hero_health_got_zero(self):
        self.hero.health = 15
        self.enemy_hero.health = 35
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(3, self.enemy_hero.level)
        self.assertEqual(10, self.enemy_hero.health)
        self.assertEqual(12.5, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_correct_message__str__method(self):
        self.assertEqual(
            "Hero Penka: 4 lvl\n"
            "Health: 33.5\n"
            "Damage: 7.5\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()
