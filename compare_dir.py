# -*- coding: utf-8 -*-
import os

'''
函数：file_name(image_dir,xml_dir)
功能：对比images文件夹中的图片文件与labels文件夹中的标签文件，找出缺少标签的图片文件列表
输入：images文件夹路径、labels文件夹路径
输出：缺失label的图片文件列表
'''

def file_name(image_dir,xml_dir):
    jpg_list = []
    xml_list = []
    # none_png = []
    none_xml = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            jpg_list.append(os.path.splitext(file)[0])
    for root, dirs, files in os.walk(xml_dir):
        for file in files:
            xml_list.append(os.path.splitext(file)[0])
    print("数据集图像总数：", len(jpg_list))

    # 差集，在xml_list中但不在jpg_list中的元素
    # diff = set(xml_list).difference(set(jpg_list))
    # for name in diff:
    #     none_xml.append(name + ".xml")
    #     print(name + ".xml")

    # 差集，在jpg_list中但不在xml_list中的元素
    diff2 = set(jpg_list).difference(set(xml_list))
    print("缺少标签的图片数：", len(diff2))
    for name in diff2:
        none_xml.append(name + ".png")
        print(name + ".png")
    print("缺少xml标签的图片文件为：", none_xml)
    return none_xml

'''
函数：delete_nonelabel_files(none_xml_list, img_path)
功能：将images缺少标签的图片文件作为无效数据删除
输入：缺少标签的图片文件列表、images文件夹路径
输出：（无输出，完成删除操作）
'''

def delete_nonelabel_files(none_xml_list, img_path):
    # 读取txt文件中的文件名列表
    for file_name in none_xml_list:
        file_path = os.path.join(img_path, file_name)
        try:
            os.remove(file_path)
            print(f"文件 '{file_name}' 已成功删除.")
        except FileNotFoundError:
            print(f"文件 '{file_name}' 未找到.")
        except Exception as e:
            print(f"删除文件 '{file_name}' 时发生错误: {e}")


if __name__ == '__main__':
    # images文件夹路径
    images_path = r'/datasets/images'
    # labels文件夹路径
    labels_path = r'/datasets/labels'

    none_label_list = file_name(images_path, labels_path)
    delete_nonelabel_files(none_label_list, images_path)
