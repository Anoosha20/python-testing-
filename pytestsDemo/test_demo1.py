# any pytest file should start with test_ or end with _test
# pytest method name should start with test
# any code should be wrapped in method only
# method name should have sense
# -k stands for method names execution , -s stands for logs in output , -v stands for more info metadata
# you can run specific file with py.test(filename)
# you can mark(tag) tests @pytest.mark.smoke and then run with -m
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture and make it
# available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and and at the end
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")


def test_secondgreetCreditCard():
    print("goodmorning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
