# -*- coding: utf-8 -*-
# coding:unicode_escape
import os
import sys
import argparse
from text_blind_watermark import TextBlindWatermark

def enc(source_data, password):
    watermark = source_data
    text = "这句话中有盲水印，你能看出来吗?" * 126 

    twm = TextBlindWatermark(password=password)
    twm.read_wm(watermark=watermark)
    twm.read_text(text=text)
    text_embed = twm.embed()

    # 将数据写入文件
    with open("data.txt", 'w') as f:
        f.write(text_embed)



    
def dec(encrypted_data_name, password):
    file = open(encrypted_data_name, 'r')
    text_embed = file.read()
    twm_new = TextBlindWatermark(password=password)
    wm_extract = twm_new.extract(text_embed)
    
    # 将解密文件写入到 decode.txt
    with open("decode.txt", 'w') as f:
        f.write(wm_extract)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--encode", type=str, help="请输入要加密的文本")
    parser.add_argument("-p","--password", type=str, help="请输入加密密码")
    parser.add_argument("-d","--decode", type=str, help="请输入要解密的文本(文件)")
    
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    source_data = args.encode
    password = args.password
    encrypted_data_name = args.decode


    if not source_data is None:
        print("加密...")
        enc(source_data, password)
        print("加密完成：data.txt")

    elif not encrypted_data_name is None:
        print("解密...")
        dec(encrypted_data_name, password)
        print("解密完成: decode.txt")





if __name__ == "__main__":
    main()
    

