from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
caps={
        "platformName": "Android",
        "deviceName": "PACM00",
        "appPackage": "zhidanhyb.chengyun",
        "appActivity": ".ui.SplashActivity"
    }
def KaiQi():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    time.sleep(2)
    TouchAction(driver).press(x=752, y=2016).move_to(x=821, y=1304).release().perform()
    driver.implicitly_wait(5)
    driver.find_element_by_accessibility_id('1').click()
    driver.find_element_by_accessibility_id('2').click()
    driver.find_element_by_accessibility_id('3').click()
    driver.find_element_by_accessibility_id('4').click()
    driver.find_element_by_accessibility_id('5').click()
    driver.find_element_by_accessibility_id('6').click()
    driver.close_app()

# 承运人登陆
def CYR_DL():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    time.sleep(2)
    # 登陆
    driver.find_element_by_id('zhidanhyb.chengyun:id/login_hz').click()
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/tv_code_login').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130419')
    driver.find_element_by_id('zhidanhyb.chengyun:id/et_pwd_login').send_keys('licong1202')
    driver.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
    time.sleep(5)
    driver.close_app()

# 承运人接单
def CYR_jiedan():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    time.sleep(2)
    TouchAction(driver).press(x=752, y=2016).move_to(x=821, y=1304).release().perform()
    driver.implicitly_wait(5)
    driver.find_element_by_accessibility_id('1').click()
    driver.find_element_by_accessibility_id('2').click()
    driver.find_element_by_accessibility_id('3').click()
    driver.find_element_by_accessibility_id('4').click()
    driver.find_element_by_accessibility_id('5').click()
    driver.find_element_by_accessibility_id('6').click()
    # 登陆
    time.sleep(8)
    driver.find_element_by_id('zhidanhyb.chengyun:id/login_hz').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/tv_code_login').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130419')
    driver.find_element_by_id('zhidanhyb.chengyun:id/et_pwd_login').send_keys('licong1202')
    driver.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
    # 点击抢单
    driver.find_element_by_id('zhidanhyb.chengyun:id/grab_order_btn').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/bumen_ok').click()
    # driver.find_element_by_id('zhidanhyb.chengyun:id/order_detail_call').click()
    driver.close_app()

# 承运人分配司机
def CYR_fenpei():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    time.sleep(10)
    # 点击我的订单
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    time.sleep(2)
    # 选择订单
    driver.find_element_by_id('zhidanhyb.chengyun:id/ll').click()
    time.sleep(2)
    # 点击分配司机
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/'
                                 'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/'
                                 'android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/'
                                 'android.widget.LinearLayout[2]/android.widget.LinearLayout').click()
    # 选择司机
    time.sleep(2)
    driver.find_element_by_id('zhidanhyb.chengyun:id/main_ll').click()
    time.sleep(2)
    msg = driver.find_element_by_id('zhidanhyb.chengyun:id/center_txt').text
    # try:
    #     msg = driver.find_element_by_id('zhidanhyb.chengyun:id/center_txt').text
    # except:
    #     msg = False
    driver.close_app()
    return msg

# 承运人退出
def CYR_TCdenglu():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
        'android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.ImageView').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/l7').click()
    # 滑动页面
    time.sleep(5)
    TouchAction(driver).press(x=360, y=1529).move_to(x=367, y=894).release().perform()
    # 点击退出
    driver.find_element_by_id('zhidanhyb.chengyun:id/setting_exit').click()
    time.sleep(3)
    aa = driver.find_element_by_id('zhidanhyb.chengyun:id/login_sj').text
    time.sleep(3)
    driver.close_app()
    return aa

def CYR_ShouYi():
    driver = webdriver.Remote("http://localhost:4725/wd/hub",caps)
    driver.implicitly_wait(10)
    time.sleep(8)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    shouyi = driver.find_element_by_id('zhidanhyb.chengyun:id/ljsy').text
    shouyi = shouyi.strip('￥')
    # 获取我的钱包余额
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/me_account_ll').click()
    time.sleep(3)
    yue=driver.find_element_by_id('zhidanhyb.chengyun:id/wallet_money_all').text
    print(float(shouyi),float(yue))
    # 点击返回
    driver.find_element_by_id('zhidanhyb.chengyun:id/left_img').click()
    # 承运人退出登陆
    time.sleep(8)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
        'android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/'
        'android.widget.RelativeLayout/android.widget.ImageView').click()
    time.sleep(2)
    driver.find_element_by_id('zhidanhyb.chengyun:id/l7').click()
    # 滑动页面
    time.sleep(8)
    TouchAction(driver).press(x=360, y=1529).move_to(x=367, y=894).release().perform()
    time.sleep(2)
    driver.find_element_by_id('zhidanhyb.chengyun:id/setting_exit').click()
    time.sleep(2)
    driver.close_app()
    return float(shouyi),float(yue)

def CYR_ShouYi_1():
    time.sleep(3)
    driver = webdriver.Remote("http://localhost:4725/wd/hub",caps)
    driver.implicitly_wait(10)
    time.sleep(8)
    driver.find_element_by_id('zhidanhyb.chengyun:id/login_hz').click()
    time.sleep(8)
    driver.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130419')
    driver.find_element_by_id('zhidanhyb.chengyun:id/verification_code').send_keys('1111')
    driver.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
    time.sleep(8)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    shouyi = driver.find_element_by_id('zhidanhyb.chengyun:id/ljsy').text
    shouyi = shouyi.strip('￥')
    # 获取我的钱包余额
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/me_account_ll').click()
    time.sleep(3)
    yue=driver.find_element_by_id('zhidanhyb.chengyun:id/wallet_money_all').text
    print(float(shouyi),float(yue))
    time.sleep(3)
    driver.close_app()
    return float(shouyi),float(yue)

def CYR_DDzhuangtai():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    time.sleep(8)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    driver.find_element_by_id('zhidanhyb.chengyun:id/ll').click()
    msg = driver.find_element_by_id('zhidanhyb.chengyun:id/center_txt').text

    return msg

if __name__ == '__main__':
    print(CYR_ShouYi_1())













