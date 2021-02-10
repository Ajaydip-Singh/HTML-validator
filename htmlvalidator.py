from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://validator.w3.org/#validate_by_input')

input_area = browser.find_element_by_id('fragment')

input_area.send_keys('Some random text')