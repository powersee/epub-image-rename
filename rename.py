import os
import re
# 填写网页中有漫画时才有的文字，例如域名
string_in_html = 'xxx.com'
# 填写解压好后文件夹的位置
os.chdir(r'F:\wufa')
current_working_dir = os.getcwd()
for j in os.listdir():
    os.chdir(current_working_dir)
    # 判断是否文件夹，是则将工作目录
    if os.path.isdir(j):
        os.chdir(current_working_dir+'/'+j)
        print(os.getcwd())
        for i in os.listdir("html"):
            # 读取文本
            f = open("html/" + i, encoding="utf-8").read()
            # 判断文本中是否存在某些字符串
            if string_in_html in f:
                # print('网页中存在图片链接')
                # 查找图片的文件名，此处我的是网页中的图片名字是  xxx.com-12345.jgp 这种格式。下方的 \d+ 指正则表达式中的一串数字。
                name = re.findall(string_in_html+r'-\d+.jpg', f)[0]
                if os.path.exists('image/' + name):
                    os.rename("image/" + name, "image/" + i + ".jpg")
