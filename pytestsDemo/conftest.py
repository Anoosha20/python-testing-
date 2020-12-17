import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will execte last")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["rahul", "shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("IE","rahul")])
def crossBrowser(request):
    return request.param