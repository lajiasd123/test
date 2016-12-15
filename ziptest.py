# -*- coding:UTF-8 -*-
import os,re,zipfile
lujing = raw_input('请输入路径')
xxx = zipfile.ZipFile(lujing+'.zip','w')
for genmulu,ziwenjianjia,ziwenjian in os.walk(lujing):
	for wenjian in ziwenjian:
		xxx.write(os.path.join(genmulu, wenjian))
#xxx.write('D:\\asd\\asd.txt',compress_type=zipfile.ZIP_DEFLATED)     #第二个参数为压缩算法，它对各种类型的数据都很有效
xxx.close()

'''wenjianjia = os.listdir('D:\\Documents\\GitHub\\temp')
wenjian_name = re.compile('(\d)(\s\()(\d{1,2})(\))(.*)')
for wenjian in wenjianjia:
	name = wenjian_name.search(wenjian)
	print name.group(5)'''

'''wenjian_name = re.compile('(asd)(\s-\s)(副本)(\s\(\d\))')
for wenjian in wenjianjia:
	name = wenjian_name.search(wenjian)
	print type(name)'''