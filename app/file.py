# f = open('test.txt', 'w')
# f.write('Testaaa')
# f.close()

with open('test.txt', 'w') as f:
    f.write('withstatement')
    # f.close()が不要