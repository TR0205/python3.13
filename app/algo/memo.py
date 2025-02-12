# p.66 ビット全探索

n = 4
s = 7 # 本では16
l = [2, 5, 9, 7]

r = ''

# 2^3回ループ
# 1に左シフト演算を行うと2乗できる
# 1 << 1 = 2
# 1 << 2 = 4
# 1 << 3 = 8
# i: 0~7
for i in range(1 << n):
    total = 0
    # j: 1から始める。1~3
    for j in range(1, n+1):
        # if i & (2 ** (j-1)) != 0:
        # iと2^j-1の論理積
        # i番目で選ぶカードを判定できる
        if i & (1 << (j-1)) != 0:
            total += l[j-1]
    if s == total:
        r = 'Yes'
        i_n = i
        j_n = j
        break

if r:
    # print(r)
    print('result: {r}, i: {i_n}, j: {j_n}'.format(r=r, i_n=i_n, j_n=j_n))
else:
    print('No')
