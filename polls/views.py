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
        print('字典初始化')
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
    print('context获得')
    context = pageInator.page(pageIndex)
    print('res获得')

    for item in context:
        res.append(item)
    ###test print####
    for item in res:
        print('打印item')
        print(item)
    data = { "code": 0,"msg": "ok","DataCount": dataCount,"data": res }
    return HttpResponse(json.dumps(data))

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
    id = '110108201001102205'
    # id = layui_patient_id
    # report_id = request.GET.get("report_id")

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
        dict['hospital'] = item.hospital
        list.append(dict)

    data = {"code": 0, "msg": "ok", "DataCount": 1, "data": list}
    return HttpResponse(json.dumps(data))



def menzhen_report_layui(request):
    id = '110108201001102205'
    hospital='华山医院'
    keshi='皮肤科'
    reports = Zhenduan03.objects(id=id,hospital=hospital,keshi=keshi)
    context = {'reports': reports}
    return render(request, 'polls/layuiadmin/hulian/menzhen_report.html', context)







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


################3

def lisen_hang(request):
    return render(request, 'polls/layuiadmin/component/table/onrow.html')
    #formal version
    # return render(request, 'polls/layuiadmin/iframe_test/onrow.html')


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
        res.append(item)
    ###test print####
    # for item in res:
    #     print('打印item')
    #     print(item)
    data = { "code": 0,"msg": "ok","DataCount": dataCount,"data": res }
    return HttpResponse(json.dumps(data))





####################
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
    pid = request.POST.get('id')
    pname = request.POST.get('name')
    response_data = {
        "code": 0
        , "msg": ""
        , "data": {
        "src": "http://cdn.layui.com/123.jpg"
        }
    }
    # if type == 'zhenduan':
    #     reports = Zhenduan03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     return render(request, 'polls/03zhenduan_report_list.html', context)
    # elif type == 'jiance':
    #     reports = Jiance03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     return render(request, 'polls/03jiance_report_list.html', context)
    # elif type == 'zhuyuan':
    #     reports = Zhuyuan03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     return render(request, 'polls/03zhuyuan_report_list.html', context)
    # elif type == 'shoushu':
    #     reports = Shoushu03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     return render(request, 'polls/03shoushu_report_list.html', context)
    #
    # elif type == 'bingli':
    #     reports = Binglibaogao03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     # return render(request, 'polls/03bingli_report.html', context)
    #     return render(request, 'polls/03bingli_report_list.html', context)
    # elif type == 'chuyuan':
    #     reports = Chuyuan03.objects(name=pname, id=pid)
    #     context = {'reports': reports}
    #     return render(request, 'polls/03chuyuan_report_list.html', context)

    # return render(request, 'polls/test_ajax.html')
    return JsonResponse(response_data)


#
# @csrf_exempt
# def ajax_submit_set(request):
#     data = request.POST
#     print(data)
#     a = data.get('a')
#     b = data.get('b')
#     response_data = {}
#     response_data['result'] = 's'
#     response_data['message'] = a+b
#     return JsonResponse(response_data)
#


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

# def ajax_test2(request):
#     return render('polls/ajax_test2.html', {})
#
# def ajax_datatest(request):
#     if request.is_ajax():
#         message = "This is ajax"
#         print(message)
#     else:
#         message = "Not ajax"
#         print(message)
#     return HttpResponse(message)

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
# def open_index(request):
#     if request.user.is_authenticated == False:
#         return HttpResponseRedirect('/account/login/')
#     else:
#         navigation = NavigationProfile.objects.all()
#         dict = []
#
#         for nav in navigation:
#             dic = {}
#             id = nav.id
#             dic['id'] = nav.id
#             dic['text'] = nav.name
#             dic['url'] = nav.url
#             dic['iconCls'] = nav.iconCls
#             dic['nid'] = 0
#             sub_navigation = NavigationSubProfile.objects.filter(parent_id=id)
#
#             sub_dict = []
#             for sub_nav in sub_navigation:
#                 sub_dic = {}
#                 sub_dic['id'] = sub_nav.id
#                 sub_dic['text'] = sub_nav.name
#                 sub_dic['url'] = sub_nav.url
#                 sub_dic['iconCls'] = sub_nav.iconCls
#                 sub_dic['nid'] = sub_nav.parent_id
#                 sub_dict.append(sub_dic)
#
#             dic["children"] = sub_dict
#             dict.append(dic)
#             return render(request,'index.html',{'dict':dict})