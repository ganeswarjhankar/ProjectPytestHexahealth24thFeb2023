""""""

from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException


class marketing_pdf_Class:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_PDF_URL, sheet_name=constants.MARKETING_PDF_SHEET)
        self.urls = df.sample(2, replace=False)['URL']

    def marketing_pdf_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])






