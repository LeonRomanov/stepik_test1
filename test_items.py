import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_button_text(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button is not None, "Button not found"