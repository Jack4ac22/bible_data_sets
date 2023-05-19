from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
driver.get("https://www.google.com/search?q=english+to+arabic+translation&oq=english+to+arabic+translation&aqs=chrome..69i57j0i512l9.5302j0j7&sourceid=chrome&ie=UTF-8")
driver.maximize_window()
reject_but = driver.find_element(By.ID, "W0wltc")
reject_but.click()
textArea = driver.find_element(By.ID, "tw-source-text-ta")
textArea.click()
textArea.send_keys("Father is one person")
results_text = driver.find_elements(By.CLASS_NAME, "Y2IQFc")
for i,v in enumerate(results_text):
    print(i,v.text)
driver.close()
