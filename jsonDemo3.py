import json

# Python 字典类型转换为 JSON 对象
with open("./t2-10.json",'r') as load_f1:
        data0 = json.load(load_f1)

studentAnswer = []
tmpAnswer = ""
tmpClassAnswer = []

Class_count = len(data0['ownedElements'][0]['ownedElements'])

for i in range(1, Class_count):
    json_str = json.dumps(data0['ownedElements'][0]['ownedElements'][i])
    data1 = json.loads(json_str)
    tmpAnswer = "Class name:  " + data1['name']
    print (tmpAnswer)
    tmpClassAnswer.append(tmpAnswer)
    tmpAnswer = ""
    if data1.__contains__('ownedElements'):
        json_str2 = json.dumps(data1['ownedElements'])
        data2 = json.loads(json_str2)
        for j in range(len(data2)):
            if data2[j]['_type'] == ('UMLGeneralization'):
                for k in range(1, Class_count):
                    searchedClassID = data0['ownedElements'][0]['ownedElements'][k].get('_id')
                    if data2[j]['target']['$ref'] == searchedClassID:
                        '''print ("\tGeneralization id: ", data2[j]['_id'])'''
                        tmpAnswer =  "Generalization: " + data1['name'] + " extends " + data0['ownedElements'][0]['ownedElements'][k].get('name')
                        print ("\t" + tmpAnswer)
                        tmpClassAnswer.append(tmpAnswer)
                        tmpAnswer = ""
    json_str3 = json.dumps(data1['attributes'])
    json_str4 = json.dumps(data1['operations'])
    data3 = json.loads(json_str3)
    data4 = json.loads(json_str4)
    for j in range(len(data3)):
        if data3[j]['type'].__contains__('$ref'):
            for k in range(Class_count):
                if data3[j]['type']['$ref'] == data0['ownedElements'][0]['ownedElements'][k].get('_id'):
                    tmpAnswer = "Attribute:  " + data0['ownedElements'][0]['ownedElements'][k].get('name') + " " + data3[j]['name']
                    print ("\t" + tmpAnswer)
                    tmpClassAnswer.append(tmpAnswer)
                    tmpAnswer = ""
        else:
            tmpAnswer = "Attribute:  " + data3[j]['type'] + " " + data3[j]['name']
            print ("\t" + tmpAnswer)
            tmpClassAnswer.append(tmpAnswer)
            tmpAnswer = ""
    for j in range(len(data4)):
        tmpAnswer = ""
        tmpAnswer += "Operation:  "
        '''print ("\tOperation: ", end = "")'''
        if data4[j].__contains__('parameters'):
            tmpAnswer += data4[j]['name']
            '''print(data4[j]['name'], end = " ")'''
            parameters_count = len(data4[j]['parameters'])
            tmpAnswer += " ( "
            '''print(" (", end = " ")'''
            for k in range(parameters_count):
                if k < parameters_count - 1:
                    '''print(data4[j]['parameters'][k]['name'],end = ", ")'''
                    tmpAnswer += data4[j]['parameters'][k]['name'] + ", "
                else: 
                    '''print (data4[j]['parameters'][k]['name'], end = "")'''
                    tmpAnswer += data4[j]['parameters'][k]['name']
            '''print (")")'''
            tmpAnswer += ")"
            print ("\t" + tmpAnswer)
            tmpClassAnswer.append(tmpAnswer)
            tmpAnswer = ""
        else: 
            tmpAnswer += data4[j]['name']
            print("\t" + tmpAnswer)
            tmpClassAnswer.append(tmpAnswer)
            tmpAnswer = ""
    studentAnswer.append(tmpClassAnswer)
    tmpClassAnswer = []
    for i in range(len(studentAnswer)):
        print(studentAnswer[i])
    
