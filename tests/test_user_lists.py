from utils.user_data import UserData

from pages.main_page import MainPage


def test_user_lists_should_be_as_expected(driver):

    actual_your_list = MainPage(driver).open_account_list()
    expected_your_lists = UserData.your_list

    assert actual_your_list == expected_your_lists
