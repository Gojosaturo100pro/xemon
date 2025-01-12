import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime

class FacebookAutoCreate:
    def __init__(self):
        self.ok = []
        self.cp = []
        self.loop = 0
        self.gender = []
        self.logo = '''   
   ▗▄▖ ▗▖ ▗▖▗▄▄▄▖▗▄▖ 
  ▐▌ ▐▌▐▌ ▐▌  █ ▐▌ ▐▌
  ▐▛▀▜▌▐▌ ▐▌  █ ▐▌ ▐▌
  ▐▌ ▐▌▝▚▄▞▘  █ ▝▚▄▞▘
========================================
  OWNER  : MD_IMRAN_SHEIKH
  GITHUB : VAMPIRE-404
  TOOL   : AUTO-CREATE
========================================'''
        self.boy = ["Imran Sheikh", "Imran Khan", "Imran Ali"]
        self.infinix = random.choice(['7060', '8076D'])
        self.ua = f"Mozilla/5.0 (Linux; Android 7.0; {self.infinix} Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(80, 105)}.0.{random.randrange(1000, 5000)}.{random.randrange(100, 399)} Mobile Safari/537.36"
    
    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(self.logo)

    def line(self):
        print('========================================')

    def get_headers(self):
        return {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua,
        }

    def start(self):
        self.clear()
        print(' [1] AUTO CREATE')
        print(' [2] EXIT ')
        self.line()
        gen = input(' CHOICE : ')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            exit()
        else:
            self.gender.append('boy')

        self.clear()
        print(" LIMIT = 1000-10000-100000")
        self.line()
        lim = int(input(' LIMIT : '))
        self.clear()
        headers = self.get_headers()

        for x in range(lim):
            sys.stdout.write(f"\r[LOADING-AUTO] {self.loop} | OK: {len(self.ok)} | CP: {len(self.cp)}")
            sys.stdout.flush()

            if 'boy' in self.gender:
                name = random.choice(self.boy).split(' ')
                sex = '2'

            self.loop += 1

            try:
                session_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=26))
                response = requests.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={session_id}&_={int(datetime.now().timestamp() * 1000)}").json()
                email = response["permalink"]["mail"]
                session = response["session_id"]
            except (KeyError, requests.exceptions.ConnectionError) as e:
                continue

            password = 'VAMPIRE@IMRAN404'

            try:
                ses = requests.Session()
                reg_page = ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                logger_id = re.search('name="logger_id" value="(.*?)"', reg_page.text).group(1)
                form = BeautifulSoup(reg_page.text, 'html.parser').find('form', {'id': 'mobile-reg-form'})

                data = {v['name']: v.get('value', '') for v in form.find_all('input') if v.get('name')}
                data.update({
                    "firstname": name[0],
                    "lastname": name[1],
                    "birthday_day": str(random.randint(1, 28)),
                    "birthday_month": str(random.randint(1, 12)),
                    "birthday_year": str(random.randint(1992, 2004)),
                    "reg_email__": email,
                    "sex": sex,
                    "reg_passwd__": password,
                    "submit": "Sign Up",
                })

                response = ses.post('https://m.facebook.com' + form['action'], headers=headers, data=data)
                cookies = ses.cookies.get_dict()

                # কুকি যাচাই করে OK এবং CP আলাদা করা
                if cookies.get('c_user'):
                    self.ok.append(f"{email} | {password}")
                    print(f'\r [OK] {email} | {password} ')
                    print(f'\r [COOKIE] {cookies.get("c_user")}')
                else:
                    self.cp.append(f"{email} | {password}")
                    print(f'\r [CP] {email} | {password} ')
            except Exception as e:
                continue

if __name__ == "__main__":
    FacebookAutoCreate().start()