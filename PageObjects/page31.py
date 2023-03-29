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


class Marketing_Index_Class:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        df = pd.read_excel(constants.MARKETING_BRAND_URL, sheet_name=constants.MARKETING_BRAND_SHEET)
        self.urls = df.sample(2, replace=False)['URL']

    def marketing_brand_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])

            try:

                self.driver.maximize_window()
                self.driver.implicitly_wait(2)

                wait = WebDriverWait(self.driver, 10)

                radio_Yes_button = self.driver.find_element(By.XPATH, "//input[@id='rYes']")
                radio_Yes_button.click()

                # lead_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='leadname5']")))
                # lead_name.send_keys("Test GJ Marketing Variant")

                # self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Doctor Variant")
                # self.driver.implicitly_wait(2)

                contact_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contactnumhomem']")))
                contact_name.send_keys("1000000100")

                select_City = Select(self.driver.find_element(By.XPATH, "//select[@id='leadcitybrand']"))
                select_City.select_by_visible_text("Gurugram ")

                select_Treatment = Select(self.driver.find_element(By.XPATH, "//select[@id='treamentconditionbrand']"))
                select_City.select_by_visible_text("Yoga ")

                submit_button = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmitbrandPagemaster']")))
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
