from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options


def OpenBrowser():
    driver = uc.Chrome(use_subprocess=True)
    driver.get("https://shopee.tw/m/topshop")
    driver.maximize_window()
    return(driver)


def ClickGooglebutton(driver):
    login = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/header/div[1]/nav/ul/a[3]')
    login.click()
    time.sleep(10)
    user_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[2]')
    user_button.click()


def GetloginwindowAndlogin(driver):
    shopee_web = driver.current_window_handle
    time.sleep(5)
    for handle in driver.window_handles:  # 處理2個windoows
        if handle != shopee_web:
            login_page = handle
    driver.switch_to.window(login_page)
    time.sleep(5)
    # def login_access(driver):
    email = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys('....')
    time.sleep(5)
    next1 = driver.find_element_by_xpath(
        '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)
    # def login_password(driver):
    password = driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys('.....')
    time.sleep(5)
    next2 = driver.find_element_by_xpath(
        '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)
    driver.switch_to.window(shopee_web)  # 交換控制的網頁


def CloseNotification(driver):
    driver.maximize_window()
    time.sleep(10)
    ActionChains(driver).move_by_offset(950, 106).click(
    ).perform()


def verify_username(driver):
    user_name = driver.find_element_by_class_name('navbar__username')
    print(user_name.text)
    assert '.....' in user_name.text


def CloseBrower(driver):
    driver.quit()


def inputsearchword(driver):
    searchbox = driver.find_element_by_xpath(
        '//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
    searchbox.send_keys('鞋')


def checkSerchWordKey(driver):
    getwordkey = driver.find_elements_by_class_name(
        '//*[@id="shopee-searchbar-listbox"]')
    print(getwordkey.text)
    assert '鞋' in getwordkey.text

# 圖片切換 list位置
# //*[@id="main"]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/ul


# def Get_Article(helpcenter_web):


def test_1st_CheckUsername():
    driver = OpenBrowser()
    time.sleep(10)
    ClickGooglebutton(driver)
    GetloginwindowAndlogin(driver)
    time.sleep(5)
    CloseNotification(driver)
    verify_username(driver)
    CloseBrower(driver)
