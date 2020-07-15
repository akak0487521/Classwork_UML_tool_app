import json
 
# Python 字典类型转换为 JSON 对象
with open("./testData.json",'r') as load_f1:
        data0 = json.load(load_f1)
'''
for i in range(len(data1['name']))
json_str = json.dumps(data1)

print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data1['attributes']: ", data1['attributes'])
print ("data1['operations']: ", data1['operations'])
'''
json_str = json.dumps(data0)
data1 = json.loads(json_str)
print ("Class name: ", data1['name'])
json_str2 = json.dumps(data0['attributes'])
json_str3 = json.dumps(data0['operations'])
data2 = json.loads(json_str2)
data3 = json.loads(json_str3)
for i in range(len(data2)):
    print ("\tAttribute name: ", data2[i]['name'])
for i in range(len(data3)):
    print ("\tOperation name: ", end = " ")
    if data3[i].__contains__('parameters'):
        print(data3[i]['name'], end = " ")
        parameters_count = len(data3[i]['parameters'])
        '''print(parameters_count)'''
        print(" (", end = " ")
        for j in range(parameters_count):
            if j < parameters_count - 1:
                print(data3[i]['parameters'][j]['name'],end = ", "),
            else: print (data3[i]['parameters'][j]['name'], end = "")
        print (")")
    else: print(data3[i]['name'])
'''for i in range(len(data3)):
    json_str4 = json.dumps(data3[i])
    print("JSON 对象：", json_str4)
    print("/n" , type(json_str4))
    data4 = json.loads(json_str4)
    print("/n" , type(data4))
    print("/nValue: ", data4.__contains__('parameters'))
    if data4.__contains__('parameters'):
        for j in range(len(json_str4)):
            json_str5 = json.dumps(data4[j])
            print("/n" , type(json_str5))
            data5 = json.loads(json_str5)
            print("/n" , type(data5))
    if data3[i].__contains__('parameters'):
        print ("Operation name: ", data3[i]['name'])
        json_str5 = json.dumps(data3['parameters'])
        data5 = json.loads(json_str5)
        for j in range(len(data3[i]['parameters'])):
            print(data3[i][j]['name'])
    else: print ("Operation name: ", data3[i]['name'])'''