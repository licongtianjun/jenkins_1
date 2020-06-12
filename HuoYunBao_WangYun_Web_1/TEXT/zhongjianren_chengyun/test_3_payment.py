from WYB_web import my_wallet,payment,QRshouhuo
from CYB_app.ChengYunRen.CYR_intermediary import CYR_income
import unittest,time

class LiuCheng(unittest.TestCase):
    def setUp(self):
        pass

    # def test_1(self):
    #     QRshouhuo.qrshouhuo()

    def test_2(self):
        time.sleep(5)
        # 获取支付前承运人的金额
        SJ_shouyi_1,SJ_yue_1 = CYR_income.CYR_income_ShouYi_1()
        self.assertEqual(SJ_shouyi_1, SJ_yue_1, '此处判断余额与收益是否一致,为test_9收集数据')
        # 网运版支付
        yue_1 = float(my_wallet.wallet())
        payment.Payment()
        yue_2 = float(my_wallet.wallet())
        yue_3 = round(yue_1 - yue_2, 2)
        yue_4 = round(250 / (1 - 0.09), 2)
        print(yue_4)
        self.assertEqual(yue_3, yue_4, '此处判断网运版支付完后余额是否准确')
        # 获取企业支付后司机的金额
        SJ_shouyi_2, SJ_yue_2 = CYR_income.CYR_income_ShouYi_1()
        # 获取司机端差额
        SJ_shouyi_3 = float(SJ_shouyi_2) - float(SJ_shouyi_1)
        SJ_yue_3 = float(SJ_yue_2) - float(SJ_yue_1)
        self.assertEqual(SJ_shouyi_3, 250, '此处判断企业支付金额是否到账累计收益')
        self.assertEqual(SJ_yue_3, 250, '此处判断企业支付金额是否到账我的钱包')
        # 退出


if __name__ == '__main__':
    unittest.main()
