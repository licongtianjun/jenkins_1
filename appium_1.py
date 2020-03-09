from appium import webdriver
import time
import unittest
from appium.webdriver.common.touch_action import TouchAction

class Ceshi(unittest.TestCase):
    def setUp(self):
        self.caps ={
          "platformName": "Android",
          "deviceName": "sagit",
          "appPackage": "com.alibaba.android.rimet",
          "appActivity": ".biz.SplashActivity"
        }
    def test_1(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub",self.caps)
        TouchAction(driver).press(x=555, y=1846).move_to(x=588, y=876).release().perform()
        driver.implicitly_wait(20)
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("com.alibaba.android.rimet:id/login_slide_btn").click()
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").clear()
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18510860419")
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("licong12023")
        driver.find_element_by_id('com.alibaba.android.rimet:id/btn_next').click()
        time.sleep(7)
        TouchAction(driver).tap(x=960, y=1832).perform()
        aa = driver.find_element_by_id('android:id/message').text
        self.assertEqual(aa,'号码或密码错误，请重新输入','账号密码不对时,测试没通过')
    def test_2(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        driver.implicitly_wait(20)
        TouchAction(driver).press(x=555, y=1846).move_to(x=588, y=876).release().perform()
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("com.alibaba.android.rimet:id/login_slide_btn").click()
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").clear()
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18510860419")
        driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("licong1202")
        driver.find_element_by_id('com.alibaba.android.rimet:id/btn_next').click()
        time.sleep(7)
        TouchAction(driver).tap(x=960, y=1832).perform()
        aa = driver.find_element_by_id('com.alibaba.android.rimet:id/menu_current_company').text
        self.assertNotEqual(aa, '号码或密码错误，请重新输入', '账号密码一致时,测试没通过')

if __name__ == '__main__':
    unittest.main()
