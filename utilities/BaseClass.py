import self as self
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException










from utilities import constants
import time

import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select



class BaseClass:
    pass


"""main Lead Form"""
name_text_xpath="//input[@id='leadname5']"
mobile_text_xpath="//input[@id='contactnum5']"
submit_button_xpath="//button[@id='LeadSubmit']"

"""Book Free Appointment"""
#NABH
BookHospital_button_css= "Book Free Appointment"


"""WhatsApp Connection"""
WA_button_css="WhatsApp Expert"

"""Top Doctors"""
#DocButton ="//*[@id='BkApntdoc']"

DocButtons=driver.find_elements(By.XPATH,"//*[@id='BkApntdoc']")


#for DocButton in DocButtons:


class AllFunctions:

    def AllFunctions2(self):
        wait = WebDriverWait(self.driver, 10)









