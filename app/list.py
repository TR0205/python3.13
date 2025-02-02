word = "Python"

print(word[0]) # P(一番最初)
print(word[-1]) # n(一番最後)
print(word[0:2]) # Py(一番最初から2文字目まで)
print(word[2:4]) # Py(3番目から3文字目まで)
print(word[:4]) # Py(一番最初から4文字目まで)
print(word[2:]) # Py(3番目から最後まで)

"""
インデックス指定の文字列入れ替えはできない。
"""
# 以下はエラー
# word[0] = 2
# print(word)

# 文字列結合をする必要がある
word = "p" + word[1:]
print(word)
