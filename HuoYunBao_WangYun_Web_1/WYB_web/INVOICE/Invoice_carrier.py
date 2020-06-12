from selenium import webdriver
import time
def invoice():
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
    # 点击开票管理
    time.sleep(3)
    ele = driver.find_element_by_xpath('//li[@class="el-submenu"][3]//span[@slot="title"]')
    ele.click()
    # 点击开票记录
    time.sleep(3)
    ele = driver.find_element_by_xpath('//li[@class="el-submenu is-opened"]//li[@class="el-menu-item"]')
    ele.click()
    # 点击添加
    time.sleep(3)
    ele = driver.find_element_by_xpath("//i[@class='el-icon-circle-plus-outline']")
    ele.click()
    # 选择普通承运人订单
    time.sleep(3)
    ele = driver.find_element_by_xpath('//div[@class="el-dialog__wrapper"]//span[@class="el-checkbox__inner"]')
    ele.click()
    # 点击确认按钮
    time.sleep(3)
    ele = driver.find_element_by_xpath('//button[@class="el-button green-shadow el-button--success el-button--small"]')
    ele.click()
    # 选择订单
    time.sleep(3)
    ele = driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//span[@class="el-checkbox__inner"]')
    ele.click()
    # 页面滑动
    time.sleep(3)
    driver.execute_script('arguments[0].scrollIntoView();', ele)
    # 点击下一步
    time.sleep(3)
    ele = driver.find_element_by_xpath('//button[@class="el-button btn el-button--danger el-button--small"]/span')
    ele.click()
    # 点击历史抬头
    time.sleep(3)
    ele = driver.find_element_by_xpath('//button[@class="el-button taitou el-button--text el-button--small"]/span')
    ele.click()
    # 选择抬头信息
    time.sleep(3)
    ele = driver.find_element_by_xpath('//form[@class="el-form"]//span[@class="el-radio__inner"]')
    ele.click()
    # 点击确定
    time.sleep(3)
    ele = driver.find_element_by_xpath('//button[@class="el-button green-shadow el-button--success el-button--small"]')
    ele.click()
    # 点击下一步
    time.sleep(3)
    ele = driver.find_element_by_xpath('//button[@class="el-button btn el-button--danger el-button--small"]/span')
    ele.click()
    time.sleep(3)
    ele = driver.find_element_by_xpath('//div[@class="suc_txt el-col el-col-24"]')
    test = ele.text
    driver.quit()
    return test


if __name__ == '__main__':
    print(invoice())


















