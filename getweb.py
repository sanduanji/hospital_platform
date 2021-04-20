import requests
from bs4 import BeautifulSoup
def test1():
    url = "http://10.176.38.224:5000/hospital/Id_card_num1/"
    url = url.rstrip()
    url3 = "http://127.0.0.1:8000/polls/"
    webdata = requests.get(url)
    print(webdata.text)



def test2():
    import requests
    from lxml import html
    page = requests.get("http://127.0.0.1:8000/polls/")
    page2 = requests.get("http://10.176.38.224:5000/hospital/Id_card_num1/")
    page3 = requests.get("http://123.56.106.249:8080/hospital2/")
    page4 = requests.get("https://www.baidu.com/")
    tree = html.fromstring(page2.text)
    content = tree.xpath('//*[@id="maincontent"]/div/div[1]/div/div/div[1]/h2/text()')
    content2 = tree.xpath('//html/body/a/text()')  #Id_card_num1
    content3 = tree.xpath('//html/body/div/div/div[2]/div/div/text()')
    content4 = tree.xpath('//*[@id="s-top-left"]/a[1]/a/text()')
    print(content2)
    for each in content2:
        replace = each.replace('\n', '').replace(' ', '')
        if replace == '\n' or replace == '':
            continue
        else:
            print(replace)

#test2()



def test3():
    import requests
    from lxml import etree

    for i in range(5,8):
        url = 'https://www.cnblogs.com/Chen-K/default.html?page='+str(i+1)
        url2 = 'http://10.176.38.224:5000/hospital/Id_card_num1/'
        html = requests.get(url)
        etree_html = etree.HTML(html.text)
        a = etree_html.xpath('//*[@id="mainContent"]/div/div[8]/div[2]/a/span/text()')
        # a = etree_html.xpath('/html/body/text()')
        for j in a:
            print(j)



test3()


def test4():
    import requests
    from lxml import etree



    url2 = 'http://10.176.38.224:5000/hospital/Id_card_num1'
    url3 = 'https://www.baidu.com/'
    url4 = 'http://123.56.106.249:8080/hospital2/'
    html = requests.get(url4)
    etree_html = etree.HTML(html.text)

    a = etree_html.xpath('/html/body/a/text()')
    a = etree_html.xpath('//*[@id="s-top-left"]/a[1]/a/text()')
    a = etree_html.xpath('//html/body/div/div/div[2]/div/div/a/text()')
    for j in a:
        print(j)

# test4()
