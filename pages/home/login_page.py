from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _username_field = "admin_user_name"
    _password_field = "admin_user_password"
    _checkcode_field = "checkcode"
    _submit_button = "validate-submit"

    def inputUsername(self, username):
        self.sendKeys(username, self._username_field)

    def inputPassword(self, password):
        self.sendKeys(password, self._password_field)

    def inputCheckcode(self, checkcode):
        self.sendKeys(checkcode, self._checkcode_field)

    def clickSubmitButton(self):
        self.ElementClick(self._submit_button)

    def login(self, username, password, checkcode):
        self.inputUsername(username)
        self.inputPassword(password)
        self.inputCheckcode(checkcode)
        self.clickSubmitButton()

    def verifiyLoginSuccessful(self):
        result = self.isElementPresent("操作文档", locatorType="link")
        return result

    def verifyTitle(self):
        if '首页' in self.getTitle():
            return True
        else:
            return False
