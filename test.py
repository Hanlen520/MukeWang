# -*- conding:utf-8 -*-
import unittest
import HTMLTestRunner

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_01(self):
        a = 1
        b = 1
        self.assertEqual(a+b,2)

    def test_02(self):
        a = 1
        b = 2
        self.assertEqual(a-b,-1)

    def test_03(self):
        a = 1
        b = 6
        self.assertEqual(a*b,5)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestDemo("test_01"),TestDemo("test_02"),TestDemo("test_03")]
    suite.addTests(tests)
    with open("测试报告.html","wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2)
        runner.run(suite)
