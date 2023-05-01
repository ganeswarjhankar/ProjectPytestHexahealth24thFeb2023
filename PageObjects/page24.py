from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class MarketingNormalSurgeryClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_NORMAL_SURGERY_URL, sheet_name=constants.SHEET_NORMAL_SURGERY)
        self.urls = df.sample(2, replace=False)['URL']



    def CalculateSurgeryCost(self):

        for url in self.urls:
            self.driver.get(url)
            print([url])


            self.driver.maximize_window()

            wait = WebDriverWait(self.driver, 10)
            calculate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='surgerytBtn']/i")))
            self.driver.execute_script("arguments[0].click();", calculate_button)


            # CalculateButton = self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
            # self.driver.execute_script("arguments[0].click();", CalculateButton)

            # self.driver.execute_script("window.scrollTo(0, 2000)")
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span").click()

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test GJ Normal Marketing ")

            # self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
            self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("9000000100")
            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
            print("MarketingNormalForm1 is passed")
            self.driver.implicitly_wait(5)

            try:
                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
            except:
                print("thank you is not displayed")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()









            # print(f"Book Appointment is Successfully done for {url}")



















    def CheckInsuranceCoverage(self):

        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.driver.maximize_window()

            wait = WebDriverWait(self.driver, 10)

            InsuranceButton = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/i")
            self.driver.execute_script("arguments[0].click();", InsuranceButton)

            # Insurance = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
            # self.driver.execute_script("arguments[0].click();", Insurance)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test GJ Normal Marketing ")

            contact_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='contactnum2']")))
            contact_xpath.send_keys("9000000100")

            #self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
            #self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("9000000100")
            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()

            try:
                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
            except:
                print("thank you is not displayed")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()




