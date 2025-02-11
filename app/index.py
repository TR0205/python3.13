word = 'python'

print(word)
print(word[0])
print(word[-1])
print(word[:3]) # pyt 012 コロンの右側に値がある場合、値を含めずに左側の要素を出力する
print(word[3:]) # hon 345 コロンの左側に値がある場合、値も含めて出力する
print(word[2:4]) # th 23 コロンの左側の値から始まり、コロンの右側の値を含めないところまでを出力

# ythoを出力
print(word[1:5])

# onを出力
print(word[4:])

# コレはエラー
# word[0] = 'j'
# 結合する方法
# word = 'j' + word[1:]
# print(word)

# print(len(word))

# 最初の要素から２つ飛ばしで出力
print(word[::2])
# こっちは2:と変わらない・・・よくわからん
print(word[2::])

# 要素を逆順で出力する。結構使いそう？
print(word[::-1])
