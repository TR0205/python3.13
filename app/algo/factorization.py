"""
実行方法

同じディレクトリにinput.txtファイルを置き、標準入力用の数値を書く

cat input.txt | python factorization.py 

"""

# TODO: 間違っているので直す

n = int(input())

r = []
while n % 2 == 0:
    # print('n: {n}'.format(n=int(n)))
    
    r.append(2)
    n /= 2

# print('finished divied 2. n: {n}'.format(n=int(n)))
# print(r)
    
while n % 3 == 0:
    # print('n: {n}'.format(n=int(n)))

    r.append(3)
    n /= 3

# print('finished divied 3. n: {n}'.format(n=int(n)))
# print(r)

while n % 5 == 0:
    # print('n: {n}'.format(n=int(n)))

    r.append(5)
    n /= 5

# print('finished divied 5. n: {n}'.format(n=int(n)))
# print(r)

if n != 1:
    r.append(int(n))

# print('finished divied ALL. n: {n}'.format(n=int(n)))
# print(r)

# map()でリストの各要素をstringへ変換
# intのままだとjoin()で使用できない
str_list = list(map(str, r))
res = ' '.join(str_list)
print(res)

l = [1, 2, 3]
str_list = map(str, l)
res = ' '.join(str_list)
print(res)