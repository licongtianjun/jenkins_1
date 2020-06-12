from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest,time

class LiuCheng(unittest.TestCase):
    def setUp(self):
        self.caps = {
            "platformName": "Android",
            "deviceName": "PACM00",
            "appPackage": "zhidanhyb.chengyun",
            "appActivity": ".ui.SplashActivity"
        }
    def test_1(self):
        """
        承运端操作
        """
        driver1 = webdriver.Remote("http://localhost:4725/wd/hub", self.caps)
        driver1.implicitly_wait(10)
        time.sleep(2)
        TouchAction(driver1).press(x=752, y=2016).move_to(x=821, y=1304).release().perform()
        driver1.implicitly_wait(5)
        driver1.find_element_by_accessibility_id('1').click()
        driver1.find_element_by_accessibility_id('2').click()
        driver1.find_element_by_accessibility_id('3').click()
        driver1.find_element_by_accessibility_id('4').click()
        driver1.find_element_by_accessibility_id('5').click()
        driver1.find_element_by_accessibility_id('6').click()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 司机登陆
        time.sleep(8)
        driver1.find_element_by_id('zhidanhyb.chengyun:id/phone_num').send_keys('18686130419')
        driver1.find_element_by_id('zhidanhyb.chengyun:id/verification_code').send_keys('1111')
        driver1.find_element_by_id('zhidanhyb.chengyun:id/normal_login').click()
        time.sleep(10)
        aa = driver1.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                          'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                          'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                          'android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/'
                                          'android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/'
                                          'android.widget.FrameLayout[1]/android.widget.TextView').text
        time.sleep(3)
        self.assertEqual(aa,'普通订单','此处判断司机是否登陆成功')
# --------------------------------------------------------------------------------------------------------------------------------------------
        # 点击立即抢单
        driver1.find_element_by_id('zhidanhyb.chengyun:id/grab_order_btn').click()
        # 点击确定
        driver1.find_element_by_id('zhidanhyb.chengyun:id/bumen_ok').click()
        # 选择车辆
        time.sleep(8)
        driver1.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
            'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/'
            'android.widget.RelativeLayout').click()
        # 点击确认使用
        driver1.find_element_by_id('zhidanhyb.chengyun:id/ok').click()
        time.sleep(3)
        driver1.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
            'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
            'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/'
            'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/'
            'android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/'
            'android.widget.LinearLayout[2]/android.widget.LinearLayout'
        ).click()
        # # 点击完成装货(上传图片步骤)
        time.sleep(3)
        driver1.find_element_by_id('zhidanhyb.chengyun:id/camera').click()
        # 点击完成卸货
        time.sleep(8)
        driver1.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
            'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
            'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/'
            'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/'
            'android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/'
            'android.widget.LinearLayout[2]/android.widget.LinearLayout'
        ).click()
        # 点击完成卸货(上传图片步骤)
        driver1.find_element_by_id('zhidanhyb.chengyun:id/camera').click()
        time.sleep(5)
        msg_1 = driver1.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.TextView').text
        self.assertEqual(msg_1, '待收货', '此处判断是司机否运输完成')
        # 点击返回
        driver1.find_element_by_id('zhidanhyb.chengyun:id/left_img').click()
        # 司机退出登陆
        time.sleep(10)
        driver1.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                      'android.widget.FrameLayout/android.widget.FrameLayout/'
                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                      'android.widget.LinearLayout/android.view.ViewGroup/'
                                      'android.view.ViewGroup/android.widget.FrameLayout[4]/'
                                      'android.widget.FrameLayout/android.widget.RelativeLayout/'
                                      'android.widget.ImageView').click()
        driver1.find_element_by_id('zhidanhyb.chengyun:id/l7').click()
        # 滑动页面
        time.sleep(5)
        TouchAction(driver1).press(x=360, y=1529).move_to(x=367, y=894).release().perform()
        # 点击退出
        driver1.find_element_by_id('zhidanhyb.chengyun:id/setting_exit').click()
        time.sleep(3)
        aa = driver1.find_element_by_id('zhidanhyb.chengyun:id/login_sj').text
        self.assertEqual(aa, '司机登录', '此处判断司机是否已经退出')
        time.sleep(2)
        driver1.close_app()


if __name__ == '__main__':
    unittest.main()
