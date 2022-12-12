import json
import time
from seleniumwire.utils import decode
from urllib.parse import parse_qs


def readPayload(request):
    if (len(request.querystring) != 0):
        body = request.querystring
    else:
        body = request.body
        body = decode(body, 'utf-8')
    payload = parse_qs(body, 'utf-8')
    payloadJsonString = json.dumps(payload)
    payloadJsonObj = json.loads(payloadJsonString)
    return payloadJsonObj


def gettingGaNetworkCalls(driver):
    gaCalls = []
    time.sleep(10)
    for request in driver.requests:
        if request.response:
            if request.url.startswith('https://www.google-analytics.com/collect'):
                payload = readPayload(request)
                gaCalls.append(payload)
    return gaCalls
