import json

import requests

url = 'https://www.pixiv.net/ranking.php?mode=daily&p=1&format=json'
headers_daily = {
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 '
                  'Safari/537.36 '
}
imgList = []
json_response = requests.get(url, headers=headers_daily).text

dr = json.loads(json_response)['contents']
for i in range(len(dr)):
    a = 0
    b = b = dr[i]['url'].find('.jpg', a + 9) + 4
    temp = dr[i]['url'][a:a + 20] + 'img-original' + dr[i]['url'][a + 40:a + 76] + '.jpg'
    print(temp)
    imgList.append(temp)



