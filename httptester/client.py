# -*- coding:utf-8 -*-
from httpcore import http_request
from validata import chick_response
from testcase import import_json_file

testcass = "test_cass.json"
testcass = import_json_file(testcass)
request = testcass.get("request")
validata = testcass.get("validata")
response = http_request(request)
chick_response(response, validata)