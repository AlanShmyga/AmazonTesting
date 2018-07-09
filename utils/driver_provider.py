from selenium import webdriver


class DriverProvider:

    @staticmethod
    def select_driver(browser_name):
        if browser_name == "Chrome":
            return webdriver.Chrome()
        elif browser_name == "Firefox":
            return webdriver.Firefox()

        raise Exception("No such browser available: " + browser_name)
