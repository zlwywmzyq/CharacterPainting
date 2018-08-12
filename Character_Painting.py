#!/usr/bin/python
#-*- coding:utf-8 -*-
from PIL import Image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', nargs="?",)
parser.add_argument('-o', '--output', nargs="?")
parser.add_argument('-width', nargs="?",type = int, default = 80)
parser.add_argument('-height', nargs="?",type = int, default = 80)
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


ascii_char=list("$@B%8&WM#*oahkbdpqwmZo0QLCJUYXZcvunxrjft/\|()1{}[]?-_=~<>i!lI;:\"^`'.")      #字符串列表

def get_char(r,g,b,alpha=256):  #将像素转换为字符函数
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)  #RGB转换为灰度

    unit=(256.0+1)/length      #
    return ascii_char[int(gray/unit)]    #获取该灰度在字符串列表中所对应的字符

if __name__=='__main__':
    im=Image.open('/Users/houxuefeng/Downloads/20160909163239122.png')      #打开图片args.file，返回Image对象
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)   #重置尺寸

    txt=""
    for i in range(HEIGHT):      #HEIGHT，WIDTH默认是80像素
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))  #获取像素，计算对应字符，保存到txt中，获取像素点这里用的是getpixel（(i,j))函数
        txt+='\n'       #每到行尾换行
    print txt     #输出

    if OUTPUT:
        with open(OUTPUT,'W') as f:
            f.write(txt)     #保存到文本中
    else:
        with open("output.txt",'w') as f:
            f.write(txt)