
#importing all library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

#Put username 
usernameStr = ''

#Put password
passwordStr = ''

#First download chromedriver and then Give the path of the chromedriver.exe file in driver 
driver=webdriver.Chrome("F:\work\DIWALI\chromedriver.exe")

#Opening instagram 
driver.get('https://www.instagram.com/accounts/login')
sleep(2)

#entering username
username=driver.find_element_by_name('username')
username.send_keys(usernameStr)

#entering password
password=driver.find_element_by_name('password')
password.send_keys(passwordStr)

sleep(1)

#clicking loging button
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()

sleep(3)

#Opening the account 
driver.get('https://www.instagram.com/'+usernameStr)
sleep(3)

#Finding the follow button and then clicking it
all_spans = driver.find_elements_by_xpath("//ul/li[3]/a/span")
all_spans[0].click()
sleep(10)

#scrolling down the follow list to open all the account
for n in range(1,50):
    unfollowWindow2 = driver.find_element_by_xpath("//button[contains(.,'Following')]")
    unfollowWindow2.send_keys(Keys.END)
    print(n)
    sleep(2)

	
#Start unfollowing all the account
for i in range(1,150):
    try:
        unfollowWindow = driver.find_element_by_xpath("//button[contains(.,'Following')]")

        unfollowWindow.click()
        sleep(2)
        unfollow=driver.find_element_by_xpath("//button[contains(.,'Unfollow')]")
        unfollow.click()
        print(i)
        sleep(45)

    except Exception as e:
        print(e)

    
	
	
	
	
	