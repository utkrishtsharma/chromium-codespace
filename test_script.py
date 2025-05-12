from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Connect to the Selenium server
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)

# Navigate to a website
driver.get("https://www.example.com")

# Perform actions
print(driver.title)

# Clean up
driver.quit()
