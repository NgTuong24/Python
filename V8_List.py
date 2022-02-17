'''
# List comprehentions

# new_list[<action> for <item> in <interator> if <some condition>]
word = "hello word"
print([char for char in word])

number = [i for i in range(0,10) if i % 2 == 0]
print(number)

transactions = [100, 200, 300, 150, 80]
Tax_Rate  = 0.08
Service_charge = 0.07
def get_price_tax_service(bill):
    return bill*(1 + Tax_Rate + Service_charge)
# print(get_price_tax_service(100))
final_prices = [get_price_tax_service(bill) for bill in transactions]
print(final_prices)

# advanced functions

my_strings = 'Welcome to my code'
list_of_chars = list(my_strings)
print(list_of_chars)

# zip()     lặp 2 list cùng nhau
wizards = ['Harry Potter', 'Ron', 'Herminone']
pets = ['Hedwig', 'Scabber', 'Crookshank']

# for wiz, pet in zip(wizards, pets):
#     print(f"{wiz} has {pet}")
# print(list(zip(wizards, pets)))

for index, (wiz, pet) in enumerate(zip(wizards, pets), 1):
    print(f"{index}. {wiz} has {pet}")

sorted_by_first = sorted(['hi', 'hello', 'you', 'say'], key=lambda el: el[1])
print(sorted_by_first)

sorted_by_key = sorted([{'name': 'codexplore', 'age': 15}, {'name': 'andy',
                        'age': 18}, {'name': 'zoe', 'age': 55}]
                       ,key=lambda el: el['name'])
print(sorted_by_key)
'''

# mang 2 chieu

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# print(matrix[1][2])
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col])
list_converted = [matrix[row][col]
                    for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)
# zip() and *
print([x for x in zip(*matrix)])