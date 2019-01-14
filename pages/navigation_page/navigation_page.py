from base.basepage import BasePage


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _productManagement_link = "//aside[@id = 'nav']//a[@class='auto']//span[text()='��Ʒ����']"
    _selfProductManagement_link = "//aside[@id = 'nav']//a[@class='auto menu-li']//span[text()='��Ӫ��Ʒ����']"
    _avatar_button = "//a[@class='dropdown-toggle bg clear']"
    _logout_link = "�˳���¼"

    def navigateToProductManagement(self):
        self.elementClick(self._productManagement_link, locatorType="xpath")

    def navigateToSelfProductManagement(self):
        self.elementClick(self._selfProductManagement_link, locatorType="xpath")

    def clickAvatarButton(self):
        self.elementClick(self._avatar_button, locatorType="xpath")

    def clickLogOutButton(self):
        self.elementClick(self._logout_link, locatorType="link")

    def logout(self):
        self.clickAvatarButton()
        self.clickLogOutButton()
