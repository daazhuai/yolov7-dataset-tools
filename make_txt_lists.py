import os

'''
功能：生成训练所需的train.txt、test.txt、val.txt
输入：文件夹路径、保存文件夹中所有文件名的.txt文件路径
输出：为已划分好的数据集生成训练所需的train.txt、test.txt、val.txt文件
'''
# def readInfo(filePath):
#     filePath = './datasets/images/test'
#     name = os.listdir(filePath)         # os.listdir方法返回一个列表对象
#     return name

def make_txt_list(datasets_path):

    train_path = datasets_path + '/images/train'
    train_file = open(datasets_path + '/train.txt', 'w')
    train_list = os.listdir(train_path)
    for i in train_list:
        rowInfo_train = train_path + i + '\n'
        print(rowInfo_train)
        train_file.write(rowInfo_train)

    test_path = datasets_path + '/images/test'
    test_file = open(datasets_path + '/test.txt', 'w')
    test_list = os.listdir(test_path)
    for i in test_list:
        rowInfo_test = test_path + i + '\n'
        print(rowInfo_test)
        test_file.write(rowInfo_test)

    val_path = datasets_path + '/images/val'
    val_file = open(datasets_path + '/val.txt', 'w')
    val_list = os.listdir(val_path)
    for i in val_list:
        rowInfo_val = val_path + i + '\n'
        print(rowInfo_val)
        val_file.write(rowInfo_val)

# 程序入口
if __name__ == "__main__":
    # fileList = readInfo()       # 读取文件夹下所有的文件名，返回一个列表
    # print(fileList)
    # file = open('datasets/test.txt', 'w')   # 创建文件，权限为写入
    # make_txt_list()
    # for i in fileList:
    #     rowInfo = '/public/home/acavbgmcz3/datasets/images/test/' + i + '\n'
    #     print(rowInfo)
    #     file.write(rowInfo)
    make_txt_list(r'E:\datasets')
