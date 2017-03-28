# 爬取图片地址上的单张图片：
import urllib.request

def get_image(url):
    request = urllib.request.Request(url)
    #构建请求
    response = urllib.request.urlopen(request)
    #获取服务器响应
    get_image = response.read()
    #读取图片内容
    with open('001.jpg','wb') as open_file:
     #以二进制写入的方式创建新文件
        open_file.write(get_image)
        print('图片下载完成')
    return

url = 'http://p2.123.sogoucdn.com/imgu/2016/10/20161019124600_428.jpg'
get_image(url)