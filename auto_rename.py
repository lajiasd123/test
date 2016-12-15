# -*- coding:UTF-8 -*-
import os,re,shutil,zipfile  #分别用于文件识别，正则式表达，文件改名，文件压缩备份

'''输入文件夹路径'''
lujing = raw_input('请将要检索的文件夹拖入这里\n>>>')

'''将文件夹打包成一个ZIP压缩包备份'''
print '即将备份文件...'
xxx = zipfile.ZipFile(lujing+'.zip','w')
for genmulu,ziwenjianjia,ziwenjian in os.walk(lujing):
	for wenjian in ziwenjian:
		xxx.write(os.path.join(genmulu, wenjian))
xxx.close()
print '完成备份'

'''创建一个正则表达式，来筛选文件名'''
wenjian_name = re.compile('(\d)(\s\()(\d{1,2})(\))(.*)')
for wenjian in os.listdir(lujing):
	name = wenjian_name.search(wenjian)
	if name:
		'''对文件改名'''
		newname = os.path.join(lujing, name.group(3) + name.group(5))
		wenjian = os.path.join(lujing, wenjian)
		print ('重命名 %s 为 %s ' % (wenjian, newname))
		queren = raw_input('请确定是否将以上文件改名\n（y or n）')
		if queren == 'y':
			shutil.move(wenjian, newname)
			print '改名完成.'
		else:
			pass
