from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os
from dotenv import load_dotenv
import pickle

load_dotenv('C:\\Users\\Gabriel\\Documents\\GitHub\\linkedinconnections\\mylogin\\.env')
passw = os.getenv('senha')

driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login')

BASE_DIR = Path(__file__).parent
login = Path(BASE_DIR / 'mylogin')
loginfile = Path(login / 'logincookie.pkl')


with open(loginfile, 'rb') as file:
    cookies = pickle.load(file)
    
for cookie in cookies:
    driver.add_cookie(cookie)
    
driver.get('https://www.linkedin.com/feed')

element_password = driver.find_element(By.XPATH, '//*[@id="password"]')
element_password.send_keys(passw)
    
driver.find_element(By.XPATH, '/html/body/div/main/div[3]/div[1]/div[3]/form/div[2]/button').click()

search_el = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[1]/input')
search_el.send_keys('Developer', Keys.ENTER)

morepeople = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,\
    '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/a')))

morepeople.click()

connectbuttons = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')




nextpage = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]/span')

