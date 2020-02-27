import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome('C:\\Users\itach\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver')  # Optional argument, if not specified will search path.
#driver = webdriver.Chrome('C:\\Webdrivers') 
driver = webdriver.Chrome('C:\\Users\itach\Downloads\chromedriver_win32 (1)\chromedriver.exe') 

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.close()

#Message: 'webdriver' executable may have wrong permissions.
