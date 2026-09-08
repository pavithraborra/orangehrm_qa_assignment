from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    PIM = (By.XPATH, "//span[normalize-space()='PIM']")

    ADD_EMPLOYEE = (
        By.XPATH, "//a[normalize-space()='Add Employee']"
    )

    EMPLOYEE_LIST = (
        By.XPATH, "//a[normalize-space()='Employee List']"
    )

    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")

    SAVE_BUTTON = (
        By.XPATH, "//button[@type='submit']"
    )

    LOADER = (
        By.CSS_SELECTOR, ".oxd-form-loader"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_pim(self):

        pim = self.wait.until(
            EC.element_to_be_clickable(self.PIM)
        )

        ActionChains(self.driver).move_to_element(pim).perform()
        pim.click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.ADD_EMPLOYEE
            )
        )

    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_EMPLOYEE
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

    def add_employee(self, first_name, last_name):

        first = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        first.clear()
        first.send_keys(first_name)

        last = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        last.clear()
        last.send_keys(last_name)

        # Wait for OrangeHRM loader to disappear
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.LOADER
                )
            )
        except:
            pass

        # Scroll Save button into view
        save = self.wait.until(
            EC.presence_of_element_located(
                self.SAVE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            save
        )

        # Wait until clickable
        self.wait.until(
            EC.element_to_be_clickable(
                self.SAVE_BUTTON
            )
        ).click()

        # Wait for page to finish loading
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.LOADER
                )
            )
        except:
            pass

        self.wait.until(
            EC.presence_of_element_located(
                self.PIM
            )
        )

    def open_employee_list(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.EMPLOYEE_LIST
            )
        ).click()