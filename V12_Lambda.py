'''
ham an danh - Lambda
'''
'''

codexplore = lambda so : so + 69
def codexplore1(so):
    return so + 69
print(codexplore(1))   #->70
print(codexplore1(11)) #->80

'''

# codexplore = lambda x, y, z : x+y-z
# print(codexplore(6, 9, 10)) # ->5
'''
 ứng dụng vào sorted
'''
coordinate2D = [(6,9), (9,6), (-1,30), (2, 10)]
print(sorted(coordinate2D, key=lambda p:p[1]))

#
number = [5,3,-2,4,-1,-3,5,4]
print(sorted(number))
print(sorted(number,key=lambda x: abs(x)))

'''
# map()
'''

list_key = ["codexplore", "welcome", "cac ban"]
print(list(map(lambda x: x.title(), list_key)))
# ~
new_list = [keyword.title() for keyword in list_key]
print(new_list)

'''
# filter() tra ve tat ca gia tri neu dkien dung
'''
list_num = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2!=0, list_num)))
# ~
new_list = [x for x in list_num if x%2!=0]
print(new_list)

'''
# reduce(func, seq) tra ve 1 gia tri don
func takes 2 arguments
'''
from functools import  reduce
seq = [1,3,5,6,9,2,8]
# print(reduce(lambda a,b : a+b, seq)) # tinh tong list
print(reduce(lambda a,b: a if a > b else b, seq)) # tim gtri max


