# page_objects.py
from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.CITYDOCTOR_URL)

    def ContactUs(self):
        pass

    def ContactUsWhatsapp(self):
        pass

    def read_data_from_excel(self, file_path):
        data = pd.read_excel(file_path)
        # process the data and return it
        return data
