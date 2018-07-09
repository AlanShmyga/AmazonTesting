from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


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
    
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element_by_id("nav-link-accountList")).perform()
    your_lists = driver.find_elements_by_xpath("//div[@id='nav-al-wishlist']//span")
    actual_your_list = [element.get_attribute("innerText") for element in your_lists]

    assert actual_your_list == expected_your_lists