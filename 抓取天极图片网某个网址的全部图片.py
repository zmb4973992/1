# 爬取某个网页的所有图片：
import urllib
import urllib.request
import re

def download_page(url):
    request = urllib.request.Request(url)
    resonse = urllib.request.urlopen(request)
    data = resonse.read()
    return data

def get_image(html):
    regex = r'http://[\S]*\.jpg'
    #定义正则表达式，意思是所有以.jpg格式结尾的网址
    pattern = re.compile(regex)
    #定义查找模式
    get_image = re.findall(pattern,repr(html))
    #用repr方式将初始网址转换为字符串，然后开始按照预定的模式进行查找，将所有符合条件的网址都放入内存中
    num = 1
    for img in get_image:
    #开始将内存中的网址取出
        image = download_page(img)
        #将每个图片链接进行解析，并按照之前的函数返回二进制数据
        with open('%s.jpg'%num,'wb') as open_file:
            open_file.write(image)
            num += 1
            print('第%s张图片下载完成'%num)

    return

url = 'http://pic.yesky.com/c/6_61112.shtml'
html = download_page(url)
get_image(html)

# 但是往往裸奔版对一些网站是爬不了的，这时就需要对爬虫进行一些伪装了。伪装浏览器或者加入延时。

# 伪装的话直接把request请求改成

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

# request = urllib.request.Request(url,headers=headers)

# 这样就成功完成伪装了

