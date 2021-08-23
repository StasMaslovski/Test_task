from Google_Search.pages.base_page import BasePage
from Google_Search import locators
from Google_Search import data


class MainPage(BasePage):

    def search(self):
        self.find_elem(locators.FORM).send_keys(data.searching_phrase)
        self.press_enter(locators.FORM)

    def should_be_more_than_10_results(self):
        assert self.get_result_number(locators.RESULT) > 10, \
               'number of results should be more than 10'

    def should_be_link_in_results(self):
        assert self.verify_availability_of_link(locators.LINKS, data.link), \
            'result should contain mvideo.ru '