# page_objects.py
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
        #self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
        try:
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("test GJ ")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Test Query check")
            self.driver.implicitly_wait(2)



            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']" ).click()







            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1 ")))
                print(thank_you.is_displayed())
                print("BookAppointmentForm1 is created Successfully")



            except (TimeoutException, NoSuchElementException):
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
            contact_number_field.send_keys("1000000100")

            # Wait for treatment condition field to be clickable
            treatment_condition_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='treamentcondition2']")))
            treatment_condition_field.send_keys("Mastectomy")

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor2']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)

            # Wait for thank you message to be visible
            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())



            except (TimeoutException, NoSuchElementException):
                print("failed 2nd Except")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()



        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")







    def BookAppointmentButtonMethod(self):
        #self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")

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
            contact_field.send_keys("1000000100")

            # Wait for the treatment condition field to be visible and send keys
            treatment_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='treamentcondition2']")))
            treatment_field.send_keys("Mastectomy")

            # Wait for the Book An Appointment button to be clickable and click it
            book_an_ap_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadSubmitDoctor2']")))
            book_an_ap_button.click()

            # Wait for the Thank You message to appear and print it
            thank_you = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.text)
            print("BookAppointmentButtonMethod success")

            # Go back to the previous page
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()


        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")










    def BookAppointmentMainForm(self):

        #self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            # self.driver.implicitly_wait(2)
            # BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            # self.driver.execute_script("arguments[0].click();", BookApButton)
            # self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Treatment ")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor']")
            # self.driver.execute_script("arguments[0].click();", NameTextBox)

            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='treatmentcondition']").send_keys("Mastectomy")

            # BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome']")
            # drop1 = Select(BengaluruCity)
            # drop1.select_by_visible_text("Bengaluru")

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("BookAppointmentMainForm is Successfully done")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()



        except (NoSuchElementException,TimeoutException):

            print("Message: no such element: Unable to locate element")
