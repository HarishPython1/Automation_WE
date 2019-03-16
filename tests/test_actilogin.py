from selenium import webdriver
import time
from pages.loginpage import LoginPage1
def test_launch_browser():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Users/BTM-FAC/PycharmProjects/Automation/drivers/chromedriver.exe")
    driver.get("http://localhost:8097/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)
def test_login():
    #driver.find_element_by_id("username").send_keys("admin")
    lp=LoginPage1(driver)
    lp.enter_un()
    lp.enter_pwd()

    #driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath("//*[text()='Login ']").click()
def test_logout():
    time.sleep(5)
    driver.find_element_by_xpath("//*[text()='Logout']").click()
