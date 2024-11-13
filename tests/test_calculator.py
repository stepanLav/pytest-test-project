import pytest

# Basic test
def test_add(calculator):
    assert calculator.add(1, 2) == 3

# Parameterized test using @pytest.mark.parametrize
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-2, -3, 6),
    (10, 10, 100)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

# Parameterized test using fixture
def test_add_parameterized(calculator, add_test_data):
    a, b, expected = add_test_data
    assert calculator.add(a, b) == expected

# Testing exceptions
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as exc_info:
        calculator.divide(1, 0)
    assert str(exc_info.value) == "Cannot divide by zero"

# Test using marks for categorization
@pytest.mark.slow
def test_large_numbers(calculator):
    assert calculator.multiply(1000, 1000) == 1000000

# Test using the history feature
def test_history(calculator_with_history):
    assert len(calculator_with_history.history) == 2
    assert calculator_with_history.history[0] == "2 + 3 = 5"
    assert calculator_with_history.history[1] == "4 * 5 = 20"

# Test reinitialize nested fixtures
@pytest.mark.parametrize('calculator', [1], indirect=True)
def test_reinitialize_nested_fixtures(calculator_with_history):
    assert len(calculator_with_history.history) == 1
