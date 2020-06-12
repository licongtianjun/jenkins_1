from selenium import webdriver
import time

def Payment():
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
    # 点击支付管理
    time.sleep(8)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/li[5]/div/div/span').click()
    # 点击申请支付
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/li[5]/ul/li[1]').click()
    # 选择订单勾选
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="el-table__fixed-body-wrapper"]//span[@class="el-checkbox__inner"]').click()
    # 点击申请支付
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="el-button el-button--success el-button--small"]').click()
    # 勾选回付运费
    time.sleep(2)
    driver.find_element_by_xpath('//span[@class="el-checkbox__input"]').click()
    # 点击确定
    while True:
        aa = driver.find_element_by_xpath('//*[@id="/payManage/applypayList"]/div/div[3]/div/div[3]/div/button[2]/span')
        if aa.text == '确定':
            aa.click()
            break
    # 点击运费支付
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/li[5]/ul/li[2]').click()
    # 勾选订单
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="el-table__fixed-body-wrapper"]//span[@class="el-checkbox__input"]').click()
    # 点击确认
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="el-button el-button--success el-button--small"]').click()
    # 输入密码
    time.sleep(2)
    driver.find_element_by_xpath(
        '//div[@style="opacity: 0; z-index: 9; margin-top: 10px; width: 240px; padding: 0px; height: 50px;"]'
        '//input[@type="password"]').send_keys('123456')
    driver.find_element_by_xpath('//button[@class="el-button green-shadow el-button--success el-button--small"]/span').click()
    time.sleep(3)
    driver.quit()

