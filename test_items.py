import time


def test_find_add_basket_button_on_the_multilanguage_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    basket = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert basket, "Button is not found"

