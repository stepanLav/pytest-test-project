import pytest

# Test using setup/teardown fixture
def test_with_setup_teardown(setup_teardown_example):
    print('Do any tests here')
    assert setup_teardown_example == "resource"

# Skip test example
@pytest.mark.skip(reason="This test is not ready yet")
def test_future_feature(calculator):
    pass

# Conditional skip
@pytest.mark.skipif(
    condition=True,  # Replace with actual condition
    reason="Skipped due to condition"
)
def test_conditional_feature(calculator):
    pass

# Expected failure
@pytest.mark.xfail(reason="Known bug - will fix later")
def test_known_bug(calculator):
    assert calculator.add(0.1, 0.2) == 0.3  # Will fail due to floating-point precision

def test_no_fixture(lol):
    assert lol == 'lol'