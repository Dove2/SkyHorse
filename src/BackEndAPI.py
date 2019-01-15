#!/usr/bin/env python3

import base64
from urllib import request, error
import datetime
import json


class BackEndAPI:

    def __init__(self, url):
        self.url = url
        self.token = ""
        self.expiresTime = datetime.datetime.now()

    def register(self, name, username, password, verifiedPassword):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            "Accept-Language": "zh-cn"
        }
        body = {
            "email": username,
            "name": name,
            "password": password,
            "verifyPassword": verifiedPassword
        }
        data = bytes(json.dumps(body), 'utf8')
        req = request.Request(url=self.url + "users", headers=headers, data=data)
        try:
            request.urlopen(req)
            return True

        except error.HTTPError as e:
            print(e)
            return False

        except error.URLError:
            print("Can not access server. Please try again later.")
            return False

    def login(self, username, password, remembered):
        encrypted_str = str(base64.b64encode((username + ":" + password).encode('utf-8')), 'utf-8')
        print(encrypted_str)
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Authorization": "Basic " + encrypted_str,
            "Accept-Language": "zh-cn"
        }
        body = {
            "remembered": remembered
        }
        data = bytes(json.dumps(body), 'utf8')
        req = request.Request(url=self.url + "login", headers=headers, data=data)
        try:
            result = request.urlopen(req)
            response = result.read()
            response_body = eval(response.decode('utf-8'))

            self.token = response_body["string"]
            expiresAt = response_body["expiresAt"]
            self.expiresTime = datetime.datetime.strptime(expiresAt[0:10] + expiresAt[11:19], '%Y-%m-%d%H:%M:%S')
            print(datetime.datetime.now(), self.expiresTime)

            return True

        except error.HTTPError as e:
            print(e)
            return False

        except error.URLError:
            print("Can not access server. Please try again later.")
            return False

    def checkIfExpired(self):
        return datetime.datetime.now() < self.expiresTime

    def getRankedVideos(self, rankType):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            "Accept-Language": "zh-cn"
        }
        body = {
            'rankType': rankType
        }
        data = bytes(json.dumps(body), 'utf8')
        req = request.Request(url=self.url + "rankedVideos", headers=headers, data=data)
        try:
            result = request.urlopen(req)
            response = result.read()
            return eval(response.decode('utf-8'))

        except error.HTTPError as e:
            print(e)
            return False

        except error.URLError:
            print("Can not access server. Please try again later.")
            return False

    def uploadVideos(self, authorization, title, url, picUrl, rank, rankType, videoType, videoSubtype):
        headers = {
            "Content-Type": "application/json",
            'Authorization': 'Basic ' + authorization
        }
        body = {
            'picUrl': picUrl,
            'rank': rank,
            'rankType': rankType,
            'title': title,
            'url': url,
            'videoType': videoType,
            'videoSubtype': videoSubtype
        }
        data = bytes(json.dumps(body), 'utf8')
        req = request.Request(url=self.url + "updateVideos", headers=headers, data=data)
        try:
            request.urlopen(req)
            return True

        except error.HTTPError as e:
            print(e)
            return False

        except error.URLError:
            print("Can not access server. Please try again later.")
            return False


# if __name__ == '__main__':
#     api = BackEndAPI("http://localhost:8080/")
#     print(type(api.getRankedVideos("ZC")[0]))
#
