import os
import zipfile

# 下方填写 epub 文件放置的文件夹
os.chdir(r'F:\xxxx')
for file in os.listdir():
    if file.endswith(".epub"):
        dir_name = file + ".unzip"
        os.makedirs(dir_name)
        zFile = zipfile.ZipFile(file, "r")
        # ZipFile.namelist(): 获取ZIP文档内所有文件的名称列表
        for fileM in zFile.namelist():
            zFile.extract(fileM, dir_name)
        zFile.close()
        print("解压完成："+file)
