import os
import time
import sys
import shutil
import requests

"""
忘记为啥是英文注释了 回头再改（不会
pep的语法规则呢。。。回头再改（不会
真·能用版本 
从旧版本的urllib改成了使用request
参考小甲鱼的python爬虫教程 直接在源码里搜关键字 没用到re


已知bug:
    连不上网不会报错？？嗯？
    
"""


# find the link of 50 small pictures and return a list which content them
def findOriginImgs(url):
    html = ""
    try:
        html = requests.get(url).text  # the original code of web
    except Exception as e:
        print(e)

    if html == "":
        print("\n忘记开全局代理了吧？检查看看(　o=^•ェ•)o　┏━┓\n")
        input("随便敲击键盘退出")
        exit(0)

    imgAddrs = []  # empty list
    i = 0  # for counting
    a = html.find('img src=') + 153  # get the head sign of picture's link(which is small one

    while a != -1 and i < 50:
        b = html.find('.jpg', a + 9) + 4  # get the tail sign of picture's link (small one)
        if b != -1:
            # get the origin picture's linking which the header is needed when accessing the link
            temp = html[a:a + 20] + 'img-original' + html[a + 40:a + 76] + '.jpg'
            print(temp)
            imgAddrs.append(temp)
        else:
            b = a + 9
        i += 1
        a = html.find('img src=', b) + 153
    return imgAddrs


def downloadFromList(url, id, count):
    id = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + id
    headers = {"Referer": id,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               }

    response = requests.get(url, headers=headers)
    # print(response.status_code)
    if response.status_code == 404:
        url = url[:69] + 'png'
        response = requests.get(url, headers=headers)

    html = response.content
    filename = (url.split('/')[-1])[:15]
    with open(filename, 'wb') as f:
        print((url.split('/')[-1])[:8] + ",", end="")
        f.write(html)
        print("The %dth one have been downloaded" % count)


if __name__ == "__main__":
    data = time.strftime("%d.%m.%Y")  # get the date 02.03.2020
    desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'  # get the dir of destop
    file = desk + data  # final saving file such as c/user/Mirokee/Desktop/02.03.2020

    if os.path.exists(file):  # if02.03.2020file exited
        shutil.rmtree(file)  # delete it
    os.makedirs(file)  # build the file
    os.chdir(file)  # point to the file

    url = 'https://www.pixiv.net/ranking.php?mode=daily'
    imgAddrs = findOriginImgs(url)  # imgAddrs is a list storaging 50 links of small pictures

    print('\n')
    print('----------------------------------------------------')
    print('\n')

    count = 1
    for each in imgAddrs:
        downloadFromList(each, (each.split('/')[-1])[:8], count)
        count += 1
    input("成功啦！桌面应该生成了一个日期命名的文件夹了\n\n随便敲击键盘退出")
    exit(0)
