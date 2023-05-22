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


class marketing_Ayush_Class(commonbaseclass):
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.MARKETING_AYUSH_URL, sheet_name=constants.MARKETING_AYUSH_SHEET)
        self.urls = df.sample(1, replace=False)['URL']




    def marketing_ayush_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.verify_whatsapp_PAN()







            try:
                #self.ListWhatsApp()
                pass
            except:
                pass




            try:
                Checkinsurance_Button = self.driver.find_element(By.XPATH, "//a[@id='surgerytBtn']")
                if Checkinsurance_Button.is_displayed():
                    self.CheckInsuranceCoverage()
            except NoSuchElementException:
                pass

            try:

                list_Doctors = self.driver.find_elements(By.XPATH, "//a[@id='BkApntdoc']")

                for item in list_Doctors:
                    # button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_WA)))
                    # item.click()
                    self.driver.execute_script("arguments[0].scrollIntoView();", item)
                    time.sleep(2)
                    item.click()


                    break

            except:
                print("list function is not working as expected")


            self.driver.refresh()


            try:

                self.driver.maximize_window()
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
                    # print(f"Book Appointment is Successfully done for {url}")

                    # wait = WebDriverWait(self.driver, 10)
                    # wait.until(EC.title_contains("Thank You"))
                    # thank_you = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
                    # print("Thank You message is displayed")






                except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                    assert False
                    print("Exception with Timeout and No elements found")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()


            except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                assert False

                print("Except Block-Lead failed to Generate")


















