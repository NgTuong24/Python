var_bool = True
# [] bool
print(type(var_bool))
a = 4 + True
print(a)

b = False
if b == 0:
    print("B is 0")

# [] None
var_none = None
print(type(var_none))

# email_address = None
email_address = "codexplore@gmail.com"
if email_address:
    print(f"Email address is {email_address}")
else:
    print(f"Email address is empty or {email_address}")

# Number (int & float)
print(type(10))
print(type(0))
print(type(-10))
print(type(0.0))
print(type(2.3))
print(type(4E2), 4E2)  #4*(10^2)

# phep toan + - * / ** // %
print(10+3)
print(10-3)
print(10**3)
print(10//3)
print(10%3)

# ham co ban
print(pow(10,3))
print(abs(-6.9))
print(round(1.6664, 2))
print(bin(512))
print(hex(512))