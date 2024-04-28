from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register_with_mandatory_fields():
    driver=webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
    driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("rajeev")
    driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("das")
    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.XPATH,"//input[@id='input-telephone']").send_keys("895647859")
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("1234568")
    driver.find_element(By.XPATH,"//input[@id='input-confirm']").send_keys("1234568")
    driver.find_element(By.XPATH,"//input[@name='agree']").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()


def test_register_all_fields():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("rajeev")
    driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("das")
    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("895647859")
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("1234568")
    driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("1234568")
    driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    driver.find_element(By.XPATH, "//input[@name='agree']").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"


