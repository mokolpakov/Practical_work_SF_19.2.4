import pytest

from app.Calculator import Calculator


class TestCalculator:

    def setup(self):
        self.Calculator = Calculator

    def test_multiply(self):
        assert self.Calculator.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.Calculator.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.Calculator.subtraction(self, 3, 2) == 1

    def test_adding(self):
        assert self.Calculator.adding(self, 1, 4) == 5


