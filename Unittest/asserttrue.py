import unittest
from selenium import webdriver


class Bing(unittest.TestCase):
    def test_open(self):
        list = ["python", "java", "ruby"]

        self.assertTrue("hi", list)  # true
        self.assertFalse("python", list)#false


if __name__ == "__main__":
    unittest.main()