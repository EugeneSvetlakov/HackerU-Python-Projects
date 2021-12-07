from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
# my_link = "https://hackeru.com/contact-us/"
my_link = "https://hackeru.com/"
driver.get(my_link)
# driver.maximize_window()

find_link_contact = driver.find_element(By.ID, 'mega-menu-item-1530')
find_link_contact.find_element(By.TAG_NAME, 'a').click()

full_name_fild = driver.find_element(
    By.ID, 'fullName')
full_name_fild.send_keys('MyName')

email_fild = driver.find_element(
    By.ID, 'email')
email_fild.send_keys('MyName@mail.ru')

phone_fild = driver.find_element(
    By.NAME, 'phone')
phone_fild.send_keys('465484')
