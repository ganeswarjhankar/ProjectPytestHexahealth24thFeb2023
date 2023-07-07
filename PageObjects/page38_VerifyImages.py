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

from utilities.BaseClass import commonbaseclass


class VerifyImages_Class(commonbaseclass):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.VERIFYIMAGES_URL)




    def verify_images_method(self):
        self.driver.maximize_window()
        # Find all image elements on the page
        images = self.driver.find_elements(By.TAG_NAME, "img")

        # Verify that each image is displayed
        for image in images:
            if image.is_displayed():
                print("images are displayed: {}".format((image.get_attribute("src"))))
            else:
                print("Image is broken: {}".format(image.get_attribute("src")))
            #assert image.is_displayed(), "Image is not displayed: {}".format(image.get_attribute("src"))

    def test_check_broken_links(self):

        # Find all the <a> elements on the page
        links = self.driver.find_elements(By.TAG_NAME, "a")

        for link in links:
            href = link.get_attribute("href")

            try:
                # Check if the link is accessible

                wait = WebDriverWait(self.driver, 30)
                wait.until(EC.url_to_be(href))

                response = urllib.request.urlopen(href)
                assert response.code == 200
            except urllib.error.HTTPError as e:
                # Handle HTTP errors, if needed
                print(f"HTTP Error: {e.code} - {href}")
            except urllib.error.URLError as e:
                # Handle URL errors, if needed
                print(f"URL Error: {e.reason} - {href}")
            except TimeoutException:
                # Handle timeout errors, if needed
                print(f"Timeout Error: {href}")
            except NoSuchElementException:
                # Handle element not found errors, if needed
                print(f"Element Not Found: {href}")











