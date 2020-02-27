import webbrowser
from selenium import webdriver
import time
	
url = 'https://intranet.seidor.es/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html'

driver = webdriver.Chrome('C:\\Users\itach\Downloads\chromedriver_win32')
driver.get (url)

id_user = 'USERNAME_FIELD-inner'
id_password = 'PASSWORD_FIELD-inner'
id_login ='LOGIN_LINK'

user = 'cgarcia'
password = 'Codigo20!'

username = driver.find_element_by_id(id_user).send_keys(user)

password = driver.find_element_by_name(id_password).send_keys(password)

print("User and Password")
driver.find_element_by_name(id_login).click()
print("Click")
#driver.find_element_by_link_text("Acceder al sistema").click()