import pytest
from Problem_1 import multipleOfInteger
from Problem_1 import sumOfNaturalsBelow

@pytest.mark.parametrize("test_input", [3, 9, 99, -33])
def test_MultipleOfThree(test_input):
    assert multipleOfInteger(test_input, 3)


@pytest.mark.parametrize("test_input", [5, 100, 8000, -89])
def test_NotAMultipleOfThree(test_input):
    assert not multipleOfInteger(test_input, 3)


@pytest.mark.parametrize("test_input", [5, 100, 7000, -5500])
def test_MultipleOfFive(test_input):
    assert multipleOfInteger(test_input, 5)


@pytest.mark.parametrize("test_input", [7, 99, 10001, -59])
def test_NotAMultipleOfFive(test_input):
    assert not multipleOfInteger(test_input, 5)


def test_SumNaturalNumbersBelow10():
    assert sumOfNaturalsBelow(10) == 23

def test_SumNaturalNumbersBelow1000():
    assert sumOfNaturalsBelow(1000) == 233168
