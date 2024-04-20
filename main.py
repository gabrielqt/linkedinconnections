from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os
from dotenv import load_dotenv
import pickle
from bs4 import BeautifulSoup
name = ''

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

idsbtn = ["ember257", "ember258", "ember259", "ember260", "ember261"]
text = f'Oi tudo bem {name}? Achei seu perfil interessante, parece que compartilhamos ideias semelhantes, acredito que poderíamos trocar idéias no futuro! '

for id_ in idsbtn:
    connectbtn = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, id_)))
    name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/p/span/strong').text
    '-'.join(name)
    name = name.split()
    name = name[0]
    driver.find_element(By.CSS_SELECTOR,'[aria-label="Adicionar nota"]').click()
    note = driver.find_element(By.XPATH, '//*[@id="custom-message"]')
    note.send_keys(text)
    
    

nextpage = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]/span')

