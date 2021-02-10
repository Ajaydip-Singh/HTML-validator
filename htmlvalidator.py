from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()

browser.get('https://validator.w3.org/#validate_by_input')

delay = 10

try: 
    input_area = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID,"fragment"))) 
except TimeoutException:
    print('Failed to find input area')

input_area.send_keys('Random Text')

try: 
    check_btn = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="validate-by-input"]/form/p[2]/a')))
except TimeoutException:
    print('Failed to find submit button')

check_btn.click()

try: 
    results_elem = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="results"]'))) 
except:
    print('Failed to find results')

errors = []
for i in range(len(results_elem)):
    errors.append(results_elem[i].text) 
