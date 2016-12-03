a = ['a','b','c','d']
a[3] = 'and ' + a[3]
print a
b = ''.join(a)
print b

import pyperclip
pyperclip.copy(b)