import unittest
from selenium import webdriver

def setUpModule():#executes before class
    print("setup module")

def tearDownModule():#executes after finishing class
    print("tear down module")


class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self):#this is executed before running every method
        print("this is a login method")

    @classmethod
    def tearDown(self):#this runs after evry method
        print("this is logout method")

    @classmethod
    def setUpClass(cls):# this runs once class is started or before all methods
        print("this class opens the application")

    @classmethod
    def tearDownClass(cls):# this runs after running all methods, while closing class
        print("this class closes the application")

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