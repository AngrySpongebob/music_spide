# -*- coding:utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "http://s.dianping.com/event/119124"


def main(url):
    print('hello')

    print (sys.argv)
    print (len(sys.argv))
    dper = sys.argv[0]
    print ("your dper is:"+dper)

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36")
    driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver', chrome_options=opts)
    driver.maximize_window()

    driver.get(url)
    driver.add_cookie({'name':'dper', 'value':dper,'path':'/'})
    category_urls=[]
    category_urls.append("http://s.dianping.com/event/shanghai/c1")
    category_urls.append("http://s.dianping.com/event/shanghai/c6")
    # for url in category_urls:
    #     process_category(url, driver)
    driver.quit()

if __name__ == '__main__':
    main(url)