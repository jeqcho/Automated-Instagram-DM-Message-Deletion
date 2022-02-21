import time
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

# malicious_domain = "socialbox"
malicious_domain = input("Enter malicious domain keyword: ")

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://instagram.com/')
print("opened browser to instagram")

WebDriverWait(driver, 1000).until(presence_of_element_located((By.CLASS_NAME, "xWeGp")))
driver.find_elements(By.CLASS_NAME, "xWeGp")[0].click()
print("navigating to DMs")

WebDriverWait(driver, 1000).until(presence_of_element_located((By.CLASS_NAME, "HoLwm")))
driver.find_elements(By.CLASS_NAME, "HoLwm")[0].click()
print("Dismissed notification request")

WebDriverWait(driver, 1000).until(presence_of_element_located((By.CLASS_NAME, "rOtsg")))
print("Users loaded")
users = driver.find_elements(By.CLASS_NAME, "rOtsg")
SCROLL_PAUSE_TIME = 0.5

# Stopper for cases where the program needs to skip some users (ie the program was terminated prematurely)
input("Paused, please press enter when you have scrolled to the users affected")

while True:
    user = driver.find_element(locate_with(By.CLASS_NAME, "rOtsg").below({By.CLASS_NAME: "S-mcP"}))
    user.click()
    WebDriverWait(driver, 1000).until(presence_of_element_located((By.CLASS_NAME, "frMpI")))
    chatbox = driver.find_elements(By.CLASS_NAME, 'frMpI')[0]
    for i in range(5):
        try:
            malicious_message = chatbox.find_element(By.PARTIAL_LINK_TEXT, malicious_domain)
        except NoSuchElementException:
            driver.execute_script("document.getElementsByClassName('frMpI')[0].scrollBy(0, -450);")
            driver.implicitly_wait(SCROLL_PAUSE_TIME)
            continue
        webdriver.ActionChains(driver).move_to_element(malicious_message).perform()
        print('Mouse hovering above danger message')
        WebDriverWait(driver, 1000, ignored_exceptions=StaleElementReferenceException).until(
            presence_of_element_located((By.CLASS_NAME, "rrUvL")))
        driver.find_elements(By.CLASS_NAME, 'rrUvL')[0].click()
        print('Clicked extra options')
        buttons = driver.find_elements(By.CLASS_NAME, 'qyrsm')
        print(f'Number of buttons {len(buttons)}')
        if len(buttons) < 3 or buttons[2].text != 'Unsend':
            print('skip deletion')
            continue
        buttons[2].click()
        print('init deletion')

        WebDriverWait(driver, 1000).until(presence_of_element_located((By.CLASS_NAME, "-Cab_")))
        driver.find_elements(By.CLASS_NAME, '-Cab_')[0].click()
        print('Unsent')
        time.sleep(1)
        break
    driver.execute_script("document.getElementsByClassName('N9abW')[0].scrollBy(0, 71);")

# infinite loop
driver.quit()
