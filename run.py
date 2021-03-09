import requests ,random ,time ,os #line:1

if "TG_USER_ID"in os .environ and os .environ ["TG_USER_ID"]:#line:5
        TG_BOT_TOKEN ='1698539466:AAG4K86swWWty6AxeHf58sifhfjXhusiqCM'#line:6
        TG_USER_ID =os .environ ["TG_USER_ID"]#line:7
        print ("Telegram 推送打开")#line:8
def fristlogin ():#line:10
    O000OO0OO000000OO ='bdEH5jnTfBaGhFywTMIscbf{a}w{b}i{c}{d}{e}P/w2SIZlbirzi7yJ2m'.format (a =random .randint (1 ,9 ),b =random .randint (1 ,9 ),c =random .choice ('ABCDEFG'),d =random .choice ('ABCDEFGH'),e =random .choice ('ABCDEFG'))#line:11
    O00OOOO0OOOOO0000 ={'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-cn','Connection':'keep-alive','Host':'pwb.wubabanjia.net','Origin':'https://web.wubabanjia.net','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E176 Safari/604.1','X-AFDAC809-9AD768A3':O000OO0OO000000OO }#line:20
    O00OOO0000OO0O000 ='https://pwb.wubabanjia.net/v1/fastlogin'#line:21
    O0O0O0O00OOOOO00O =0 #line:22
    while O0O0O0O00OOOOO00O <=10 :#line:23
        O0O0O0O00OOOOO00O +=1 #line:24
        try :#line:25
            OOO0000OOOOOO0O0O =requests .get (O00OOO0000OO0O000 ,headers =O00OOOO0OOOOO0000 )#line:26
            if OOO0000OOOOOO0O0O .status_code ==200 :#line:27
                print (OOO0000OOOOOO0O0O .json ()['response']['token'])#line:28
                return OOO0000OOOOOO0O0O .json ()['response']['token']#line:29
                break #line:30
        except Exception as O00OOOOOO0000OO0O :#line:31
            print (O00OOOOOO0000OO0O )#line:32
            time .sleep (10 )#line:33
    else :#line:34
        print ('网络问题，等待下一次邀请！')#line:35
        telegram_bot ('Lutup','网络问题，等待下一次邀请！')#line:36
        exit()
def register_email (OOO000OOOOO00O000 ):#line:38
    O0OO00OO00OOO000O ='{}@qq.com'.format (random .randint (1000000 ,99999999 ))#line:39
    print (O0OO00OO00OOO000O )#line:40
    OOO00O00OOO00OO00 ={'platform':(None ,'uj72624275'),'email':(None ,O0OO00OO00OOO000O ),'password':(None ,'sdEWWEqqCEWW@!')}#line:45
    O0OO00O0O0O000OO0 ='https://pwb.wubabanjia.net/v1/register/email?token={}'.format (OOO000OOOOO00O000 )#line:46
    O0O0OO00O00OOO00O =requests .post (O0OO00O0O0O000OO0 ,files =OOO00O00OOO00OO00 )#line:48
def main ():#line:84
    if 'START' in os.environ and os.environ["START"] =='JKASNDWKND':
        O00000OO00OOOO0OO =fristlogin ()#line:85
        time .sleep (5 )#line:86
        register_email (O00000OO00OOOO0OO )#line:87
        time .sleep (5 )#line:88
        invite (O00000OO00OOOO0OO )#line:89
    else:
        telegram_bot ('撸先生','没有启动码，请去188极速列车公众号查看文章获取！')#li
def telegram_bot (O0O0O0OOOOOOO0O00 ,O0O00O000000O0O00 ):#line:50
    print ("\n")#line:51
    O0OOO0000OOOO0OO0 =TG_BOT_TOKEN #line:52
    OOO000O00O00O000O =TG_USER_ID #line:53
    if "TG_BOT_TOKEN"in os .environ and "TG_USER_ID"in os .environ :#line:54
        O0OOO0000OOOO0OO0 ='1698539466:AAG4K86swWWty6AxeHf58sifhfjXhusiqCM'#line:55
        OOO000O00O00O000O =os .environ ["TG_USER_ID"]#line:56
    if not O0OOO0000OOOO0OO0 or not OOO000O00O00O000O :#line:57
        print ("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")#line:58
        return #line:59
    print ("Telegram 推送开始")#line:60
    OO0OOO000OOOOOOOO ={"chat_id":OOO000O00O00O000O ,"text":O0O0O0OOOOOOO0O00 +'\n\n'+O0O00O000000O0O00 ,"disable_web_page_preview":"true"}#line:62
    OO0OO00000OO0O0O0 =requests .post (url ='https://api.telegram.org/bot%s/sendMessage'%(O0OOO0000OOOO0OO0 ),data =OO0OOO000OOOOOOOO )#line:64
    print (OO0OO00000OO0O0O0 .text )#line:65
def invite (OO0OO0OOOO00000OO ):#line:66
    OOO0OOOO00OO0OO00 =os .environ ["INVITECODE"]#line:67
    OO0O0OOO0000OO00O ={'code':(None ,OOO0OOOO00OO0OO00 )}#line:68
    O00OOOO000O00OO00 ='https://pwb.wubabanjia.net/v1/user/invite?token={}'.format (OO0OO0OOOO00000OO )#line:69
    OO00OOOOO000O0O00 =requests .post (O00OOOO000O00OO00 ,files =OO0O0OOO0000OO00O )#line:71
    print (OO00OOOOO000O0O00 .text )#line:72
    choice_vip ()#line:73
def choice_vip ():#line:74
    if 'TOKEN'in os .environ :#line:76
        O000OO0OO000O0OO0 =os .environ ["TOKEN"]#line:77
        O0O0000OO000OO0OO ='https://pwb.sjzrongshida.cn/v1/lottery/1?token={}'.format (O000OO0OO000O0OO0 )#line:78
        OO0O00OO000O00O00 =requests .post (O0O0000OO000OO0OO )#line:79
        time .sleep (2 )#line:80
        telegram_bot ('撸先生','邀请完成！随机抽奖完成！')#line:81
    else :#line:82
        telegram_bot ('撸先生','邀请完成！未开启随机抽奖！（需要抽奖请填写TOKEN)')#line:83

if __name__ =='__main__':#line:90
    main ()
