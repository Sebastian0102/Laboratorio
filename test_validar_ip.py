import unittest
from validar_ip import es_ip_valida

class TestValidarIP(unittest.TestCase):

    def test_ip_valida(self):
        self.assertTrue(es_ip_valida("192.168.1.1"))

    def test_ip_octeto_mayor_255(self):
        self.assertFalse(es_ip_valida("192.168.300.1"))

    def test_ip_con_letras(self):
        self.assertFalse(es_ip_valida("192.16a.1.1"))

    def test_ip_menos_de_4_partes(self):
        self.assertFalse(es_ip_valida("10.0.1"))

    def test_ip_mas_de_4_partes(self):
        self.assertFalse(es_ip_valida("172.16.0.1.5"))

if __name__ == '__main__':
    unittest.main()
