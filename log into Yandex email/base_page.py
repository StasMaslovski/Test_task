from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(5)

    def find_elem(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(EC.visibility_of_element_located(locator))

    def go_to_site(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def exist_check(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
