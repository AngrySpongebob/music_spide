import requests
from bs4 import BeautifulSoup
url ='http://www.zbj.com/appdingzhikaifa/sq10054601k0.html'
res=requests.get(url)
res.encoding='utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.pagination'):
	h2=news.select('li')
	if len(h2)>0:
		a=h2[13].select('a')[0]['href']


base_url='http://www.zbj.com'
url1=base_url+a
driver=webdriver.Chrome()
driver.get(url1)
results = driver.find_elements_by_xpath("//div[@class='witkey-name j-witkey-name']/a")
count =0
res=[]
for result in results:
	if result.text not in res:
		res.append(result.text)

for r in res:
	s=r.encode("gbk")
print(s)
