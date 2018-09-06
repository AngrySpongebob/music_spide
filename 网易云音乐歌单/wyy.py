# 以下使用selenium方式获取到的soup
 
import re
from selenium import webdriver
from bs4 import BeautifulSoup
     
path='D:\\chromedriver'
url='https://music.163.com/#/playlist?id=90771773'
driver=webdriver.Chrome(path)
driver.get(url)
driver.switch_to.frame('g_frame') 
    # 如果报错missing value值，则将Chrome与Chromedriver更新到最新
     
soup=BeautifulSoup(driver.page_source, 'lxml')

# 获取用户名
string=soup.title.string
obj=re.compile('.*喜欢的音乐')
username=obj.findall(string)[0] #obj.findall 获取到的是一个list，此处获取list中的元素值
 
# 获取歌单列表包含歌曲名称，歌曲作者，歌曲专辑
trlist=soup.tbody.find_all('tr')
songlist=[]
for each in trlist:
    aux=[]
    aux.append(each.find('b')['title'].replace('\xa0',' ')
    temp=each.find_all('div','text')
    aux.append(temp[0].span['title'].replace('\xa0',' ')
    aux.append(temp[1].a['title'].replace('\xa0',' ')
    songlist.append(aux)
 
#导出为CSV文件
 
songlist.to_csv('%s.csv' % username)