import os
import shutil

'''
labelimg在不同文件夹下分别打标签，将文件夹合并
'''

# 原文件夹
old_path = "D:/SDUer/work/yolov7/BP_OD/image/segment/193/"
# 查看原文件夹下所有的子文件夹
filenames = os.listdir(old_path)
print(filenames)
# 新文件夹
target_path = "D:/SDUer/work/yolov7/BP_OD/image/segment/all/"
if not os.path.exists(target_path):
    os.mkdir(target_path)

for file in filenames:
    # 所有的子文件夹
    sonDir = "D:/SDUer/work/yolov7/BP_OD/image/segment/193/" + file
    # print(sonDir)
    # 遍历子文件夹中所有的文件
    for root, dirs, files in os.walk(sonDir):
    	# 如果文件夹中有文件
        if len(files) > 0:
            for f in files:
                newDir = sonDir + '/' + f
                # 将文件移动到新文件夹中
                shutil.move(newDir, target_path)
        else:
            print(sonDir + "文件夹是空的")