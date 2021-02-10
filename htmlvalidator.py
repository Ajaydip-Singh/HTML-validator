import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

filename = sys.argv[1]
with open(filename, 'r') as f:
    content = f.read()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://validator.w3.org/#validate_by_input')

delay = 10

try: 
    input_area = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID,"fragment"))) 
    input_area.send_keys(content)
    
    check_btn = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="validate-by-input"]/form/p[2]/a')))
    check_btn.click()

    results_elem = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="results"]'))) 

    with open('validatorResult.txt', 'w') as f:
        for i in range(len(results_elem)):
            f.write(results_elem[i].text) 

except Exception as e:
    print(e)

finally:
    browser.quit()
    

