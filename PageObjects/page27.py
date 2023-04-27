from utilities import constants
import time
import urllib.request
#import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException


class Marketing_CallPrimary_Class:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_CALLPRIMARY_URL, sheet_name=constants.MARKETING_CALLPRIMARY_SHEET)
        self.urls = df.sample(3, replace=False)['URL']

    def marketing_CallPrimary_Method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:

                self.driver.maximize_window()

                wait = WebDriverWait(self.driver, 10)
                lead_name_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadname5']")))
                lead_name_xpath.send_keys("Test Gj Board test")

                contact_num_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contactnum5']")))
                contact_num_xpath.send_keys("9000000100")

                Submit_Button_Xpath=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='LeadSubmit']")))
                Submit_Button_Xpath.click()

                #self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit']").click()

                try:

                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")


                except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                    print("Exception with Timeout and No elements found")

                self.driver.back()
                self.driver.implicitly_wait(5)
                self.driver.refresh()

            except (TimeoutException, NoSuchElementException, InvalidArgumentException):

                print("Except Block-Lead failed to Generate")
