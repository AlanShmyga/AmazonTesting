from pytest import fixture
from selenium import webdriver

from pages.main_page import MainPage


@fixture()
def driver(request):
    web_driver = webdriver.Chrome()
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_user_lists_should_be_as_expected(driver):
    expected_your_lists = ["Create a List",
                           "Find a List or Registry",
                           "Find a Gift",
                           "Save Items from the Web",
                           "Wedding Registry",
                           "Baby Registry",
                           "Friends & Family Gifting",
                           "Pantry Lists",
                           "Your Hearts",
                           "Explore Idea Lists",
                           "Explore Shop by Look",
                           "Explore Showroom"]

    driver.get("https://www.amazon.com")

    actual_your_list = MainPage(driver).open_account_list()

    assert actual_your_list == expected_your_lists
