from pytest import fixture
from utils.driver_provider import DriverProvider
from utils.user_data import UserData

from pages.main_page import MainPage


@fixture()
def driver(request):
    web_driver = DriverProvider.select_driver("Chrome")
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_user_lists_should_be_as_expected(driver):
    driver.get("https://www.amazon.com")

    actual_your_list = MainPage(driver).open_account_list()
    expected_your_lists = UserData.your_list

    assert actual_your_list == expected_your_lists
