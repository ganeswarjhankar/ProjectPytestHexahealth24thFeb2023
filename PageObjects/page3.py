# page_objects.py
import time

from selenium.webdriver.support.select import Select

from utilities import constants

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException, TimeoutException


class DoctorClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.DoctorPage_URl)

    def BookAppointmentForm1(self):
        # self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
        try:
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadnamedoctor3']").send_keys("test GJ ")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumdoctor3']").send_keys("9000000100")

            #BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            #drop1 = Select(BengaluruCity)
            #drop1.select_by_index(3)

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treatmentcondition3']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_index(2)

            #self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Test Query check")
            #self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitDoctor3']").click()

            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1 ")))
                print(thank_you.is_displayed())
                print("BookAppointmentForm1 is created Successfully")



            except (TimeoutException, NoSuchElementException):
                assert False
                print("failed 2nd Except No Lead Is Generated")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()




        except NoSuchElementException:
            print("Message: no such element: Unable to locate element")

    def NABHAccreditedHospitals(self):
        try:
            self.driver.maximize_window()

            BookApButton = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div[6]/div/div/div[1]/div/div[5]/div/div[1]/div[2]/div[2]/a/span")
            self.driver.execute_script("arguments[0].click();", BookApButton)

            # Wait for lead name field to be clickable
            lead_name_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadnamedoctor2']")))
            lead_name_field.send_keys("Test GJ XYZ")

            # Wait for contact number field to be clickable
            contact_number_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnumdoctor2']")))
            contact_number_field.send_keys("9000000100")

            # Wait for treatment condition field to be clickable
            #treatment_condition_field = WebDriverWait(self.driver, 10).until(
            #    EC.element_to_be_clickable((By.XPATH, "//*[@id='treatmentcondition2']")))
            #treatment_condition_field.send_keys("Mastectomy")
            #Drop down feature is implemented below for the treatment field.
            treatment_condition_field1 = self.driver.find_element(By.XPATH, "//*[@id='treatmentcondition2']")
            drop1 = Select(treatment_condition_field1)
            drop1.select_by_index(2)

            self.driver.implicitly_wait(5)

            Hospital_drop = self.driver.find_element(By.XPATH, "//select[@id='hospitallist2']")
            drop1 = Select(Hospital_drop)
            drop1.select_by_index(3)

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor2']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            self.driver.implicitly_wait(5)

            # Wait for thank you message to be visible
            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")




            except NoSuchElementException:

                print("Message: no such element: Unable to locate element")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()



        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")

    def BookAppointmentButtonMethod(self):
        # self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")

        try:
            self.driver.maximize_window()

            # Wait for the Book Appointment button to be clickable
            book_ap_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Book Appointment")))
            book_ap_button.click()

            # Wait for the name field to be visible and send keys
            name_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='leadnamedoctor2']")))
            name_field.send_keys("Test GJ Treatment")

            # Wait for the contact number field to be visible and send keys
            contact_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='contactnumdoctor2']")))
            contact_field.send_keys("9000000100")

            # Wait for the treatment condition field to be visible and send keys
            #treatment_field = WebDriverWait(self.driver, 10).until(
            #    EC.visibility_of_element_located((By.XPATH, "//*[@id='treamentcondition2']")))
            #treatment_field.send_keys("Mastectomy")

            treatment_field_drop = self.driver.find_element(By.XPATH, "//*[@id='treatmentcondition2']")
            drop1 = Select(treatment_field_drop)
            drop1.select_by_index(2)

            self.driver.implicitly_wait(5)  # Wait for up to 10 seconds for elements to appear

            Hospital_drop = self.driver.find_element(By.XPATH, "//select[@id='hospitallist2']")
            drop1 = Select(Hospital_drop)
            drop1.select_by_index(3)
            #drop1.select_by_visible_text("HealthFort Clinic")

            #sel = self.driver.find_element(By.XPATH, "//select[@id='hospitallist']")
            #dropdown=Select(sel)
            # sel.select_by_index(1)
            #dropdown.select_by_visible_text("HealthFort Clinic")




            # Wait for the Book An Appointment button to be clickable and click it
            book_an_ap_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadSubmitDoctor2']")))
            book_an_ap_button.click()

            # Wait for the Thank You message to appear and print it
            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")



            except (TimeoutException, NoSuchElementException):
                print("failed 2nd Except")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()



        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")

    def BookAppointmentMainForm(self):

        # self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            # self.driver.implicitly_wait(2)
            # BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            # self.driver.execute_script("arguments[0].click();", BookApButton)
            # self.driver.implicitly_wait(2)
            wait = WebDriverWait(self.driver, 10)
            lead_page = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadnamedoctor1']")))
            lead_page.send_keys("Test Doctor Page url 4")

            #self.driver.find_element(By.XPATH, "//*[@id='leadnamedoctor1']").send_keys("Test GJ Treatment ")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor']")
            # self.driver.execute_script("arguments[0].click();", NameTextBox)

            self.driver.find_element(By.XPATH, "//*[@id='contactnumdoctor1']").send_keys("9000000100")
            self.driver.implicitly_wait(2)

            #self.driver.find_element(By.XPATH, "//*[@id='contactnumdoctor1']").send_keys("Mastectomy")


            #Drop down treatment
            Treatment_drop_down = self.driver.find_element(By.XPATH, "//select[@id='treatmentcondition1']")
            drop1 = Select(Treatment_drop_down)
            drop1.select_by_index(2)

            Hospital_drop = self.driver.find_element(By.XPATH, "//select[@id='hospitallist1']")
            drop1 = Select(Hospital_drop)
            drop1.select_by_index(1)



            # BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome']")
            # drop1 = Select(BengaluruCity)
            # drop1.select_by_visible_text("Bengaluru")

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor1']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")



            except (TimeoutException, NoSuchElementException):
                print("Lead Is Not Generated")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()




        except (NoSuchElementException, TimeoutException):

            print("Message: no such element: Unable to locate element")
