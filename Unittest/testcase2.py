import unittest
from selenium import webdriver

class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("this is a login method")

    def test1(self):
        print("this is 1st testcase run")

    def test2(self):
        print("this is 2nd testcase run")


    def test3(self):
        print("this is 3rd testcase run")


    def test4(self):
        print("this is  testcase run")



if __name__ == "__main__":
    unittest.main()