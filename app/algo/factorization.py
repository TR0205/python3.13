"""
実行方法

同じディレクトリにinput.txtファイルを置き、標準入力用の数値を書く

cat input.txt | python factorization.py 

"""

# TODO: 間違っているので直す

# n = int(input())
n = 64

r = []
for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        r.append(i)
        n /= i
if n > 1:
    r.append(n)

r_str = map(str, r)
print(' '.join(r_str))
