from selenium import webdriver
from pytest import fixture
import pytest

username = "deepakchowbey8"  # Replace the username
access_key = "zp3rTCmyZCezPP0iquDonHq0gtwGmo8bdI2B2e3762tdmXmDIF"  # Replace the access key


browsers = [
{
    "build": 'Lambdatest - Selenium 101 Certification - Deepak Chowbey',  # Change your build name here
    "name": 'Assignment Selenium 101 - Date - 10 Nov 2021 to 11 Nov 2021',  # Change your test name here
    "platform": 'MacOS Big sur',  # Change your OS version here
    "browserName": 'Chrome',  # Change your browser here
    "version": 'latest',  # Change your browser version here
    "console": True,
    "network": True,
    "visual": True,
},
{
        "build": 'Lambdatest - Selenium 101 Certification - Deepak Chowbey',  # Change your build name here
        "name": 'Assignment Selenium 101 - Date - 10 Nov 2021 to 11 Nov 2021',  # Change your test name here
        "platform": 'WIN10',  # Change your OS version here
        "browserName": 'MicrosoftEdge',  # Change your browser here
        "version": 'latest',  # Change your browser version here
        "console": True,
        "network": True,
        "visual": True,
    }
]

@fixture()
def get_browser():
    driver = webdriver.Firefox(executable_path="/Users/dchowbey/PycharmProjects/SeleniumLambda/drivers/geckodriver")
    yield driver
    driver.quit()


@fixture(params=browsers)
def get_remote_driver(request):
    caps = request.param
    driver = webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
                              desired_capabilities=caps)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

