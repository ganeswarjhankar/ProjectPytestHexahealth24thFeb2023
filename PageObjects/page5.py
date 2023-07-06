# page_objects.py
from utilities import constants

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException











class ConditionClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.ConditionPage_URL)

    def BookAppointmentForm1(self):
        # self.driver.get("https://www.hexahealth.com/condition/piles")
        try:

            wait = WebDriverWait(self.driver, 10)

            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadnamecondition4']").send_keys("test Condition Page URL 1")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumcondition4']").send_keys("9000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcitycondition4']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_index(2)

            #YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            #drop2 = Select(YogaTreatment)
            #drop2.select_by_index(2)

            #self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("Query test")
            #query_text_xpath=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@id='leadquery']")))
            #query_text_xpath.send_keys("Query test")



            submit_button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='LeadSubmitCondition4']")))
            submit_button_xpath.click()

            #self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()

            try:

                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
                print("Lead is Generated Successfully")




            except (NoSuchElementException,TimeoutException):
                print("Message: no such element: Unable to locate element")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except (NoSuchElementException,TimeoutException):

            print("Message: no such element: Unable to locate element")









    def NABHAccreditedHospitals(self):
        # self.driver.get("https://www.hexahealth.com/condition/piles")

        try:
            self.driver.maximize_window()

            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control20']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            two = self.driver.find_element(By.XPATH, "//*[@id='slick-slide21']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", two)
            self.driver.implicitly_wait(2)

            #self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Gj Test check")
            #self.driver.implicitly_wait(2)

            wait = WebDriverWait(self.driver, 10)

            lead_name_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadnamecondition2']")))
            lead_name_xpath.send_keys("Test Condtionpage URL 2")



            contact_num = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contactnumcondition2']")))
            contact_num.send_keys("9000000100")

            #self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcitycondition2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_index(2)

            # self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            # self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition2']")
            self.driver.execute_script("arguments[0].click();", Button)
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











    def ConditionExpertDoctors(self):
        # self.driver.get("https://www.hexahealth.com/condition/piles")

        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control10']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", OneSlide)
            self.driver.execute_script("arguments[0].click();", OneSlide)
            self.driver.implicitly_wait(2)
            BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", BookApButton)
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamecondition2']").send_keys("Test conditon page Url 3")

            contact_num = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnumcondition2']")))
            contact_num.send_keys("9000000100")

           # self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcitycondition2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_index(2)

            self.driver.implicitly_wait(2)
            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition2']")
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




        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")








    def BookAppointmentButtonMethod(self):
        # self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")

        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.refresh()
            self.driver.implicitly_wait(2)
            BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            lead_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='leadnamecondition2']")))
            lead_field.send_keys("Test condition page Url 4 ")
            contact_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnumcondition2']")))
            contact_field.send_keys("9000000100")

            # self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ Treatment ")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcitycondition2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_index(3)

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition2']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)

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











    def BookAppointmentMainForm(self):
        # self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")

        try:
            self.driver.maximize_window()

            self.driver.implicitly_wait(2)
            # BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            # self.driver.execute_script("arguments[0].click();", BookApButton)
            # self.driver.implicitly_wait(2)

            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadnamecondition1']").send_keys("Test Condition page Url 5")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumcondition1']").send_keys("9000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcitycondition1']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_index(5)

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition1']")
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


        except NoSuchElementException:

            print("Message: no such element: Unable to locate element")
