from __future__ import print_function

tableData = [['a3','b34','c','d'],
             ['aa','bb624423','cc3','dd2324'],
             ['q','w','e4','r32']]

def printtable():
    for x in range(4):
        for y in range(3):
            print (tableData[y][x]+' ',end='')
        print (' ')

printtable()