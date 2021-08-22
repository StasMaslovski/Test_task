from Google_Search.pages.base_page import BasePage
from Google_Search import locators
from Google_Search import data


class MainPage(BasePage):

    def checking_up_the_searcher(self):
        self.find_elem(locators.FORM).send_keys(data.searching_phrase)
        self.press_enter(locators.FORM)
        assert self.get_result_number(locators.RESULT) > 10, \
            'number of results should be more than 10'
        assert self.verify_availability_of_link(locators.LINKS, data.link), \
            'result should contain mvideo.ru '
