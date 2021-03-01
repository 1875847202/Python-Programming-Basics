#UA伪装：User-Agent （骑牛载体的身份标识）
#UA检测：门户网站的服务器会检测对应请求的身份标识，如果检测到其标识是一个浏览器，那么就说明该请求是正常请求
#但是若身份标识不是浏览器，则为不正常请求，则服务器端会拒绝该请求

import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw = input('输入一个关键词')
    param = {
        'query':kw
    }
    #对指定的url发起的请求携带参数，并且在请求过程中处理了参数
    response = requests.get(url = url,params = param)
    #获取响应数据
    page_text = response.text

    #持久化存储
    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8') as pf:
        pf.write(page_text)

    print('保存成功')
