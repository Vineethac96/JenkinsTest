'''Create Global Pytest Fixture using conftest.py file
By doing so, we define a fixture in conftest.py and use it within for the tests within that directory, and no need to write fixtures again and again in every test file


similar way for test_fixture_params, we create a conftest and run only tests without any fixtures in that file
Simple example as input is common for all tests'''

# import pytest

# @pytest.fixture
# def input_total():
#     total = 100
#     return total


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

#instead of writing diff fixture for diff browsers, we can optimize using params
@pytest.fixture(params=["chrome", "firefox"],scope='class') #this fixture is applied for 1st-chrome and 2nd-firefox
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
