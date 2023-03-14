from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class MarketingCostClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.COST_MARKETING_URL, sheet_name=constants.SHEET_COST_URL)
        self.urls = df.sample(2, replace=False)['URL']

    def cost_variant(self):


        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:

                self.driver.maximize_window()

                wait = WebDriverWait(self.driver, 10)
                radio_button = wait.until(EC.presence_of_element_located((By.ID, 'rNo')))
                radio_button.click()

                contact_num = wait.until(EC.presence_of_element_located((By.ID, 'contactnumhomem')))
                contact_num.send_keys("1000000100")

                submit_button = wait.until(EC.presence_of_element_located((By.ID, 'LeadSubmitCostPageMaster')))
                submit_button.click()

                #wait.until(EC.title_contains("Thank You"))
                #thank_you = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text

                try:
                    print("passed Lead is Generated")

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




##*****Need to check and again the issue##