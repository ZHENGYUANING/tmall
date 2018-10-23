from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time 

# class login(object):
#     def __init__(self):
#         self.browser = webdriver.Chrome()
#         self.browser.get("https://music.163.com/")
#   
browser = webdriver.Chrome()
url = "https://music.163.com/"
browser.get(url)
browser.maximize_window()
wait = WebDriverWait(browser,25)
wait.until(
    EC.element_to_be_clickable((By.XPATH,'//a[contains(@class,"link s-fc3")]'))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH,'//a[@class="u-btn2 u-btn2-2"]'))
).click()

username = wait.until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="p"]'))
)

username.clear()
username.send_keys('15270284451')

password = wait.until(
   EC.presence_of_element_located((By.XPATH,'//*[@id="pw"]'))
)

password.clear()
password.send_keys('wawnsbxysmly')

login = wait.until(
    EC.presence_of_element_located((By.XPATH,'//a[@class="j-primary u-btn2 u-btn2-2"]'))
)

login.click()
