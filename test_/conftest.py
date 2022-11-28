import pytest
from selenium import webdriver
from Library.config import Config

@pytest.fixture(params=["Chrome", "Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_Path)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    driver.save_screenshot("test_profile.png")
    driver.close()
