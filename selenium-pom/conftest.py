import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver .maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def navigate_url(request):
        request.cls.driver.get("https://www.jcpenney.com/")


