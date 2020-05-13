
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

    def test_with_complete_input_12(self):
        dif = roll_functions.get_num_dices('12d10>10')
        assert(dif == 12)

    def test_with_missing_type(self):
        dif = roll_functions.get_num_dices('10')
        assert(dif == 10)

class TestBuildResults(TestCase):
    
    def test_simple_success_checks(self):
        result = roll_functions.success_checks([4,5,6], 6)
        assert(result == [])
        result = roll_functions.success_checks([4,5,6], 5)
        assert(result == [6])
        result = roll_functions.success_checks([4,5,6], 5, abouveOnly=False)
        assert(result == [5, 6])

    def test_success_checks_with_neg_crits(self):
        result = roll_functions.crit_failures([4,5,6])
        assert(result == [])
        result = roll_functions.crit_failures([1,5,6])
        assert(result == [1])
        result = roll_functions.crit_failures([1,5,1])
        assert(result == [1, 1])

    def test_critical_balance(self):
        dificulty, all_dices  = 10, [1,2,3,4,5,6,7,9,10]
        success = roll_functions.success_checks(all_dices, 6)
        crits = roll_functions.crit_success(success, dificulty)
        neg_crit = roll_functions.crit_failures(all_dices)

        assert(success == [7,9,10])
        assert(crits == [10])
        assert(neg_crit == [1])
