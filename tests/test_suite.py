import unittest
from tests.home.login_tests import LoginTest

# Get all tests from the test classes
test_case1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create a test suite combining all test classes
loginTest = unittest.TestSuite([test_case1])

unittest.TextTestRunner(verbosity=2).run(loginTest)
