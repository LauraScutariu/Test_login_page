"""
js_alert = self.chrome.switch_to.alert
js_alert.accept()

De asemenea, putem sa respingem o alerta:

js_confirm = self.chrome.switch_to.alert
js_confirm.dismiss()

Sau putem sa inseram text intr-o alerta in care acest lucru e posibil:
js_prompt = self.chrome.switch_to.alert
js_prompt.accept()

Incercati sa creati teste cu tratarea alertelor de pe pagina: https://the-internet.herokuapp.com/javascript_alerts

"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_alert_trigger = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
js_alert_trigger.click()

time.sleep(3)

js_alert = driver.switch_to.alert
js_alert.accept()

driver.quit()