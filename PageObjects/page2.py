import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from utilities import constants


class CityHospitalClass:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.CITYHOSPITAL_URL)

    def cityhospitalbookmethod1(self):

        # self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
        #self.driver.implicitly_wait(5)
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

        Handles2 = self.driver.window_handles[0]

        ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
        print("Book Appointment is Successfully done")
        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def cityhospitallistmethod2(self):

        # self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        BookAppointmentButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[3]/a[2]/span").click()
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

        Handles2 = self.driver.window_handles[0]

        ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
        print("Book Appointment is Successfully done")
        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def cityhospitalformmethod3(self):

        # self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
        # self.driver.implicitly_wait(5)
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
        self.driver.implicitly_wait(2)
        ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1")
        print(ThankYou.text)
        print("Book Appointment is Successfully done")
        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

