from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
import requests
import json
import allure


url = "https://shopee.tw/m/topshop"
url_requests = 'https://shopee.tw/api/v4/search/trending_search?bundle=popsearch&offset=0'


@allure.step("開啟網頁")
def open_browser():
    driver = uc.Chrome(use_subprocess=True)
    driver.get(url)
    driver.maximize_window()
    return driver


@allure.step("開啟網頁_request")
def open_browser_requests():
    payload = {}
    driver_requests = requests.get(
        url_requests, verify=False)
    return driver_requests


@allure.step("選擇google方式登入")
def click_google_button(driver):
    login = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/header/div[1]/nav/ul/a[3]')))
    login.click()
#    time.sleep(10)
    user_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                              '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[2]')))
    user_button.click()


@ allure.step("輸入帳密")
def login(driver):
    shopee_web = driver.current_window_handle
    time.sleep(5)
    for handle in driver.window_handles:  # 處理2個windoows
        if handle != shopee_web:
            login_page = handle
    driver.switch_to.window(login_page)
    email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    email.send_keys('your mail')
    mail_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '//*[@id="identifierNext"]/div/button/span'))).click()
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                 '//*[@id="password"]/div[1]/div/div[1]/input')))
    password.send_keys('your password')

    password_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '//*[@id="passwordNext"]/div/button/span'))).click()
    time.sleep(5)
    driver.switch_to.window(shopee_web)  # 交換控制的網頁


@ allure.step("關閉特惠通知")
def close_notification(driver):
    driver.maximize_window()
    time.sleep(10)
    ActionChains(driver).move_by_offset(950, 106).click(
    ).perform()


@ allure.step("驗證使用者")
def verify_username(driver):
    user_name = driver.find_element(By.CLASS_NAME, 'navbar__username')
    assert 'your name' in user_name.text


@ allure.step("關閉網頁")
def close_browser(driver):
    driver.quit()


@ allure.step("輸入搜尋字")
def input_searchword(driver):
    searchbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/header/div[2]/div/div[1]/div[1]/div/form/input')))
    searchbox.send_keys('鞋')


@ allure.step("切換搜尋範圍")
def switch_searchbox(driver):
    switchbutton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     '//*[@id="pc-drawer-id-1"]/div/div')))
    ActionChains(driver).move_to_element(switchbutton).perform()
    switchitem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            ' //*[@id="pc-drawer-id-1"]/div/div/div[2]/div')))

    switchitem.click()


@ allure.step("確認搜尋關鍵字")
def check_search_wordkey(driver):
    get_word_key1 = driver.find_elements(By.XPATH,
                                         '//*[@id="shopee-searchbar-listbox"]/*/div/span[1]')
    get_word_key2 = driver.find_elements(By.XPATH,
                                         '//*[@id="shopee-searchbar-listbox"]/*/div/span[2]')
    for i in nums(0, 8):
        search_word = get_word_key1[i].text+get_word_key2[i].text
        assert '鞋' in search_word
    print('PASS')


def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)


@ allure.step("取得熱門關鍵字(selenium)")
def get_hot_searchword_selenium(driver):
    user_name = driver.find_elements(By.CLASS_NAME, 'UPUwyq')
    for i in nums(0, 7):
        selenium_data = user_name[i].text
        return selenium_data


@ allure.step("取得熱門關鍵字(requests)")
def get_hot_searchword_request(driver_requests):
    # obj = json.loads(respones.text) #其一方式
    obj = driver_requests.json()  # 其二方式 (建議)
    dric = (obj['data'])
    for i in nums(0, 7):
        request_data = dric['querys'][i]['text']
        return request_data


@ allure.step("比對熱門關鍵字")
def compare_hot_searchword_date(request_data, selenium_data):
    assert selenium_data in request_data


@ allure.step("取得imglink的json資料")
def get_imglink_json(driver):
    with open('image_link.json') as image_link:
        data = json.load(image_link)
    for i in range(11):
        link_json = data[i]['link']
        image_scr_json = data[i]['img src']
        return link_json, image_scr_json


@ allure.step("抓取網頁imglink資料")
def get_imglink(driver):
    picture_link = driver.find_elements(
        By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[5]/div/div/div/div[3]/div/ul/li[*]/div/a')
    picture_image = driver.find_elements(
        By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[5]/div/div/div/div[3]/div/ul/li[*]/div/a/picture/img')
    for i in range(11):
        link = picture_link[i].get_attribute('href')
        image_src = picture_image[i].get_attribute('src')
        return link, image_src


@ allure.step("比對imglink資料")
def compare_imglink(link_json, image_scr_json, link, image_src):
    for i in range(11):
        assert link_json == link and image_scr_json == image_src
        print('image&link' + str(i) + ' PASS')


def test_1_check_username():
    driver = open_browser()
    click_google_button(driver)
    login(driver)
    close_notification(driver)
    verify_username(driver)
    close_browser(driver)


def test_2_check_searchword():
    driver = open_browser()
    input_searchword(driver)
    switch_searchbox(driver)
    check_search_wordkey(driver)
    close_browser(driver)


def test_3_compare_hotsearchword():
    driver = open_browser()
    selenium_data = get_hot_searchword_selenium(driver)
    driver_requests = open_browser_requests()
    request_data = get_hot_searchword_request(driver_requests)
    compare_hot_searchword_date(request_data, selenium_data)
    close_browser(driver)


def test_4_compare_imglink():
    driver = open_browser()
    (link_json, image_scr_json) = get_imglink_json(driver)
    (link, image_src) = get_imglink(driver)
    compare_imglink(link_json, image_scr_json, link, image_src)
    close_browser(driver)
