import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixture("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        self.driver.find_element(By.XPATH, "//input[@class='form-control input-lg']").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_a_invalid_product(self):
        self.driver.find_element(By.XPATH, "//input[@class='form-control input-lg']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
            expected_text)

    def test_search_for_a_without_enter_product(self):
        self.driver.find_element(By.XPATH, "//input[@class='form-control input-lg']").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
            expected_text)
