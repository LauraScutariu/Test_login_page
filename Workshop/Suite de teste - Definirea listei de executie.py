"""
Libraria de executie va contine toate clasele de test pe care ne dorim sa le executam intr-o rulare.

Suita de teste trebuie facuta intr-o clasa numita TestSuite care sa mosteneasca unittest.TestCase:
class TestSuite(unittest.TestCase):

In interiorul acestei clase vom avea o metoda numita test_suite care sa contina un obiect instantiat din clasa TestSuite:

test_de_rulat = unittest.TestSuite()

Prin intermediul acestui obiect vom apela metoda addTests care va primi drept parametru o lista de clase de test care se doreste a fi executate.

teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Firefox)
        ])

"""