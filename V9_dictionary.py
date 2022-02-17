# my_dict = {'name': 'codexplore',
#            'content': 'programming youtube channel', 'city': 'singapore'}
# print(my_dict)
#
# my_dict2 = dict(name = 'codexplore', content = 'program', city = 'singapore')
# print(my_dict2)
#
# # access items
# content_in_dict = my_dict["content"]
# print(content_in_dict)

# try:
#     print(my_dict['age'])
# except KeyError:
#     print("No key found")
#
# add and change items
# add a new key
my_dict = {'name': 'codexplore',
           'content': 'programming youtube channel', 'city': 'singapore'}
my_dict['email'] = 'codexplore@gmail.com'
print(my_dict)
my_dict['email'] = 'code@gmail'
print(my_dict)
'''
# delete a key-value
del LIST[<key>]
LIST.pop(<key>)
    .popitem()      xoa gtri cuoi cung
'''
del my_dict['city']
print(my_dict)
my_dict.popitem()
print(my_dict)

'''
loop over keys
'''
for key in my_dict:
    print(key, my_dict[key])
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
