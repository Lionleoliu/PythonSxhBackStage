from base.selenium_driver import SeleniumDriver
from utilities import custom_Logger as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: +" + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: +" + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED :: +" + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")

    def mark(self, result, resultMessage):

        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):

        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
