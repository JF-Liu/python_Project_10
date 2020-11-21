"""
data update to mongodb ip@username
view admin_mongodb

"""



import pymongo
import json


#建立連線
myclient = pymongo.MongoClient('mongodb://Admin:nimdA@192.168.1.113:13896')

#檢查database
dblist = myclient.list_database_names()

#1 --> 存在  0 -->不在
if "project_test" in dblist:
    print("1")
else:
    print("0")







# 檢查collection
#連線的database
mydb = myclient["project_test"]
collist = mydb.list_collection_names()

# 1 --> 存在  0 -->不在
if "test" in collist:
    print("1")
else:
    print("0")

str1 = open('./interior_talk_05_ta/【TV】狹長格局暢行無阻！大人小孩都圈粉的低奢莫蘭迪.json', 'r', encoding='utf-8-sig').read()
data = []
data.extend(json.load())
collist.insert_one(data)

    # output = json.load(f)

print("output")


#
# def updateMongo():
#     #讀取csv
#     df_mongo = pd.read_csv('./104ForMongo.csv',index_col=0) #不抓index
#
#     #開始更新Mongo
#     myclient = MongoClient("mongodb://localhost:27017/")
#     mydb = myclient['104skill']
#     collection = mydb["collection"]   # SQL: Table Name
#     records = df_mongo.to_dict('records') # 參數 record 代表把列轉成個別物件
#     print(records)
#     collection.insert_many(records)
#
# #檢查盪案是否存在
# if processing_mode == 'U':
#     #已存在檔案, 更新DB
#     updateMySql()
#     updateMongo()
# else: #缺少檔案 , 重新讀取json檔案
#     get_data()








