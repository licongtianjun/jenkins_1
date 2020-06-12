import unittest
from WYB_web.FaHuo import FaHuoGuanLi


class FaHuo(unittest.TestCase):

    def setUp(self):
        pass
    def test_1(self):
        self.aa = FaHuoGuanLi.fahuo_intermediary_DesignatedDriver()

        self.assertEqual(self.aa,'发货成功','此处判断是否发货成功')
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
