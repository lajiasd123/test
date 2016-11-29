# -*- coding:UTF-8 -*-

num = raw_input('>>>')
try:
    int(num)
except ValueError:
    print '请输入一个整数'
finally:
    
while num != 1:
    if num % 2 == 0:    #num是偶数
        num = num / 2
        print num
        continue
    else :
        num = 3 * num + 1
        print num
        continue

