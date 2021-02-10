from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://validator.w3.org/#validate_by_input')

input_area = browser.find_element_by_id('fragment')
check_btn = browser.find_element_by_xpath('//*[@id="validate-by-input"]/form/p[2]/a')

input_area.send_keys('Some random text')

check_btn.click()
