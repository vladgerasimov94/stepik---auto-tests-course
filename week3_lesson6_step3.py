import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_parametrize(browser, task):
    link = f"https://stepik.org/lesson/{task}/step/1"
    browser.get(link)
    browser.find_element_by_css_selector('#ember67')




# answer = math.log(int(time.time()))