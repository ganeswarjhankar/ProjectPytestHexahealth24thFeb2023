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


class marketing_faqverythin_Class(commonbaseclass):
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.MARKETING_FAQVERYTHIN_URL, sheet_name=constants.MARKETING_FAQVERYTHIN_SHEET)
        self.urls = df.sample(1, replace=False)['URL']

    def marketing_faqverythin_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.driver.maximize_window
            self.verify_whatsapp_PAN()     ## calling the function method in the mid to execute
            self.CalculateSurgeryCost()    # Calling the Calculate Surgery Cost  Function
            self.CheckInsuranceCoverage()  ##Calling the Insurancecoverage Function



            try:

                self.driver.implicitly_wait(5)

                wait = WebDriverWait(self.driver, 10)

                lead_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadname5']")))
                lead_name.send_keys("Test GJ Marketing Variant")

                # self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Doctor Variant")
                # self.driver.implicitly_wait(2)

                contact_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contactnum5']")))
                contact_name.send_keys("9000000100")



                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='LeadSubmit']")))
                submit_button.click()



                try:

                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")

                except:

                    print("Thank you page is Failed")
            except:
                print("Field Level Failed")










