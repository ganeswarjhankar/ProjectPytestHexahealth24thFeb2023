from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class MarketingHospitalClass:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.HospitalMarketing_URl, sheet_name=constants.SheetHospiMarket_URL)
        self.urls = df.sample(3, replace=False)['URL']




    def HospitalVariant(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])

            try:
                self.driver.maximize_window()
                self.driver.implicitly_wait(2)
                self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Marketing Variant")
                self.driver.implicitly_wait(2)
                self.driver.find_element(By.XPATH, "//input[@id='contactnum5']").send_keys("9000000100")
                self.driver.implicitly_wait(2)
                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit']").click()

                try:


                    wait = WebDriverWait(self.driver, 10)
                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")



                except (TimeoutException, NoSuchElementException):
                    print("Message: no such element: Unable to locate element")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()

            except:
                print("Except Block-Lead failed to Generate")






