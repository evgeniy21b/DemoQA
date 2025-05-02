from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def create_driver():
    chrome_driver_path = r"C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver