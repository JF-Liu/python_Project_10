import json, re
import pandas as pd
from os import listdir


path = 'D:/pytel_data/interior_talk'
filelist = listdir(path)
fileIndex = []
for i in range(1, len(filelist)+1):
    index = i
    fileIndex.append(int(index))

data_homedata = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig')  as f:
        data = f.read()
        json_data = json.loads(data)
        print(fileName)
        # new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know'])
        # + json_data['colour'] + json_data['title'] + json_data['summary']
        homeData = onlyText(''.join(json_data['home_data']))
        dateData = onlyText(''.join(json_data['date']))
        titelData = onlyText(''.join(json_data['title']))
        textData = onlyText(json_data['內文'])


        remix = [fileName.replace(".json", ""), titelData, dateData, homeData, textData]
        data_homedata.append(remix)

df_homedata = pd.DataFrame(data_homedata, columns=['fileName', 'titel', 'date', 'homeData','內文'])
# df_homedata.index = df_homedata.index + 1
print(df_homedata)

#匯出csv 用excel (encoding='utf-8-sig')
df_homedata.to_csv(r'D:/pytel_data/excel/Forum_all.csv', encoding='utf-8-sig')