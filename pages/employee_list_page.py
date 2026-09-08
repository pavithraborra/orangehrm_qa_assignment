from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class EmployeeListPage:

    EMPLOYEE_NAME = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']/following::input[1]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    AUTOCOMPLETE = (
        By.XPATH,
        "//div[contains(@class,'oxd-autocomplete-option')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_employee(self, first_name):

        box = self.wait.until(
            EC.element_to_be_clickable(self.EMPLOYEE_NAME)
        )

        # Completely clear previous search
        box.click()
        box.send_keys(Keys.CONTROL, "a")
        box.send_keys(Keys.BACKSPACE)

        # Type new name
        box.send_keys(first_name)

        # Select autocomplete
        try:
            option = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.AUTOCOMPLETE)
            )
            option.click()
        except:
            pass

        # Search
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()

        time.sleep(2)

        # Get current page text
        text = self.driver.find_element(
            By.TAG_NAME, "body"
        ).text.lower()

        # Verify searched name
        if first_name.lower() in text:
            print(f"{first_name} - Name Verified")
            return True

        print(f"{first_name} - Name NOT Verified")
        return False