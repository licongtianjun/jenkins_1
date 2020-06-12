from selenium import webdriver
import time
def qrshouhuo():
    # path = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=path)
    driver = webdriver.Chrome()

    # option = webdriver.ChromeOptions()
    # option.add_argument('disable-infobars')
    # driver = webdriver.Chrome(chrome_options=option, desired_capabilities=None)
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
    # 点击订单管理
    time.sleep(5)
    ele_ddgl = driver.find_element_by_xpath('//li[@class="el-submenu"][2]/div[@class="el-submenu__title"]')
    ele_ddgl.click()
    # 点击我的订单
    ele_wddd = driver.find_element_by_xpath('//li[@class="el-submenu is-opened"]//li[@class="el-menu-item"]')
    # ele_wddd = driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]')
    ele_wddd.click()

    # 点击确认收货
    time.sleep(5)
    # ele_qrsh = driver.find_element_by_xpath('//button[@class="el-button inlineBtn el-button--default el-button--mini"]/span')
    ele_qrsh = driver.find_element_by_xpath('//*[@id="pane-doing"]/div[2]/div/div[5]/div[2]/table/tbody/tr/td[16]/div/button[2]/span')
    ele_qrsh.click()
    time.sleep(2)
    ele_qr = driver.find_element_by_xpath('//button[@class="el-button el-button--default el-button--small el-button--primary "]/span')
    ele_qr.click()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    qrshouhuo()
