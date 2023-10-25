import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_positive_login(self):
	username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
		(By.ID, "username")
	))
	username_field.send_keys("blablabla")
	time.sleep(4)
	username_field.send_keys(Keys.CONTROL,'a')  #selecteaza textul de mai sus CTRL + a'
	username_field.send_keys(Keys.BACKSPACE)
	time.sleep(4)
	username_field.send_keys("student")

	password_field = self.driver.find_element(By.ID, "password")
	password_field.send_keys("Password123")
	text = password_field.is_displayed()

	submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit']")
	submit_button.click()

	time.sleep(2)

	expected_url = "https://practicetestautomation.com/logged-in-successfully/"
	actual_url = self.driver.current_url
	assert expected_url == actual_url, "URL verification faild"
