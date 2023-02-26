import unittest

from translator import englishToFrench, frenchToEnglish


class TestMyModule(unittest.TestCase):

    def test_englishToFrance(self):
        testAgainstFr = 'Hello'
        self.assertEqual(englishToFrench(testAgainstFr), 'Bonjour')

    def test_englishToFrance(self):
        testAgainstFr = 'Hello'
        self.assertNotEqual(englishToFrench(testAgainstFr), 'Hello')

    def test_franceToEnglish(self):
        testAgainstEn = 'Bonjour'
        self.assertEqual(frenchToEnglish(testAgainstEn), 'Hello')


    def test_franceToEnglish(self):
        testAgainstEn = 'Bonjour'
        self.assertNotEqual(frenchToEnglish(testAgainstEn), 'Bonjour')



if __name__ == '__main__':
    unittest.main()
