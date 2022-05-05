from selenium import webdriver
import pytest
import time


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/aagjo/AppData/Local/Programs/Python/Python39/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe")
    time.sleep(2)
    driver.maximize_window()
    yield
    driver.implicitly_wait(100)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    driver.find_element_by_id("report").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_id("btnsignout").click()
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test Completeed...")

def test_signin(test_setup):
    driver.get("http://127.0.0.1:8000/signin")
    driver.find_element_by_id("username").send_keys("Aum")
    driver.find_element_by_id("pass1").send_keys("123")
    driver.find_element_by_id("btnsignin").click()

#def test_teardoen():
#    driver.implicitly_wait(100)
#    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#    driver.implicitly_wait(100)
#    driver.find_element_by_id("report").click()
#    driver.implicitly_wait(100)
#    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#    driver.implicitly_wait(100)
#    driver.find_element_by_id("btnsignout").click()
#    driver.implicitly_wait(100)
#    driver.close()
#    driver.quit()
#    print("Test Completeed...")
