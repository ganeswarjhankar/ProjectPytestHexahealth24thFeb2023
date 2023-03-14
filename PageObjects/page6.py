# page_objects.py
from utilities import constants

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TreatmentClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.TREATMENT_URL)


    def BookAppointmentForm1(self):

        try:

            # self.driver.get("https://www.hexahealth.com/treatment/piles-laser-treatment")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)

            lead_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_field.send_keys("Test GJ Treatmentpage LeadFieldName")

            #self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Treatmentpage Name")
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")

            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("Query test")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()
            # Lead1 in CRM
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
            print("Lead is not created and failed")









    def TreatmentExpertDoctors(self):
        # self.driver.get("https://www.hexahealth.com/treatment/piles-laser-treatment")


        try:

            self.driver.maximize_window()

            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control00']")
            self.driver.execute_script("arguments[0].click();", one)

            two = self.driver.find_element(By.XPATH, "//*[@id='slick-slide00']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", two)

            lead_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_field.send_keys("Test GJ Treatment ")
            contact_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnum2']")))
            contact_field.send_keys("1000000100")

            city_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadcity2']")))
            city_field.send_keys("Gurugram")

            treament_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='treamentcondition1']")))
            treament_field.send_keys("Tips Procedure ")

            query_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadquery']")))
            query_field.send_keys("Query Test check")

            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", Button)
            # Lead3 in CRM
            self.driver.implicitly_wait(2)
            print("The Expert Doctor form is passed")

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


        except:
            print("Lead is not created and Failed")




    def NABHAccreditedHospitals(self):

        #self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control01']")
        self.driver.execute_script("arguments[0].click();", OneSlide)
        self.driver.implicitly_wait(2)
        BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
        self.driver.execute_script("arguments[0].click();", BookApButton)
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ XYZ")

        self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
        self.driver.implicitly_wait(2)

        BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
        drop1 = Select(BengaluruCity)
        drop1.select_by_visible_text("Bengaluru")

        BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement1']")
        self.driver.execute_script("arguments[0].click();",BookAnAppointmentButton )
        # Lead4 in CRM
        self.driver.implicitly_wait(2)
        print("NABHAccreditedHospitals Form is Passed")

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




    def BookAppointmentButtonMethod(self):
        #self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")
        self.driver.maximize_window()


        self.driver.implicitly_wait(2)
        BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
        self.driver.execute_script("arguments[0].click();", BookApButton)
        self.driver.implicitly_wait(2)

        lead_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='leadnamehome1']")))
        lead_field.send_keys("Test GJ Treatment ")

        contact_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='contactnumhome1']")))
        contact_field.send_keys("1000000100")



        #self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ Treatment ")
        #self.driver.implicitly_wait(2)
        #self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
        #self.driver.implicitly_wait(2)
        self.driver.implicitly_wait(2)
        BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
        drop1 = Select(BengaluruCity)
        drop1.select_by_visible_text("Bengaluru")

        BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement1']")
        self.driver.execute_script("arguments[0].click();",BookAnAppointmentButton)
        # Lead4 in CRM
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



    def BookAppointmentMainForm(self):
        #self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.implicitly_wait(2)
        # BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
        # self.driver.execute_script("arguments[0].click();", BookApButton)
        # self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Treatment ")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")
        self.driver.implicitly_wait(2)

        BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome']")
        drop1 = Select(BengaluruCity)
        drop1.select_by_visible_text("Bengaluru")

        BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement']")
        self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
        # Lead4 in CRM
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








