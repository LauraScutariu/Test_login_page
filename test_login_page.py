import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/")
driver.maximize_window()

time.sleep(3)

driver.quit()

class TestLoginPage(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.driver.get("https://practicetestautomation.com/practice-test-login/")

	def test_run(self):
		self.driver.quit()

	@unittest.skip
	def test_run_2(self):
		time.sleep(3)


	def test_positive_login(self):
		username_field = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
			(By.ID, "username")
			))
		username_field.send_keys("student")

		password_field = self.driver.find_element(By.ID,"password")
		password_field.send_keys("Password123")
		text = password_field.is_displayed()

		submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit']")
		submit_button.click()

		time.sleep(2)

		expected_url = "https://practicetestautomation.com/logged-in-successfully/"
		actual_url = self.driver.current_url
		assert expected_url == actual_url, "URL verification faild"

	#TEMA
	def test_negative_username_login(self):
		pass


	#TEMA
	def test_negative_password_logi(self):
		pass



	def tearDown(self):
		self.driver.quit()

