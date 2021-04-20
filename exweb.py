import requests
from lxml import etree

url="https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
#用于补全url
base_url="https://www.dytt8.net"
def get_domain_urls(url):
    response=requests.get(url=url,headers=headers)
    text=response.text
    html=etree.HTML(text)
        #找到具有class="tbspan"的table下的所有a下面的href里面的值
    detail_urls=html.xpath("//table[@class='tbspan']//a/@href")
        #将url进行补全
    detail_urls=map(lambda url:base_url+url,detail_urls)
    return detail_urls

url="https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
for i in get_domain_urls(url):
    print(i)