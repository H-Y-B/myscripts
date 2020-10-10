# -*- coding: UTF-8 -*-
from optparse import OptionParser



#构造OptionParser的对象
optParser = OptionParser()

#往OptionParser对象中增加option
optParser.add_option('-f','--file' , action = 'store'      ,type = "string" ,dest ='filename'                                                   )
optParser.add_option("-v","--vison", action = "store_false",                 dest ="verbose", default='hello',help="make lots of noise [default]")

#option = Option(action="store", type="string", dest, default, nargs=1, choices, 
#                help, metavar, const, callback, callback_args, callback_kwargs)
#
#action:  "store"       需要输入
#         "store_false" 存在，verbose': False 
#         "store_true " 存在，verbose': True 
#
#type：   "int"
#         "string"
#         "float"
#
#default: True/False
#         "intermediate"
#
#choices: 限制用户的输入。choices是一个字符串的列表，包含所有用户能用的输入。如提供choices=[‘1’,‘2’,‘3’]，那么用户只能输入1,2,3中的一个，如果不符，会抛出异常。
#

#optParser.parse_args() 剖析并返回一个字典和列表，
#字典中的关键字是我们所有的add_option()函数中的dest参数值，
#而对应的value值，是add_option()函数中的default的参数或者是
#由用户传入optParser.parse_args()的参数
fakeArgs = ['-f','file.txt','-v','how are you', 'arg1', 'arg2']


#默认
option , args = optParser.parse_args()
#输入
op , ar       = optParser.parse_args(fakeArgs)

print("option : ",option)
print("args : ",args)
print("op : ",op)
print("ar : ",ar)