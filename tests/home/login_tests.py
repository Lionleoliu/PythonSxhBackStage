import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.TestStatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        # driverLocation = "E:\\PythonProject\\SxhOnlineStage\\Driver\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)
        self.lp.login("383383", "123123a@", "aa040128$")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title verified")
        #assert result1 == True
        result2 = self.lp.verifiyLoginSuccessful()
        self.ts.markFinal("test_valid_login", result2, "Login was successful")

