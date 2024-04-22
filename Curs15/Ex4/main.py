from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
text_box.send_keys("Selenium")
submit_button.click()
driver.quit()