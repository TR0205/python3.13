word = 'python'

print(word)
print(word[0])
print(word[-1])
print(word[:3]) # pyt 012 コロンよりも左側の要素を出力する
print(word[3:]) # hon 345 右側にコロンがある場合はその値も含めて出力する
print(word[2:4]) # th コロンの両側に要素がある場合、コロンの右(:3とか)の方が優位に働く
# コロンの右側に要素がある場合はその要素を含めないから、word[2]のtから始まってword[4]の前のword[3まで]

# ythoを出力
print(word[1:5])

# onを出力
print(word[4:])

# コレはエラー
# word[0] = 'j'
# 結合する方法
word = 'j' + word[1:]
print(word)

print(len(word))