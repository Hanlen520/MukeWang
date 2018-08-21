# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import requests
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_01_post(self):
        url = "http://127.0.0.1:5000/login"
        payload = {"username":"admin","password":"123456"}
        headers = {
            'Content-Type': "application/json"
            }
        response = requests.request("POST", url, json=payload, headers=headers)
        data = response.json()
        code = data['code']
        self.assertEqual(code,200)
    

    def test_02_get(self):
        url = "http://127.0.0.1:5000/getinfo"
        response = requests.request("GET", url)
        data = response.json()
        code = data["code"]
        self.assertEqual(code, 201)


if __name__ == '__main__':
    tests = [TestDemo("test_01_post"),TestDemo("test_02_get")]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    # with open('report.txt','w') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)
    with open('report.html','wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title="测试报告", description="执行人：浪晋")
        runner.run(suite)

