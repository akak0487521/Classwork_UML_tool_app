import json
 
# Python 字典类型转换为 JSON 对象
with open("./testData2.json",'r') as load_f1:
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
Class_count = len(data0['Classes'])
'''print(Class_count)'''
for i in range(Class_count):
    json_str = json.dumps(data0['Classes'][i])
    data1 = json.loads(json_str)
    print ("Class name: ", data1['name'])
    if data1.__contains__('ownedElements'):
        json_str2 = json.dumps(data1['ownedElements'])
        data2 = json.loads(json_str2)
        for j in range(len(data2)):
            if data2[j]['_type'] == ('UMLGeneralization'):
                for k in range(Class_count):
                    searchedClassID = data0['Classes'][k].get('_id')
                    if data2[j]['target']['$ref'] == searchedClassID:
                        '''print ("\tGeneralization id: ", data2[j]['_id'])'''
                        print ("\tGeneralization: ", data1['name']," extends ", data0['Classes'][k].get('name'))
    json_str3 = json.dumps(data1['attributes'])
    json_str4 = json.dumps(data1['operations'])
    data3 = json.loads(json_str3)
    data4 = json.loads(json_str4)
    for j in range(len(data3)):
        if data3[j]['type'].__contains__('$ref'):
            for k in range(Class_count):
                if data3[j]['type']['$ref'] == data0['Classes'][k].get('_id'):
                    print ("\tAttribute: ", data0['Classes'][k].get('name'), " ", data3[j]['name'])
        else: print ("\tAttribute: ", data3[j]['type'], " ", data3[j]['name'])
    for j in range(len(data4)):
        print ("\tOperation: ", end = " ")
        if data4[j].__contains__('parameters'):
            print(data4[j]['name'], end = " ")
            parameters_count = len(data4[j]['parameters'])
            print(" (", end = " ")
            for k in range(parameters_count):
                if k < parameters_count - 1:
                    print(data4[j]['parameters'][k]['name'],end = ", "),
                else: print (data4[j]['parameters'][k]['name'], end = "")
            print (")")
        else: print(data4[j]['name'])
    
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