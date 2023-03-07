# Estudiantes:
# Natalia Andrea Bohorquez Chevejoni.  cc: 1035869600
# Karen Vanessa Marin Marin.  cc: 1017236921

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://buggy.justtestit.org/register")

Login = driver.find_element(By.NAME, 'username')
Login.send_keys("Maria1133445566" + Keys.TAB)

First_Name = driver.find_element(By.NAME, 'firstName')
First_Name.send_keys("Maria" + Keys.TAB)

Last_Name = driver.find_element(By.NAME, 'lastName')
Last_Name.send_keys("Gomez" + Keys.TAB)

Password = driver.find_element(By.ID, "password")
Password.send_keys("Maria123." + Keys.TAB)

Confirm_Password = driver.find_element(By.ID, "confirmPassword")
Confirm_Password.send_keys("Maria123." + Keys.ENTER)



time.sleep(10)
