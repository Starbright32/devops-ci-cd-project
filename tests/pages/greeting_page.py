from selenium.webdriver.common.by import By

class GreetingPage:
    """Represents the greeting page of the application."""
    def __init__(self, driver):
        self.driver = driver
        self.greeting_heading = (By.TAG_NAME, "h1")

    def get_greeting_text(self):
        """Returns the text of the greeting heading."""
        return self.driver.find_element(*self.greeting_heading).text
