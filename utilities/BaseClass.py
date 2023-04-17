from utilities import constants
import time
import urllib.request
# import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def open(self):

        try:
            df = pd.read_excel(constants.MARKETING_BOARD_URL, sheet_name=constants.MARKETING_BOARD_SHEET_URL)
            self.urls = df.sample(3, replace=False)['URL']

        except:
            print("Excel file is not found")






"""This is common verification process of the whatsApp in all the marketing fields"""



class commonbaseclass:

    def __init__(self, driver):
        self.driver = driver



    def verify_whatsapp_PAN(self):

        # self.driver.get("https://www.hexahealth.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='whtsapHeaderBtn']").click()
        # self.driver.switch_to.window(self.driver.window_handles[2])
        msg = self.driver.find_element(By.XPATH, "//p[@class='_9vd5']")
        print(msg.text)

        # Get the current URL
        current_url = self.driver.current_url
        print(current_url)
        # Verify that the current URL contains the expected value

        ######################
        # import urllib.request

        # current_url = "https://api.example.com"

        if "api." in current_url:
            try:
                response = urllib.request.urlopen(current_url)
                if response.status == 200:
                    print("Status Code 200 Ok")
                else:
                    print("Failed")
            except urllib.error.URLError as e:
                print("Failed:", e.reason)
        else:
            print("URL does not contain 'api.'")

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()



