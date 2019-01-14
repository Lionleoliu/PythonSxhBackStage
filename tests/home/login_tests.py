import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from pages.navigation_page.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login_logout(self):
        # driverLocation = "E:\\PythonProject\\SxhOnlineStage\\Driver\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)
        # self.lp.login("383383", "123123a@", "aa040128$")
        resultForTitle = self.lp.verifyTitle()
        self.ts.mark(resultForTitle, "Title Verified")
        resultForFile = self.lp.verifiyLoginSuccessful()
        self.ts.markFinal("test_valid_login ", resultForFile, "Login was successful")
        self.nav.logout()
        # assert result2 == True

