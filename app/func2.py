t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

# r = []
# for i in t:
#     r.append(i)

# print(r)

# そのままリストへ入れる
r = [i for i in t]
# 二倍にしてリストへ入れる
r = [i * 2 for i in t]
# 条件追加
r = [i for i in t if i % 2 == 0]

# ２つループ
r = [i * j for i in t for j in t2]
print(r)