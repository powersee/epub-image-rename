最近不想再用 calibre 来观看 epub 格式的漫画了，因为它不能同屏显示两页。

我想提取里面的图片出来，然后用 蜂蜜浏览器 来观看。提取倒是很简单，直接把 epub 后缀改为 zip 就可以解压，然后就可以看到里面的图片。

但是，问题来了，里面的图片并不是按照顺序排的。所以直接提取我就没法正常观看了……

所以我研究了一番，找到了解决方案。

## 分析

我发现里面有 html 和 image 这两个文件夹，每一个 html 文件里面，都存放着图片的名字。而 html 的文件名是按 1.html 2.html ... 100.html 这样排序的。

那么我岂不是可以通过遍历，查找 html 里面图片的名字，然后再到 image 文件夹里面，将图片的名字改为 html 的名字。例如，1.html 里面的图片是 xxx-9527.jpg ，我就将它改为 1.html.jpg 。

## 实现

通过 for i in os.listdir() 查找每一个 html 文件里的文本，然后去修改对应图片的名字。

于是我通过 rename.py 这个脚本实现了这个功能。

与此同时我还写了 unzip_file.py 这个脚本来实现批量将 epub 文件解压的功能。