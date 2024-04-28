from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


# def test_login_with_valid_credentiasl():
#
#     driver = webdriver.Chrome()
#     driver.get("https://tutorialsninja.com/demo/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
#     driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
#     driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("amotooricap1@gmail.com")
#     driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("12345")
#     driver.find_element(By.XPATH,"//input[@value='Login']").click()
#     assert driver.find_element(By.LINK_TEXT,"Edit your account information")
#     driver.quit()

def test_login_with_valid_credentiasl():

    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("amotooricap1@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("12345")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    assert driver.find_element(By.LINK_TEXT,"Edit your account information")
    driver.quit()
#
# def test_login_with_valid_email_and_invalid_password():
#     driver = webdriver.Chrome()
#     driver.get("https://tutorialsninja.com/demo/")
#     driver.maximize_window()
#     driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
#     driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("amotooricap1@gmail.com")
#     driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345547")
#     driver.find_element(By.XPATH, "//input[@value='Login']").click()
#     expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
#     assert driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
#         expected_warning_message)
#     driver.quit()
#
# def test_login_without_entering_credentisal():
#     driver = webdriver.Chrome()
#     driver.get("https://tutorialsninja.com/demo/")
#     driver.maximize_window()
#     driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
#     driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(generate_email_with_time_stamp())
#     driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("")
#     driver.find_element(By.XPATH, "//input[@value='Login']").click()
#     expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
#     assert driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
#         expected_warning_message)
#     driver.quit()
#
# def generate_email_with_time_stamp():
#     time_stamp =datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     return "amotoori"+time_stamp+"@gmail.com"
