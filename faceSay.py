#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64

import requests



# 人脸图片转base64
def imgtobase64():
    with open(".\images\\zt005.jpg", "rb") as f:  # 图片路径转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
    return base64_data  # str(base64_data, 'utf-8')


# 调用百度人脸搜索API进行查找
def facesearch():
    access_token = ""
    sendMessage = ""
    imageBase64 = imgtobase64()
    ak = "flOXbwIWB6FxfBECn0w3Y3F3"
    sk = "AnNRfoWYYF1BfuTCp1SoZ1xrom0NNNbE"
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + ak + "&client_secret=" + sk
    akResponse = requests.get(host)
    if akResponse:
        access_token = akResponse.json()["access_token"]
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = "{\"image\":\"" + imageBase64 + "\",\"image_type\":\"BASE64\",\"group_id_list\":\"faceTest\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        rdata = response.json()
        userList = rdata["result"]["user_list"]
        if len(userList) > 0 or userList != "" :
            userScore = rdata["result"]["user_list"][0]["score"]
            userId = rdata["result"]["user_list"][0]["user_id"]
            if userScore > 80 :   #匹配度大于80时
                sendMessage = "{\"code\":11,\"message\":{\"uid\":\"" + userId + "\",\"image\":\"\"}}"
        else:
            sendMessage = "{\"code\":11,\"message\":{\"uid\":\"001\",\"image\":\"" + imageBase64 + "\"}}"
        return sendMessage


if __name__ == '__main__':
    print facesearch()
