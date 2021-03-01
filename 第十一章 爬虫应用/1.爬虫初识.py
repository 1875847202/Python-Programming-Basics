"""
爬虫使用的场景：
    1.通用爬虫：抓取互联网的一整张页面数据
    2.聚焦爬虫：是建立在通用爬虫的基础之上，抓取的是页面中特定的局部内容
    3.增量式爬虫：检测网站中数据更新的情况，只会网站中最近更新的内容

robots.txt协议：
          规定了网站中那些数据可以被爬取
"""

#request模块
#request模块是python原生的基于网络请求的模块，效率极高
"""
request模块作用：
   - 模拟浏览器发起请求

request模块使用（request模块的编码流程）：
   - 指定URL
   - 发起请求
   - 获取响应数据
   - 持久化存储响应数据
"""

import requests
if __name__ == "__main__":
    #step_1.指定url
    url = 'https://www.sogou.com/'
    #step_2.发起get请求
    response = requests.get(url=url)
    #get会返回一个响应对象
    #step_3.返回响应对象.text返回字符串显示的响应数据
    page_text = response.text
    print(page_text)
    #step_4.持久化存储
    with open('sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')
