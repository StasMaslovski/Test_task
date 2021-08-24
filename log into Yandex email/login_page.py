from base_page import BasePage
import locators


class LoginPage(BasePage):
    def go_to_login_page(self):
        self.go_to_site()
        self.find_elem(locators.SIGN_IN_BUTTON).click()

    def check_authorization_title(self):
        assert self.get_title() == 'Авторизация'

    def input_login(self):
        self.find_elem(locators.ID_FORM).send_keys('+375447403005')

    def input_password(self):
        self.find_elem(locators.PASSWORD).send_keys('mns161015')

    def press_sign_in_button(self):
        self.find_elem(locators.SUBMIT).click()

    def check_mail_page_title(self):
        print(self.get_title())

    def should_be_button_write(self):
        self.exist_check(locators.BUTTON_WRITE)
