import json
import sys
import time
from seleniumwire.utils import decode

from urllib.parse import parse_qs

sys.path.insert(1, 'C:\\Users\\ahota\\PycharmProjects\\GA')
from Calls.finalCall import driver

gaCalls = []
time.sleep(10)
for request in driver.requests:
    if request.response:
        if request.url.startswith('https://www.google-analytics.com/collect'):
            body = request.querystring
            if(len(body)==0):
                body = request.body
            print(body)
            try:
                body = decode(body,'utf-8')
            except:
                pass
            payload = parse_qs(body,'utf-8')
            payloadJsonString = json.dumps(payload)
            payloadJsonObj = json.loads(payloadJsonString)
            gaCalls.append(payloadJsonObj)



print("Final gaCalls - ", gaCalls)
