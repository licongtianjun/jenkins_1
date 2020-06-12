from WYB_web.INVOICE import Invoice_carrier
from background import Invoice as B_invoice
import unittest,time


class invoice_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        test = Invoice_carrier.invoice()
        self.assertEqual(test,'恭喜您开票成功！','此处判断是否开票成功')

    def test_2(self):
        test = B_invoice.invoice()
        self.assertEqual(test,'状态：开票成功','此处判断后台是否给开票成功')


if __name__ == '__main__':
    unittest.main()


