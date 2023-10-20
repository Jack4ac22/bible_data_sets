from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def translate_this(text):
    driver = webdriver.Chrome(
        options=options, executable_path='./chromedriver')
    driver.get("https://www.google.com/search?q=english+to+arabic+translation&oq=english+to+arabic+translation&aqs=chrome..69i57j0i512l9.5302j0j7&sourceid=chrome&ie=UTF-8")
    driver.maximize_window()
    reject_but = driver.find_element(By.ID, "W0wltc")
    reject_but.click()
    textArea = driver.find_element(By.ID, "tw-source-text-ta")
    textArea.click()
    time.sleep(random.uniform(0.3, 1))
    for i in text:
        textArea.send_keys(i)
        time.sleep(random.uniform(0, 0.2))
    # for i, v in enumerate(results_text):
    #     print(i, v.text)
    time.sleep(random.uniform(2, 4))
    results_text = driver.find_elements(By.CLASS_NAME, "Y2IQFc")
    time.sleep(random.uniform(0.5, 0.7))
    res = results_text[2].text
    time.sleep(1)
    driver.close()
    print('done')
    return res


def updateText(text: str, desired_length: int):
    if len(text) > desired_length:
        splited = text.split("). ")
        updated_sample = ""
        for portion in splited:
            updated_sample = updated_sample + "). "+ translate_this(portion)
        # print(type(portion))
            # print((portion))
        # print(updated_sample)
    else:
        updated_sample = translate_this(text)
    return updated_sample

# updateText("Hi My name is Jack and I am here testing this app. I do not know if google will catch this, but it is worth it to try", 30)