import requests

proxy = {
    'http': 'http://180.94.134.9:63072',
    'https': 'http://180.94.134.9:63072'
}

'''head 信息'''
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 
        'Connection': 'keep-alive'
}

'''http://icanhazip.com会返回当前的IP地址'''
p = requests.get('http://icanhazip.com', headers=head)
print(p.text)    