import json
import os
import webbrowser

from flask import Flask
from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)
@app.route('/')
def hello():
    return "helloworld"
@app.route('/hospital/<idcard>')
def case_info(idcard):
    options = Options()
    options.add_argument('--headless')
    options.add_argument("start-maximized")  # 初始化就最大化
    # driver = webdriver.Chrome(chrome_options=options)
    location = "/home/hulian/firefox/firefox"
    driver =webdriver.Firefox(firefox_options=options,executable_path='/home/hulian/geckodriver',firefox_binary=location)
    driver.maximize_window()  # 第一种加载完成后最大化
    driver.get("http://123.56.106.249:8080/hospital")
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/form/div[1]/div/div/input").send_keys(idcard)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/form/div[2]/div/button").click()
    time.sleep(2)
    # seq = ('科室', '姓名', '年龄', '出生日期', '性别', '婚姻状况', '出生地', '职业', '操作')
    # infos = dict.fromkeys(seq)
    # i=0
    infos = {}
    infos['身份证号'] = idcard
    # infos['身份证号'] = driver.find_element_by_xpath(
    #     "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[2]/div").text
    infos['科室'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[3]/div").text
    infos['姓名'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[4]/div").text
    infos['年龄'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[5]/div").text
    infos['出生日期'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[6]/div").text
    infos['性别'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[7]/div").text
    infos['婚姻状况'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[8]/div").text
    infos['出生地'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[9]/div").text
    infos['职业'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[10]/div").text
    # datas = driver.find_elements_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td/following-sibling::div")
    # for data in datas:
    #     infos[seq[i]] = data.text
    #     i = i+1
    # del infos['操作']
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[11]/div/span").click()
    time.sleep(2)
    infos['病史陈述人'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[4]/div[6]/div").text
    infos['用药历史'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[6]/div/div").text
    infos['主诉'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[8]/div/div").text
    jinfos = json.dumps(infos, ensure_ascii=False)
    driver.close()
    return jinfos

@app.route('/hospital2/<idcard>/<reportnum>')
def report_info(idcard,reportnum):
    options = Options()
    options.add_argument('--headless')
    options.add_argument("start-maximized")  # 初始化就最大化
    # driver = webdriver.Chrome(chrome_options=options)
    location = "/home/hulian/firefox/firefox"
    driver = webdriver.Firefox(firefox_options=options,executable_path='/home/hulian/geckodriver',firefox_binary=location)
    driver.maximize_window()  # 第一种加载完成后最大化
    driver.get("http://123.56.106.249:8080/hospital2")
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/form/div[1]/div/div/input").send_keys(idcard)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/form/div[2]/div/button").click()
    time.sleep(2)
    infos = {}
    infos['身份证号'] = idcard
    # infos['身份证号'] = driver.find_element_by_xpath(
    #     "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[2]/div").text
    infos['科室'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[3]/div").text
    infos['姓名'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[4]/div").text
    infos['年龄'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[5]/div").text
    infos['出生日期'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[6]/div").text
    infos['性别'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[7]/div").text
    infos['婚姻状况'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[8]/div").text
    infos['出生地'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[9]/div").text
    infos['职业'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[10]/div").text
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/table/tbody/tr/td[11]/div/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/form/div[1]/div/div/input").send_keys(reportnum)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/form/div[2]/div/button").click()
    infos['报告编号'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[2]/div").text
    infos['报告类别'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[3]/div").text
    infos['报告名称'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[4]/div").text
    infos['医技部门'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[5]/div").text
    infos['操作员'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[6]/div").text
    infos['审核人'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[7]/div").text
    infos['采样时间'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[8]/div").text
    infos['报告时间'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[9]/div").text
    infos['报告状态'] = driver.find_element_by_xpath(
        "/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[10]/div").text
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/table/tbody/tr/td[11]/div/span").click()
    time.sleep(3)
    infos['项目'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div").text
    infos['代码'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[2]/div[4]/div").text
    infos['结果'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[2]/div[6]/div").text
    infos['标本性状'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[3]/div[2]/div").text
    infos['标本标识'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[3]/div[4]/div").text
    infos['单位'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div").text
    infos['标本种类'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[4]/div[4]/div").text
    infos['床位'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[4]/div[6]/div").text
    infos['送检医生'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[5]/div[4]/div").text
    infos['参考范围'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[5]/div[6]/div").text
    infos['临床诊断'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[7]/div/div").text
    infos['备注'] = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div[9]/div/div").text
    jinfos = json.dumps(infos, ensure_ascii=False)
    driver.close()
    return jinfos

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)