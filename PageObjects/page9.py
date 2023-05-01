# page_objects.py
from utilities import constants

import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException











class BlogClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.BlogPage_URL)

    def BookAppointmentForm12(self):
        # self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
        try:

            wait = WebDriverWait(self.driver, 10)

            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("9000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            #self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("Query test")
            query_text_xpath=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@id='leadquery']")))
            query_text_xpath.send_keys("Query test")



            submit_button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='LeadSubmitNewHome']")))
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

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control51']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            Two_Book_Button = self.driver.find_element(By.XPATH, "//*[@id='slick-slide51']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", Two_Book_Button)
            self.driver.implicitly_wait(2)

            #self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Gj Test check")
            #self.driver.implicitly_wait(2)

            wait = WebDriverWait(self.driver, 10)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test Lead patient name")



            contact_num = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnum2']")))
            contact_num.send_keys("9000000100")

            #self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//*[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            Treatment_xpath = self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']")
            drop1 = Select(Treatment_xpath)
            drop1.select_by_visible_text("Yoga")

            query_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadquery']")))
            query_xpath.send_keys("Query Test")

            # self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            # self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
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











    def BlogExpertDoctors(self):
        # self.driver.get("https://www.hexahealth.com/condition/piles")

        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control41']")
            self.driver.execute_script("arguments[0].click();", OneSlide)
            self.driver.implicitly_wait(2)
            BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide41']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            wait = WebDriverWait(self.driver, 10)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test Lead patient name")

            contact_num = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnum2']")))
            contact_num.send_keys("9000000100")

            # self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//*[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            Treatment_xpath = self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']")
            drop1 = Select(Treatment_xpath)
            drop1.select_by_visible_text("Yoga")

            query_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadquery']")))
            query_xpath.send_keys("Query Test")

            # self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            # self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", Button)





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
            BookApButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a")
            self.driver.execute_script("arguments[0].click();", BookApButton)

            wait = WebDriverWait(self.driver, 10)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test Lead patient name")

            contact_num = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnum2']")))
            contact_num.send_keys("9000000100")

            # self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//*[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            Treatment_xpath = self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']")
            drop1 = Select(Treatment_xpath)
            drop1.select_by_visible_text("Yoga")

            query_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadquery']")))
            query_xpath.send_keys("Query Test")

            # self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            # self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
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











    def BookAppointmentMainForm(self):
        # self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")

        try:
            wait = WebDriverWait(self.driver, 10)
            self.driver.maximize_window()

            self.driver.implicitly_wait(2)
            # BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            # self.driver.execute_script("arguments[0].click();", BookApButton)
            # self.driver.implicitly_wait(2)

            self.driver.implicitly_wait(2)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadnamehome']")))
            lead_name_xpath.send_keys("Test Lead patient name")

            contact_num = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contactnumhome']")))
            contact_num.send_keys("9000000100")

            # self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            # self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//*[@id='leadcity1']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            Treatment_xpath = self.driver.find_element(By.XPATH, "//*[@id='treamentcondition']")
            drop1 = Select(Treatment_xpath)
            drop1.select_by_visible_text("Yoga")

            #query_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='leadquery']")))
            #query_xpath.send_keys("Query Test")

            # self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            # self.driver.implicitly_wait(2)
            # self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            # self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitBlog']")
            self.driver.execute_script("arguments[0].click();", Button)




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