
from unittest import TestCase
from app.dice_commands.roll_functions import roll_functions

class TestGetDificulty(TestCase):

    def test_simple(self):
        dif = roll_functions.get_difficulty('>10')
        assert(dif == 10)

    def test_with_complete_input(self):
        dif = roll_functions.get_difficulty('10d10>10')
        assert(dif == 10)

    def test_with_missing_dificulty(self):
        dif = roll_functions.get_difficulty('10d10')
        assert(dif == 0)

class TestGetTypeOfDice(TestCase):

    def test_simple(self):
        dif = roll_functions.get_type_dices('10d10')
        assert(dif == 10)

    def test_with_complete_input(self):
        dif = roll_functions.get_type_dices('10d10>10')
        assert(dif == 10)

    def test_with_missing_type(self):
        dif = roll_functions.get_type_dices('10')
        assert(dif == 0)

class TestGetNumberOfDices(TestCase):
    def test_simple(self):
        dif = roll_functions.get_num_dices('10d10')
        assert(dif == 10)

    def test_with_complete_input(self):
        dif = roll_functions.get_num_dices('10d10>10')
        assert(dif == 10)

    def test_with_missing_type(self):
        dif = roll_functions.get_num_dices('10')
        assert(dif == 10)