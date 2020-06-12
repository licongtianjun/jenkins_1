from appium import webdriver
import time
caps={
        "platformName": "Android",
        "deviceName": "PACM00",
        "appPackage": "zhidanhyb.chengyun",
        "appActivity": ".ui.SplashActivity"
    }

def CYR_income_ShouYi_1():
    driver = webdriver.Remote("http://localhost:4725/wd/hub",caps)
    driver.implicitly_wait(10)
    time.sleep(8)
    driver.find_element_by_id('zhidanhyb.chengyun:id/login_hz').click()
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130412')
    driver.find_element_by_id('zhidanhyb.chengyun:id/verification_code').send_keys('1111')
    driver.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
    time.sleep(8)
    # 点击我的
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                 'android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/'
                                 'android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/'
                                 'android.widget.RelativeLayout/android.widget.ImageView').click()
    # 获取收益
    shouyi = driver.find_element_by_id('zhidanhyb.chengyun:id/ljsy').text
    shouyi = float(shouyi.strip('￥'))
    # 获取我的钱包余额
    time.sleep(3)
    driver.find_element_by_id('zhidanhyb.chengyun:id/me_account_ll').click()
    time.sleep(3)
    yue = float(driver.find_element_by_id('zhidanhyb.chengyun:id/wallet_money_all').text)
    print(float(shouyi),float(yue))

    return shouyi,yue