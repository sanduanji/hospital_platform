from pymongo import MongoClient
#连接mongodb
connect = MongoClient('localhost')
#连接库
db = connect.hulian
#连接集合
emp = db.bingren

#读取内容
#1.查询所有
cursor = emp.find()
for each in cursor:
    print(each)
'''
#2.条件查询
cursor1 = emp.find({'name':'李四'})
print(list(cursor1)[1])

for each in cursor1:
    print(each)

for i,v in enumerate(cursor1):
    print(i+1,v,sep='条是：')
#3多条件查询
corsor2 = emp.find(
    {'name':{
        '$in':['张三','李四']
        }
    }
)
for echo in corsor2:
    print(echo)
#4.and
cursor3 = emp.find({
    'name':{'$in':['张三','李四']},
    'age':30
})
for echo in cursor3:
    print(echo)
#5or
cursor4 = emp.find({
    '$or':[
        {'name':{'$in':['张三','李四']}},
        {'age':{'$lt':25}}
    ]
})
for echo in cursor4:
    print(echo)
#6子条件
cursor5 = emp.find({
    'contect.email':'abc@qq.com'
})
for echo in cursor5:
    print(echo)

'''