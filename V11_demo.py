# tham số bắt buộc & tham số mặc định
# def print_name(name, greeting = "Welcome"):
#     print(f"{name}, {greeting}")

# def codexplore(a, b, c):
#     print(a, b, c)

'''
*args
**kwargs
'''

def Example_1(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

def main():
    '''
    print_name("codexplore")
    print_name("codexplore", "xinChao")

    # Positional arguments: Biến vị trí
    codexplore(1, 2, 3)

    # Keyword arguments : Bien theo khoa
    codexplore(a = "hello_world", c = "c_value", b = 2)
    '''

    # *args ->list
    #Example_1('a', 'b', 'hello world',1 , 2, 3)

    # **kwargs ->dictionary
    Example_1('a', 'b', 'hello', 1, size = 'over', name = 'code')
if __name__ == "__main__":
    main()