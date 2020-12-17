import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_Program():
    msg = " hello"
    assert msg == "hi", "test failed beacause strings do not match"

def test_secondCreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "addition do not match"
