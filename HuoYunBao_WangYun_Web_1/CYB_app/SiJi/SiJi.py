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

# 司机登陆
def sj_DL():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    driver.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130419')
    driver.find_element_by_id('zhidanhyb.chengyun:id/verification_code').send_keys('1111')
    driver.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
    time.sleep(10)
    aa = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                   'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                   'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                   'android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/'
                                   'android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/'
                                   'android.widget.FrameLayout[1]/android.widget.TextView').text
    time.sleep(3)
    driver.close_app()
    return aa

# 司机接单
def sj_JD():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    driver.implicitly_wait(10)
    # 点击承运人订单
    driver.find_element_by_id('zhidanhyb.chengyun:id/main_rb_supei').click()
    # 点击立即抢单
    driver.find_element_by_id('zhidanhyb.chengyun:id/grab_order_btn').click()
    # 点击确定
    driver.find_element_by_id('zhidanhyb.chengyun:id/bumen_ok').click()
    # 选择车辆
    time.sleep(5)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
        'android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/'
        'android.widget.RelativeLayout').click()
    # 点击确认使用
    driver.find_element_by_id('zhidanhyb.chengyun:id/ok').click()
    # msg = driver.find_element_by_id('zhidanhyb.chengyun:id/center_txt').text
    time.sleep(3)
    driver.close_app()
    # return msg

def SJ_zhuanghuo():
    driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
    time.sleep(10)
    driver.implicitly_wait(10)
    # 点击我的订单
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    # 选择订单
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/ll').click()
    # 点击完成装货
    time.sleep(3)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/'
        'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/'
        'android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/'
        'android.widget.LinearLayout[2]/android.widget.LinearLayout'
    ).click()
    # # 点击完成装货(上传图片步骤)
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/camera').click()
    # 点击完成卸货
    time.sleep(7)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/'
        'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/'
        'android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/'
        'android.widget.LinearLayout[2]/android.widget.LinearLayout'
    ).click()
    # 点击完成卸货(上传图片步骤)
    driver.find_element_by_id('zhidanhyb.chengyun:id/camera').click()
    time.sleep(6)
    msg_1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                      'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                      'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                      'android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.TextView').text
    time.sleep(8)
    driver.close_app()
    return msg_1

def sj_TuiChu():
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
    time.sleep(10)
    aa = driver.find_element_by_id('zhidanhyb.chengyun:id/login_sj').text
    time.sleep(3)
    driver.close_app()
    return aa

if __name__ == '__main__':
    print(sj_DL())


