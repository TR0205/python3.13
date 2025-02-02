l = [1, 2, 3]

try:
    print(l[0])
except IndexError as ex:
    print('Error: {}'.format(ex))
else: # 例外が発生しない場合
    print('done')
finally: # 必ず最後に実行される
    print('Finished')
