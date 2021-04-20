import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["testsame"]


def ins():
    mydict = {'手术方式为直肠前切1，miles2，Hartmann': 3, 'J住院号': 220212, 'J姓名': '沈美娥', 'J年龄': 73, 'J性别': '女',
              '联系号码': ' ', '术后病理': {'病理号': '2007-00354', '病理检查时间': '2007-01-16', '肉眼所见': '',
                                    '病理诊断': '（直肠）溃疡型管状腺癌，中分化，癌肿大小2x3x0.8cm。肿瘤浸润肠壁全层及周围纤维脂肪组织。脉管内查见癌栓，神经束膜周围见癌累犯。标本上、下切缘未见癌累犯。系膜侧见癌结节4枚，肿物旁淋巴结（2/3）、肿物上淋巴结（1/6）查见癌转移。另送（右盆腔淋巴结）为癌结节。'}}

    x = mycol.insert_one(mydict)
    print(x)
    print(x)



ins()