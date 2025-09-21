from selenium.webdriver.common.by import By

class IndexPage:
    """Represents the index page of the application."""
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "name")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.about_link = (By.CSS_SELECTOR, "body > a")
    
    def click_about(self):
        about_element = self.driver.find_element(*self.about_link)
        about_element.click()

    def enter_name(self, name):
        """Enters a name into the input field."""
        name_input_element = self.driver.find_element(*self.name_input)
        name_input_element.send_keys(name)

    def submit_form(self):
        """Clicks the submit button."""
        submit_button_element = self.driver.find_element(*self.submit_button)
        submit_button_element.click()
