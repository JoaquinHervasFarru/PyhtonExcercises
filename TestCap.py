import unittest
import Cap

class TestCap(unittest):

    def testOneWord(self):
        text = "python"
        result = Cap.capText(text)
        self.self.assertEqual(result, "Python")

    def testMultipleWords(self):
        text = "testing python"
        result = cap.capText(text)
        self.self.assertEqual(result, "Testing Python")
if __name__ == '__main__':
    unittest.main()
