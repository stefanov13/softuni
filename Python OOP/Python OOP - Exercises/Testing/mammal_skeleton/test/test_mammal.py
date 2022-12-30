from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Govedo', 'Cow', 'Moo')


    def test_correct_initializing(self):
        self.assertEqual('Govedo', self.mammal.name)
        self.assertEqual('Cow', self.mammal.type)
        self.assertEqual('Moo', self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_return_correctly_message(self):
        result = self.mammal.make_sound()
        self.assertEqual("Govedo makes Moo", result)

    def test_get_kingdom_correctly_message(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_geting_info_returns_correctly_message(self):
        result = self.mammal.info()
        self.assertEqual("Govedo is of type Cow", result)


if __name__ == "__main__":
    main()
