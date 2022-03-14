import time


def test_basket_button(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        button = browser.find_elements_by_css_selector(".btn-add-to-basket")
        assert button != []
    finally:
        browser.quit()
