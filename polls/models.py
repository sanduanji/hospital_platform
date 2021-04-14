from django.db import models

# Create your models here.
import mongoengine
from django.db import models
from django import forms
from django.forms import fields,widgets
from mongoengine import connect
connect('hulian', host='111.231.88.241', port =27017, username='root', password= 'mongoadmin', authentication_source='admin')


class Patient(mongoengine.Document):
    _id = mongoengine.StringField()
    age = mongoengine.StringField()
    bingshichenshu = mongoengine.StringField()
    birthday = mongoengine.StringField()
    born = mongoengine.StringField()
    id = mongoengine.StringField()
    keshi = mongoengine.StringField()
    marry = mongoengine.StringField()
    medicine_history = mongoengine.StringField()
    name = mongoengine.StringField()
    profession = mongoengine.StringField()
    sex = mongoengine.StringField()
    zhusu = mongoengine.StringField()
    hospital = mongoengine.StringField()


    ###
    zhuzhi = mongoengine.StringField()
    patient_id = mongoengine.StringField()
    minzu = mongoengine.StringField()
    meta = {'collection':'bingren'}


#报告种类类别01

class ReportType(mongoengine.Document):
    _id = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    hospital = mongoengine.StringField()
    type = mongoengine.StringField()
    keshi = mongoengine.StringField()
    meta = {'collection':'report_type'}


#报告种类类别03，包含全部的


class ReportTypeList(mongoengine.Document):
    _id = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    zhenduan = mongoengine.StringField()
    jianyan = mongoengine.StringField()
    zhuyuan = mongoengine.StringField()
    zhiliao = mongoengine.StringField()
    gender = mongoengine.StringField()
    history = mongoengine.StringField()
    birth = mongoengine.StringField()
    birthday = mongoengine.StringField()
    age = mongoengine.StringField()
    # type = mongoengine.StringField()
    shebao = mongoengine.StringField()

    meta = {'collection':'report_type_list'}


#所有病人所有类型报告的简要信息汇总
class ReportList(mongoengine.Document):
    _id = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    shebao = mongoengine.StringField()
    hospital = mongoengine.StringField()
    report_id = mongoengine.StringField()
    age = mongoengine.StringField()
    report_type = mongoengine.StringField()
    report_date = mongoengine.StringField()
    gender = mongoengine.StringField()
    meta = {'collection':'report_list_04'}

#
class Report(mongoengine.Document):
    _id = mongoengine.StringField()
    caiyangtime = mongoengine.StringField()
    name = mongoengine.StringField()
    operator = mongoengine.StringField()
    report_id = mongoengine.StringField()
    report_type = mongoengine.StringField()
    reporttime = mongoengine.StringField()
    reportzhuangtai = mongoengine.StringField()
    shenhe = mongoengine.StringField()
    yijibumen  = mongoengine.StringField()

    # modify 0106
    id = mongoengine.StringField()
    keshi = mongoengine.StringField()
    hospital = mongoengine.StringField()
    report_name = mongoengine.StringField()
    meta = {'collection':'report'}

    # 诊断报告
class ZhenDuan_Report(mongoengine.Document):
    _id = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    patient_id = mongoengine.StringField()
    record_time = mongoengine.StringField()

    gender = mongoengine.StringField()
    age = mongoengine.StringField()
    minzu = mongoengine.StringField()
    profession = mongoengine.StringField()
    birth  = mongoengine.StringField()

    born = mongoengine.StringField()
    address = mongoengine.StringField()
    marry = mongoengine.StringField()
    bingshichenshu = mongoengine.StringField()

    medicine_history = mongoengine.StringField()
    zhusu = mongoengine.StringField()
    hospital = mongoengine.StringField()
    keshi = mongoengine.StringField()
    meta = {'collection':'zhenduan'}

#检验报告
class Content(mongoengine.Document):
    _id = mongoengine.StringField()
    age = mongoengine.StringField()
    beizhu = mongoengine.StringField()
    bianhao = mongoengine.StringField()
    biaobenbiaoshi = mongoengine.StringField()
    biaobenzhonglei = mongoengine.StringField()
    cankaofanwei = mongoengine.StringField()
    chuangwei = mongoengine.StringField()
    code = mongoengine.StringField()
    danwei = mongoengine.StringField()
    jieguo = mongoengine.StringField()
    keshi  = mongoengine.StringField()
    linchuangzhenduan = mongoengine.StringField()
    name = mongoengine.StringField()
    report_id = mongoengine.StringField()
    sex = mongoengine.StringField()
    songjian_doctor = mongoengine.StringField()
    xiangmu = mongoengine.StringField()

    #
    biaobenxingzhuang = mongoengine.StringField()
    huanzhe_id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    id = mongoengine.StringField()
    baogao_name = mongoengine.StringField()
    baogao_time = mongoengine.StringField()
    baogao_zhuangtai = mongoengine.StringField()
    caiyang_time = mongoengine.StringField()
    #操作员
    operator = mongoengine.StringField()
    #报告类型
    report_type = mongoengine.StringField()
    shenheren = mongoengine.StringField()
    yijibumen = mongoengine.StringField()


    meta = {'collection': 'content'}


class Jiekou(mongoengine.Document):
    _id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    data = mongoengine.StringField()
    ##新加科室+功能
    keshi = mongoengine.StringField()
    gongneng = mongoengine.StringField()
    username = mongoengine.StringField()
    userphone = mongoengine.StringField()
    meta = {'collection':'hospital_data'}


####################03更新数据库#######################

class Zhenduan03(mongoengine.Document):
    _id = mongoengine.StringField()
    name = mongoengine.StringField()
    hospital = mongoengine.StringField()
    id = mongoengine.StringField()
    menzhenhao = mongoengine.StringField()
    jilushijian = mongoengine.StringField()
    minzu = mongoengine.StringField()
    hunyin = mongoengine.StringField()
    zhiye = mongoengine.StringField()
    shengri = mongoengine.StringField()
    chushengdi = mongoengine.StringField()
    jiguandi = mongoengine.StringField()
    bingshichenshu = mongoengine.StringField()
    yongyaolishi = mongoengine.StringField()
    zhusu = mongoengine.StringField()
    tigejiancha = mongoengine.StringField()
    chubuzhenduan = mongoengine.StringField()
    chuli = mongoengine.StringField()
    age = mongoengine.StringField()
    keshi = mongoengine.StringField()
    gender = mongoengine.StringField()
    meta = {'collection':'zhenduan_vthree'}


class Zhuyuan03(mongoengine.Document):
    _id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    name  = mongoengine.StringField()
    id  = mongoengine.StringField()
    gender = mongoengine.StringField()
    minzu = mongoengine.StringField()
    birthday = mongoengine.StringField()
    chushengdi = mongoengine.StringField()
    hunyin = mongoengine.StringField()
    zhuzhi = mongoengine.StringField()
    zhiye = mongoengine.StringField()
    zhuyuanhao = mongoengine.StringField()
    keshi = mongoengine.StringField()
    bingshi = mongoengine.StringField()
    chuangwei = mongoengine.StringField()
    ruyuanriqi = mongoengine.StringField()
    caishiriqi = mongoengine.StringField()
    fangshehao = mongoengine.StringField()
    gongshuzhe = mongoengine.StringField()
    zhusu = mongoengine.StringField()
    bingqingmiaoshu = mongoengine.StringField()
    jibingshi = mongoengine.StringField()
    fabing = mongoengine.StringField()
    chuanran = mongoengine.StringField()
    meta = {'collection':'03zhuyuan'}

class Jiance03(mongoengine.Document):
    _id = mongoengine.StringField()
    keshi = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    report_id = mongoengine.StringField()
    report_time = mongoengine.StringField()
    gender = mongoengine.StringField()
    age = mongoengine.StringField()
    zhuyuanhao = mongoengine.StringField()
    chuangwei = mongoengine.StringField()
    songjiandoc = mongoengine.StringField()
    caozuoyuan = mongoengine.StringField()
    shenheren = mongoengine.StringField()
    yiji = mongoengine.StringField()
    biaobentype = mongoengine.StringField()
    biaobenbiaoshi = mongoengine.StringField()
    biaobenxingzhuang = mongoengine.StringField()
    xiangmu = mongoengine.StringField()
    code = mongoengine.StringField()
    range = mongoengine.StringField()
    jieguo = mongoengine.StringField()
    danwei = mongoengine.StringField()
    linchuang = mongoengine.StringField()
    beizhu = mongoengine.StringField()
    report_type = mongoengine.StringField()
    hospital = mongoengine.StringField()
    img = mongoengine.StringField()
    meta = {'collection':'03jiance'}


class Shoushu03(mongoengine.Document):
    _id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    zhuyuanhao = mongoengine.StringField()
    shoushubianhao = mongoengine.StringField()
    shoushuxingzhi = mongoengine.StringField()
    shoushumingcheng = mongoengine.StringField()
    shoushuyisheng = mongoengine.StringField()
    hushi = mongoengine.StringField()
    mazuiyisheng = mongoengine.StringField()
    mazuifangfa = mongoengine.StringField()
    bingzao = mongoengine.StringField()
    yuanfazhongliu = mongoengine.StringField()
    linba = mongoengine.StringField()
    zhuanyi = mongoengine.StringField()
    ganzhuanyi = mongoengine.StringField()
    qita = mongoengine.StringField()
    qiechufanwei = mongoengine.StringField()
    shoushuriqi = mongoengine.StringField()
    gender = mongoengine.StringField()
    age = mongoengine.StringField()

    meta = {'collection':'03shoushu'}


class Binglibaogao03(mongoengine.Document):
    _id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    name = mongoengine.StringField()
    id = mongoengine.StringField()
    gender = mongoengine.StringField()
    age = mongoengine.StringField()
    keshi = mongoengine.StringField()
    bingqu = mongoengine.StringField()
    chuangweihao = mongoengine.StringField()
    report_id = mongoengine.StringField()
    jianchariqi = mongoengine.StringField()
    binglibaogao = mongoengine.StringField()
    meta={'collection':'03binglibaogao'}

class Chuyuan03(mongoengine.Document):
    _id = mongoengine.StringField()
    hospital = mongoengine.StringField()
    name = mongoengine.StringField()
    id = mongoengine.StringField()
    zhuyuanhao = mongoengine.StringField()
    ruyuanzhenduanriqi = mongoengine.StringField()
    ruyuanzhenduan = mongoengine.StringField()
    ruyuanriqi = mongoengine.StringField()
    bingshi = mongoengine.StringField()
    bingli = mongoengine.StringField()
    huayan = mongoengine.StringField()
    shuqianzhenduan = mongoengine.StringField()
    hebingzheng = mongoengine.StringField()
    bingfa = mongoengine.StringField()
    bingchengxiaoguo = mongoengine.StringField()
    chuyuanriqi = mongoengine.StringField()
    chuyuanzhenduan = mongoengine.StringField()
    chuyuanqingkuang = mongoengine.StringField()
    huifu = mongoengine.StringField()

    meta = {'collection':'03chuyuan'}


class Patientinfo03(mongoengine.Document):
    _id = mongoengine.StringField()
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    gender = mongoengine.StringField()
    age  = mongoengine.StringField()
    birthday = mongoengine.StringField()
    minzu = mongoengine.StringField()
    hunyin = mongoengine.StringField()
    zhiye = mongoengine.StringField()
    chushengdi = mongoengine.StringField()
    jiguan = mongoengine.StringField()
    yongyaolishi = mongoengine.StringField()
    jiwangbingshi = mongoengine.StringField()
    guominshi = mongoengine.StringField()
    meta = {'collection':'03patientinfo'}
####结构化病理报告

class BingliJiegouhua(mongoengine.Document):
    _id = mongoengine.StringField()
    bingli_id = mongoengine.StringField()
    name = mongoengine.StringField()
    gender = mongoengine.StringField()
    age = mongoengine.StringField()
    songjian_date = mongoengine.StringField()
    zhuyuanhao = mongoengine.StringField()
    biaoben_type = mongoengine.StringField()
    zhongliu_location = mongoengine.StringField()
    chuankong = mongoengine.StringField()
    ximo = mongoengine.StringField()
    qiuchu_length = mongoengine.StringField()
    meta = {'collection':'jiegouhua'}

####layui医院接口查看

class Hospital_Jiekou_Layui(mongoengine.Document):
    _id = mongoengine.StringField()
    name = mongoengine.StringField()
    hospital = mongoengine.StringField()
    keshi = mongoengine.StringField()
    address = mongoengine.StringField()
    system_name = mongoengine.StringField()
    phone = mongoengine.StringField()
    email = mongoengine.StringField()
    use = mongoengine.StringField()
    gongneng = mongoengine.StringField()
    beizhu = mongoengine.StringField()
    meta = {'collection':'jiekou_new'}
#######################
# 节点类
# class NavigationProfile(models.Model):
#     name=models.CharField(max_length=20,verbose_name='节点名称')
#     url=models.CharField(max_length=50,verbose_name='链接地址')
#     iconCls=models.CharField(max_length=50,verbose_name='图标icon')
#
#     class Meta:
#         verbose_name='节点名称'
#         verbose_name_plural=verbose_name
#
#     def __str__(self):
#         return self.name
#
# # 子节点类
# class NavigationSubProfile(models.Model):
#     name=models.CharField(max_length=20,verbose_name='子节点名称')
#     url=models.CharField(max_length=50,verbose_name='链接地址')
#     iconCls=models.CharField(max_length=50,verbose_name='图标icon')
#     parent=models.ForeignKey(NavigationProfile,on_delete=models.CASCADE,verbose_name='父节点')
#
#     class Meta:
#         verbose_name='子节点名称'
#         verbose_name_plural=verbose_name
#
#     def __str__(self):
#         return self.name