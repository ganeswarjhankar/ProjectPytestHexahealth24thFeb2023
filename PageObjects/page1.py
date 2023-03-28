import traceback

from utilities import constants

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# page_objects.py
from utilities import constants


import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select






"""update loginpage class"""

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.CITYDOCTOR_URL)

    def CityDoctorBookmethod1(self):

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        BookAppointmentButton = self.driver.find_element(By.XPATH, "//a[@class='link-appointment']").click()
        #assert BookAppointmentButton.is_displayed()

        self.driver.implicitly_wait(5)
        lead_field = self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Patient Name")
        #assert lead_field.is_displayed()

        contact_field = self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
        #assert contact_field.is_ and contact_field.is_enabled()

        BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
        drop1 = Select(BengaluruCity)
        drop1.select_by_visible_text("Bengaluru")

        YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
        drop2 = Select(YogaTreatment)
        drop2.select_by_visible_text("Yoga")

        query_field=self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("Query Test For City Doctor")
        #assert query_field.is_displayed() and query_field.is_enabled()
        #query_field

        #BookApButton = self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitBlog']")
        #self.driver.execute_script("arguments[0].click();", BookApButton)


        BookApButton = self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']")
        self.driver.execute_script("arguments[0].click();", BookApButton)
        #assert BookApButton.is_displayed() and BookApButton.is_enabled()



        Handles2 = self.driver.window_handles[0]

        #ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
        #assert ThankYou =="Thank You"
        #assert self.driver=="Thank You"

        #print("Book Appointment is Successfully done")

        try:

            wait = WebDriverWait(self.driver, 10)
            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.is_displayed())
            print("Lead Is Generated")



        except (TimeoutException, NoSuchElementException):
            print("failed 2nd Except")
            print(traceback.format_exc())

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()



    def CityDoctorListMethod2(self):
        #self.driver.get("https://www.hexahealth.com/delhi/doctors/cardiologist")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        BookAppointmentButton = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[3]/a[2]/span").click()
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

        try:

            wait = WebDriverWait(self.driver, 10)
            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            #print(thank_you.is_displayed())
            #print("Lead Is Generated")












        except (TimeoutException, NoSuchElementException):
            print("failed 2nd Except")

        assert self.driver.find_element(By.CLASS_NAME, "thankyou-title")
        assert "ThankYou" in self.driver.current_url


        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def CityDoctorFormMethod3(self):
        #self.driver.get("https://www.hexahealth.com/delhi/doctors/cardiologist")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # BookAppointmentButton = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[3]/a[2]/span").click()
        # self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Patient Name")
        self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")

        BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity1']")
        drop1 = Select(BengaluruCity)
        drop1.select_by_visible_text("Bengaluru")

        YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition']")
        drop2 = Select(YogaTreatment)
        drop2.select_by_visible_text("Yoga")

        # self.driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test For City Doctor")

        BookApButton = self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitBlog']")
        self.driver.execute_script("arguments[0].click();", BookApButton)

        Handles2 = self.driver.window_handles[0]

        try:

            wait = WebDriverWait(self.driver, 10)
            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.is_displayed())
            print("Lead Is Generated")




        except (TimeoutException, NoSuchElementException):
            print("failed 2nd Except")
            print(traceback.format_exc())

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()
