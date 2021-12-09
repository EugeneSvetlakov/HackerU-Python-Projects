import configparser
import time
from datetime import date

from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

# ДЗ № 7 Светлаков Е.С.
# Зайти на лмску и отметиться что был на уроке автоматически


# Encrypt passwd
key = 'vdEt5DDrwvuZB9tQVLGEoJPmGVVgmw3TtUbPkx0-KfY='
f = Fernet(key)
secret_text = "This is a secret text"
encrypted_text = f.encrypt(secret_text.encode())
decrypted_text = f.decrypt(encrypted_text)

# Get settings from file 'settings.ini'
config = configparser.ConfigParser()
config.read('./DZ/settings.ini')
config.sections()
usr_login = config['auth_data']['login']
encr_key = config['auth_data']['key'].encode()
encr_passwd = config['auth_data']['pwd'].encode()
f = Fernet(encr_key)
usr_passwd = f.decrypt(encr_passwd).decode()

# start
lesson_key = input("Введите код отметки посещения занятия: ")

driver = webdriver.Firefox()
driver.implicitly_wait(3)
my_link = "https://lms.hackeru.pro/my/"
driver.get(my_link)
time.sleep(2)

# get tags
login_input = driver.find_element(By.ID, 'username')
passwd_input = driver.find_element(By.ID, 'password')

# Enter data and click button
login_input.send_keys(usr_login)
passwd_input.send_keys(usr_passwd)
# time.sleep(2)
login_btn = driver.find_element(By.ID, 'loginbtn')
login_btn.click()
time.sleep(2)

# Go to Course
# //a[., 'Python Programming For Penetration Testing']
link_to_course = driver.find_element(
    By.XPATH,
    "//a[contains(text(), 'Python Programming For Penetration Testing')]")
link_to_course.click()
time.sleep(2)

link_to_lessons = driver.find_element(
    By.XPATH, "//a/span[contains(text(), 'Занятия курса')]")
link_to_lessons.click()
time.sleep(2)

# Current date
cur_date = date.today().strftime("%-d.%m.%y")
tr_cur_lesson = driver.find_element(
    By.XPATH, f"//tr/td[contains(text(), {cur_date})]")
# tr_cur_lesson = driver.find_element(
#     By.XPATH, "//td[contains(text(), '11.12.21')]")
link_send_present = driver.find_element(locate_with(
    By.XPATH, "//a[contains(text(), 'Отправить посещаемость')]")
    .to_right_of(tr_cur_lesson))
link_send_present.click()
time.sleep(2)

# Enter lesson code
find_input = driver.find_element(By.ID, 'id_studentpassword')
find_input.send_keys(lesson_key)
time.sleep(2)
save_btn = driver.find_element(By.ID, 'id_submitbutton')
save_btn.click()
