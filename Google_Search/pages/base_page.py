from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(5)

    def find_elem(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def go_to_site(self):
        self.driver.get(self.url)

    def get_result_number(self, locator):
        result = self.driver.find_element(*locator).text
        for i in result:
            if i.isdigit():
                return int(''.join(result[result.index(i):result.find('(')].split()))

    def press_enter(self, locator):
        self.driver.find_element(*locator).send_keys(u'\ue007')

    def verify_availability_of_link(self, locator, link):
        links_list = []
        for i in self.driver.find_elements(*locator):
            if link in i.text:
                links_list.append(i.text)
                return links_list
