#関数の勉強
def say_hello():
    print('kazui')

#引数
def say_name(name):
    print('hello, {name}'.format(name = name))

#複数の引数
def add_num(a, b):
    print(a + b)
add_num(5, 2)

def mainasu_num(a, b):
    print(a - b)
mainasu_num(8, 1)

def kakeru_num(a, b):
    print(a * b)
kakeru_num(4, 7)

def waru_num(a, b):
    print(a / b)
waru_num(6, 2)