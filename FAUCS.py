#read the README.md
#the tutorial: https://streamable.com/ei0wo2
__author__ = "CS"
__FileName__   = "Forward Assault Updated Credit Script[FAUCS]"
__version__ = "1.38H00"
__desc__   = "this script works for mobile aswell :D as of 21 Jul 2021"
__date__   = "21 Jul 21"
class CSnice:
        banner = '''
███████╗ █████╗ ██╗   ██╗ ██████╗███████╗
██╔════╝██╔══██╗██║   ██║██╔════╝██╔════╝
█████╗  ███████║██║   ██║██║     ███████╗
██╔══╝  ██╔══██║██║   ██║██║     ╚════██║
██║     ██║  ██║╚██████╔╝╚██████╗███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝
Forward Assault Updated  Credit  Script                                                                  
'''
        dec = "                Works with PC and MOBILE accounts! version 1.38H00"
import requests, hashlib, threading, re, os, time, getpass
from termcolor import colored
try:
    os.system("clear")
    print(colored(CSnice.banner, 'blue'))
    print(colored(CSnice.dec, 'red'))
    help = input(colored("[y]help?:~$ ", 'green'))
    try:
        if(help.lower() == "y"):
            print("\nthis program was created by CS(ooCSoo, iamCS, testaccountcs123, oooCSooo)")
            print("bad choice to copyright strike my channel")
            print("i was leaving the game, now i want to take")
            print("this game to the fucking grave, dumbasses")
            print("this program was made to make credit exploitation easy.")
            print("anyways, im guessing you need to find out how to find the pubg")
            print("here is an exmaple of how to find it, https://imgur.com/a/iR2Ea0t")
            print("press f12 on the crazygames.com/game/forward-assault and move to networks")
            print("then search for getaccountinfoWebgl.php after you login in the game and press on it")
            print("of course this will also work for mobile")
            print("you will have to either have all caps or no caps username, to get the pubg when you are login in")
            print("so just look out for that \n ~ yours truly CS")
    except:
        print(colored('[-1] wrong input!', 'red'))
    username = input(colored("username?:~$ ", 'green'))
    password = getpass.getpass(prompt = colored("password?:~$ ", 'green'))
    pubg = input(colored("pubg?:~$ ", 'green'))
    thred = 50
    encoded=password.encode()
    result = hashlib.sha512(encoded)
    url = "https://fa.blayzegames.com/OnlineAccountSystem_NewFPS/getaccountinfoWebgl.php?"
    login_data = {
        "username": username,
        "password": result.hexdigest(),
        "pubg": pubg,
        "d_username": "",
        "d_kills": "0",
        "d_deaths": "0",
        "d_totalWins": "0",
        "d_totalLosses": "0",
        "d_headshots": "0",
        "d_mWonLastChg": "0",
        "platform": "WebGL",
        "version": "1.2013",
        "d_timePlayed": "0",
        "d_glovesEquipped": "0",
        "d_assists": "0",
        "store": "WEB",
        "d_credits": "10000",
    }
    req = requests.post(url, data=login_data).text
    try:
        if(req == "-3"):
            print(colored('[-3] outdated or not working pubg!', 'red'))
            exit
        elif(req == "-2"):
            username = username.upper()
            req = requests.post(url, data=login_data).text
            if (req == "-2"):
                username = username.lower()
                req = requests.post(url, data=login_data).text
                if(req == "-2"):
                    print(colored('[-2] wrong password or username(tried mobile)!', 'red'))
            exit
        else:
            os.system("clear");print(colored('[0] Worked!', 'green'))
            time.sleep(1)
            os.system("clear");print(colored('Starting In 3!', 'green'))
            time.sleep(1)
            os.system("clear");print(colored('Starting In 2!', 'green'))
            time.sleep(1)
            os.system("clear");print(colored('Starting In 1!', 'green'))
            time.sleep(1);os.system("clear")
            def threadFunc():
                while True:
                    try:
                        req = requests.post(url, data=login_data).text
                        x = re.search("(?<=credits>).*?(?=</credits>)",req).group()
                        print("press "+colored("|Stop", "green")+" to exit, credits: "+colored(x, "green")+"!", end='\r')
                    except:
                        pass         
            try:        
                threads = []
                for i in range(thred):
                    t = threading.Thread(target=threadFunc)
                    t.daemon = True
                    threads.append(t)
                for i in range(thred):
                    threads[i].start()
                for i in range(thred):
                    threads[i].join()
            except:
                pass          
    except:
        pass
except:
    pass
