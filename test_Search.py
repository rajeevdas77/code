from selenium import webdriver
from selenium.webdriver.common.by import By



def test_search_for_a_valid_product():
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//input[@class='form-control input-lg']").send_keys("HP")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    driver.quit()


def test_search_for_a_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//input[@class='form-control input-lg']").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_text ="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()

def test_search_for_a_without_entring_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//input[@class='form-control input-lg']").send_keys("")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_text ="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()












