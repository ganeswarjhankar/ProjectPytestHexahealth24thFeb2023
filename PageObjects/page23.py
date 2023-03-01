from utilities import constants
import time
import urllib.request
#import pandas as pd

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


class MarketingNormalClass:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.MarketingNormal_URl, sheet_name=constants.SHEET_NORMAL_URL)
        self.urls = df.sample(2, replace=False)['URL']




    def MarketingNormalForm1(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])

            try:

                self.driver.maximize_window()

                wait = WebDriverWait(self.driver, 10)
                Lead_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='leadname5']")))
                Lead_text.send_keys("Test GJ Test GJ Normal Marketing Automation Suite")

                contact_num = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contactnum5']")))
                contact_num.send_keys("1000000100")

                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmit']")))
                submit_button.click()

                try:

                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    #print(f"Book Appointment is Successfully done for {url}")


                except (TimeoutException, NoSuchElementException,InvalidArgumentException):
                    print("failed 2nd Except")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()



            except TimeoutException:
                print("Out of the List, few URL have Issues with OOPS or TimeOut Issue")



































