#ReadME
##Task
###`class Task`
*接口类*


~~~python
def __init__(self, URL, output_dir='.', filename=None, auto_rename=False, cookies=None, debug=False, 
				 extractor_proxy=None, force=False, format=None, help=False, http_proxy=None, info=False,
                 input_file=None, itag=None, json=False, no_caption=False, no_merge=False, no_proxy=False,
                 output_filename=None, password=None, player=None, playlist=False, socks_proxy=None,
                 stream=None, timeout=600, url=False, version=False):
~~~

~~~python
def download(self):
~~~

~~~python
def speed(self):
~~~

~~~python
def progress(self):
~~~

~~~python
def received(self):
~~~

~~~python
def totalSize(self):
~~~

##BackEndAPI
###`class BackEndAPI`:
~~~python
 def __init__(self, url):
~~~
 初始化方法，需要一个url参数，类型String，为后端入口

---

~~~python 
 def register(self, name, username, password, verifiedPassword):
~~~
 注册方法

 参数全是字符串，其中**username is unique**

 返回布尔值，当注册成功将返回`True`，反之`False`
 
 ---
 
 ~~~python
 def login(self, username, password, remembered):
 ~~~
 登陆方法，参数1,2为`String`，参数3为`Bool`
 
 *remembered表示是否记住此账号，若记住，该账号将维持一个月的登录状态*
 
 ---
 
 ~~~python
 def checkIfExpired(self):
 ~~~
如果账号登录状态未失效则 `return True`
反之`return False`

---

~~~python
def uploadVideos(self, authorization, title, url, picUrl, rank, rankType, videoType, videoSubtype):
~~~

---

~~~python
def getRankedVideos(self, rankType)
~~~
*arguments:*  
  `ranktype`: `String`
  
*return:*  

~~~swift
list[dict<String: String>]
~~~