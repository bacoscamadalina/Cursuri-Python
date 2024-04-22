'''
4.Create a new PyCharm project. Make sure it has a virtualenv. Install all the following packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file.
Create a main.py file and add the following lines to ensure that all packages are installed correctly:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
text_box.send_keys("Selenium")
submit_button.click()
driver.quit()


Working in pairs, upload your project to Github and send it to a colleague. Each one of you will run the other one’s
project.
'''