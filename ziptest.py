# -*- coding:UTF-8 -*-
import os,zipfile

xxx = zipfile.ZipFile('D:\\asd.zip','w')
xxx.write('D:\\asd\\asd.txt',compress_type=zipfile.ZIP_DEFLATED)     #第二个参数为压缩算法，它对各种类型的数据都很有效
xxx.close()