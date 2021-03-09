import requests,random,time,os
TG_BOT_TOKEN =''#line:11
TG_USER_ID =''#line:12
TOKEN=''
if  "TG_USER_ID" in os .environ and os .environ ["TG_USER_ID"]:#line:13
        TG_BOT_TOKEN ='1698539466:AAHqZNARtVq2MJiFQIcygSxEjVDGpOJjY5k'#line:14
        TG_USER_ID =os .environ ["TG_USER_ID"]#line:15
        print ("Telegram 推送打开")#line:16

def fristlogin():
    a='bdEH5jnTfBaGhFywTMIscbf{a}w{b}i{c}{d}{e}P/w2SIZlbirzi7yJ2m'.format(a=random.randint(1, 9),b=random.randint(1, 9),c=random.choice('ABCDEFG'),d=random.choice('ABCDEFGH'),e=random.choice('ABCDEFG'))
    ploy={
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Host': 'pwb.wubabanjia.net',
        'Origin': 'https://web.wubabanjia.net',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E176 Safari/604.1',
        'X-AFDAC809-9AD768A3':a}
    url='https://pwb.wubabanjia.net/v1/fastlogin'
    while True:
        try:
            result=requests.get(url,headers=ploy)
            if result.status_code==200:
                print(result.json()['response']['token'])
                return result.json()['response']['token']
                break
        except Exception as e:
            print(e)
            time.sleep(2)

def register_email(token):
    email='{}@qq.com'.format(random.randint(1000000,99999999))
    print(email)
    fils={
        'platform':(None,'uj72624275'),
        'email':(None,email),
        'password':(None,'sdEWWEqqCEWW@!')
          }
    url = 'https://pwb.wubabanjia.net/v1/register/email?token={}'.format(token)
    #print(url)
    result = requests.post(url, files=fils)
    #print(result.text)
def telegram_bot(title, content):
    print("\n")
    tg_bot_token = TG_BOT_TOKEN
    tg_user_id = TG_USER_ID
    if "TG_BOT_TOKEN" in os.environ and "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +
                 '\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url='https://api.telegram.org/bot%s/sendMessage' % (tg_bot_token), data=send_data)
    print(response.text)
def invite(token):
    invitecode=os.environ["INVITECODE"]
    fils={'code':(None,invitecode)}
    url='https://pwb.wubabanjia.net/v1/user/invite?token={}'.format(token)
    #print(url)
    result=requests.post(url,files=fils)
    print(result.text)
    choice_vip()
def choice_vip():

    if 'TOKEN' in os.environ:
        mytoken=os.environ["Token"]
        url='https://pwb.sjzrongshida.cn/v1/lottery/1?token={}'.format(mytoken)
        s=requests.post(url)
        time.sleep(2)
        telegram_bot('撸先生', '邀请完成！随机抽奖完成！')
    else:
        telegram_bot('撸先生', '邀请完成！未开启随机抽奖！（需要抽奖请填写TOKEN)')
def main():
    token = fristlogin()
    time.sleep(5)
    register_email(token)
    time.sleep(5)
    invite(token)
if __name__=='__main__':
    main()
