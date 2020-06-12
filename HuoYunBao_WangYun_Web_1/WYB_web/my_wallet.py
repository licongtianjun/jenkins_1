from selenium import webdriver
import time

def wallet():
    # option = webdriver.ChromeOptions()
    # option.add_argument('disable-infobars')
    path = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = 'http://47.99.108.104:1003/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/input').send_keys('18510860419')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/input').send_keys('licong1202')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/button').click()
    # 点击企业设置
    time.sleep(5)
    ele_shezhi = driver.find_element_by_xpath('//li[@class="el-submenu"][6]')
    ele_shezhi.click()
    # 点击企业钱包
    time.sleep(3)
    ele_qianbao = driver.find_element_by_xpath('//li[@class="el-submenu is-opened"]//li[@class="el-menu-item"][3]')
    ele_qianbao.click()
    time.sleep(3)
    # 企业余额
    balance = driver.find_element_by_xpath('//div[@class="text"]/span').text
    driver.quit()
    return balance
