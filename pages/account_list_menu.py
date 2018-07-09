class AccountMenuPage:

    your_list_items = "//div[@id='nav-al-wishlist']//span"

    def __init__(self, driver):
        self.driver = driver

    def get_your_list(self):
        return self.driver.find_elements_by_xpath(self.your_list_items)
