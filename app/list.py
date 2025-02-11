word = "Python"

"""
インデックス指定の文字列入れ替えはできない。
"""
# 以下はエラー
# word[0] = 2
# print(word)

# 文字列結合をする必要がある
word = "p" + word[1:]
print(word)

l = [1, 2, 47, 98, 66, 0]
l2 = ['ko', 66]

print(l)
print(l[:])

# 要素を2つ飛ばしで表示
print(l[::2])

# これは2:と同じ・・・よくわからん
print(l[2::])

# リストを逆順で表示
print(l[::-1])

l[0] = 7
print(l)

print(l + l2)

l = [1, 2, 47, 98, 66, 0]

l.append(100)
print(l)
l.insert(0, '67')
print(l)
# 最後の要素から３番目に追加
l.insert(-2, '67')
print(l)

l = [1, 2, 47, 98, 66, 0]
l.pop() # 最後の要素を削除
print(l)
l.pop(2) # 要素のインデックス指定して削除
print(l)
l = [1, 2, 47, 98, 66, 0]
l.remove(2) # 値を指定して削除
print(l)

l = [1, 3, 2, 10, 5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse() # 同じ
print(l)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)
