from Google_Search.pages.main_page import MainPage
import data


def test_for_google_search(browser):
    main_pg = MainPage(browser, data.main_url)
    main_pg.go_to_site()
    main_pg.search()
    main_pg.should_be_more_than_10_results()
    main_pg.should_be_link_in_results()

