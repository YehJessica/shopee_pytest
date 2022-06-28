from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options

driver = uc.Chrome(use_subprocess=True)
# driver = webdriver.Chrome(ChromeDriverManager().install()) #登入帳號後,下一頁不能輸入,改用uc
driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F")


shopee_web = driver.current_window_handle
time.sleep(5)

# 點選Google按鈕
user_button = driver.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[2]')
# user_button=driver.find_element_by_class_name('lCoei YZVTmd SmR8')  #ng
user_button.click()

# 處理2個windoows
for handle in driver.window_handles:
    if handle != shopee_web:
        login_page = handle

driver.switch_to.window(login_page)

time.sleep(5)
""""
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div').click()
driver.switch_to.window(shopee_web)
time.sleep(12)
"""

# 登入mail
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('........')

# 確認帳號
time.sleep(5)
#wait = WebDriverWait(driver, 20)
#next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]')))
go1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
go1.click()
time.sleep(5)


# 登入password
password = driver.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(',,,,,,,')
time.sleep(5)
go2 = driver.find_element_by_xpath(
    '//*[@id="passwordNext"]/div/button/span').click()
# go2=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[3]').click()
time.sleep(5)


# 交換控制的網頁
driver.switch_to.window(shopee_web)
""""
#關閉chrom通知
option= Options()
option.add_argument('--disable-notification')
option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", 
{"profile.default_content_setting_values.notifications": 2 
 }) 
"""""
time.sleep(5)

# 比對user name
# 關閉首頁通知
driver.maximize_window()
time.sleep(10)

ActionChains(driver).move_by_offset(950, 106).click(
).perform()  # 滑鼠左鍵點擊 ,使用coordinates chorm找 x,y

# 使用class name 值比對
# user_name=driver.find_element_by_xpath('//*[@id="stardust-popover6"]/div/div/div[2]').click()
user_name = driver.find_element_by_class_name('navbar__username')
print(user_name.text)
"""""
if 'jessiceyeh'in user_name.text:
    print('pass,user_name is correct')
else :
    print('user_name is wrong')
"""
assert 'jessiceyeh' in user_name.text
driver.quit()
