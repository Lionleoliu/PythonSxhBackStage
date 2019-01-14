import os

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        driver = webdriver
        baseURL = "https://testsxhadmin.shixiangyiwei.com/adminuser/logout.html"
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="D:\\GeckoDriver\\geckodriver.exe")
        elif self.browser == "chrome":
            driverLocation = "E:\\PythonProject\\SxhOnlineStage\\Driver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        else:
            print("Wrong browser type")

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
