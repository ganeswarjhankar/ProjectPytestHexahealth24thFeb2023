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


class Marketing_Display_Class:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_DISPLAY_URL, sheet_name=constants.MARKETING_DISPLAY_SHEET)
        self.urls = df.sample(3, replace=False)['URL']

    def Marketing_Display_Method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:

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

            except:
                print("Something went wrong")


