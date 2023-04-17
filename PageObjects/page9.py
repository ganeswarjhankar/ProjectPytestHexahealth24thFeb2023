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




class BlogPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.CITYDOCTOR_URL)

    def BlogpageMethodForm(self):

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










    def BlogSearchmethod(self):
        try:
            #self.driver =driver
            self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Piles Laser Treatment")

            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Piles Laser Treatment")))
            self.driver.find_element(By.LINK_TEXT, "Piles Laser Treatment").click()
            print("'Piles Laser Treatment'  is been Searched successfully")
            handles = self.driver.window_handles



        except:
            print("Get a FREE Second Opinion from Top Surgeons! Book an Appointment » Form link got failed")




    def BookAppointmentForm1(self):
        try:
            self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
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
            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Get a FREE Second Opinion from Top Surgeons! Book an Appointment » Successfully Passed")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()
            self.driver.quit()

        except:
            print("Get a FREE Second Opinion from Top Surgeons! Book an Appointment » Form link got failed")




    def ContactUsWhatsapp(self):
        #import urllib.request

        try:
            self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
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


        except:
            print("Failed")

            # finally:
            # print("This is Cost Variant Marketing Pages")


    def ExpertDoctors(self):
        try:
            self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
            self.driver.maximize_window()


            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control40']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            two =self.driver.find_element(By.XPATH, "//*[@id='slick-slide40']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", two)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Gj Test check")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")


        #self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")

        #self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            self.driver.implicitly_wait(2)
            Button =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", Button)
            # Lead3 in CRM
            self.driver.implicitly_wait(2)
            print("The Expert Doctor form is passed")

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except:
            print("The Expert Doctors form is failed")
        self.driver.quit()





    def NABHAccreditedHospitals(self):
        try:

            self.driver.get("https://www.hexahealth.com/blog/best-age-to-get-pregnant")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control50']")
            self.driver.execute_script("arguments[0].click();", OneSlide)
            self.driver.implicitly_wait(2)
            BookApButton =self.driver.find_element(By.XPATH, "//*[@id='slick-slide50']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ XYZ")

            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test")



            BookAnAppointmentButton =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            print("NABHAccreditedHospitals Form is Passed")

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except:
            print("NABHAccreditedHospitals Form is Failed")