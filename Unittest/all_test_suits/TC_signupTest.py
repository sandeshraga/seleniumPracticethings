import unittest

class signupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("this is signup by email")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("this is signup by FB")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("this is signup by Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()