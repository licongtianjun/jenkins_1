from selenium import webdriver
import time

def invoice():
    path = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = 'http://47.99.108.104:1002/'

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    name = driver.find_element_by_xpath('//input[@placeholder="请填写用户名"]')
    name.send_keys('18510860419')
    password = driver.find_element_by_xpath('//input[@placeholder="请填写登录密码"]')
    password.send_keys('123456aa')
    affirm = driver.find_element_by_class_name('loginBtn')
    affirm.click()

    # 点击开票管理
    time.sleep(2)
    ele = driver.find_element_by_xpath('//li[@class="el-submenu"][2]')
    ele.click()
    # 点击开票列表
    time.sleep(2)
    ele = driver.find_element_by_xpath('//li[@class="el-submenu is-opened"]//li')
    ele.click()
    # 判断提交公司,如果一致,就开票
    time.sleep(2)
    ele = driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-left"]//td[@class="el-table_1_column_3 is-center "]/div')
    if ele.text == '天津安果科技有限公司':
        # 点击详情
        # details = driver.find_element_by_xpath('//button[@class="el-button pop-btn el-button--success el-button--mini"]/span')
        details = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/button[1]/span')
        details.click()
        # 判断第二行
    else:
        ele = driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-left"]//tr[2]//td[@class="el-table_1_column_3 is-center "]/div')
        if ele.text == '天津安果科技有限公司' :
            details = driver.find_element_by_xpath('//table[@class="el-table__body"]//tr[2]//button[@class="el-button pop-btn el-button--success el-button--mini"]')
            details.click()
        else:
            aa = '没找到发票'
            return aa
    # 点击开票成功
    time.sleep(2)
    ele = driver.find_element_by_xpath('//button[@class="el-button green-shadow detail-btn el-button--success el-button--small"]')
    ele.click()
    # 填写发票号码
    time.sleep(2)
    ele = driver.find_element_by_xpath('//div[@class="el-form-item__content"]//input[@class="el-input__inner"]')
    ele.send_keys(str(time.time())[0:10])
    # 点击确定
    time.sleep(2)
    ele = driver.find_element_by_xpath('//div[@aria-label="开票"]//div[@class="el-dialog__footer"]/span/button')
    ele.click()
    # 确认状态
    time.sleep(2)
    ele = driver.find_element_by_xpath('//div[@class="layout-cell el-col el-col-6"][2]')
    aa = ele.text
    return aa


if __name__ == "__main__":
    invoice()
