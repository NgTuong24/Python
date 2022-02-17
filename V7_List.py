list_1 = ["banana", "apple", "orange", "cherry"]
list_2 = [5, "code", False, None]
#print(list_2)

# len()
print(len(list_2))
# index()
print(list_2.index('code')) # > 1
# count()
my_list = [1, 2, 3, 3, 3, 4, 3]
print(my_list.count(3))

# for item in my_list:
#     print(item, end=" ")


# enumerate function
presidents = ["washington", "Adams", "Jefferson"
             "Madison", "Jackson"]
for index, president in enumerate(presidents, start=1):
    print(f"President #{index}: {president}")

# Slicing cắt
# List[start : end : step]
my_list = [1, 2, 3, '5']
# print(my_list[:2])
# print(my_list[-1])
# print(my_list[::-1])
my_list2 = my_list*2
my_list2.append(2)
my_list2.extend([2,3,4,5])
print(my_list2)

# .insert(index, value)
my_list = [1, 2, 3, 4]
my_list.insert(2, 'c')
del my_list[1]
print(my_list)
'''
remove from list
'''
#   List.pop() xoa ptu cuoi
#       .pop(index)
#       .remove(value) xoa gia tri dau tien trong list
#       del List[index]

'''
    sorting
        .sort()
        .sort(reverse = True)
        .reverse()
        sorted(List)
        reversed(List)
'''
my_list = [1, 2, 8, 5, 7, 6]
print(sorted(my_list))
print(list(reversed(my_list)))
print(my_list)

# max(list)
# sum(list)

