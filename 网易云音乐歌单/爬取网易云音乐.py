# -*- coding:utf-8 -*-
import csv
from selenium import webdriver
import time
import sys
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

t = time.localtime()
csv_file = open("playlist{}.csv".format(time.asctime(t).replace(":", "_")), "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(['song_title', 'song_time', 'song_url'])
song_sheet = []  # 存储歌单的链接


def allsonglist(song_sheet_urls, driver):
	jindu = 0
	for song_sheet_url in song_sheet_urls:
		# 循环访问每一个歌单
		driver.get(song_sheet_url)
		driver.switch_to.frame("contentFrame")
		song_data = driver.find_elements_by_css_selector(".m-table tbody tr")
		for song in song_data:
			# 获取歌曲名字
			song_name = song.find_element_by_css_selector('.txt a b').\
				get_attribute('title')
			# 去掉字符串中的&nbsp;
			song_name = "".join(song_name.split())
			# 获取歌曲时长
			song_time = song.find_element_by_class_name('u-dur').\
				text.split()
			# 获取歌曲链接
			song_url = song.find_element_by_css_selector('.txt a').\
				get_attribute('href')
			# 将获取到的内容写入到文件中
			try:
				writer.writerow([song_name, song_time, song_url])
			except Exception as e:
				print(e)
			else:
				pass
			finally:
				pass
		# 进度条的长度
		jindu += 1
		progress_bar = "\r[%s%s]%d%%"%("*"*jindu, " "*(100-jindu), jindu)
		sys.stdout.write(progress_bar)
		# 进度条的内容，这里要注意了，pycharm有可能不显示write的方法
		sys.stdout.flush()
		# 刷新缓存
		time.sleep(0.5)


def main(url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('''Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36''')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	# 禁用图片加载
	prefs = {
		'profile.default_content_setting_values': {
			'images': 2
		}
	}
	chrome_options.add_experimental_option('prefs', prefs)
	driver = webdriver.Chrome(executable_path='/opt/chromedriver',chrome_options=chrome_options)

	while url != 'javascript:void(0)':

		driver.get(url)
		# 切換到上一層的frame
		driver.switch_to.frame("contentFrame")
		# 要注意这里的find_elements_by_class_name 得到的是有个list对象
		data = driver.find_elements_by_class_name("u-cover")
		for i in data:
			driver.implicitly_wait(5)
			# 获取到每一个歌单的链接
			msk = i.find_element_by_class_name('msk').\
			get_attribute("href")
			song_sheet.append(msk)

		url = 'javascript:void(0)'

	allsonglist(song_sheet, driver)
	print('全量爬完')
	driver.quit()
	csv_file.close()


# 获取每个歌单的歌曲列表


if __name__ == '__main__':
	url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
	main(url)


"""
header = {
"Referer": "https://music.163.com/",
'Host': 'music.163.com',
"Cookie": "UM_distinctid=1643c6fa62d5c1-0c860cc2464919-435f5444-1fa400-1643c6fa62e382; vjuids=-4cbc04c87.1643c6fa7c9.0.7a208051b9d2c; vjlast=1530022308.1531923660.11; _ntes_nnid=9d10295e9eedd882ab11429dfc8aaffc,1530022307810; vinfo_n_f_l_n3=d10b82bf550095a1.1.8.1530022307829.1531826450023.1531923675856; _ntes_nuid=9d10295e9eedd882ab11429dfc8aaffc; __gads=ID=f27871795e195817:T=1530081112:S=ALNI_MbM_FxMP-ovdh4nGWfHPY5aFnSOJw; __f_=1530274174866; JSESSIONID-WYYY=g3u0pUDsOhtKUts9a6OZhu6xg0iZVDPVzVH%5CeaDvQymBTjasFnJxA62w5Iok%2B%2F5UE56NNEBsAA5DjOcm3zia3geyI2BC%5CrabYolUyeKuPlrmm%2Fjvg6U1%2BzUtvJBtoSZ4dR%2FEpOEEg%5C6AdutJDGJ7cJpYfIU9yMNfJATkU1CX9XQOOW1J%3A1535260914776; _iuqxldmzr_=32; __utma=94650624.175800079.1535191373.1535253576.1535259115.4; __utmz=94650624.1535259115.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=qtKP9du%2BDk2qm16qAJK2UBvusmTWNVewWQcLbrvigu0jdPbLnkKTYcG9RgdBt%2B0SVGDOu0TsbfvbRQgCyxjr9qMEginUxNN0%2FW7zMz6DJbPYxVRFb%2BkNAHJpFv381UFxQzc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5d73d94b0a8a4c56bb69ba599c73bede99691cf608b98bbabe8658cef88b5cc2af0fea7c3b92ab3ac85b1bc70b7f58c8cb17bafeffa92c44289ee9ba3f57fb1b39cb8cd5ea7a999b2e248a2aeba8ae67ff4b6acb1e148aeb585b5dc6985e79e88e74ab8f500b4d54d8891bbd1d779a2baba83d15ba59db799e97afbaf83a6e663ae8bb8afcd3ced89f99bd072f69c8683d353bc8a9ea7e121a9928fa9c97c86aafdd9b45f86a89f9be237e2a3; WM_TID=MQ1i6%2BTVZ0Em6fmex7BJZavuEY%2BK8afa; __utmc=94650624; __utmb=94650624.6.10.1535259115",
"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=header) #发起请求
reponse = urllib.request.urlopen(request).read()

	#	wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

with open("wangyiyun.html", "wb") as f: #自动关闭文件并释放资源
	f.write(reponse)
print('success')
"""
'''
#cookie的使用 涉及到登录信息的时候
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=La2A2'
data={
    'username':'zhanghao',
    'password':'mima',
}
postdata=urllib.parse.urlencode(data).encode('utf8')
header={
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

request=urllib.request.Request(url,postdata,headers=header)
#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
cookie=urllib.request.HTTPCookieProcessor(cjar)
opener=urllib.request.build_opener(cookie)
#将opener安装为全局
urllib.request.install_opener(opener)

try:
    reponse=urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

fhandle=open('./test1.html','wb')
fhandle.write(reponse.read())
fhandle.close()

url2='http://bbs.chinaunix.net/forum-327-1.html'   #打开test2.html文件，会发现此时会保持我们的登录信息，为已登录状态。也就是说，对应的登录状态已经通过Cookie保存。
reponse2=urllib.request.urlopen(url)
fhandle2=open('./test2.html','wb')
fhandle2.write(reponse2.read())
fhandle2.close()

'''
