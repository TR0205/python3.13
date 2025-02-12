# 約数を全て出力

n = 100

d = []

# n**0.5はnの0.5乗を表す、つまり√nになる
# 0.5をかけることでfloat型となるため、int型でキャストしている
# range(1, int(100**0.5)) -> 1から9まで
# range(1, int(100**0.5)+1) -> 1から10まで
for i in range(1, int(n**0.5)+1):
    # 割り切れない場合は約数でないためスキップ
    if n % i != 0:
        continue
    # 存在している場合は追加しない
    if i not in d:
        d.append(i)
    # 存在している場合は追加しない
    if int(n / i) not in d:
        d.append(int(n / i))

d.sort()
print(d)