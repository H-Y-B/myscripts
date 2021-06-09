import json
 
# 将类文件对象中的JSON字符串直接转换成 Python 字典
with open('pengjunlee.json', 'r', encoding='utf-8') as f:
    ret_dic = json.load(f)
    print(ret_dic['name']) 
    print(ret_dic['age']) 
    print(ret_dic['address']['city']) 
    print(ret_dic['list'][0]['name']) 
