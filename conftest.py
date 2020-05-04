import pytest

@pytest.fixture
def input_value():
    input = 30
    return input

@pytest.fixture
def supply_url():
    url = "https://api.github.com"
    return url

