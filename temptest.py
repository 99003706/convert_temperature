import pytest
from temp import Temperature


@pytest.fixture
def get_t1():
    return Temperature(35)


@pytest.fixture
def get_t2():
    return Temperature(22)


def test_add(get_t1, get_t2):
    res = get_t1 + get_t2
    assert Temperature(57) == res


def test_convert(get_t1, get_t2):
    assert get_t1.convert() == 95
    assert get_t2.convert() == 71.6


def test_equal(get_t1, get_t2):
    assert (get_t1 == get_t2) == False


def test_lesser(get_t1, get_t2):
    assert (get_t1 < get_t2) == False
