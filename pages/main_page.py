from selenium.webdriver.common.action_chains import ActionChains
from pages.account_list_menu import AccountMenuPage


class MainPage:

    account_list = "nav-link-accountList"

    def __init__(self, driver):
        self.driver = driver

    def open_account_list(self):
        actions = ActionChains(self.driver)

        self.open_main_page()

        actions.move_to_element(self.driver.find_element_by_id(self.account_list)).perform()
        your_lists = AccountMenuPage(self.driver).get_your_list()
        return [element.get_attribute("innerText") for element in your_lists]

    def open_main_page(self):
        self.driver.get("https://www.amazon.com")