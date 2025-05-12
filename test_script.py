from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Connect to the Selenium server
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Navigate to a website and print the title
driver.get("https://www.example.com")
print("Page title is:", driver.title)

# Clean up
driver.quit()
