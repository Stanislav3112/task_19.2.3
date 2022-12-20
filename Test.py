import pytest
from app. calc import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) ==2
        assert self.calc.subtraction(self, 4, 3) ==1
        assert self.calc.division(self, 4, 2) ==2
        assert self.calc.multiply(self, 5, 5) == 25

    # def test_adding_unsucces(self):
    #     assert self.calc.adding(self, 1, 1) ==3
    #     assert self.calc.subtraction(self, 4, 1) ==2


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print("Выполнение метода Teardown")
