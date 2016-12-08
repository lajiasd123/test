# -*- coding:UTF-8 -*-
import os,re,shutil,zipfile  #分别用于文件识别，正则式表达，文件改名，文件压缩备份

'''输入文件夹路径'''
lujing = raw_input('请将要检索的文件夹拖入这里\n>>>')

'''创建一个正则表达式，来筛选文件名'''
wenjian_name = re.compile('(asd)(\s-\s)(副本)(\s\(\d\))')
for wenjian in os.listdir(lujing):
	name = wenjian_name.search(wenjian)

'''将文件夹打包成一个ZIP压缩包备份'''
zipduixiang = open(lujing+'.zip','w')
zipmake = zipfile.ZipFile(lujing+'.zip')
zipmake.write(lujing,compress_type=zipfile.ZIP_DEFLATED)
zipmake.close()

'''对文件改名'''
newname = name.group(1) + name.group(2)+ name.group(4)
wenjian = os.path.join(lujing,wenjian)
print ('重命名 %s 为 %s ' % (name , newname))
queren = raw_input('请确定是否将以上文件改名\n（y or n）')
if queren == y:
	shutil.move(name, newname)
