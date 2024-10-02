from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

github_url = input("Enter a public GitHub repository: ")

# initialize chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # run in headless mode
chrome_options.add_argument("--no-sandbox")  # bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # overcome resource limitations

# intialize the web driver
driver = webdriver.Chrome(options=chrome_options)

# navigate to the webpage
driver.get("https://repo2txt.simplebasedomain.com/")

# find the input element and enter content
github_url_input = driver.find_element(By.ID, "repoUrl")
github_url_input.send_keys(github_url)

# find the button and click it
# fetch_button = driver.find_element(
#     By.XPATH, "//button[contains(text(), 'Fetch Directory Structure')]"
# )
fetch_button = driver.find_element(By.CSS_SELECTOR, "button.bg-blue-500")
fetch_button.click()
time.sleep(1)


generate_text_file_button = driver.find_element(By.ID, "generateTextButton")
generate_text_file_button.click()
time.sleep(1)

# wait for the textarea to be populated (adjust the timeout as needed)
textarea = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.ID, "outputText"), "")
)

# get the context of textarea
result_content = driver.find_element(By.ID, "outputText").get_attribute("value")

print("Extracted Content: ")
print(result_content)

driver.quit()
