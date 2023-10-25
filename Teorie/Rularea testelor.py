"""
Atunci cand vrem sa rulam testele putem sa o facem sub mai multe forme:

1.Click pe triunghiul verde de langa numele clasei de test -> va rula toate testele din acea clasa
2.Click pe triunghiul verde de langa numele metodei de test -> va executa doar metoda de test pe care am rulat-o
4.Rularea din terminal a unui fisier de teste specific: python -m unittest filename.py
4.Rularea din terminal a tuturor fisierelor de test: python -m unittest

"""
import unittest


#Decoratorul skip

@unittest.skip
def test_js_alert_accept(self):
	self.chrome.find_element(*self.JS_ALERT).click()
	js_alert = self.chrome.switch_to.alert
	js_alert.accept()
	js_alert_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
	expected_text = "You succesfully clicked an alert"
	assert js_alert_text == expected_text , f"Error:expected: {expected_text}, actual: {js_alert_text}"