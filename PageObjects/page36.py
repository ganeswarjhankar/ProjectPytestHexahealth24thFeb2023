from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities import constants
import time
import urllib.request
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException


class marketing_TopSticky_Class:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        df = pd.read_excel(constants.MARKETING_TOPSTICKY_URL, sheet_name=constants.MARKETING_TOPSTICKY_SHEET)
        self.urls = df.sample(2, replace=False)['URL']

    def marketing_topsticky_method(self):
        for url in self.urls:
            self.driver.get(url)
            print([url])
            self.verify_whatsapp_PAN()    ## calling the function method in the mid to execute



            try:


                self.driver.maximize_window()
                self.driver.implicitly_wait(5)

                wait = WebDriverWait(self.driver, 10)

                lead_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='leadname5']")))
                lead_name.send_keys("Test GJ Marketing Variant")

                # self.driver.find_element(By.XPATH, "//input[@id='leadname5']").send_keys("Test GJ Doctor Variant")
                # self.driver.implicitly_wait(2)

                contact_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contactnum5']")))
                contact_name.send_keys("9000000100")



                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='LeadSubmit']")))
                submit_button.click()



                try:
                    thank_you = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/h1")))
                    print(thank_you.is_displayed())
                    print("Lead is Generated Successfully")
                    # print(f"Book Appointment is Successfully done for {url}")

                    # wait = WebDriverWait(self.driver, 10)
                    # wait.until(EC.title_contains("Thank You"))
                    # thank_you = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
                    # print("Thank You message is displayed")






                except (TimeoutException, NoSuchElementException, InvalidArgumentException):
                    print("Exception with Timeout and No elements found")

                self.driver.back()
                self.driver.implicitly_wait(2)
                self.driver.refresh()


            except (TimeoutException, NoSuchElementException, InvalidArgumentException):

                print("Except Block-Lead failed to Generate")



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





