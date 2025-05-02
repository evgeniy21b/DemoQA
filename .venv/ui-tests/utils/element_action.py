from selenium.webdriver.common.by import By

def input_text(driver, locator_type, locator, value):
    element = driver.find_element(locator_type, locator)
    element.click()
    element.send_keys(value)
    return element

def click_element(driver, locator_type, locator):
    element = driver.find_element(locator_type, locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
##