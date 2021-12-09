import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
[doc_and_examples](https://selenium-python.readthedocs.io/installation.html#introduction)
[location_elements](https://selenium-python.readthedocs.io/locating-elements.html)
[Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
[Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
[Firefox](https://github.com/mozilla/geckodriver/releases)
[Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

1. add +x rights
2. place to venv/bin directory

[selenium_antidetect](https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver)
[oz:firefoxOptions.binary](https://stackoverflow.com/questions/65318382/expected-browser-binary-location-but-unable-to-find-binary-in-default-location)

[try_find_by_XPATH](http://xpather.com/)
"""


driver = webdriver.Firefox()
driver.get("https://yandex.ru")
driver.maximize_window()
input_text = driver.find_element(By.ID, 'text')
time.sleep(1)
for c in "Мамкин хакер ищет ботинки":
    time.sleep(0.3)
    input_text.send_keys(c)

time.sleep(2)
search_div = driver.find_element(By.CLASS_NAME, 'search2__button')
btn = search_div.find_element(By.TAG_NAME, 'button')
btn.click()
