#coding=utf-8
import os

from xml.dom.minidom import Document
import glob
import cv2

#######
#1.先将每个文件夹对应的unit.txt标签文件转换为各个文件对应的标签文件
#2.再将对应的txt转换为VOC格式使用的xml格式。
#######
DirPath = '../PTLR/PTLR dataset/Training set/Italy/'
# TotalTxtPath = DirPath + '01/' + 'unit.txt'
# with open(TotalTxtPath, 'r') as fread:
#     for line in fread.readlines():
#         TxtFileName = line.split()[0] + '.txt'
#         fwite = open(DirPath + '06/' + TxtFileName, 'a')
#         fwite.write(line)

#
def writeXml(txtfile, imgName, xmlFileName, w, h):
    doc = Document()
    # owner
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    # owner
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode("VOC2007")
    folder.appendChild(folder_txt)

    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    filename_txt = doc.createTextNode(imgName)
    filename.appendChild(filename_txt)
    # ones#
    source = doc.createElement('source')
    annotation.appendChild(source)

    database = doc.createElement('database')
    source.appendChild(database)
    database_txt = doc.createTextNode("The PTLR Database")
    database.appendChild(database_txt)
    # onee#

    # twos#
    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    size.appendChild(width)
    width_txt = doc.createTextNode(str(w))
    width.appendChild(width_txt)

    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode(str(h))
    height.appendChild(height_txt)

    depth = doc.createElement('depth')
    size.appendChild(depth)
    depth_txt = doc.createTextNode("3")
    depth.appendChild(depth_txt)
    # twoe#

    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    segmented_txt = doc.createTextNode("0")
    segmented.appendChild(segmented_txt)

    with open(txtfile, 'r') as f:
        for line in f.readlines():
            nameValue = line.split()[1]
            xminValue = int(float(line.split()[2])*1280)
            yminValue = int(float(line.split()[3])*720)
            xmaxValue = int(float(line.split()[4])*1280)
            ymaxValue = int(float(line.split()[5])*720)
            # threes#
            object_new = doc.createElement("object")
            annotation.appendChild(object_new)

            name = doc.createElement('name')
            object_new.appendChild(name)
            name_txt = doc.createTextNode(str(nameValue))
            name.appendChild(name_txt)

            pose = doc.createElement('pose')
            object_new.appendChild(pose)
            pose_txt = doc.createTextNode("Unspecified")
            pose.appendChild(pose_txt)

            truncated = doc.createElement('truncated')
            object_new.appendChild(truncated)
            truncated_txt = doc.createTextNode("0")
            truncated.appendChild(truncated_txt)

            difficult = doc.createElement('difficult')
            object_new.appendChild(difficult)
            difficult_txt = doc.createTextNode("0")
            difficult.appendChild(difficult_txt)
            # threes-1#
            bndbox = doc.createElement('bndbox')
            object_new.appendChild(bndbox)

            xmin = doc.createElement('xmin')
            bndbox.appendChild(xmin)
            xmin_txt = doc.createTextNode(str(xminValue))
            xmin.appendChild(xmin_txt)

            ymin = doc.createElement('ymin')
            bndbox.appendChild(ymin)
            ymin_txt = doc.createTextNode(str(yminValue))
            ymin.appendChild(ymin_txt)

            xmax = doc.createElement('xmax')
            bndbox.appendChild(xmax)
            xmax_txt = doc.createTextNode(str(xmaxValue))
            xmax.appendChild(xmax_txt)

            ymax = doc.createElement('ymax')
            bndbox.appendChild(ymax)
            ymax_txt = doc.createTextNode(str(ymaxValue))
            ymax.appendChild(ymax_txt)
            # threes-1#
            #threee#

    with open(xmlFileName, "w") as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    return

if __name__ == "__main__":
    TxtPath = DirPath + '06/'
    for txtfile in glob.glob(TxtPath + '/*.txt'):
        # print txtfile   #列出所有txt后缀的文件
        (filepath, tempfilename) = os.path.split(txtfile)
        (filename, extension) = os.path.splitext(tempfilename)
        imgName = filename + '.jpg'
        # img = cv2.imread(TxtPath + filename + '.jpg')
        # width = img.shape[1]
        # height = img.shape[0]
        wdith = 1280
        height = 720

        xmlFileName = TxtPath + filename + '.xml'
        writeXml(txtfile, imgName, xmlFileName, wdith, height)
