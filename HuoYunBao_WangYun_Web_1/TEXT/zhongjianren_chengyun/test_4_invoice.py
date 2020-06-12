from WYB_web.INVOICE import Invoice_carrier
import unittest,time

class invoice_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        test = Invoice_carrier.invoice()
        self.assertEqual(test,'恭喜您开票成功！','此处判断是否开票成功')

if __name__ == '__main__':
    unittest.main()


