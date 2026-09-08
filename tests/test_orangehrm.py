import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.employee_list_page import EmployeeListPage


URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

USERNAME = "Admin"
PASSWORD = "admin123"


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(URL)

    yield driver

    driver.quit()


def test_employee_workflow(driver):

    # ---------------- LOGIN ----------------

    login = LoginPage(driver)

    login.login(
        USERNAME,
        PASSWORD
    )

    print("Login Successful")


    # ---------------- PIM ----------------

    pim = PIMPage(driver)

    pim.open_pim()

    print("PIM Opened")


    # ---------------- ADD EMPLOYEES ----------------

    employees = [
        ("Pavithra", "QA"),
        ("Rahul", "Tester"),
        ("Anjali", "Engineer"),
        ("Kiran", "Analyst")
    ]

    for first_name, last_name in employees:

        pim.click_add_employee()

        pim.add_employee(
            first_name,
            last_name
        )

        print(
            f"Employee Added: {first_name} {last_name}"
        )

        # Go back to PIM
        pim.open_pim()


    # ---------------- EMPLOYEE LIST ----------------

    pim.open_employee_list()

    print("Employee List Opened")


    # ---------------- VERIFY ----------------

    employee_list = EmployeeListPage(driver)

    for first_name, last_name in employees:

        assert employee_list.verify_employee(
            first_name
        )


    # ---------------- LOGOUT ----------------

    user_menu = (
        By.XPATH,
        "//span[contains(@class,'oxd-userdropdown-tab')]"
    )

    logout = (
        By.XPATH,
        "//a[normalize-space()='Logout']"
    )

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(user_menu)
    ).click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(logout)
    ).click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.NAME, "username")
        )
    )

    print("Logout Successful")