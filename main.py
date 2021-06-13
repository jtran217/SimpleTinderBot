from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

#EMAIL AND PASS IN RESPECT TO FACEBOOK LOGIN
EMAIL = "YOUREMAIL"
PASS = "YOURPASSWORC"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
URL = "https://tinder.com/"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.maximize_window()
driver.get(URL)

sleep(3)
login = driver.find_element_by_xpath('//*[@id="u86258596"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
sleep(3)
fb_button = driver.find_element_by_xpath('//*[@id="u-1642122480"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_button.click()
sleep(5)


#Swtich Windows to FB
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#LOGIN FB
email_form = driver.find_element_by_id("email")
email_form.send_keys(EMAIL)
pass_form = driver.find_element_by_id("pass")
pass_form.send_keys(PASS)
pass_form.send_keys(Keys.ENTER)
sleep(3)

#LOCATION CONFIRMATION
driver.switch_to.window(base_window)
sleep(2)
allow_button = driver.find_element_by_xpath('//*[@id="u-1642122480"]/div/div/div/div/div[3]/button[1]')
allow_button.click()
sleep(2)
enable_button = driver.find_element_by_xpath('//*[@id="u-1642122480"]/div/div/div/div/div[3]/button[1]')
enable_button.click()
sleep(3)


#BUTTON FOR LIKING
#100 free swipe day for free account
for n in range(100):
    sleep(1)
    try:
        like_button = driver.find_element_by_xpath('//*[@id="u86258596"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup=driver.find_element_by_css_selector(".itsAmatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(2)

            
driver.quit()





