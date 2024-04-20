from selenium import webdriver
import pickle
from pathlib import Path
BASE_DIR = Path(__file__).parent
login = Path(BASE_DIR / 'mylogin')
loginfile = Path(login / 'logincookie.pkl')


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.linkedin.com/login')

cookies = driver.get_cookies()

with open (loginfile, 'wb') as file:
    pickle.dump(cookies,file)