"""Search Script Overall Automation Pytest script"""

# page_objects.py
from utilities import constants
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException,StaleElementReferenceException,NoSuchElementException


class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(constants.Search_URL)
        self.driver.maximize_window()

    def Doctormethod(self):

        try:


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

        except (TimeoutException,StaleElementReferenceException):
            print("Search failed for Doctor")





    def Hospitalmethod(self):
        # self.driver = driver
        # self.driver.get("https://www.hexahealth.com/")
        #self.driver.implicitly_wait(5)
        try:

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
            Handles1 = self.driver.window_handles[0]
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except (TimeoutException, StaleElementReferenceException):
            print("Search Failed for Hospital")












    def TreatmentSearchmethod(self):
        # self.driver =driver
        # self.driver.get("https://www.hexahealth.com")
        #self.driver.implicitly_wait(5)
        try:

            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Piles Laser Treatment")

            # search_field3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Piles Laser Treatment")))
            # search_field3.click()

            wait = WebDriverWait(self.driver, 20)
            text_box_linktext=wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Piles Laser Treatment")))

            self.driver.implicitly_wait(5)

            text_link=wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Piles Laser Treatment")))
            text_link.click()


            #self.driver.find_element(By.LINK_TEXT, "Piles Laser Treatment").click()
            #print("'Piles Laser Treatment'  is been Searched successfully")
            Handles1 = self.driver.window_handles[0]


            #assert "HexaHealth" in self.driver.title





            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except (TimeoutException, StaleElementReferenceException):
            print("Search Failed for Treatment")










    def Conditionmethod(self):
        # self.driver.get("https://www.hexahealth.com/")
        #self.driver.implicitly_wait(5)

        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Gallstones")

            #search_field4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtArticls']")))
            #search_field4.send("Gallstones")

            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Gallstones")))
            BookApButton = self.driver.find_element(By.LINK_TEXT, "Gallstones")
            self.driver.execute_script("arguments[0].click();", BookApButton)

            print("Condition as GallStones  is been Searched successfully")
            Handles1 = self.driver.window_handles[0]
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except (TimeoutException, StaleElementReferenceException):
            print("Search Failed for condition")



