#import pandas as pd

import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities import constants
from utilities.BaseClass import commonbaseclass


class MarketingNormalClass(commonbaseclass):
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.MarketingNormal_URl, sheet_name=constants.SHEET_NORMAL_URL)
        self.urls = df.sample(2, replace=False)['URL']




    def MarketingNormalForm1(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.verify_whatsapp_PAN()

            try:

                wait = WebDriverWait(self.driver, 10)

                self.driver.maximize_window()


                Lead_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='leadname5']")))
                Lead_text.send_keys("Test GJ Test GJ Normal Marketing Automation Suite")

                contact_num = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contactnum5']")))
                contact_num.send_keys("9000000100")

                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmit']")))
                submit_button.click()

                try:

                    wait = WebDriverWait(self.driver, 10)

                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")
                    #print(f"Book Appointment is Successfully done for {url}")


                except (TimeoutException, NoSuchElementException,InvalidArgumentException):
                    print("Message: no such element: Unable to locate element")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()



            except (TimeoutException,InvalidArgumentException,NoSuchElementException):
                print("Out of the List, few URL have Issues with OOPS or TimeOut Issue")



































