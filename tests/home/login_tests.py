import unittest
import pytest
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        # driverLocation = "E:\\PythonProject\\SxhOnlineStage\\Driver\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)
        self.lp.login("383383", "123123a@", "aa040128$")
        result2 = self.lp.verifiyLoginSuccessful()
        assert result2 == True
