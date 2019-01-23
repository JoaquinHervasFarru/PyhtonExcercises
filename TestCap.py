import unittest
import Cap

class TestCap(unittest.TestCase):

    def testOneWord(self):
        text = "python"
        result = Cap.capText(text)
        self.assertEqual(result, "Python")

    def testMultipleWords(self):
        text = "testing python"
        result = Cap.capText(text)
        self.assertEqual(result, "Testing Python")
if __name__ == '__main__':
    unittest.main()
