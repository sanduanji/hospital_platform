import csv
import pandas as pd

from pymongo import MongoClient
adata=[]
file_path = '/Users/saber/Downloads/result.csv'
mongo_client = MongoClient(host='127.0.0.1', port=27017)
mongo_db = mongo_client["hulian"]
mongo_col =mongo_db["jiegouhua"]

mongo_col2 = mongo_db['jiekou_new']
def in_django():

    with open(file_path) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            adata.append(row)
            print(row)



def pd_csv():
    csv_data = pd.read_csv(file_path)
    # print(csv_data.shape)
    df = pd.DataFrame(csv_data)
    for i in range(len(df)):
        # bingli_report = {}
        # if i==0:
        #     continue
        bingli_id = df.iat[i, 0]
        name = df.iat[i, 1]
        gender = df.iat[i, 2]
        age = df.iat[i,3]
        age = int(age)
        songjian_date = df.iat[i,4]
        zhuyuanhao = df.iat[i,8]
        zhuyuanhao = int(zhuyuanhao)
        biaoben_type = df.iat[i,12]
        zhongliu_location = df.iat[i,13]
        chuankong = df.iat[i,15]
        ximo = df.iat[i,16]
        qiechu_length = df.iat[i,17]
        print(bingli_id)
        print(type(bingli_id))
        print(name)
        print(type(name))
        print(gender)
        print(type(gender))
        print(age)
        print(type(age))
        print(songjian_date)
        print(type(songjian_date))
        print(zhuyuanhao)
        print(type(zhuyuanhao))
        print(biaoben_type)
        print(type(biaoben_type))
        print(zhongliu_location)
        print(type(zhongliu_location))
        print(chuankong)
        print(type(chuankong))
        print(ximo)
        print(type(ximo))
        print(qiechu_length)
        print(type(qiechu_length))
        bingli_report={"bingli_id":bingli_id,"name":name, "gender":gender,"age":age, "songjian_date":songjian_date,
                       "zhuyuanhao":zhuyuanhao, "biaoben_type":biaoben_type,"zhongliu_location":zhongliu_location,
                       "chuankong":chuankong,"ximo":ximo,"qiuchu_length":qiechu_length}
        print(bingli_report)
        x = mongo_col.insert_one(bingli_report)
        print(x)

    slice = df[2:3]
    print(slice)
    bid = df.iat[2,0]
    name = df.iat[2,1]
    gender = df.iat[2,2]
    age = df.iat[2,3]

    print(gender)
    # for i in range(len(df)):
    #     document = df[i:i+1]
    #     print(document, '\n')

# pd_csv()


#填写数据库医院注册信息
def jiekou_mongo():
    jiekou1 = {"name":"张少少", "hospital":"复旦大学附属华山医院","keshi":"皮肤科","address":"http://10.176.38.224:5000/huashan/hospital/<idcard>","system_name":"病历管理系统","phone":"13487456743",
               "email":"12312312@fudan.edu.cn","use":"医院诊疗参考","gongneng":"获取病人在华山医院的病历信息","beizhu":"无"}

    jiekou2 = {"name":"王明", "hospital":"复旦大学附属肿瘤医院","keshi":"内科","address":"http://10.136.42.219:8000/zhongliu/hospital/<idcard>","system_name":"患者个人信息系统","phone":"16732879021",
               "email":"345253442342@fudan.edu.cn","use":"数据分析","gongneng":"获取病人在肿瘤医院的检验报告，idcard为身份证号","beizhu":"无"}
    jiekou3 = {"name":"钟良", "hospital":"复旦大学附属华山医院","keshi":"神经内科","address":"http://10.176.39.224:3000/huashan/hospital/<idcard>","system_name":"神经内科病历系统","phone":"19832647823",
               "email":"5437456375@fudan.edu.cn","use":"科研","gongneng":"获取华山医院神经科室的所有病历信息","beizhu":"无"}
    x = mongo_col2.insert_one(jiekou1)
    x = mongo_col2.insert_one(jiekou2)
    x = mongo_col2.insert_one(jiekou3)

# in_django()

jiekou_mongo()
