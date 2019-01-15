#!/usr/bin/env python3
import os
import sys
import threading
from time import sleep

_srcdir = '%s/you-get/src/' % os.path.dirname(os.path.realpath(__file__))
_filepath = os.path.dirname(sys.argv[0])
sys.path.insert(1, os.path.join(_filepath, _srcdir))

if sys.version_info[0] == 3:
    import you_get
else:  # Python 2
    from you_get.util import log

    log.e("[fatal] Python 3 is required!")
    log.wtf("try to run this script using 'python3 you-get'.")


class Task:
    """
    接口类
    """
    taskTag = 0

    def __init__(self, URL="", output_dir='.', filename=None, auto_rename=False, cookies=None, debug=False,
                 extractor_proxy=None, force=False, format=None, help=False, http_proxy=None, info=False,
                 input_file=None, itag=None, json=False, no_caption=False, no_merge=False, no_proxy=False,
                 output_filename=None, password=None, player=None, playlist=False, socks_proxy=None,
                 stream=None, timeout=600, url=False, version=False):
        self.tag = Task.taskTag
        Task.taskTag += 1

        self.currentSpeed = "0 KB/s"
        self.currentProgress = 0.0
        self.currentReceived = 0
        self.totalSize = 0
        self.totalPieces = 1
        self.done = False

        self.URL = URL
        self.output_dir = output_dir
        self.filename = filename
        self.auto_rename = auto_rename
        self.cookies = cookies
        self.debug = debug
        self.extractor_proxy = extractor_proxy
        self.force = force
        self.format = format
        self.help = help
        self.http_proxy = http_proxy
        self.info = info
        self.input_file = input_file
        self.itag = itag
        self.json = json
        self.no_caption = no_caption
        self.no_merge = no_merge
        self.no_proxy = no_proxy
        self.output_filename = output_filename
        self.password = password
        self.player = player
        self.playlist = playlist
        self.socks_proxy = socks_proxy
        self.stream = stream
        self.timeout = timeout
        self.url = url
        self.version = version

    def download(self):
        you_get.main(repo_path=_filepath, URL=self.URL, filename=self.filename, auto_rename=self.auto_rename,
                     cookies=self.cookies, debug=self.debug, extractor_proxy=self.extractor_proxy, force=self.force,
                     format=self.format, help=self.help, http_proxy=self.http_proxy, info=self.info,
                     input_file=self.input_file, itag=self.itag, json=self.json, no_caption=self.no_caption,
                     no_merge=self.no_merge, no_proxy=self.no_proxy, output_dir=self.output_dir,
                     output_filename=self.output_filename, password=self.password, player=self.player,
                     playlist=self.playlist, socks_proxy=self.socks_proxy, stream=self.stream, timeout=self.timeout,
                     url=self.url, version=self.version, instance=self)
        self.done = True

    def speed(self):
        return self.currentSpeed

    def progress(self):
        return self.currentProgress

    def received(self):
        return self.currentReceived

    def totalSize(self):
        return self.totalSize

    def isDone(self):
        return self.done

    def outputFilename(self):
        return self.output_filename


def showSpeed(task):
    while task.done is not True:
        while task.outputFilename is None:
            pass
        print(task.outputFilename())
        sleep(1)


if __name__ == '__main__':
    # task = Task("https://www.bilibili.com/video/av39770651", "/Users/zhangdefu/Desktop")
    # t1 = threading.Thread(target=task.download)
    # # threads.append(t1)
    # t2 = threading.Thread(target=task.speed)
    # # threads.append(t2)
    # t1.start()
    # t2.start()

    task2 = Task("https://www.bilibili.com/video/av39770651", "/Users/zhangdefu/Desktop")
    t3 = threading.Thread(target=task2.download)
    t3.start()
    t4 = threading.Thread(target=showSpeed, args=[task2])
    t4.start()
    # for t in threads:
    #     # t.setDaemon(True)
    #     t.start()
    # task.download("https://www.bilibili.com/video/av39770651", "/Users/zhangdefu/Desktop")
