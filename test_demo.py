# -*- coding:utf-8 -*-
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
        self.assertEqual(1,1)
    
    def test_02(self):
        self.assertEqual(1,2)


if __name__ == '__main__':
    tests = [TestDemo("test_01"),TestDemo("test_02")]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    # with open('report.txt','w') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)
    with open('report.html','wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title="测试报告", description="执行人：浪晋")
        runner.run(suite)

