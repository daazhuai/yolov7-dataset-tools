import os, shutil, random
from tqdm import tqdm

'''
功能：原始数据集划分
将文件夹datasets中存在存放图片数据的images文件夹和存放标签数据的labels文件夹
输入：原图片数据路径（文件夹images路径）、原标签数据路径（文件夹labels路径）、训练集测试集验证集划分比例列表、划分后数据集存放路径（Data）
输出：将images和labels下的文件分别划分为子文件夹train、val、test，分别保存在images和labels中
'''

def split_img(img_path, label_path, split_list):
    try:  # 创建数据集文件夹
        # 坑！！必须python创建的文件夹python才有写入权限！！
        # 创建存放划分后数据集的文件夹
        Data = r'E:\datasets'
        # os.mkdir(Data)

        train_img_dir = Data + '/images/train/'
        val_img_dir = Data + '/images/val/'
        test_img_dir = Data + '/images/test/'

        train_label_dir = Data + '/labels/train/'
        val_label_dir = Data + '/labels/val/'
        test_label_dir = Data + '/labels/test/'

        # 创建文件夹
        os.makedirs(train_img_dir)
        os.makedirs(train_label_dir)
        os.makedirs(val_img_dir)
        os.makedirs(val_label_dir)
        os.makedirs(test_img_dir)
        os.makedirs(test_label_dir)

    except:
        print('文件目录已存在')

    train, val, test = split_list
    all_img = os.listdir(img_path)
    all_img_path = [os.path.join(img_path, img) for img in all_img]
    all_label = os.listdir(label_path)
    all_label_path = [os.path.join(label_path, label) for label in all_label]
    train_img = random.sample(all_img_path, int(train * len(all_img_path)))
    train_img_copy = [os.path.join(train_img_dir, img.split('\\')[-1]) for img in train_img]
    train_label = [toLabelPath(img, label_path) for img in train_img]
    train_label_copy = [os.path.join(train_label_dir, label.split('\\')[-1]) for label in train_label]
    for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):
        _copy(train_img[i], train_img_dir)
        _copy(train_label[i], train_label_dir)
        all_img_path.remove(train_img[i])
    val_img = random.sample(all_img_path, int(val / (val + test) * len(all_img_path)))
    val_label = [toLabelPath(img, label_path) for img in val_img]
    for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
        _copy(val_img[i], val_img_dir)
        _copy(val_label[i], val_label_dir)
        all_img_path.remove(val_img[i])
    test_img = all_img_path
    test_label = [toLabelPath(img, label_path) for img in test_img]
    for i in tqdm(range(len(test_img)), desc='test ', ncols=80, unit='img'):
        _copy(test_img[i], test_img_dir)
        _copy(test_label[i], test_label_dir)


def _copy(from_path, to_path):
    shutil.copy(from_path, to_path)


def toLabelPath(img_path, label_path):
    img = img_path.split('\\')[-1]
    label = img.split('.png')[0] + '.txt'
    return os.path.join(label_path, label)


def main():
    img_path = r'/datasets/images'
    label_path = r'/datasets/labels'
    split_list = [0.8, 0.1, 0.1]  # 数据集划分比例[train:val:test]
    split_img(img_path, label_path, split_list)


if __name__ == '__main__':
    main()
# aia.lev1_euv_12s.2011-01-31T000009Z.193.image_lev1_58.png