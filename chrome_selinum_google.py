from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
service = Service(executable_path='./chromedriver')
 
chrome_browser = webdriver.Chrome(service=service)