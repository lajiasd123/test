# -*- coding:UTF-8 -*-

num = raw_input('>>>')
num = int(num)
while num != 1:
    if num % 2 == 0:    #num是偶数
        num = num / 2
        print num
        continue
    else :
        num = 3 * num + 1
        print num
        continue

