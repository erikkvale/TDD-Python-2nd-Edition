from selenium import webdriver

driver_path = r'drivers\chromedriver.exe'

browser = webdriver.Chrome(executable_path=driver_path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
