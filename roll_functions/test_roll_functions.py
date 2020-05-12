import pytest
from unittest import TestCase
from roll_functions import roll_functions


class RollFunctionsTest(TestCase):

    def test_get_difficulty_simple(self):
        dif = roll_functions.get_difficulty('whatever > 10')
        assert dif == 10, "expected dificulty result to be 10"

    def test_get_difficulty_ignore_extra_stuff(self):
        dif = roll_functions.get_difficulty('whatever > 10 + 10')
        assert dif == 10, "expected dificulty result to be 10"
