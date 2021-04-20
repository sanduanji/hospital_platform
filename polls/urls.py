from django.urls import path,re_path

from . import views

urlpatterns = [path('', views.index, name='index'),]




from django.urls import path
from django.urls import include, path

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # path('polls/', include('polls.urls')),
        # url(r'^polls/', include('polls.urls', namespace='polls')),

        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('home', views.Home, name='Home'),
        path('hello/', views.testhellow, name='hello'),

        path('bingrenxinxi', views.bingren_xinxi, name='bingren_xinxi'),
        path('loadmodel', views.zhuyuan_xinxi, name='zhuyuan_xinxi'),
        path('jianyan_baogao', views.jianyan_baogao, name='jianyan_baogao'),

        path('detecperson', views.detecperson, name='detecperson'),
        path('view_dataset', views.view_dataset, name='view_dataset'),
        path('bingli_baogao', views.bingli_baogao, name='bingli_baogao'),
        path('sign_up', views.sign_up, name='sign_up'),
        path('sign_im', views.sign_in, name='sign_in'),
        path('contact', views.contact, name='contact'),
        path('view_output', views.view_output, name='view_output'),

        ###hospital
        path('hospital_zhuce',views.yiyuan_zhuce, name='hospital_zhuce'),
        path('jieru_list', views.jieru_list, name = 'jieru_list'),
        path('show_patient', views.show_patient, name = 'show_patient'),

        path('view_patient', views.getname, name='view_patient'),
        path('view_report', views.getreport, name='view_report'),
        path('view_content', views.getcontent, name='view_content'),
        path('view_reportlist', views.getreport_list, name='view_reportlist'),

        ###各类报告显示页面
        # path('zhenduan_repo', views.zhenduan_repo, name = 'zhenduan_repo'),
        # path('jiance_repo', views.jiance_repo, name = 'jiance_repo'),
        # path('zhuyuan_repo', views.zhuayuan_repo, name = 'zhuyuan_repo'),
        # path('shoushu_repo', views.shoushu_repo, name = 'shoushu_repo'),
        # path('bingli_repo', views.bingli_repo, name = 'bingli_repo'),
        # path('chuyuan_repo', views.chuyuan_repo, name = 'chuyuan_repo'),
        # path('repo_type', views.repo_types, name = 'repo_type'),
        #个人信息路径
        # path('person_info', views.person_info, name = 'person_info'),
        path('denglu', views.denglu, name = 'denglu'),
        path('layuitest', views.testlayui, name='layuitest'),
        path('layui_tabletest', views.tabeltest, name='layui_tabletest'),
        ######0328测试
        # path('get-navigationProfile/',views.get_navigationProfile,name='get_navigationProfile'),

        # path('home', views.Home, name='Home'),
        ## layui admin 样例界面
        path('hulian_console/', views.hulian_console),
        path('layuiad_home1/', views.layuiad_home1),
        path('layuiad_home2/', views.layuiad_home2),
        path('layuiad_list/', views.layuiad_list),
        path('layuiad_reload/', views.layuiad_reload),
        #进入单个病人的多个报告列表
        path('patient_reports_layui/', views.patient_reports_layui),
        path('menzhen_report_layui/', views.menzhen_report_layui),
    #   user info
        path('userinfo_layui/', views.userinfo_layui),
        path('denglu_layui/', views.denglu_layui),
        path('webusers_layui/', views.webusers_layui),
        path('webadmins_layui/', views.webadmins_layui),
        path('webroles_layui/', views.webroles_layui),
        path('passswd_layui/', views.passswd_layui),
        path('message_layui/', views.message_layui),
        path('listen_hang/', views.lisen_hang, name = 'listen_hang'),
        path('quanduan_fuza/', views.quanduan_fuza),
        path('test_tabs/', views.test_tabs),
        path('report_intab/', views.report_intab),

        #接收选择病人
        path('patient_submit_set/', views.patient_submit_set, name = 'patient_submit_set'),
        ##测试ajax
        path('ajax_submit_set/', views.ajax_submit_set, name='ajax_submit_set'),
        path('ajax_index/', views.ajax_index),
        path('cal/', views.cal),
        #iframe报告显示
        path('jizhen_report/', views.jizhen_report, name = 'jizhen_report'),
        path('shoushu_report/', views.shoushu_report, name = 'shoushu_report'),
        path('fangshe_report/', views.fangshe_report, name = 'fangshe_report'),
        path('yaofang_report/', views.yaofang_report, name = 'yaofang_report'),


        #显示结构化结果
        path('show_jiegouhua/', views.show_jiegouhua, name='show_jiegouhua'),
        #上传未结构化数据页面
        path('upload_unjiegou/', views.upload_unjiegou, name = 'upload_unjiegou'),
        #注册接口
        path('zhuce_jiekou/', views.zhuce_jiekou, name = 'zhuce_jiekou'),
        #查看已注册接口layui
        path('view_jiekoulist/', views.view_jiekoulist, name = 'view_jiekoulist'),
        #显示接口图片
        path('visual_jiegouhua/', views.visual_jiegouhua, name = 'visual_jiegouhua'),
        #用户登录显示界面
        path('user_home/', views.user_home, name = 'user_home'),
        #用户搜索没有相关记录
        path('user_search_none/', views.user_search_none, name = 'user_search_none'),

        # url(r'^$', 'polls.views.ajax_test2', name='ajax_test2'),
        # url(r'^ajax_test/$', 'polls.views.ajax_datatest', name='ajax_datatest'),
        ######iframe test#####3for
        path('iframe_test/', views.iframe_test, name = 'iframe_test'),
        path('iframe_page/', views.iframe_page, name='iframe_page'),
        #测试分页
        path('test_fenye/', views.test_fenye, name='test_fenye'),

]
