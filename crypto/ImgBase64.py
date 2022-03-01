import os
import sys
import base64
import argparse


def imgToBase64(imagePath):
    with open(imagePath, "rb") as f:
        base64data = base64.b64encode(f.read())
        #print(base64data)
        path = './output/base64/'+imageName(imagePath)+'.txt'
        file = open(path, "wb")
        file.write(base64data)
        file.close()
        print("已保存到: {}".format(path))

def base64ToImage(base64filePath):
    with open(base64filePath, "r") as f:
        imgdata = base64.b64decode(f.read())
        path = './output/imgs/'+imageName(base64filePath) + '.jpg'
        file = open(path, 'wb')
        file.write(imgdata)
        file.close()
        print("已保存到: {}".format(path))

def imageName(imagePath):
    name = os.path.basename(imagePath).split('.')[0]
    return name

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--image", type=str, help="输入待转换的图片名称. ex:python3 ImageBase64.py -i 1.jpg")
    parser.add_argument("-b","--base64", type=str, help="输入待转换的base64文件.ex:python3 ImageBase64.py -b 1.txt")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    imagePath = args.image
    base64filePath = args.base64

    if not imagePath is None:
        print("图片转base64")
        imgToBase64(imagePath)
    elif not base64filePath is None:
        print("base64转图片")
        base64ToImage(base64filePath)

    
if __name__ == '__main__':
    main()
