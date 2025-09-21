from selenium.webdriver.common.by import By

class AboutPage:
  """Represents the About Page"""
  def __init__(self, driver):
    self.driver = driver
    self.about_heading = (By.CSS_SELECTOR, "body > div > h1")

  def get_about_header_text(self):
        return self.driver.find_element(*self.about_heading).text