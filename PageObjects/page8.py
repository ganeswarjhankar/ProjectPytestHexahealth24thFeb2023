# page_objects.py
from utilities import constants
import time

import urllib.request

from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException




class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.CITYDOCTOR_URL)



    def ContactUs(self):

        try:

            # self.driver.get("https://www.hexahealth.com/delhi/doctors/cardiologist")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            BookAppointmentButton = self.driver.find_element(By.XPATH, "//a[@class='link-appointment']").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test For City Doctor")

            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']").click()
            self.driver.implicitly_wait(2)

            try:

                wait = WebDriverWait(self.driver, 20)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")




            except NoSuchElementException:
                print("Message: no such element: Unable to locate element")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()


        except (NoSuchElementException,TimeoutException, InvalidArgumentException):
            print("Failed with Error")





    def ContactUsWhatsapp(self):

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








