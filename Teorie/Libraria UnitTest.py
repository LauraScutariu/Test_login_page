#Libraria unittest este o librarie care suporta crearea de teste  rulabile direct
# in interiorul clasei

#Exemplu:
# class TestAlerts(unittest.TestCase):

#Componente:
# 1. metoda setUp() -> toate activitatile care trebuie sa fie executate inainte de
# ORICE TEST din clasa respectiva
#
# 2. metoda tearDown() -> toate activitatile care trebuie sa fie executate dupa de
# ORICE TEST din clasa respectiva
#
# 3. toate metodele de test trebuie sa aiba prefixul test_
