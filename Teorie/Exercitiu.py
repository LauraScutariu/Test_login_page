"""
Implementati exercitiile pe care le-ati avut de facut pe site-ul elefant.ro la
 workshopul 5 in libraria unit test.

"""
# - Test 1: Intrati pe site-ul https://www.elefant.ro/
# - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
# - Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "] (puteti sa va folositi de find_elements)
# - Test 4: Extrageti titlul paginii si verificati ca este corect
# - Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
# Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
# - Dati click pe butonul "conectare" si verificati urmatoarele:
#              1. Faptul ca nu s-a facut logarea in cont
#             2. Faptul ca se returneaza eroarea corecta
# # - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
#
# Nota:
# Daca nu aveti timp sa le faceti in timpul sesiunii de weekend le puteti implementa in oricare din framework-urile de automatizare pe care le veti invata la cursurile viitoare
#
# Ce tipuri / tehnici de testare ati folosit pentru testele de mai sus? Mai sunt alte teste pe care le puteti face folosind alte tipuri si tehnici de testare folosite la cursul de testare manuala?

import time   # ALT+SHIFT+Sageata sus =pentru a aranja in ordinea alfabetica
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestElefantApp(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		self.driver.maximize_window()
		self.driver.get("https://www.elefant.ro/")
		self.driver.implicitly_wait(10)

	def test_case_iphone_14(self):
		search_bar_locator = self.driver.find_element(By.XPATH, "//*[@id='MobileSearchRow']/div/form/input[1]")
		search_bar_locator.send_keys("Iphone 14")
		search_bar_locator.send_keys(Keys.ENTER)
		iphone_products = self.driver.find_elements(By.CLASS_NAME,'product-title')

		assert len(iphone_products) > 10, "Less then 10 Products was found"

	def tearDown(self):
		self.driver.quit()

