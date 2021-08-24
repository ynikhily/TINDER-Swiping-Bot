from selenium import webdriver
import time


options = webdriver.ChromeOptions()
# Path to your chrome profile. Default profile is used to retain the login session.
options.add_argument("user-data-dir=C:/Users/<Your user>/AppData/Local/Google/Chrome/User Data")
chrome_driver_path = ""  # PATH TO YOUR CHROMEDRIVER.EXE
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()
time.sleep(10)
time.sleep(10)
time.sleep(10)
reject_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')

start_time = time.time()
end_time = start_time + 60

while time.time() < end_time:
    reject_button.click()
    time.sleep(5)

driver.quit()
