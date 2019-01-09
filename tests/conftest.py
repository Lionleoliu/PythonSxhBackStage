import os

import pytest
import shutil
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    # my_file = 'E:\\GitHubProject\PythonBackStage\\automation.log'
    # if os.path.exists(my_file):
    #     # 删除文件，可使用以下两种方法。
    #     os.remove(my_file)
    # else:
    #     print('no such file:%s' % my_file)
    webDeriverFactory = WebDriverFactory(browser)
    driver = webDeriverFactory.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
