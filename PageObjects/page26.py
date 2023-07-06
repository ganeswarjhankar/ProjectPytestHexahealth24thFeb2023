import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utilities import constants
from utilities.BaseClass import BaseClass



class Marketing_Brand_Class:
    def __init__(self, driver):
        self.driver = driver
        self.urls = []

    def open(self):
        df = pd.read_excel(constants.MARKETING_BRAND_URL, sheet_name=constants.MARKETING_BRAND_SHEET)
        self.urls = df.sample(1, replace=False)['URL']

    def marketing_brand_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])

            self.driver.maximize_window()
            wait = WebDriverWait(self.driver, 10)

            radio_yes_button = self.driver.find_element(By.XPATH, "//*[@id='rNo']")
            radio_yes_button.click()

            contact_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='contactnumhomem']")))
            contact_name.send_keys("9000000100")

            gurugram_city = Select(self.driver.find_element(By.XPATH, "//*[@id='leadcitybrand']"))
            #gurugram_city.select_by_visible_text("Gurugram ")
            gurugram_city.select_by_index(2)

            yoga_text = Select(self.driver.find_element(By.XPATH, "//*[@id='treamentconditionbrand']"))

            #yoga_text.select_by_visible_text("Yoga ")
            yoga_text.select_by_index(2)

            submit_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='LeadSubmitbrandPagemaster']")))
            submit_button.click()

            try:
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")
            except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                print("Exception with Timeout and No elements found")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

