from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from ..utils.driver_setup import create_driver
from ..utils.element_action import input_text
from ..utils.element_action import click_element




driver = create_driver()
driver.get("https://demoqa.com/elements")


click_element(driver, By.ID, "item-0")

input_text(driver, By.XPATH, "//input[@type ='text']", "Evgeniy")
input_text(driver, By.XPATH, "//input[@type ='email']", "bererere@ya.com")
input_text(driver, By.XPATH, "//textarea[@placeholder ='Current Address']", "Moscow city, Pushkina street, Kolotushkina 9")
input_text(driver, By.ID, "permanentAddress", "SPB, Nevskyi prospect 1")

click_element(driver, By.ID, "submit")



time.sleep(30)
#id =item-0



