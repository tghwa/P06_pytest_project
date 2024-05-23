from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 5
        b = 3
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 2
        assert result == expected

    def test_multiply(self):
        a = 10
        b = 2
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 20
        assert result == expected

    def test_divide(self):
        a = 20
        b = 5
        cal = Calculator()

        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)
