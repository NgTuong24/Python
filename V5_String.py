# String
my_string = 'I\'m a "Cuc Du Hoc Sinh Singapore"'
my_string = "I'm living in \"Singapore\""
print(type(my_string))
print(my_string)

# backslash if you want to continue in the next line
my_string = "voi mong muon tao nen mot flatform \
chia se nhung kien thuc ve Laptrinh"
print(my_string)

my_string = "Hello World"
char = my_string[0]
charr = my_string[-1]
print(charr)

# my_string[0] = "M" -> FALSE

print(my_string[0:7]) #Hello W
print(my_string[:5])

# reverse string[::-1]
print(my_string[::-1])

'''
concat strings with +
nối chuỗi
'''

greeting = 'Hello'
channel = 'codexplore'
sentence = greeting + " Chao mung cac ban den voi channel cua " + channel
# .join()
my_list = ['How', 'are', 'you','doing']
sentence = '-'.join(my_list)
#
my_string = "xin chao cac ban"
# for char in my_string:
#     print(char)

if "r" in my_string:
    print("yes")
else:
    print("no")
# .strip()
print("  I am alone  ".strip())
print("ohelloo".strip("o"))
# .split()
print("heloo cac ban".split())
# replace()
print("hello world".replace('hello', 'xin chao'))
# startswith(), endswith()
my_string = "and cook rice"
print(my_string.startswith('a'))
print(my_string.endswith('ce'))
# index()
print(my_string.index('k'))
print(my_string.find('k'))

'''
.upper() IN Hoa
.lower() IN thuong
.title() in hoa chu cai dau moi tu
.capitalize() in hoa chu cai dau tien
.count() dem ki tu

'''

# String Formating   %, .format(), f-Strings
name = "codexplore"
sd = 26546.5654
my_string = "welcome to %s , %.2f" % (name, sd)
print(my_string )

#.format()
age = 24.0
height = 170.5
my_string = "I am {:.2f} years old; {:.3f} cm".format(age, height)
print(my_string)

# f-Strings
pi = 3.14159
name = 'code'
my_string = f"Pi is {pi:.2f} and name is {name}"
print(my_string)
