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
        self.urls = df.sample(3, replace=False)['URL']



    def CalculateSurgeryCost(self):

        try:

            for url in self.urls:
                self.driver.get(url)
                print([url])

                try:

                    self.driver.maximize_window()

                    self.driver.implicitly_wait(5)

                    wait = WebDriverWait(self.driver, 10)
                    calculate_button = wait.until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='surgerytBtn']/span")))
                    calculate_button.click()

                    # CalculateButton = self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
                    # self.driver.execute_script("arguments[0].click();", CalculateButton)

                    # self.driver.execute_script("window.scrollTo(0, 2000)")
                    # time.sleep(2)
                    # self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span").click()

                    self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys(
                        "Test GJ Normal Marketing ")
                    self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
                    self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
                    print("MarketingNormalForm1 is passed")
                    self.driver.implicitly_wait(5)

                    wait = WebDriverWait(self.driver, 10)
                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    # print(f"Book Appointment is Successfully done for {url}")

                    self.driver.back()
                    self.driver.implicitly_wait(2)
                    self.driver.refresh()


                except:

                    print("Except Block-Lead failed to Generate")

        except:
            print("This is under developed and making it as pass")


















    def CheckInsuranceCoverage(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        self.driver.implicitly_wait(5)
        for url in self.urls:
            self.driver.get(url)
            print([url])

            wait = WebDriverWait(self.driver, 10)
            self.driver.maximize_window()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            #self.driver.execute_script("window.scrollTo(0, 2000)")
            #time.sleep(2)

            InsuranceButton = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
            self.driver.execute_script("arguments[0].click();", InsuranceButton)



            #Insurance = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
            #self.driver.execute_script("arguments[0].click();", Insurance)
            self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
            self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()

            self.driver.implicitly_wait(5)

            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.is_displayed())

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()