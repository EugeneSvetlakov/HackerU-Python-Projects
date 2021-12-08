from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from cryptography.fernet import Fernet

# ДЗ № 7 Светлаков Е.С.
# Зайти на лмску и отметиться что был на уроке автоматически

# Encrypt passwd
key = 'vdEt5DDrwvuZB9tQVLGEoJPmGVVgmw3TtUbPkx0-KfY='
f = Fernet(key)
secret_text = "This is a secret text".encode()
encrypted_text = f.encrypt(secret_text)
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
driver = webdriver.Firefox()
my_link = "https://lms.hackeru.pro/my/"
driver.get(my_link)

# get tags
login_input = driver.find_element(By.ID, 'username')
passwd_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'loginbtn')

# Enter data and click button
login_input.send_keys(usr_login)
passwd_input.send_keys(usr_passwd)
login_btn.click()
