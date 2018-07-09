from pytest import fixture
from utils.driver_provider import DriverProvider


@fixture()
def driver(request):
    web_driver = DriverProvider.select_driver("Chrome")
    request.addfinalizer(web_driver.quit)
    return web_driver
