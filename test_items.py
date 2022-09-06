from selenium.webdriver.common.by import By
import time

def test_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button, "Basket button not found"
    

    
    
