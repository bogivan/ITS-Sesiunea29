import unittest
import sesiunea29


# class Test_sesiunea29(unittest.TestCase):
#
#     def test_adunare(self):
#         self.assertEqual(sesiunea29.adunare(5, 10), 15)
#         self.assertEqual(sesiunea29.adunare(-1, -3), -4)
#
#     def test_scadere(self):
#         self.assertEqual(sesiunea29.scadere(10, 5), 5)
#         self.assertEqual(sesiunea29.scadere(-5, 4), -9)
#
#     def test_inmultire(self):
#         self.assertEqual(sesiunea29.inmultire(5, 10), 50)
#
#     def test_impartire(self):
#         self.assertEqual(sesiunea29.impartire(10, 5), 2)
#         self.assertRaises(ZeroDivisionError, sesiunea29.impartire, 10, 0)

class Test_Sesiunea29_Angajat(unittest.TestCase):

    def setUp(self):
        self.ang_1 = sesiunea29.Angajat('Bogdan', 'Ivan', 50)
        self.ang_2 = sesiunea29.Angajat('Ysera', 'Caine', 100)

    def tearDown(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.ang_1.fullname(), 'Bogdan Ivan')
        self.assertEqual(self.ang_2.fullname(), 'Ysera Caine')

    def test_email(self):
        self.assertEqual(self.ang_1.email(), 'Bogdan.Ivan@email.com')
        self.assertEqual(self.ang_2.email(), 'Ysera.Caine@email.com')

    def test_raise_salar(self):
        self.ang_1.raise_salar()
        self.ang_2.raise_salar()

        self.assertEqual(self.ang_1.salar, 75)
        self.assertEqual(self.ang_2.salar, 150)