import pytest
from src.calculator import Calculator

@pytest.fixture(autouse=True)
def print_test_name(request):
    """Print the name of the test being executed"""
    print(f"\n\n\nRunning test: {request.node.name}\n\n\n")

@pytest.fixture
def calculator(request):
    """Basic calculator fixture"""
    max_history_size = getattr(request, 'param', None)
    return Calculator(max_history_size)

@pytest.fixture
def calculator_with_history(calculator):
    """Calculator fixture with some pre-recorded history"""
    calculator.add(2, 3)
    calculator.multiply(4, 5)
    return calculator

@pytest.fixture(params=[
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (10, 20, 30)
])
# ], ids=['positive_numbers', 'zeros', 'negative_numbers', 'large_numbers'])
def add_test_data(request):
    """Parameterized fixture for addition tests"""
    return request.param
