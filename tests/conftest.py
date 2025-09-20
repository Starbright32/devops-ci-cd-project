import pytest
from selenium import webdriver

# This fixture provides a Selenium WebDriver instance for all tests in the project.
@pytest.fixture(scope="module")
def driver():
    """Provides a Selenium WebDriver instance for a test module."""
    # Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    yield driver
    # Close the browser instance after all tests in the module are complete
    driver.quit()
