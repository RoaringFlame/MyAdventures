# -*- coding: utf-8 -*-
from xml.dom import minidom
from Image import Image
import sys, os

file_path = []


def get_attribute_value(node, attribute_name):
    return node.getAttribute(attribute_name) if node else ''


def get_xml_node(node, name):
    return node.getElementsByTagName(name) if node else[]


def getNameList(dir, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if os.path.isdir(fullname) & recursion:
            getNameList(fullname, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file_path.append(fullname)
                    print(fullname)
                    break


def read_xml(path):
    # 解析xml
    print(path)
    doc = minidom.parse(path)
    # 得到根节点
    root = doc.documentElement
    # 读取跟节点对应的信息
    imagePath = root.getAttribute("imagePath")
    print (imagePath)
    new_file_name = imagePath.split(".")[0]

    image_file_dir = path.split("\\")
    image_file_path = ""
    for index, item in enumerate(image_file_dir):
        if index == len(image_file_dir) - 1:
            break;
        if index == 0:
            image_file_path = ("%s\\") % (item)
        elif index == len(image_file_dir) - 2:
            image_file_path = ("%s%s\\") % (image_file_path, item)
        else:
            image_file_path = ("%s%s\\") % (image_file_path, item)
    new_file_path = ("%s%s") % (image_file_path, new_file_name)
    print (new_file_path)
    if os.path.exists(new_file_path) <> True:
        os.mkdir(new_file_path)
    image_file_path = ("%s%s") % (image_file_path, imagePath)
    print(image_file_path)

    # 子节点中的信息，ImageName，x,y,width,height
    subTexture_nodes = get_xml_node(root, 'SubTexture')
    for node in subTexture_nodes:
        name = get_attribute_value(node, 'name')
        x = get_attribute_value(node, 'x')
        y = get_attribute_value(node, 'y')
        width = get_attribute_value(node, 'width')
        height = get_attribute_value(node, 'height')

        name = ("%s.png") % (name)
        x = x.encode("utf-8")
        y = y.encode("utf-8")
        width = width.encode("utf-8")
        height = height.encode("utf-8")
        name = name.encode("utf-8")

        left = int(x)
        upper = int(y)
        right = int(x) + int(width)
        lower = int(y) + int(height)

        image = Image.open(image_file_path)
        print(image.size)
        box = (left, upper, right, lower)
        # box = (x,y,width,height)
        print(box)
        print(image_file_path)
        region = image.crop(box)
        region.save(("%s\\%s") % (new_file_path, name), 'png')


def run():
    getNameList(sys.path[0], ".xml", 1)
    file_name_list = file_path
    image_name_list = ""
    for file_name in file_name_list:
        a = file_name.find(".xml")
        print (a)
        if a != -1:
            read_xml(file_name)


if __name__ == "__main__":
    print("/////////ImageCutting/////////")
    run()