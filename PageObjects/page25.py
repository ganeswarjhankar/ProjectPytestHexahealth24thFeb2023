"""This is the script for the marketing Board website for sanity Testing"""

import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utilities import constants


from utilities.BaseClass import BaseClass


class Marketing_Board_Class(BaseClass):
    LEAD_FIELD = By.XPATH, "//input[@id='leadname5']"
    CONTACT_NUM = By.XPATH, "//input[@id='contactnum5']"
    SUBMIT_BUTTON = By.XPATH, "//button[@id='LeadSubmit']"
    THANKYOU_MSG = By.XPATH, "/html/body/div/div/div/h1"

    def marketing_board_form1(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            try:

                self.driver.maximize_window()

                wait = WebDriverWait(self.driver, 10)
                lead_name_xpath = wait.until(EC.presence_of_element_located(self.LEAD_FIELD))
                lead_name_xpath.send_keys("Test Gj Board test")

                contact_num_xpath = wait.until(EC.presence_of_element_located(self.CONTACT_NUM))
                contact_num_xpath.send_keys("9000000100")

                submit_button_xpath = wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON))
                submit_button_xpath.click()

                try:

                    wait = WebDriverWait(self.driver, 10)
                    thank_you = wait.until(EC.presence_of_element_located(self.THANKYOU_MSG))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")

                except (TimeoutException, NoSuchElementException, InvalidArgumentException):

                    print("Exception Occurred")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()




            except (TimeoutException, InvalidArgumentException, NoSuchElementException):

                print("Out of the List, few URL have Issues with OOPS or TimeOut Issue")
