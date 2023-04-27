import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utilities import constants
from utilities.BaseClass import BaseClass


class Marketing_Brand_Class(BaseClass):








    def open(self):
        df = pd.read_excel(constants.MARKETING_BRAND_URL, sheet_name=constants.MARKETING_BRAND_SHEET)
        self.urls = df.sample(1, replace=False)['URL']

    def marketing_brand_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])

            try:

                #self.RADIO_BUTTON = By.XPATH, "//*[@id='rNo']"
                #self.CONTACT_NUMBER = By.XPATH, "//*[@id='contactnumhomem']"
                #self.CITY_DROPDOWN = By.XPATH, "//select[@id='leadcitybrand']"
                #self.TREATMENT_DROPDOWN = By.XPATH, "//select[@id='treamentconditionbrand']"
                #self.SUBMIT_BUTTON = By.XPATH, "//button[@id='LeadSubmit']"
                #self.THANKYOU_MSG = By.XPATH, "/html/body/div/div/div/h1"


                wait = WebDriverWait(self.driver, 10)

                self.driver.maximize_window()
                self.driver.implicitly_wait(2)



                radio_Yes_button = self.driver.find_element(By.XPATH, "//*[@id='rYes']")
                radio_Yes_button.click()

                # lead_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='leadname5']")))
                # lead_name.send_keys("Test GJ Marketing Variant")

                # self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Doctor Variant")
                # self.driver.implicitly_wait(2)

                contact_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contactnumhomem']")))
                contact_name.send_keys("9000000100")

                gurugram_city=self.driver.find_element((By.XPATH, "//select[@id='leadcitybrand']"))
                select_City = Select(gurugram_city)
                select_City.select_by_visible_text("Gurugram ")

                yoga_text=self.driver.find_element((By.XPATH, "//select[@id='treamentconditionbrand']"))

                select_Treatment = Select(yoga_text)
                select_City.select_by_visible_text("Yoga")

                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmit']")))
                submit_button.click()

                try:
                    thank_you = wait.until(EC.presence_of_element_located(By.XPATH,"/html/body/div/div/div/h1"))
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
