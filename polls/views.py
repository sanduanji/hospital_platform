# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from mongoengine import connect
from .models import *
import time
from django.http import HttpResponse,JsonResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from bson import json_util
from django.core import serializers

from django.forms.models import model_to_dict

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# from django.shortcuts import render_to_response
# 接入MongoDB

connect('hulian', host='127.0.0.1', port =27017)

name = '张三'


###layui确定待搜索的单个病人的全局变量####
layui_patient_id = ''

def index(request):
    # context = "a":"f"
    context = {"reiddata": "dsfasdfadfsa"}
    return render(request, 'polls/home.html', context)
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
#模板界面
#------------------------------------------------------
def Home(request):
    context = {"reiddata": "dsfasdfadfsa"}

    return render(request,'polls/home.html', context)

def hello(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


def testhellow(request):
    context = ""
    return render(request, 'polls/testhellow.html', context)

def bingren_xinxi(request):
    # obj_list = NewDataset.objects[:]
    #    return render(requset,'real.html',{'obj':obj})
    context = {'obj_list': 'fdasf'}
    return render(request, 'polls/bingren_xinxi.html', context)

def zhuyuan_xinxi(request):
    # cklist = Checkpoint.objects[:]
    context = {'cklist':'dfadsf'}
    return render(request, 'polls/zhuyuan_xinxi.html', context)

def jianyan_baogao(request):
    # datasets = Dataset.objects[:]
    context = {'dataset':'dafdsf'}
    return render(request,'polls/jianyan_baogao.html',context)

def detecperson(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context = {'ff':'dffd'}
    return render(request, 'polls/detecperson.html', context)

def view_dataset(request):
    # lists = Dataset.objects[:]
    context = {'lists':'fdfd'}
    return render(request, 'polls/view_dataset.html', context)

def bingli_baogao(request):
    return render(request, 'polls/bingli_baogao.html')

def sign_up(request):
    return render(request, 'polls/sign_up.html')

def sign_in(request):
    return render(request, 'polls/sign_in.html')

def contact(request):
    return render(request, 'polls/contact.html')

def view_output(request):
    # lists = Outlog.objects[:]
    context={'lists':'fdfd'}
    return render(request, 'polls/view_outputs.html', context)

def yiyuan_zhuce(request):
    context = {'dfdf':'dsfasdf'}
    return render(request, 'polls/hospital_zhuce.html', context)

def jieru_list(request):
    # context = {'fdsfas':'fasdfasdfsaf'}
    hospitals = Jiekou.objects[:]
    context = {'hospitals':hospitals}
    return render(request, 'polls/jieru_list.html', context)
def show_patient(request):
    context = {'dsfa':'fdsafasdfsa'}
    return render(request, 'polls/show_patient.html', context)



##测试连接mongo

def getname(request):
    patients = Patient.objects[:]
    context = {'patient':patients}
    return render(request, 'polls/view_patient.html', context)


def getreport(request):
    reports = Report.objects[:]
    context = {'reports':reports}
    return render(request, 'polls/view_report.html', context)


def getcontent(request):
    contents = Content.objects[:]
    context = {'contents':contents}
    return render(request, 'polls/view_content.html', context)

#病人报告列表显示界面
def getreport_list(request):
    reports = Report.objects[:]
    context = {'reports':reports}
    return render(request, 'polls/view_reportlist.html', context)


def search_patient(request):
    pname = request.POST["name"]
    pid = request.POST["id"]
    hospital = request.POST["hospital"]
    keshi = request.POST["keshi"]


    # patients = Patient.objects[:]
    # context = {'patient':patients}
    # print('its pid')
    # print(pid)
    # print(type(pid))
    # if(pid==''):
    #     print('pid is kong')
    # elif(not pid):
    #     print('fdfaasdfdsa')
    # print('its pname')
    # print(pname)
    # print(type(pname))
    # print('its hospital')
    # print(hospital)
    # print(type(hospital))
    # print('its keshi')
    # if keshi=='all':
    #     print('keshi alll')
    # print(keshi)
    # print(type(keshi))


    if pid!='' and pname!='' and hospital=='all' and keshi=='all':
        patients = Patient.objects(name=pname, id = pid)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(name = pname, id=pid)
        context = {'patient': patients, 'report_types': report_tp}

    #无身份证 有姓名  不限医院  不限科室
    elif pid=='' and pname!='' and hospital=='all' and keshi=='all':
        patients = Patient.objects(name=pname)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(name = pname)
        context = {'patient': patients, 'report_types': report_tp}

    # 有身份证 不限姓名  不限医院  不限科室
    elif pid!='' and pname=='' and hospital == 'all' and keshi == 'all':
        patients = Patient.objects(id=pid)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(id=pid)
        context = {'patient': patients, 'report_types': report_tp}

    # 有身份证 无姓名  限制医院  不限科室
    elif pid and pname=='' and hospital!='all' and keshi=='all':
        patients = Patient.objects(id=pid, hospital__contains = hospital)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(id=pid, hospital=hospital)
        context = {'patient': patients, 'report_types': report_tp}

    # 有身份证 无姓名  不限医院  限制科室
    elif pid and pname=='' and hospital == 'all' and keshi != 'all':
        patients = Patient.objects(id=pid, keshi=keshi)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(id=pid, keshi=keshi)
        context = {'patient': patients, 'report_types': report_tp}

    # 有身份证 无姓名  限制医院  限制科室
    elif pid!= '' and pname=='' and hospital != 'all' and keshi != 'all':
        patients = Patient.objects(id=pid, hospital__contains=hospital, keshi=keshi)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(id=pid, hospital = hospital, keshi=keshi)
        context = {'patient': patients, 'report_types': report_tp}
    # 无身份证 无姓名  不限医院  不限科室
    elif pid=='' and pname=='' and hospital=='all' and keshi =='all':
        patients = Patient.objects[:]
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects[:]
        context = {'patient': patients, 'report_types': report_tp}

    # 无身份证 无姓名  不限医院  限制科室
    elif pid=='' and pname=='' and hospital == 'all' and keshi != 'all':
        patients = Patient.objects(keshi=keshi)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(keshi=keshi)
        context = {'patient': patients, 'report_types': report_tp}
    # 无身份证 无姓名  限制医院  不限科室
    elif pid == '' and pname == '' and hospital != 'all' and keshi == 'all':
        patients = Patient.objects(hospital__contains=hospital)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(hospital=hospital)
        context = {'patient': patients, 'report_types': report_tp}
    # 无身份证 无姓名  限制医院  限制科室
    elif pid=='' and pname=='' and hospital != 'all' and keshi != 'all':
        patients = Patient.objects(hospital__contains = hospital, keshi=keshi)
        # 找到病人相关的报告种类数信息
        report_tp = ReportType.objects(hospital = hospital, keshi=keshi)
        context = {'patient': patients, 'report_types': report_tp}



    time.sleep(6)
    return render(request, 'polls/view_patient.html', context)

#查找检验报告
def search_content(request):
    # pname = request.POST["name"]
    pid = request.POST["id"]
    # contents = Content.objects[:]
    contents = Content.objects(id=pid)
    context = {'contents':contents}
    # if pid:
    #     context = {'contents': contents, 'pname':pname, 'pid':pid}
    # else:
    #     context = {'contents': contents}


    # time.sleep(12)
    return render(request, 'polls/view_content.html', context)


def search_report(request):
    # pname = request.POST["name"]
    pid = request.POST["id"]
    reports = ZhenDuan_Report.objects(id = pid)
    # if pname:
    #     context = {'reports': reports, 'pname':pname, 'pid':pid}
    # else:
    #     context = {'reports': reports, 'pname':''}
    # time.sleep(12)
    context = {'reports':reports}


    # time.sleep(12)
    return render(request, 'polls/view_report.html', context)

# 根据报告类别跳转至检验+诊断报告
def search_reportlist(request):
    # pname = request.POST["name"]
    pid = request.POST["id"]
    report_type = request.POST["report_tp"]

    print('its pid')
    print(pid)
    print(type(pid))

    print('its report_type')
    print(report_type)
    print(type(report_type))
    if report_type == '诊断报告':
        reports = ZhenDuan_Report.objects(id = pid)
        context = {'reports': reports}
        print(context)

        # time.sleep(12)
        return render(request, 'polls/view_report.html', context)
    elif report_type == '检验报告':
        reports = Content.objects(id = pid)
        context = {'contents': reports}

        # time.sleep(12)
        return render(request, 'polls/view_content.html', context)

    elif report_type == '无报告':
        context = {}
        return render(request, 'polls/no_report.html', context)


def insert_hospital(request):
    hospital = request.POST["hospital"]
    jiekou = request.POST["jiekou"]
    user = request.POST["user"]
    userphone = request.POST["userphone"]
    keshi = request.POST["keshi"]
    gongneng = request.POST["gongneng"]
    case = Jiekou(hospital=hospital, data=jiekou, username=user, userphone=userphone, gongneng = gongneng, keshi = keshi)
    case.save()
    return render(request, 'polls/zhuce_ok.html')

def get_hospital(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals':hospitals}

    # time.sleep(12)
    return render(request, 'polls/jieru_list.html', context)

#获取单个病人在单个医院，单个科室，单次诊断记录
def search_single_report(request):
    id = request.POST["id"]
    name = request.POST["name"]
    report_id = request.POST["report_id"]
    reports = Report.objects(name=name, report_id=report_id, id =id)
    context = {'reports':reports, 'name':name, 'id':id, 'report_id':report_id}

    # time.sleep(12)
    return render(request, 'polls/view_report.html', context)



#返回patient list
def back_patientlist(request):
    return HttpResponseRedirect('/search_patient/')

######03按个人为中心更新##############
#测试病人列表页面
#查找到指定的病人
def test_patientlist(request):
    pname = request.POST["name"]
    pid = request.POST["id"]

    if pid != '' and pname != '':
        patients = ReportTypeList.objects(name = pname, id = pid)
        context = {'patients': patients}
    #无身份证 有姓名
    elif pid=='' and pname!='' :
        patients = ReportTypeList.objects(name = pname)
        context = {'patients': patients}

    # 有身份证 不限姓名
    elif pid!='' and pname=='' :
        patients = ReportTypeList.objects(id = pid)
        context = {'patients': patients}

    return render(request, 'polls/03patient_list.html', context)
##查找指定病人的报告情况
def test_patientreport(request):
    pname = request.POST["name"]
    pid = request.POST["id"]
    # contents = Content.objects(id=pid)


    reports = ReportTypeList.objects(id = pid, name=pname)
    print('测试输出')
    for i in reports:

        print(i.name)
        print(i.id)


    context = {'reports':reports}
    return render(request, 'polls/03repo_typelist.html', context)








# def search_reportlist(request):


def zhenduan_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']
    hospital = request.POST['hospital']
    keshi = request.POST['keshi']

    reports = Zhenduan03.objects(name = pname, id = pid, hospital=hospital, keshi=keshi)

    context = {'reports':reports}

    return render(request, 'polls/03zhenduan_report.html', context)



def jiance_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']

    hospital = request.POST['hospital']
    keshi = request.POST['keshi']
    report_id = request.POST['report_id']

    print('检测样例')
    print(pname)
    print(pid)
    print(hospital)
    print(report_id)
    reports = Jiance03.objects(name=pname, id=pid, hospital=hospital, keshi=keshi)
    for i in reports:
        print(i.yiji)
    context = {'reports':reports}

    return render(request, 'polls/03jiance_report.html', context)


def zhuayuan_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']
    hospital = request.POST['hospital']
    keshi = request.POST['keshi']
    zhuyuanhao = request.POST['zhuyuanhao']
    reports = Zhuyuan03.objects(name=pname, id=pid, hospital=hospital, keshi=keshi)
    context = {'reports':reports}
    return render(request, 'polls/03zhuyuan_report.html', context)


def shoushu_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']
    hospital = request.POST['hospital']
    shoushubianhao = request.POST['shoushubianhao']
    shoushuxingzhi = request.POST['shoushuxingzhi']

    reports = Shoushu03.objects(name=pname, id=pid, hospital= hospital, shoushuxingzhi = shoushuxingzhi)
    context = {'reports':reports}
    return render(request, 'polls/03shoushu_report.html', context)


def bingli_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']
    hospital = request.POST['hospital']
    keshi = request.POST['keshi']
    report_id = request.POST['report_id']


    reports = Binglibaogao03.objects(name=pname, id=pid, hospital=hospital, report_id=report_id)
    context = {'reports':reports}
    return render(request, 'polls/03bingli_report.html', context)



def chuyuan_repo(request):
    pname = request.POST['name']
    pid = request.POST['id']
    hospital = request.POST['hospital']
    # keshi = request.POST['keshi']
    zhuyuanhao = request.POST['zhuyuanhao']

    reports = Chuyuan03.objects(name=pname, id=pid, hospital=hospital, zhuyuanhao=zhuyuanhao)
    context= {'reports':reports}
    return render(request, 'polls/03chuyuan_report.html', context)


def person_info(request):
    pname = request.POST['name']
    pid = request.POST['id']
    type = request.POST['type']
    print('点击类别')
    print(type)
    if type == 'info':
        print('its info')
    reports = Patientinfo03.objects(name=pname, id=pid)
    context= {'reports':reports}
    return render(request, 'polls/03person_info.html', context)

##03个人全部记录

def repo_types(request):
    pname = request.POST['name']
    pid = request.POST['id']
    type = request.POST['type']

    if type == 'info':
        reports = Patientinfo03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03person_info.html', context)
    elif type == 'zhenduan':
        reports = Zhenduan03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03zhenduan_report_list.html', context)
    elif type == 'jiance':
        reports = Jiance03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03jiance_report_list.html', context)
    elif type == 'zhuyuan':
        reports = Zhuyuan03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03zhuyuan_report_list.html', context)
    elif type == 'shoushu':
        reports = Shoushu03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03shoushu_report_list.html', context)

    elif type == 'bingli':
        reports = Binglibaogao03.objects(name=pname, id=pid)
        context = {'reports': reports}
        # return render(request, 'polls/03bingli_report.html', context)
        return render(request, 'polls/03bingli_report_list.html', context)
    elif type == 'chuyuan':
        reports = Chuyuan03.objects(name=pname, id=pid)
        context = {'reports': reports}
        return render(request, 'polls/03chuyuan_report_list.html', context)


    # return render(request, 'polls/03repo_typelist.html', context)


#########


def denglu(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals':hospitals}

    # time.sleep(12)
    return render(request, 'polls/03denglu.html', context)

def testlayui(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals':hospitals}

    # time.sleep(12)
    # return render(request, 'polls/03layuitest2.html', context)
    # return render(request, 'polls/layuimini/welcome-1.html', context)
    return render(request, 'polls/layuiadmin/layuiadmin_test1.html', context)
    # return render(request, 'polls/layuiadmin/layui_test1.html', context)
    # return render(request, 'polls/layuiadmin/console.html', context)




####0403测试Django分页#######
from django.shortcuts import render
from django.core.paginator import Paginator   # Django内置分页功能模块

def tabeltest(request):
    # 提供json数据
    resp = {"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75},{"id":10010,"username":"user-10","sex":"女","city":"城市-10","sign":"签名-10","experience":1016,"logins":182,"wealth":71294671,"classify":"诗人","score":34},{"id":10011,"username":"user-11","sex":"女","city":"城市-11","sign":"签名-11","experience":492,"logins":107,"wealth":8062783,"classify":"诗人","score":6},{"id":10012,"username":"user-12","sex":"女","city":"城市-12","sign":"签名-12","experience":106,"logins":176,"wealth":42622704,"classify":"词人","score":54},{"id":10013,"username":"user-13","sex":"男","city":"城市-13","sign":"签名-13","experience":1047,"logins":94,"wealth":59508583,"classify":"诗人","score":63},{"id":10014,"username":"user-14","sex":"男","city":"城市-14","sign":"签名-14","experience":873,"logins":116,"wealth":72549912,"classify":"词人","score":8},{"id":10015,"username":"user-15","sex":"女","city":"城市-15","sign":"签名-15","experience":1068,"logins":27,"wealth":52737025,"classify":"作家","score":28},{"id":10016,"username":"user-16","sex":"女","city":"城市-16","sign":"签名-16","experience":862,"logins":168,"wealth":37069775,"classify":"酱油","score":86},{"id":10017,"username":"user-17","sex":"女","city":"城市-17","sign":"签名-17","experience":1060,"logins":187,"wealth":66099525,"classify":"作家","score":69},{"id":10018,"username":"user-18","sex":"女","city":"城市-18","sign":"签名-18","experience":866,"logins":88,"wealth":81722326,"classify":"词人","score":74},{"id":10019,"username":"user-19","sex":"女","city":"城市-19","sign":"签名-19","experience":682,"logins":106,"wealth":68647362,"classify":"词人","score":51},{"id":10020,"username":"user-20","sex":"男","city":"城市-20","sign":"签名-20","experience":770,"logins":24,"wealth":92420248,"classify":"诗人","score":87},{"id":10021,"username":"user-21","sex":"男","city":"城市-21","sign":"签名-21","experience":184,"logins":131,"wealth":71566045,"classify":"词人","score":99},{"id":10022,"username":"user-22","sex":"男","city":"城市-22","sign":"签名-22","experience":739,"logins":152,"wealth":60907929,"classify":"作家","score":18},{"id":10023,"username":"user-23","sex":"女","city":"城市-23","sign":"签名-23","experience":127,"logins":82,"wealth":14765943,"classify":"作家","score":30},{"id":10024,"username":"user-24","sex":"女","city":"城市-24","sign":"签名-24","experience":212,"logins":133,"wealth":59011052,"classify":"词人","score":76},{"id":10025,"username":"user-25","sex":"女","city":"城市-25","sign":"签名-25","experience":938,"logins":182,"wealth":91183097,"classify":"作家","score":69},{"id":10026,"username":"user-26","sex":"男","city":"城市-26","sign":"签名-26","experience":978,"logins":7,"wealth":48008413,"classify":"作家","score":65},{"id":10027,"username":"user-27","sex":"女","city":"城市-27","sign":"签名-27","experience":371,"logins":44,"wealth":64419691,"classify":"诗人","score":60},{"id":10028,"username":"user-28","sex":"女","city":"城市-28","sign":"签名-28","experience":977,"logins":21,"wealth":75935022,"classify":"作家","score":37},{"id":10029,"username":"user-29","sex":"男","city":"城市-29","sign":"签名-29","experience":647,"logins":107,"wealth":97450636,"classify":"酱油","score":27}
    # 每页显示5条数据
    paginator = Paginator(resp, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'polls/layuiadmin/layui_table.html', {'contacts': contacts})



####layui admin 样例界面########
####跳转layui console#####
def hulian_console(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals':hospitals}
    return render(request, 'polls/layuiadmin/home/console.html')

def layuiad_home1(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals': hospitals}
    return render(request, 'polls/layuiadmin/home/homepage1.html')

def layuiad_home2(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals': hospitals}
    return render(request, 'polls/layuiadmin/home/homepage2.html')

def layuiad_list(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals': hospitals}
    return render(request, 'polls/layuiadmin/app/content/list.html')

def layuiad_reload(request):
    hospitals = Jiekou.objects[:]
    context = {'hospitals': hospitals}
    return render(request, 'polls/layuiadmin/component/table/reload.html')




######读取mongodb数据上传layui前端#########
# def mongo_tolayui(request):
#     patients = ReportTypeList.objects()
#     context = {'patients': patients}
#     return render()


def reportlist_layui(request):
    print('前端传过来的wheere testid')
    testid = request.GET.get("testid")
    print(testid)
    data = ReportTypeList.objects.all()
    dataCount = data.count()
    pageIndex = request.GET.get("pageIndex")
    pageSize = request.GET.get("pageSize")

    if pageIndex is None:
        print('pageindex none')
        pageIndex=1
    if pageSize is None:
        print('pageindex none')
        pageSize = 5
    print("当前索引:{} 当前大小:{}".format(pageIndex,pageSize))
    print("所有记录:{} 数据总条数:{}".format(data,dataCount))

    list = []
    res = []
    for item in data:
        # print('字典初始化')
        dict = {}
        dict['id'] = item.id
        dict['name'] = item.name
        dict['gender'] = item.gender
        dict['birthday'] = item.birthday
        dict['age'] = item.age
        dict['shebao'] = item.shebao
        # dict['type'] = item.type
        list.append(dict)
    # print('page获得')
    pageInator = Paginator(list,pageSize)
    # print('context获得')
    context = pageInator.page(pageIndex)
    # print('res获得')

    for item in context:
        res.append(item)
    ###test print####
    # for item in res:
    #     print('打印item')
    #     print(item)
    data = { "code": 0,"msg": "ok","DataCount": dataCount,"data": res }
    return HttpResponse(json.dumps(data))
#表格搜索reload后台操作
def search_layui(request):
    name = request.GET.get("hostname")
    print('测试get')
    print(request.GET)

    # data1 = ReportTypeList.objects.all().filter(name=name)
    data = ReportTypeList.objects.all().filter(id=name)
    # if data1 is not None:
    #     data = data1
    # else:
    #     data = data2
    list = []
    print('接受name')
    print(data)
    for item in data:
        dict = {}
        dict['id'] = item.id
        dict['name'] = item.name
        dict['gender'] = item.gender
        dict['birthday'] = item.birthday
        dict['age'] = item.age
        dict['shebao'] = item.shebao
        list.append(dict)

    data = { "code": 0,"msg": "ok","DataCount": 1,"data": list }
    return HttpResponse(json.dumps(data))

def patient_reports_layui(request):
    id = request.GET.get("id")
    # report_id = request.GET.get("report_id")
    layui_patient_id = id
    print('接受到id')
    print(id)

    list = []
    # print()
    # data = ReportList(id=id)
    data = ReportList.objects.all().filter(id=id)

    list = []
    for item in data:
        dict = {}
        dict['id'] = item.id
        dict['name'] = item.name
        dict['gender'] = item.gender
        dict['shebao'] = item.shebao
        dict['age'] = item.age
        dict['report_id'] = item.report_id
        dict['report_type'] = item.report_type
        dict['report_date'] = item.report_date
        list.append(dict)

    data = {"code": 0, "msg": "ok", "DataCount": 1, "data": list}
    return render(request, 'polls/layuiadmin/hulian/patient_reports.html', data)

    # return HttpResponse(json.dumps(data))


def search_patient_reports_layui(request):
    id = request.GET.get("id")
    pid =request.GET.get("pid")
    print("当前页面显示pid")
    print(pid)
    id = '110108201001102205'
    # id = layui_patient_id
    # report_id = request.GET.get("report_id")

    list = []
    # print()
    # data = ReportList(id=id)
    data = ReportList.objects.all().filter(id=pid)

    list = []
    for item in data:
        dict = {}
        dict['id'] = item.id
        dict['name'] = item.name
        dict['gender'] = item.gender
        dict['shebao'] = item.shebao
        dict['age'] = item.age
        dict['report_id'] = item.report_id
        dict['report_type'] = item.report_type
        dict['report_date'] = item.report_date
        dict['hospital'] = item.hospital
        list.append(dict)

    data = {"code": 0, "msg": "ok", "DataCount": 1, "data": list}
    return HttpResponse(json.dumps(data))


################3
#接受选择的病人是哪个
def lisen_hang(request):
    id = request.GET.get("id")
    print('选择要查看的病人id是')
    print(id)
    return render(request, 'polls/layuiadmin/component/table/onrow.html')
    #formal version
    # return render(request, 'polls/layuiadmin/iframe_test/onrow.html')

#从listen_hang转到选择病人显示
@csrf_exempt
def patient_submit_set(request):
    # 客户端发送过来的数据
    if request.method == 'GET':
        print('its get')
    elif request.method == 'POST':
        print('its post')
    if request.is_ajax():
        print('收到选择病人ajax信号')
    print("前端选择病人返回数据")
    print(request.POST)
    print(request.POST.get('id'))
    print(request.GET)
    id = request.POST.get('id')

    response_data = {
        "code": 0
        , "msg": ""
        , "data": {
        "id": id
        }
    }
    context ={'id':id}
    return render(request, 'polls/layuiadmin/component/table/onrow.html', context)

    # return JsonResponse(response_data)




def menzhen_report_layui(request):
    id = '110108201001102205'
    hospital='华山医院'
    keshi='皮肤科'
    reports = Zhenduan03.objects(id=id,hospital=hospital,keshi=keshi)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/jizhen_report.html', context)


##iframe 急诊报告
def jizhen_report(request):
    reports = Zhenduan03.objects(id=id)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/jizhen_report.html', context=context)

##iframe 手术报告
def shoushu_report(request):
    reports = Zhenduan03.objects(id=id)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/shoushu_report.html', context=context)


##iframe 放射报告
def fangshe_report(request):
    # reports = Zhenduan03.objects(id=id)
    # context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/fangshe_report.html')



##iframe 药房报告
def yaofang_report(request):
    reports = Zhenduan03.objects(id=id)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/yaofang_report.html', context=context)


##iframe 检验报告
def jianyan_report(request):
    reports = Zhenduan03.objects(id=id)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/jianyan_report.html', context=context)
############layui模板用户部分##########
def userinfo_layui(request):
    id = '110108201001102205'
    hospital='华山医院'
    keshi='皮肤科'
    reports = Zhenduan03.objects(id=id,hospital=hospital,keshi=keshi)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/set/user/info.html', context)


def denglu_layui(request):
    id = '110108201001102205'
    reports = Zhenduan03.objects(id=id)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/user/login.html', context)

def webusers_layui(request):
    return render(request, 'polls/layuiadmin/user/user/list.html')

def webadmins_layui(request):
    return render(request, 'polls/layuiadmin/user/administrators/list.html')

def webroles_layui(request):
    return render(request, 'polls/layuiadmin/user/administrators/role.html')

def passswd_layui(request):
    return render(request, 'polls/layuiadmin/set/user/password.html')



def message_layui(request):
    return render(request, 'polls/layuiadmin/app/message/index.html')



def quanduan_fuza(request):
    return render(request, 'polls/layuiadmin/component/grid/all.html')

def test_tabs(request):
    return render(request, 'polls/layuiadmin/component/tabs/index.html')

def report_intab(request):
    return render(request, 'polls/layuiadmin/component/tabs/report_intab.html')




####显示结构化数据
def show_jiegouhua(request):
    return render(request, 'polls/layuiadmin/hulian/jiegouhua.html')

#上传未结构化数据
def upload_unjiegou(request):
    return render(request, 'polls/layuiadmin/hulian/upload.html')
#获取数据库结构化信息

def jiegouhua_database(request):
    data = BingliJiegouhua.objects.all()
    dataCount = data.count()
    pageIndex = request.GET.get("pageIndex")
    pageSize = request.GET.get("pageSize")

    if pageIndex is None:
        print('pageindex none')
        pageIndex=1
    if pageSize is None:
        print('pageindex none')
        pageSize = 5
    print("当前索引:{} 当前大小:{}".format(pageIndex,pageSize))
    print("所有记录:{} 数据总条数:{}".format(data,dataCount))

    list = []
    res = []
    for item in data:
        # print('字典初始化')
        dict = {}
        dict['id'] = item.bingli_id
        dict['name'] = item.name
        dict['gender'] = item.gender
        dict['songjian_date'] = item.songjian_date
        dict['age'] = item.age
        dict['zhuyuanhao'] = item.zhuyuanhao
        dict['biaoben_type'] = item.biaoben_type
        dict['zhongliu_location'] = item.zhongliu_location
        dict['chuankong'] = item.chuankong
        dict['ximo'] = item.ximo
        dict['qiechu_length'] = item.qiuchu_length
        # dict['type'] = item.type
        list.append(dict)
    # print('page获得')
    pageInator = Paginator(list,pageSize)
    print('context获得')
    context = pageInator.page(pageIndex)
    # print('res获得')

    for item in context:
        # print(item)
        res.append(item)
    ###test print####
    # for item in res:
    #     print('打印item')
    #     print(item)
    data = { "code": 0,"msg": "ok","DataCount": dataCount,"data": res }


    return HttpResponse(json.dumps(data))

#结构化搜索reload后台操作
def search_jiegouhua(request):
    date_range = request.GET.get("hostname")
    print('测试get')
    print('测试search 结构化')
    print(request.GET)
    start_date = date_range.split(' ')[0]
    end_date = date_range.split(' ')[2]
    print(start_date)
    print(end_date)

    start_year = int(start_date.split('-')[0].strip())
    start_month = int(start_date.split('-')[1].strip())
    start_day = int(start_date.split('-')[2].strip())
    end_year = int(end_date.split('-')[0].strip())
    end_month = int(end_date.split('-')[1].strip())
    end_day = int(end_date.split('-')[2].strip())

    data = BingliJiegouhua.objects.all()
    dataCount = data.count()
    pageIndex = request.GET.get("pageIndex")
    pageSize = request.GET.get("pageSize")

    if pageIndex is None:
        print('pageindex none')
        pageIndex=1
    if pageSize is None:
        print('pageindex none')
        pageSize = 20
    # print("当前索引:{} 当前大小:{}".format(pageIndex,pageSize))
    # print("所有记录:{} 数据总条数:{}".format(data,dataCount))
    # print('开始年')
    # print(start_year)
    # print('开始月')
    # print(start_month)
    # print('开始日')
    # print(start_day)
    # print('结束年')
    # print(end_year)
    # print('结束月')
    # print(end_month)
    # print('结束日')
    # print(end_day)

    list = []
    res = []
    flo = 0
    zheng = str(8)
    for item in data:
        if (type(item.songjian_date) == type('sdfadsfasdf')):
            # print('str送检时间')
            # print(type(item.songjian_date))
            # print(item.songjian_date)
            # continue
        # print('送检时间')
        # print(item.songjian_date)
        # print(type(item.songjian_date))
            if item.songjian_date == 'nan':
                print('这条是空的')
                print(item.songjian_date)
                flo = flo + 1
                continue
            data_year = int(str(item.songjian_date).split('-')[0])
            data_month = int(str(item.songjian_date).split('-')[1])
            data_day = int(str(item.songjian_date).split('-')[2])

            if data_year>= start_year and data_year <= end_year and data_month>=start_month and data_month<= end_month and data_day>= start_day and data_day<=end_day:
                print('数据符合')
            # print('数据年')
            # print(data_year)
            # print('数据月')
            # print(data_month)
            # print('数据日')
            # print(data_day)
            # print('字典初始化')
                dict = {}
                dict['id'] = item.bingli_id
                dict['name'] = item.name
                dict['gender'] = item.gender
                dict['songjian_date'] = item.songjian_date
                dict['age'] = item.age
                dict['zhuyuanhao'] = item.zhuyuanhao
                dict['biaoben_type'] = item.biaoben_type
                dict['zhongliu_location'] = item.zhongliu_location
                dict['chuankong'] = item.chuankong
                dict['ximo'] = item.ximo
                dict['qiechu_length'] = item.qiuchu_length
                # print(dict)
                list.append(dict)
                # list.append(item)
                # else:
                #     continue
    print('page获得')
    pageInator = Paginator(list,pageSize)
    print('context获得')
    context = pageInator.page(pageIndex)
    for item in context:
        print(item)
        res.append(item)
    print('按时间范围筛选获得')
    print(len(res))
    print('时间不规范报告数')
    print(flo)
    print(res)

    test_list = [{
        "id": "2018-18238",
        "name": "李华",
        "gender": "男",
        "age": 38,
        "songjian_date": "2018-04-28",
        "zhuyuanhao": 558405,
        "biaoben_type":"直肠及肛门切除标本",
        "zhongliu_location":"直肠（紧邻齿状线）",
        "chuankong":"否",
        "ximo": "/",
        "qiechu_length": "14   cm"
    },

    ]
    # for item in context:
    #     res.append(item)
    ###test print####
    # for item in res:
    #     print('打印item')
    #     print(item)
    data = { "code": 0,"msg": "ok","DataCount": len(res), "data": res}
    return HttpResponse(json.dumps(data))

def visual_jiegouhua(request):
    img_path = 'xray1.jpg'
    context = {'img_path':img_path}
    return render(request, "polls/layuiadmin/hulian/visual_jiegouhua.html", context)


########################################################################################################################
##ajax 接受
###可用 接受行监听事件
@csrf_exempt
def ajax_submit_set(request):
    # 客户端发送过来的数据
    if request.method == 'GET':
        print('its get')
    elif request.method == 'POST':
        print('its post')
    if request.is_ajax():
        print('收到ajax信号')
    print("前端ajax返回数据")
    print(request.POST)
    print(request.POST.get('report_id'))
    print(request.GET)
    report_id = request.POST.get('report_id')
    report_type = request.POST.get('report_type')
    print('接受报告类型')
    if report_type == '放射报告':
        print('接受放射报告')


        fangshe_detail = HuashanFangshe.objects(report_id = report_id)
        json_data= fangshe_detail.to_json()
        json_report= json.loads(json_data)

        print(fangshe_detail)
        print('json报告细节')
        print(json_report)
        patient_name = json_report[0]['patient_name']
        patient_id = json_report[0]['patient_id']
        report_id = json_report[0]['report_id']
        jiancha_id = json_report[0]['jiancha_id']
        jiancha_keshi = json_report[0]['jiancha_keshi']
        jiancha_detail = json_report[0]['jiancha_detail']
        huojian_buwei = json_report[0]['huojian_buwei']
        doc = json_report[0]['doc']
        date = json_report[0]['date']


        print(patient_name)

        # print(fangshe_detail.jiancha_keshi)
        # jiancha_keshi = fangshe_detail.
        response_data = {
            "code": 0
            , "msg": ""
            , "data": {
                'patient_name':patient_name,
                'patient_id':patient_id,
                'report_id':report_id,
                'jiancha_id':jiancha_id,
                'jiancha_detail':jiancha_detail,
                'huojian_buwei':huojian_buwei,
                'doc':doc,
                'date': date,
                'jiancha_keshi':jiancha_keshi,
            }

        }
    elif report_type == '急诊报告':
        print('接受急诊报告')

        fangshe_detail = HuashanJizhen.objects(report_id = report_id)
        json_data= fangshe_detail.to_json()
        json_report= json.loads(json_data)

        print(fangshe_detail)
        print('json报告细节')
        print(json_report)
        patient_name = json_report[0]['patient_name']
        patient_id = json_report[0]['patient_id']
        report_id = json_report[0]['report_id']

        icd = json_report[0]['icd']
        diagname = json_report[0]['diagname']
        diagtime = json_report[0]['diagtime']
        diagdoctor = json_report[0]['diagdoctor']
        diag_docid = json_report[0]['diag_docid']

        print(patient_name)
        response_data = {
            "code": 0
            , "msg": ""
            , "data": {
                'patient_name':patient_name,
                'patient_id':patient_id,
                'report_id':report_id,
                'icd':icd,
                'diagname':diagname,
                'diagtime':diagtime,
                'diagdoctor':diagdoctor,
                'diag_docid': diag_docid,
            }

        }

    elif report_type == '检验报告':
        print('接受检验报告')

        jianyan_detail = HuashanJianyan.objects(report_id = report_id)
        json_data= jianyan_detail.to_json()
        json_report= json.loads(json_data)

        print(jianyan_detail)
        print('json报告细节')
        print(json_report)
        patient_name = json_report[0]['patient_name']
        patient_id = json_report[0]['patient_id']
        report_id = json_report[0]['report_id']

        jigan_data = json_report[0]['jigan_data']
        jigan_range = json_report[0]['jigan_range']
        jigan_danwei = json_report[0]['jigan_danwei']

        lensuanmei_data = json_report[0]['lensuanmei_data']
        lensuanmei_range = json_report[0]['lensuanmei_range']
        lensuanmei_danwei = json_report[0]['lensuanmei_danwei']
        baidanbai_data = json_report[0]['baidanbai_data']
        baidanbai_range = json_report[0]['baidanbai_range']
        baidanbai_danwei = json_report[0]['baidanbai_danwei']

        date = json_report[0]['date']

        print(patient_name)
        response_data = {
            "code": 0
            , "msg": ""
            , "data": {
                'patient_name':patient_name,
                'patient_id':patient_id,
                'report_id':report_id,
                'jigan_data':jigan_data,
                'jigan_range':jigan_range,
                'jigan_danwei': jigan_danwei,
                'lensuanmei_data':lensuanmei_data,
                'lensuanmei_range':lensuanmei_range,
                'lensuanmei_danwei': lensuanmei_danwei,
                'baidanbai_data': baidanbai_data,
                'baidanbai_range': baidanbai_range,
                'baidanbai_danwei': baidanbai_danwei,
                'date':date,
            }

        }
    elif report_type == '手术报告':

        print('接受手术报告')
        print('手术报告编号')
        print(report_id)

        fangshe_detail = HuashanShoushu.objects(report_id=report_id)
        json_data = fangshe_detail.to_json()
        json_report = json.loads(json_data)

        print(fangshe_detail)
        print('json报告细节')
        print(json_report)
        patient_name = json_report[0]['patient_name']
        patient_id = json_report[0]['patient_id']
        report_id = json_report[0]['report_id']
        operation_id = json_report[0]['operation_id']
        icd = json_report[0]['icd']
        diagname = json_report[0]['diagname']
        shoushuname = json_report[0]['shoushuname']
        doc = json_report[0]['doc']
        date = json_report[0]['time']
        firstassistant = json_report[0]['firstassistant']
        mazui = json_report[0]['mazui']
        mazui_doc = json_report[0]['mazui_doc']
        shoushujingguo = json_report[0]['shoushujingguo']

        print(patient_name)

        # print(fangshe_detail.jiancha_keshi)
        # jiancha_keshi = fangshe_detail.
        response_data = {
            "code": 0
            , "msg": ""
            , "data": {
                'patient_name': patient_name,
                'patient_id': patient_id,
                'report_id': report_id,
                'operation_id': operation_id,
                'shoushujingguo': shoushujingguo,
                'firstassistant': firstassistant,
                'doc': doc,
                'date': date,
                'mazui': mazui,
                'icd':icd,
                'diagname':diagname,
                'shoushuname':shoushuname,
                'mazui_doc':mazui_doc,
            }

        }

    elif report_type == '处方报告':
        print('处方报告')

        print('接受手术报告')
        print('手术报告编号')
        print(report_id)

        fangshe_detail = HuashanYaofang.objects(report_id=report_id)
        json_data = fangshe_detail.to_json()
        json_report = json.loads(json_data)

        print(fangshe_detail)
        print('json报告细节')
        print(json_report)
        patient_name = json_report[0]['patient_name']
        patient_id = json_report[0]['patient_id']
        report_id = json_report[0]['report_id']

        chufang_id = json_report[0]['chufang_id']
        med_type = json_report[0]['med_type']
        med_id = json_report[0]['med_id']
        med_name = json_report[0]['med_name']
        guige = json_report[0]['guige']
        baozhuangliang = json_report[0]['baozhuangliang']
        danwei = json_report[0]['danwei']
        jiliang = json_report[0]['jiliang']
        pinci = json_report[0]['pinci']
        tujing = json_report[0]['tujing']
        danjia = json_report[0]['danjia']

        print(patient_name)

        # print(fangshe_detail.jiancha_keshi)
        # jiancha_keshi = fangshe_detail.
        response_data = {
            "code": 0
            , "msg": ""
            , "data": {
                'patient_name': patient_name,
                'patient_id': patient_id,
                'report_id': report_id,
                'chufang_id': chufang_id,
                'med_type': med_type,
                'med_id': med_id,
                'guige': guige,
                'baozhuangliang':baozhuangliang,
                'danwei':danwei,
                'jiliang':jiliang,
                'pinci':pinci,
                'tujing':tujing,
                'danjia':danjia,
                'med_name':med_name,
            }

        }

    print(report_type)
    pid = request.POST.get('id')
    pname = request.POST.get('name')

    return JsonResponse(response_data)

# Create your views here.
def ajax_index(request):
    return render(request, "polls/test_ajax_cal.html")


def cal(request):
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    print('num1')
    print(num1)
    print('num2')
    print(num2)
    ret = int(num1) + int(num2)
    return HttpResponse(str(ret))



####################################################ajax test end##################
#获取上传文件
@csrf_exempt
def get_layuifile(request):
    file_url = request.FILES.get('file')
    # response_data = {"info":"成功上传文件"}
    response_data = {
        "code": 0
        , "msg": ""
        , "data": {
        "src": "http://cdn.layui.com/123.jpg"
    }
    }

    return JsonResponse(response_data)


#注册接口

def zhuce_jiekou(request):
    return render(request, 'polls/layuiadmin/hulian/zhuce_jiekou.html')

def jiekou_data_layui(request):
    data = Hospital_Jiekou_Layui.objects.all()
    dataCount = data.count()
    pageIndex = request.GET.get("pageIndex")
    pageSize = request.GET.get("pageSize")

    if pageIndex is None:
        print('pageindex none')
        pageIndex=1
    if pageSize is None:
        print('pageindex none')
        pageSize = 5
    print("当前索引:{} 当前大小:{}".format(pageIndex,pageSize))
    print("所有记录:{} 数据总条数:{}".format(data,dataCount))

    list = []
    res = []
    for item in data:
        # print('字典初始化')
        dict = {}
        dict['name'] = item.name
        dict['hospital'] = item.hospital
        dict['keshi'] = item.keshi
        dict['address'] = item.address
        dict['system_name'] = item.system_name
        dict['phone'] = item.phone
        dict['email'] = item.email
        # dict['use'] = item.use
        dict['gongneng'] = item.gongneng
        dict['beizhu'] = item.beizhu
        dict['cunchu'] = item.cunchu
        dict['analysis'] = item.analysis
        dict['zhenliao'] = item.zhenliao
        dict['fenxi'] = item.fenxi
        dict['keyan'] = item.keyan
        # dict['type'] = item.type
        list.append(dict)
    # print('page获得')
    pageInator = Paginator(list,pageSize)
    print('context获得')
    context = pageInator.page(pageIndex)
    # print('res获得')

    for item in context:
        res.append(item)
    ###test print####
    # for item in res:
    #     print('打印item')
    #     print(item)
    data = { "code": 0,"msg": "ok","DataCount": dataCount,"data": res }
    return HttpResponse(json.dumps(data))

def view_jiekoulist(request):
    return render(request, 'polls/layuiadmin/hulian/view_jiekou.html')






############0419新增需求###################
def user_home(request):
    return render(request, 'polls/layuiadmin/hulian/user_home.html')
#用户搜索病人或疾病
def user_search(request):
    search = request.POST.get('search')
    patient_name = ReportTypeList.objects(name=search)

    patient_id = ReportTypeList.objects(id = search)

    json_data = patient_id.to_json()
    json_report = json.loads(json_data)
    context = {'report':'110108201001102205'}

    print('按姓名搜索')
    print(patient_name)
    print('按id搜索')
    print(patient_id)
    print(json_report)
    print('报告数量')
    print(len(json_report))
    if patient_id == None and patient_name == None:
        print('wrong')
    # return render(request, 'polls/layuiadmin/hulian/user_search_none.html')
    return render(request, 'polls/layuiadmin/component/table/reload.html', context)



def user_search_none(request):
    return render(request, 'polls/layuiadmin/hulian/user_search_none.html')


def get_zhuce(request):
    if request.method == "POST":
        print('注册接口post')
        hospital = request.POST.get('hospital')
        keshi = request.POST.get('keshi')
        system_name = request.POST.get('system_name')
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        cunchu = request.POST.get('cunchu')
        analysis = request.POST.get('analysis')
        zhenliao = request.POST.get('zhenliao')
        fenxi = request.POST.get('fenxi')
        keyan = request.POST.get('keyan')
        gongneng = request.POST.get('gongneng')
        beizhu = request.POST.get('beizhu')
        print('接口接受信息')
        print(hospital)
        print(keshi)
        print(system_name)
        print(address)
        print(name)
        print(phone)
        print(email)
        print(zhenliao)
        print(fenxi)
        print(gongneng)
        print(beizhu)
        print('是否存储')
        print(cunchu)
        print('同意分析')
        print(analysis)
        if cunchu=='on':
            cunchu='是'
        else:
            cunchu='否'
        if analysis=='on':
            analysis = '是'
        else:
            analysis = '否'
        if zhenliao == 'on':
            zhenliao = '是'
        else:
            zhenliao = '否'
        if fenxi == 'on':
            fenxi = '是'
        else:
            fenxi = '否'
        if keyan == 'on':
            keyan = '是'
        else:
            keyan = '否'



        from pymongo import MongoClient

        mongo_client = MongoClient(host='127.0.0.1', port=27017)
        mongo_db = mongo_client["hulian"]
        mongo_col = mongo_db["jiekou_new"]

        jiekou_zhuce = {"hospital":hospital, "keshi":keshi, "system_name":system_name, "address":address, "name":name,
                        "phone":phone,"email":email, "cunchu":cunchu,"analysis":analysis,"zhenliao":zhenliao,"fenxi":fenxi,
                        "keyan":keyan,"gongneng":gongneng,"beizhu":beizhu}
        x = mongo_col.insert_one(jiekou_zhuce)
    return render(request, 'polls/layuiadmin/hulian/view_jiekou.html')



#####按病人报告列表中的时间接口筛选报告

def search_time_report(request):
    date_range = request.GET.get("hostname")
    pid = request.GET.get("patid")
    print('测试get')
    print('测试search 结构化')
    print(request.GET)
    start_date = date_range.split(' ')[0]
    end_date = date_range.split(' ')[2]
    print(start_date)
    print(end_date)
    print('病人时间列表选择id')
    print(pid)
    pageIndex = request.GET.get("pageIndex")
    pageSize = request.GET.get("pageSize")


    start_year = int(start_date.split('-')[0])
    start_month = int(start_date.split('-')[1])
    start_day = int(start_date.split('-')[2])
    end_year = int(end_date.split('-')[0])
    end_month = int(end_date.split('-')[1])
    end_day = int(end_date.split('-')[2])

    data = ReportList.objects(id = pid)
    list = []
    res = []
    for item in data:
        data_year = int(str(item.report_date).split('.')[0])
        data_month = int(str(item.report_date).split('.')[1])
        data_day = int(str(item.report_date).split('.')[2])
        if data_year >= start_year and data_year <= end_year and data_month >= start_month and data_month <= end_month and data_day >= start_day and data_day <= end_day:
            dict = {}
            dict['report_id'] = item.report_id
            dict['report_type'] = item.report_type
            dict['report_date'] = item.report_date
            dict['hospital'] = item.hospital
            print(dict)
            list.append(dict)

        else:
            continue

    pageInator = Paginator(list,pageSize)
    print('context获得')
    context = pageInator.page(pageIndex)
    # print('res获得')

    for item in context:
        # print(item)
        res.append(item)
    test_list = [{
        "report_id": "0032",
        "report_type": "急诊报告",
        "report_date": "2020.10.11",
        "hospital": "华山医院"
    }]
    print('按时间搜索出的病人报告列表')
    print(list)
    print(res)

    dataCount = len(res)
    # data = { "code": 0,"msg": "ok","DataCount": 100 , "data": test_list}
    data = { "code": 0,"msg": "ok","DataCount": dataCount , "data": list}

    return HttpResponse(json.dumps(data))

#########################################
#####测试分页#########
def test_fenye(request):
    return render(request, 'polls/layuiadmin/component/table/resetPage.html')


#########测试djan下载文件
from django.http import FileResponse
from django.http import StreamingHttpResponse

# def file_down(request):
#     file=open('/Users/saber/Downloads/result.csv','rb')
#     response =FileResponse(file)
#     response['Content-Type']='application/octet-stream'
#     response['Content-Disposition']='attachment;filename="result.csv"'
#     return response


def file_down(request, id):
    file_path = '/Users/saber/Downloads/result.csv'
    file_name = 'result.csv'

    data = [{"id": "1", "image": "animation.jpg"}]  # 模拟mysql表数据

    def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    try:
        # 设置响应头
        # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
        response = StreamingHttpResponse(file_iterator(file_path))
        # 以流的形式下载文件,这样可以实现任意格式的文件下载
        response['Content-Type'] = 'application/octet-stream'
        # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    except:
        return HttpResponse("Sorry but Not Found the File")

    return response




#########iframe test#############

def iframe_test(request):
    return render(request, 'polls/iframe_test/iframe_home.html')

def iframe_page(request):
    return render(request, 'polls/iframe_test/iframepage.html')
    # ######0330测试######
