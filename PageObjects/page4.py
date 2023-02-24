"""Search Script Overall Automation Pytest script"""

# page_objects.py
from utilities import constants
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(constants.Search_URL)
        self.driver.maximize_window()

    def Doctormethod(self):

        self.driver.maximize_window()


        self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Anu Jain")
        self.driver.implicitly_wait(2)

        # search_field1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, " Aman Priya Khanna ")))
        # search_field1.click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Anu Jain")))
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "Anu Jain").click()

        print("Doctor Search is Working successfully")
        self.driver.implicitly_wait(5)
        Handles1 = self.driver.window_handles[0]
        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def Hospitalmethod(self):
        # self.driver = driver
        # self.driver.get("https://www.hexahealth.com/")
        #self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # SearchBox = driver.find_element(By.XPATH,"//input[@id='txtArticls']").send_keys("Anu")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Apollo Hospital, Noida")

        # search_field2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Apollo Hospital, Noida")))
        # search_field2.click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Apollo Hospital, Noida")))
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "Apollo Hospital, Noida").click()
        print("Hospital Apollo is been Searched successfully")
        Handles2 = self.driver.window_handles[0]
        self.driver.back()
        self.driver.implicitly_wait(2)

        self.driver.refresh()

    def TreatmentSearchmethod(self):
        # self.driver =driver
        # self.driver.get("https://www.hexahealth.com")
        #self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Piles Laser Treatment")

        # search_field3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Piles Laser Treatment")))
        # search_field3.click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Piles Laser Treatment")))
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT,"Piles Laser Treatment").click()
        print("'Piles Laser Treatment'  is been Searched successfully")
        Handles3 = self.driver.window_handles[0]
        self.driver.back()
        self.driver.implicitly_wait(2)

        self.driver.refresh()

    def Conditionmethod(self):
        # self.driver.get("https://www.hexahealth.com/")
        #self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Gallstones")

        # search_field4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Gallstones")))
        # search_field4.click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Gallstones")))
        BookApButton = self.driver.find_element(By.LINK_TEXT, "Gallstones")
        self.driver.execute_script("arguments[0].click();", BookApButton)


        print("Condition as GallStones  is been Searched successfully")
        Handles4 = self.driver.window_handles[0]
        self.driver.back()
        self.driver.implicitly_wait(2)

        self.driver.refresh()
