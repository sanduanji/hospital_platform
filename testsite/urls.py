"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.urls import re_path

from polls import views as pviews

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    # url(r'^polls/', include('polls.urls', namespace='polls')),
    re_path('download/(?P<id>\d+)', pviews.file_down, name="download"),

    path('admin/', admin.site.urls),
    # path('home', views.Home,x name='Home'),
    url(r'^home',pviews.Home),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    path('search_patient/', pviews.search_patient),
    path('search_content/', pviews.search_content),
    path('search_report/', pviews.search_report),
    path('insert_hospital/', pviews.insert_hospital),#注册医院
    path('get_hospital/', pviews.get_hospital),
    path('search_reportlist/', pviews.search_reportlist),
    path('search_single_report/', pviews.search_single_report),

    #######03以病人为中心
    path('patient_list/', pviews.test_patientlist),
    path('test_searchrepolist/', pviews.test_patientreport),
    #显示各个类别表单#
    path('zhenduan_report/', pviews.zhenduan_repo),
    path('jiance_report/',pviews.jiance_repo),
    path('zhuyuan_report/',pviews.zhuayuan_repo),
    path('shoushu_report/', pviews.shoushu_repo),
    path('bingli_report/', pviews.bingli_repo),
    path('chuyuan_report/', pviews.chuyuan_repo),
    path('person_info/', pviews.person_info),
    ##显示所有
    path('report_type/', pviews.repo_types),
    ##layui admin test####
    ###mongodb 对接layui表格接口######
    path('reportlist_layui/', pviews.reportlist_layui),
    path('search_layui/', pviews.search_layui),
    path('search_patient_reports_layui/', pviews.search_patient_reports_layui),
    ####mongodb 对接结构化
    path('jiegouhua_database/', pviews.jiegouhua_database),
    path('search_jiegouhua/', pviews.search_jiegouhua),
    #接受id
    # path('patient_reports_layui/', pviews.patient_reports_layui),
    #接受上传数据
    # 执行上传数据接受
    path('get_layuifile/', pviews.get_layuifile, name='get_layuifile'),
    # 查看已注册接口信息
    path('data_jiekou_layui/', pviews.jiekou_data_layui, name='data_jiekou_layui'),
    #插入新注册信息
    path('get_zhuce/', pviews.get_zhuce, name='get_zhuce'),
    # url(r'^get_zhuce/$', pviews.get_zhuce),
    #用户搜索记录
    path('user_search/',pviews.user_search, name = 'user_search'),

    #显示图片
    # url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/Users/saber/Downloads/testsite/static'}),
    # path('ajax_submit_set/', pviews.ajax_submit_set),

]