def add(a,b):
    return a+b

# if add(1,1) == 3:
#     print("测试通过")
# else:
#     print("测试失败")

import unittest
import HTMLTestRunner
import requests
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("开始测试。。。")
    @classmethod
    def tearDownClass(cls):
        print("结束测试...")

    def test_01_true(self):
        self.assertEqual(add(1,1),2,"成功的用例")

    def test_02_false(self):
        self.assertEqual(add(1,1),3,"失败的用例")
        
    def test_03_login(self):
        url = "http://127.0.0.1:5000/login"
        payload = {"userneme":"admin","password":"123456"}
        headers = {
            'Content-Type': "application/json"
            }
        response = requests.request("POST", url, json=payload, headers=headers)
        hdata = response.json()
        code = hdata["code"]
        self.assertEqual(code,200,"测试登陆接口")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    tests = [TestAdd("test_01_true"),TestAdd("test_02_false"),TestAdd("test_03_login")]
    suite.addTests(tests)
    with open("测试报告.html","wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2)
        runner.run(suite)