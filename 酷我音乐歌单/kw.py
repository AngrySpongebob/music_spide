# -*- coding:utf-8 -*-

import csv
import sys

import requests
import re
import time
from selenium import webdriver


def banglist(bang_name, bang_id):
    song_list = requests.get("http://www.kuwo.cn/bang/content?name={0}&bangId={1}".format(bang_name, bang_id))
    song_list1 = re.sub(r'\s+', '', song_list.text, re.S)
    song_lists = re.findall(r'<ul class="listMusic">.*?</ul>', song_list1, re.S)
    song_list3 = re.findall(r'<li(.*?)</li>', song_lists[0], re.S)
    for k in song_list3:
        # print(k)
        song = re.findall(r'<div class="name">(.*?)</div>', k, re.S)
        song_url = re.findall(r'href="(.*?)"', song[0])  # 歌曲播放链接
        song_name = re.findall(r'>(.*?)</a>', song[0])  # 歌曲标题
        writer.writerow([song_name[0], song_url[0]])


def getquote(url):
    jindu = 0
    header = {
        'User-Agent': 'Mozilla / 5.0(X11;Ubuntu;Linux x86_64;rv: 61.0)'
                       'Gecko / 20100101Firefox / 61.0'
    }
    resp = requests.get(url, headers=header, verify=False, stream=True)
    div_left = re.compile(r'<li data-name=(.*?)>', re.S) #匹配所有榜单
    quotes = re.findall(div_left, resp.text)  # list
    for i in quotes:
        data = re.findall(r'"(.*?)"', i)
        data_name = data[0]
        data_id = data[1]
        banglist(data_name, data_id)
        jindu += 1
        s1 = "\r[%s%s]%d%%" % ("*" * jindu, " " * (100 - jindu), jindu)
        sys.stdout.write(">")
        # 进度条的内容，这里要注意了，pycharm有可能不显示write的方法
        sys.stdout.flush()
        time.sleep(0.3)
    print('ok')
    csv_file.close()


if __name__ == '__main__':
    t = time.localtime()
    csv_file = open("files/kw{}.csv".format(time.asctime(t).replace(":", "_")), "w", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['song_title', 'song_url'])
    getquote('http://www.kuwo.cn/bang/index')
