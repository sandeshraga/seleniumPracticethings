import unittest
from selenium import webdriver


class Bing(unittest.TestCase):
    def test_open(self):
        list = ["python", "java", "ruby"]

        # self.assertIn("python", list)  # true
        # self.assertIn("hi", list)  # false

        # self.assertNotIn("ruby", list)  # false
        self.assertNotIn("hi", list)  # true


if __name__ == "__main__":
    unittest.main()