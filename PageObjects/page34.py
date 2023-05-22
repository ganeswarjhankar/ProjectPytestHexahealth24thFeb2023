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

from utilities.BaseClass import commonbaseclass


class marketing_pilot_Class(commonbaseclass):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_PILOT_URL, sheet_name=constants.MARKETING_PILOT_SHEET)
        self.urls = df.sample(2, replace=False)['URL']

    def marketing_pilot_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.verify_whatsapp_PAN()

            try:

                self.driver.maximize_window()
                self.driver.implicitly_wait(2)

                wait = WebDriverWait(self.driver, 10)

                name_text_xpath = self.driver.find_element(By.XPATH, "//*[@id='leadname5']")
                name_text_xpath.send_keys("test Pilot Name")



                contact_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contactnum5']")))
                contact_name.send_keys("9000000100")


                submit_button = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmit']")))
                submit_button.click()

                try:
                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")
                    # print(f"Book Appointment is Successfully done for {url}")

                    # wait = WebDriverWait(self.driver, 10)
                    # wait.until(EC.title_contains("Thank You"))
                    # thank_you = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
                    # print("Thank You message is displayed")




                except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                    print("Exception with Timeout and No elements found")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()


            except (TimeoutException, NoSuchElementException, InvalidArgumentException):

                print("Except Block-Lead failed to Generate")



