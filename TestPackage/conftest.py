# conftest.py
import pytest
from selenium import webdriver
#import requests


from selenium.webdriver.chrome.service import Service

from PageObjects.page1 import LoginPage
from PageObjects.page2 import CityHospitalClass
from PageObjects.page3 import DoctorClass
from PageObjects.page4 import SearchPage
from PageObjects.page5 import ConditionClass
from PageObjects.page6 import TreatmentClass
from PageObjects.page7 import HexaHomepageClass
from PageObjects.page8 import ContactUsPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser_name")
    S = Service("D:\\chromedriver.exe")
    driver = webdriver.Chrome(service=S)
    yield driver
    driver.quit()

@pytest.fixture
def city_doctor(driver):
    page = LoginPage(driver)
    page.open()
    return page

@pytest.fixture
def city_hospital(driver):
    page = CityHospitalClass(driver)
    page.open()
    return page

@pytest.fixture
def doctor_page(driver):
    page = DoctorClass(driver)
    page.open()
    return page

@pytest.fixture
def search_page(driver):
    page = SearchPage(driver)
    page.open()
    return page


@pytest.fixture
def condition_page(driver):
    page = ConditionClass(driver)
    page.open()
    return page


@pytest.fixture
def treatment_page(driver):
    page = TreatmentClass(driver)
    page.open()
    return page


@pytest.fixture
def home_page(driver):
    page = HexaHomepageClass(driver)
    page.open()
    return page


@pytest.fixture
def ContactUs_page(driver):
    page = ContactUsPage(driver)
    page.open()
    return page


#test_url9

@pytest.fixture
def Blog_page(driver):
    page = BlogPage(driver)
    page.open()
    return page

#test_url10
@pytest.fixture
def ProcedureCostIndia_page(driver):
    page = ProcedureCostIndiaPage(driver)
    page.open()
    return page


#test_url11
@pytest.fixture
def ProcedureCostCity_page(driver):
    page = ProcedureCostCityPage(driver)
    page.open()
    return page







@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(item.funcargs['driver'], file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)







