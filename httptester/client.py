# -*- coding:utf-8 -*-
from httpcore import HttpCore
from response import Response
from testcase import import_json_file
from validata import chick_validata

testcass = "test_cass.json"
testcass = import_json_file(testcass)
# print(testcass)
request = testcass.get("request")
validata = testcass.get("validata")
response = HttpCore(request).run()
validatas = Response(response,validata).get_response_args()
chick_validata(validatas)