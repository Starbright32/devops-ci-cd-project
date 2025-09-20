import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.pages.index_page import IndexPage
from tests.pages.greeting_page import GreetingPage

def test_greeting_with_name(driver):
    # Instantiate the page objects
    index_page = IndexPage(driver)
    greeting_page = GreetingPage(driver)

    # Navigate to the Flask application's home page
    driver.get("http://127.0.0.1:5000")

    # Perform actions using the page object methods
    index_page.enter_name("Alice")
    index_page.submit_form()

    # Wait for the greeting element to be visible before asserting
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(greeting_page.greeting_heading)
    )

    # Verify the greeting on the next page
    assert "Hello, Alice!" in greeting_page.get_greeting_text()
