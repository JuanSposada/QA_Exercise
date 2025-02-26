import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.prueba
def test_prueba():
    driver = webdriver.Chrome()

    driver.get("https://www.liverpool.com.mx/tienda?s=smart+tv")
    checkbox_locator = driver.find_element(By.XPATH,"//div[@id='brandFilterWEB']/div[3]/div/div/input" )
    checkbox_locator.click()