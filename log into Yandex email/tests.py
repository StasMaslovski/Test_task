from login_page import LoginPage

URL = "https://mail.yandex.ru/"


def test_login(browser):
    login_page = LoginPage(browser, URL)
    login_page.go_to_site()
    login_page.go_to_login_page()
    login_page.check_authorization_title()
    login_page.input_login()
    login_page.press_sign_in_button()
    login_page.input_password()
    login_page.press_sign_in_button()
    login_page.should_be_button_write()
