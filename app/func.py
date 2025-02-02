def calc(a: int, b: int) -> int:
    return a + b

print(calc('a', 'b'))

# 位置引数のタプル化
# 位置引数：関数に渡す引数の順序を守る場合
def say(*args):
    # print(args) # ('hihi', 'fofo', 'ququ') タプル
    for v in args:
        print(v)

say('hihi', 'fofo', 'ququ')

# キーワード引数の辞書化
def menu(**kwargs):
    print('menu kwargs', kwargs) # menu= {'entree': 'beef', 'drink': 'ice coffee'} 辞書で取得される
    # for k, v in kwargs.items():
    #     print(k, v)

menu(entree='beef', drink='ice coffee')

# 辞書にしてから渡すことも可能
# printの結果は同じ
d = {
    'entree': 'beef',
    'drink': 'ice coffee'
}
menu(**d)

# デコレータ
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        r = func(*args, **kwargs)
        print('end')

        return r
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(2,4)
print(r)
# r = print_info(add_num)
# print(r(2, 4))

