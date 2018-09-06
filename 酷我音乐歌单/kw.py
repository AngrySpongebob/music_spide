# -*- coding:utf-8 -*-

import csv
import re
import sys
import time
import requests


def banglist(bang_name, bang_id):
    """
    获取榜单列表
    :param bang_name: 榜单的名称
    :param bang_id: 榜单的id, 从酷我音乐链接中获取,非人力所能改变
    :return: 无返回值
    """
    song_list = requests.get("http://www.kuwo.cn/bang/content?name={0}&bangId={1}".format(bang_name, bang_id))
    song_list1 = re.sub(r'\s+', '', song_list.text, re.S)
    song_lists = re.findall(r'<ul class="listMusic">.*?</ul>', song_list1, re.S)
    song_list3 = re.findall(r'<li(.*?)</li>', song_lists[0], re.S)
    for k in song_list3:
        song = re.findall(r'<div class="name">(.*?)</div>', k, re.S)
        song_url = re.findall(r'href="(.*?)"', song[0])  # 歌曲播放链接
        # http://www.kuwo.cn/yinyue/49987523?catalog=yueku2016
        song_id = re.findall(r'http://www.kuwo.cn/yinyue/(.*?)\?.*?', song_url[0])  # 从类似上面的链接中获取歌曲的id,即那一堆很长的数字
        song_name = re.findall(r'>(.*?)</a>', song[0])  # 歌曲名
        writer.writerow([song_name[0], song_url[0]])
        # 进行音乐的下载
        download_song(song_name[0], song_id[0])
        time.sleep(0.3)
    return None


def download_song(song_name, song_id):
    """

    :param song_name: 歌曲名称,方便创建歌曲文件的时候使用
    :param song_id: 歌曲的id,酷我音乐中歌曲的id,用于请求歌曲下载链接中的参数
    :return: 无返回自
    """
    headers = {
        'User-Agent': 'Mozilla / 5.0(X11;Ubuntu;'
                      'Linux x86_64;rv: 61.0)'
                      'Gecko / 20100101Firefox / 61.0'
    }
    response = requests.get("http://antiserver.kuwo.cn/anti.s?"
                            "format=aac|mp3&rid=MUSIC_{}&"
                            "type=convert_url&response=res".format(song_id),
                            headers=headers, verify=False, stream=True)
    if response.status_code == 200:
        # 以二进制读写的方式打开文件,若文件存在打开,不存在则创建后打开
        mp3 = open('music_file/{}.aac'.format(song_name), 'wb+')
        mp3.write(response.content)
        mp3.close()
    else:
        return False
    return None


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
        s1 = "\r[%s%s]%d%%" % (">" * jindu, " " * (50 - jindu), jindu)
        sys.stdout.write(s1)
        # 进度条的内容，这里要注意了，pycharm有可能不显示write的方法
        sys.stdout.flush()
        time.sleep(0.3)
    print(' ok')
    csv_file.close()


if __name__ == '__main__':
    t = time.localtime()
    csv_file = open("files/kw{}.csv".format(time.asctime(t).replace(":", "_")), "w", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['song_title', 'song_url'])
    getquote('http://www.kuwo.cn/bang/index')


# 下载歌曲的链接 http://antiserver.kuwo.cn/anti.s?
# format=aac|mp3&rid=MUSIC_50601684&
# type=convert_url&response=res
