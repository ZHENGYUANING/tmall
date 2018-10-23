
# import requests 
# import random 
# from pickle import loads,dumps
# from requests import Request 


# proxies_url =[
#     '61.145.203.234:38695',
#     '110.188.0.67:60459',
#     '39.135.9.226:8080',
#     '210.72.14.142:80'
# ]

# proxies = random.choice(proxies_url)
#测试IP代理池
# proxies = {
#     'http':'http://'+proxies,
# }
# try:
#     req = requests.get('http://www.httpbin.org/get',proxies=proxies,timeout=10)
#     print(req.text)
# except Exception as e:
#     print(e)
# class RedisQueue():
#     def __init__(self):
#         """
#         初始化redis
#         """
#         self.db = StrictRedis(host='127.0.0.1',port='6379',password='root123')
#     def add(self,request):
#         if isinstance(request,Request):
#             return self.db.rpush(REDIS_KEY,dumps(request))
#         return False 

#     def pop(self):
#         if self.db.llen(REDIS_KEY):
#             return loads(self.db.lpop(REDIS_KEY))
#         else:
#             return False 


from lxml import etree
import requests
class Login(object):
    def __init__(self):
        self.headers = {
            'Referer':'https://www.github.com',
            'User-Angent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host':'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/emails'
        self.session = requests.Session()
    #提取出autheticity_token里面的value值
    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        selector = etree.HTML(response.text)
        # print(selector)
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        print(token)
        return token 


    def login(self,email,password):
        post_data = {
            'commit':'Sign in',
            'utf-8':'✓',
            'authenticity_token':self.token(),
            'login':email,
            'password':password
        }
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)

        if response.status_code == 200:
            # print('aaaa')
            self.dynamics(response.text)
        response = self.session.get(self.logined_url,headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)
           
    def dynamics(self,html):
        selector = etree.HTML(html)
        itmes = selector.xpath('//div[contains(@lass,"news")]//div[contains(@class,"alert")]')
        for item in itmes:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self,html):
        selector = etree.HTML(html)
        # name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        # email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        email = selector.xpath('//*[@id="settings-emails"]/li[1]/span[1]/@title')[0]
        print(email)
    
            
if __name__ == '__main__':
    login = Login()
    login.login(email='ZHENGYUANING',password='wawnsbxysmly52')
    # login.token()
