from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def fahuo_qiyeCYR():
    path = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = 'http://47.99.108.104:1003/'
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/input').send_keys('18510860419')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/input').send_keys('licong1202')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/button').click()
    time.sleep(5)
    # 点击发货管理
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[1]/ul/li[2]/div/div').click()
    # 点击发货管理
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[1]/ul/li[2]/ul/li[1]').click()
    # 输入流水号
    time.sleep(2)
    # driver.find_element_by_xpath(
    #     '//*[@id="/useCar"]/div/div[1]/form/div[1]/div/div[1]/div/div/div[1]/input').send_keys(str(time.time())[0:10])
    # 选择发货日期
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').send_keys(Keys.ENTER)

    # 选择发货时间
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[3]/div/div/input').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]').click()
    # 输入发货地
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys('万达B')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.DOWN)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[2]/div/button/i').click()
    # 输入收货地址
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[1]/div/div/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys('青坨小学')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[2]/div/button/span').click()
    # 输入收货人姓名电话
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[3]/div/div/div[1]/input').send_keys('李聪')
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[4]/div/div/div[1]/input').send_keys('18510860419')
    # 输入货物名称
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[1]/div/div/div[1]/input').send_keys('食物')
    # 选择货物类型
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').click()
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').send_keys(Keys.ENTER)
    # 输入货物重量
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[3]/div/div/div[1]/input').send_keys('10')

    # 选择业务类型
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').send_keys(Keys.ENTER)
    # 滑动到指定坐标
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[1]/div/label')
    driver.execute_script('arguments[0].scrollIntoView();', e)
    # 选择承运方式
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[4]/div[2]/div/div/label[2]/span[1]/span').click()
    # 选择承运人
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[5]/div[2]/div/button/span').click()
    time.sleep(5)
    # 弹框处选择承运人
    ele_chengyunren=driver.find_element_by_xpath('//input[@placeholder="请选择承运人，可搜索关键字"]')
    ele_chengyunren.click()
    ele_chengyunren.send_keys(Keys.DOWN)
    ele_chengyunren.send_keys(Keys.ENTER)
    ele_chengyunqueren=driver.find_element_by_xpath(
        '//div[@aria-label="选择承运人"]//button[@class="el-button green-shadow el-button--success el-button--small"]')
    ele_chengyunqueren.click()
    # 填写运费
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[1]/div/div/div[1]/input').send_keys(0)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[2]/div/div/div[1]/input').send_keys(0)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[3]/div/div/div[1]/input').send_keys(250)
    # 点击下单
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[8]/div/div[2]/button/span').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[8]/div/div[2]/button/span').click()
    time.sleep(3)
    ele=driver.find_element_by_xpath('//div[@class="el-message-box__btns"]//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    ele.click()
    time.sleep(5)
    title_new = driver.title
    driver.quit()
    return title_new

def fahuo_intermediary_DesignatedDriver():
    path = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = 'http://47.99.108.104:1003/'
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/input').send_keys('18510860419')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/input').send_keys('licong1202')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/button').click()
    time.sleep(5)
    # 点击发货管理
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[1]/ul/li[2]/div/div').click()
    # 点击发货管理
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[1]/ul/li[2]/ul/li[1]').click()
    # 输入流水号
    time.sleep(2)
    # driver.find_element_by_xpath(
    #     '//*[@id="/useCar"]/div/div[1]/form/div[1]/div/div[1]/div/div/div[1]/input').send_keys(str(time.time())[0:10])
    # 选择发货日期
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div/input').send_keys(Keys.ENTER)

    # 选择发货时间
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[2]/div/div[3]/div/div/input').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]').click()
    # 输入发货地
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys('万达B')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.DOWN)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[2]/div/button/i').click()
    # 输入收货地址
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[1]/div/div/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys('青坨小学')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[3]/div/div[2]/form/div[2]/div/button/span').click()
    # 输入收货人姓名电话
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[3]/div/div/div[1]/input').send_keys('李聪')
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[2]/div[4]/div[4]/div/div/div[1]/input').send_keys('18510860419')
    # 输入货物名称
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[1]/div/div/div[1]/input').send_keys('食物')
    # 选择货物类型
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').click()
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[2]/div/div/div/div/input').send_keys(Keys.ENTER)
    # 输入货物重量
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[3]/div/div/div[1]/input').send_keys('10')

    # 选择业务类型
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[4]/div/div/div/div/input').send_keys(Keys.ENTER)
    # 滑动到指定坐标
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="/useCar"]/div/div[1]/form/div[3]/div[2]/div[1]/div/label')
    driver.execute_script('arguments[0].scrollIntoView();', e)
    # 选择承运方式
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[4]/div[2]/div/div/label[2]/span[1]/span').click()
    # 选择承运人
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[5]/div[2]/div/button/span').click()
    time.sleep(5)
    # 弹框处选择承运人
    ele_chengyunren=driver.find_element_by_xpath('//input[@placeholder="请选择承运人，可搜索关键字"]')
    ele_chengyunren.send_keys('田军(委托人)')
    ele_chengyunren.send_keys(Keys.DOWN)
    ele_chengyunren.send_keys(Keys.ENTER)
    ele_chengyunqueren=driver.find_element_by_xpath(
        '//div[@aria-label="选择承运人"]//button[@class="el-button green-shadow el-button--success el-button--small"]')
    ele_chengyunqueren.click()
    # 选择司机
    time.sleep(3)
    ele_driver = driver.find_element_by_xpath('//div[@class="cell"]//span[@class="el-radio__inner"]')
    ele_driver.click()
    ele_affirm = driver.find_element_by_xpath(
        '//div[@class="el-dialog__wrapper"][4]//button[@class="el-button green-shadow el-button--success el-button--small"]/span')
    ele_affirm.click()
    # 填写运费
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[1]/div/div/div[1]/input').send_keys(0)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[2]/div/div/div[1]/input').send_keys(0)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[6]/div[2]/div[3]/div/div/div[1]/input').send_keys(250)
    # 点击下单
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[8]/div/div[2]/button/span').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '//*[@id="/useCar"]/div/div[1]/form/div[8]/div/div[2]/button/span').click()
    time.sleep(3)
    ele=driver.find_element_by_xpath('//div[@class="el-message-box__btns"]//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    ele.click()
    time.sleep(5)
    title_new = driver.title
    time.sleep(2)
    driver.quit()
    return title_new

if __name__ == '__main__':
    print(fahuo_qiyeCYR())








