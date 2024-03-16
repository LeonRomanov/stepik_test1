import time
from selenium.webdriver.common.by import By

def test_button_add_to_cart_presence(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)  # добавлено для демонстрации, можно использовать явные ожидания
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) == 1, f"Expected to find 1 'Add to basket' button, but found {len(button)}"