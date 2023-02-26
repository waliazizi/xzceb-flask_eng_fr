import unittest

from translator import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):
    def test_englishToFrance(self):
        testAgainstFr= 'Hello'
        self.assertEqual(englishToFrench(testAgainstFr), 'Bonjour')

    def test_franceToEnglish(self):
        testAgainstEn= 'Bonjour'
        self.assertEqual(frenchToEnglish(testAgainstEn), 'Hello')

if __name__ == '__main__':
    unittest.main()

