import unittest
from selenium import webdriver

class AppTest(unittest.TestCase):
    @unittest.skip
    def test1(self):
        print("this is 1st testcase run")
        
    @unittest.skip(reason="I am skipping this method, as it is no need")
    def test2(self):
        print("this is 2nd testcase run")

    @unittest.skipIf(1==1, "one is equals to one")
    def test3(self):
        print("this is 3rd testcase run")

    def test4(self):
        print("this is 4th testcase run")

if __name__ == "__main__":
    unittest.main()