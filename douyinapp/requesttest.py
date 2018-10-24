
import requests

i=0
while  i<=1:
    i=i+1
    # url='https://m.weibo.cn/api/comments/show?id=4188633986790962&page=6'
    url='https://m.weibo.cn/api/comments/show?id=4188633986790962&page='+str(i)
    html=requests.get(url)
    # print(html)
    # print(html.json())
    # for j in range(10):
    for j in range(len(html.json()['data']['data'])):

        print(html.json()['data']['data'][j]['user']['id'])