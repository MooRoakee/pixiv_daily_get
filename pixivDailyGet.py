import json
import os
import shutil
import time

import requests

"""


=====================2.0/2020/11.29船新版本========================

Note:
    需要全局代理流量(如果原地区网络访问不了pixiv
    1.0的exe也还能用

1.不知道啥时候pixiv图片变成动态加载了，解决了动态加载的图片在源代码里获取不到的问题
2.在网上搜全是用beautiful soup和selenium的神奇方法(需要配置chromedriver和浏览器位置巴拉巴拉
3.clash配置好规则也不用开global(woc美滋滋
4.好耶！





=======1.0旧版本注释==============================
忘记为啥是英文注释了 回头再改（不会
pep的语法规则呢。。。回头再改（不会
真·能用版本 
从旧版本的urllib改成了使用request
参考小甲鱼的python爬虫教程 直接在源码里搜关键字 没用到re


已知bug:
    连不上网不会报错？？嗯？
    
"""





def find_original_images(target_url):
    """
    变量：url
    返回：img list
    说明：url源码里有所有图片的链接，找到他们（2.0的源码是json格式
        直接load成dick就找完了可带劲了），然后转换成原图的链接（源
        码里本来的链接全是全损图），然后存在Img list里返回

        其中返回的list所有原图链接全为jpg（当然是错误的，有些原图应
        该是png）,其中错误的下载的时候会失败，在下载失败的时候才再替
        换成png
    """

    headers_daily = {
        'referer': 'https://www.pixiv.net/ranking.php?mode=daily',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 '
                      'Safari/537.36 '
    }
    json_response = ''
    try:
        json_response = requests.get(url, headers=headers_daily).text
    except Exception as e:
        print(e)

    if json_response == "":
        print("\n忘记开全局代理了吧？检查看看(　o=^•ェ•)o　┏━┓\n")
        input("随便敲击键盘退出")
        exit(0)

    file_create()

    dr = json.loads(json_response)['contents']
    image_list = []  # empty list
    for i in range(len(dr)):
        a = 0
        b = b = dr[i]['url'].find('.jpg', a + 9) + 4
        temp = dr[i]['url'][a:a + 20] + 'img-original' + dr[i]['url'][a + 40:a + 76] + '.jpg'
        print(temp)
        image_list.append(temp)

    return image_list


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


def file_create():
    data = time.strftime("%d.%m.%Y")  # get the date 02.03.2020
    desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'  # get the dir of destop
    file = desk + data  # final saving file such as c/user/Mirokee/Desktop/02.03.2020

    if os.path.exists(file):  # if02.03.2020file exited
        shutil.rmtree(file)  # delete it
    os.makedirs(file)  # build the file
    os.chdir(file)  # point to the file


if __name__ == "__main__":

    # 采用js动态加载图片的真request地址，1个p有50个图
    url = 'https://www.pixiv.net/ranking.php?mode=daily&p=1&format=json'
    img_list = find_original_images(url)

    print('\n')
    print('=============================================================')
    print('\n')

    count = 1
    for each in img_list:
        downloadFromList(each, (each.split('/')[-1])[:8], count)
        count += 1
    input("成功啦！桌面应该生成了一个日期命名的文件夹了\n\n随便敲击键盘退出")
    exit(0)
