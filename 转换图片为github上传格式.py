#@author 叶志豪
#@description 删除白底文件夹和原图,视频重命名为p.mp4 水印重命名为logo
#@date 20220920
#@version 1.0
import os,glob,shutil
input("删除白底文件夹和原图?")
dirs=glob.glob(".\\*[0-9]*\\")#获取OEM文件夹
for dir in dirs:
	print(dir,"\n")
	if os.path.exists(dir+"\\白底\\"):
		#删除白底文件夹
		shutil.rmtree(dir+"\\白底\\")
	

	files= glob.glob(dir+"\\*.mp4")#获取所有视频文件
	for file in files:
		print(file)
		print(dir+"\\p.mp4")
		#视频重命名为p.mp4
		shutil.move(file,dir+"\\p.mp4")
		#水印重命名为logo
		if os.path.exists(dir+"\\水印\\"):
			os.rename(dir+"\\水印\\",dir+"\\logo\\")
	#删除原图
	files=glob.glob(dir+"\\*.jpg")#获取所有原图文件
	for file in files:
		print(file)
		os.remove(file)
	# if not os.path.exists(dir+"\\原图\\"):
		# os.mkdir(dir+"\\原图\\")#创建原图文件夹
	# 	print(dir+"\\原图\\")
# 	files= glob.glob(dir+"\\*.mp4")#获取所有视频文件
# 	# print(files)
# 	for file in files:
# 		print(file)
# 		dir1=dir.replace(".","")
# 		print(dir)
# 		print(dir1)
# 		dir1=dir1.replace("\\","")
# 		print(dir1)
# 		shutil.copy(dir+"\\p.mp4","gdiVideo\\"+dir1+".mp4")
# 		print("源文件"+file,"目标文件"+dir+"\\原图\\")
# #os.mkdir(file+r""+"原图")
# if os.path.isfile(file):
# os.remove(r""+file)

# import shutil
# shutil.move(r".\白底\7.jpg",r".\水印\1.jpg")
# shutil.move(r".\白底\8.jpg",r".\水印\2.jpg")
# shutil.move(r".\白底\9.jpg",r".\水印\3.jpg")
# shutil.move(r".\白底\10.jpg",r".\水印\4.jpg")
# shutil.move(r".\白底\11.jpg",r".\水印\5.jpg")
# shutil.move(r".\白底\12.jpg",r".\水印\6.jpg")
# #创建文件夹
# import os,glob
# os.mkdir("原图")
# files=glob.glob(r".\*[0-9]*")
# for file in files:
#  # print(file)
#  shutil.move(r""+file,r".\原图")
