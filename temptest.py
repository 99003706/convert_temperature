import pytest
from temperature1 import Temperature


@pytest.fixture
def temp1():
    return Temperature(65)


@pytest.fixture
def temp2():
    return Temperature(80)


def test_add(temp1, temp2):
    res = temp1 + temp2
    assert Temperature(145) == res


def test_convert(temp1, temp2):
    assert temp1.convert() == 149
    assert temp2.convert() == 176


def test_equal(temp1, temp2):
    assert (temp1 == temp2) == False


def test_lesser(temp1, temp2):
    assert (temp1 < temp2) == True
