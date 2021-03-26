import unittest

from package1.TC_LoginTest import LoginTest
from package1.TC_signupTest import signupTest

from package2.TC_paymenttest import Paymenttest
from package2.TC_paymentreturns import Paymentreturns

#get all tests from logintest,signuptest,Paymenttest, Paymentreturns
TC1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2=unittest.TestLoader().loadTestsFromTestCase(signupTest)
TC3=unittest.TestLoader().loadTestsFromTestCase(Paymenttest)
TC4=unittest.TestLoader().loadTestsFromTestCase(Paymentreturns)

#creating testsuits
#sanitytestsuite=unittest.TestSuite([TC1,TC2])# sanity test
functionaltestsuite=unittest.TestSuite([TC3, TC4])#functional test
#mastertestsuite=unittest.TestSuite([TC1, TC2, TC3, TC4])#mastertestsuite

unittest.TextTestRunner().run(functionaltestsuite)