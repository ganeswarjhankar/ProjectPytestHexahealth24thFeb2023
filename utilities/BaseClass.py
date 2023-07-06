from utilities import constants
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
# import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def open(self):

        try:
            df = pd.read_excel(constants.MARKETING_BOARD_URL, sheet_name=constants.MARKETING_BOARD_SHEET_URL)
            self.urls = df.sample(3, replace=False)['URL']

        except:
            print("Excel file is not found")


"""This is common verification process of the whatsApp in all the marketing fields"""


class commonbaseclass:

    def __init__(self, driver):
        self.driver = driver

    def verify_whatsapp_PAN(self):

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

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def GetACallBack(self):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        MobileNo_text_footer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='contactnum1']")))
        MobileNo_text_footer.send_keys("9000000100")

        #self.driver.execute_script("arguments[0].scrollIntoView();", MobileNo_text_footer)

        BookApButton_Footer= self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit1_marketing']")
        #self.driver.execute_script("arguments[0].click();", BookApButton_call)

        self.driver.execute_script("arguments[0].scrollIntoView();", BookApButton_Footer)


        assert True


    def CheckInsuranceCoverage(self):

        self.driver.maximize_window()

        wait = WebDriverWait(self.driver, 10)

        InsuranceButton = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/i")
        self.driver.execute_script("arguments[0].click();", InsuranceButton)

        lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
        lead_name_xpath.send_keys("Test GJ Normal Marketing ")

        contact_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='contactnum2']")))
        contact_xpath.send_keys("9000000100")


        self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()

        try:
            wait = WebDriverWait(self.driver, 10)
            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.is_displayed())
        except:
            print("thank you is not displayed")

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()



    def CommonClosingProcess(self):

        try:
            wait = WebDriverWait(self.driver, 10)

            thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
            print(thank_you.is_displayed())
            print("Lead is Generated Successfully")

        except (TimeoutException, NoSuchElementException, InvalidArgumentException):
            assert False
            print("Exception with Timeout and No elements found")

        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def AllSingleClose(self):
        self.driver.back()
        self.driver.implicitly_wait(2)
        self.driver.refresh()

    def AllMarketing_List_Doctors(self):

        Name=self.driver.find_element(By.XPATH,"//*[@id='leadname2']")
        Name.send_keys("Test GJ Marketing")

        Mobile_number=self.driver.find_element(By.XPATH,"//*[@id='contactnum2']")
        Mobile_number.send_keys("9000000100")

















    def ListWhatsApp(self):
        WA1 = "//*[@id='whtsapHeaderBtn']/span/b"
        WA2 = "//*[@id='whtsaphandset']/span"
        WA3 = "//*[@id='whstpconslt']/img"
        WA4 = "//*[@id='whatspbottomBtn']/span"
        listWA = [WA1, WA2,WA3, WA4]

        self.driver.maximize_window()

        for button_WA in listWA:

            # Wait for the button to be clickable
            button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_WA)))

            try:
                # Scroll to the button's location

                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                time.sleep(1)

                button.click()
                time.sleep(5)
                current_url =self.driver.current_url
                print(current_url)

                # Verify that the current URL contains the expected value
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

            except Exception as e:
                print(f"Error clicking the button: {str(e)}")

            self.driver.back()
            self.driver.implicitly_wait(2)
            time.sleep(2)  # Add a short delay for demonstration purposes


#"""This Function is used in the Calculate Surgery button"""
    def CalculateSurgeryCost(self):

        for url in self.urls:
            self.driver.get(url)
            print([url])


            self.driver.maximize_window()

            wait = WebDriverWait(self.driver, 10)
            calculate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='surgerytBtn']/i")))
            self.driver.execute_script("arguments[0].click();", calculate_button)


            # CalculateButton = self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span")
            # self.driver.execute_script("arguments[0].click();", CalculateButton)

            # self.driver.execute_script("window.scrollTo(0, 2000)")
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, "//*[@id='surgerytBtn']/span").click()

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test GJ Normal Marketing ")

            # self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Test GJ Normal Marketing ")
            self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("9000000100")
            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()
            print("MarketingNormalForm1 is passed")
            self.driver.implicitly_wait(5)

            try:
                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
            except:
                print("thank you is not displayed")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()









            # print(f"Book Appointment is Successfully done for {url}")

















#"""This Function is used in the insurance coverage button"""

    def CheckInsuranceCoverage(self):

        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.driver.maximize_window()

            wait = WebDriverWait(self.driver, 10)

            InsuranceButton = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/i")
            self.driver.execute_script("arguments[0].click();", InsuranceButton)

            # Insurance = self.driver.find_element(By.XPATH, "//*[@id='insurancetBtn']/span")
            # self.driver.execute_script("arguments[0].click();", Insurance)

            lead_name_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leadname2']")))
            lead_name_xpath.send_keys("Test GJ Normal Marketing ")

            contact_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='contactnum2']")))
            contact_xpath.send_keys("9000000100")

            self.driver.find_element(By.XPATH, "//button[@id='LeadSubmit2']").click()

            try:
                wait = WebDriverWait(self.driver, 10)
                thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                print(thank_you.is_displayed())
            except:
                print("thank you is not displayed")

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()