import pytest

# Fixture with setup and teardown
@pytest.fixture
def setup_teardown_example():
    # Setup
    print("\nSetting up resource")
    data = 'resource'
    yield data
    # Teardown
    print("\nCleaning up resource")
    data = None
    print(f'Data is now {data}')
