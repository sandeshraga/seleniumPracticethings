import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("this is login by email")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("this is login by FB")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("this is login by Twitter")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()