import os
import time
from colorama import Fore, Back, Style
import itertools
import threading
import sys
import webbrowser



AceAgain = False
clear = lambda: os.system('cls')
clear()
done = False
def animate():
    for c in itertools.cycle(['Made By : itzmeclay ']):
        if done:
            break
        sys.stdout.write(Fore.CYAN + '\rLoading | '+ Fore.RED + c )
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\r1st extrap bin ')

t = threading.Thread(target=animate)
t.start()

time.sleep(5)
done = True


clear()
clear()
print(Fore.RED + """
  ______   __         ______   __      __ 
 /      \ /  |       /      \ /  \    /  |
/$$$$$$  |$$ |      /$$$$$$  |$$  \  /$$/ 
$$ |  $$/ $$ |      $$ |__$$ | $$  \/$$/  
$$ |      $$ |      $$    $$ |  $$  $$/   
$$ |   __ $$ |      $$$$$$$$ |   $$$$/    
$$ \__/  |$$ |_____ $$ |  $$ |    $$ |    
$$    $$/ $$       |$$ |  $$ |    $$ |    
 $$$$$$/  $$$$$$$$/ $$/   $$/     $$/     
                                          
                                          
""")
time.sleep(1)
print(Fore.CYAN + "\nWelcome To Extrap Maker  \n")
time.sleep(2)

print(Fore.MAGENTA + "If You Are Done With The Requirements, Take You Bin And \n Generate Some CC Using namso-gen.com \n")
time.sleep(3)
clear()
clear()



def step2(cc1, cc2):
  liststr1 = list(cc1)
  liststr2 = list(cc2)
  a = int(liststr1[9])
  b = int(liststr1[10])
  ms = round(((a + b)/2)*5)
  c = int(liststr2[9])
  d = int(liststr2[10])
  ms2 = round(((c + d)/2)*5)

  msfinal = ms + ms2
  msfinall = str(msfinal)
  liststr1[9] = "x"
  liststr2[9] = "x"
  liststr1[10] = "x"
  liststr2[10] = "x"

  mslist = list(msfinall)

  for i in range(8,10):
    for j in range(0,2):
      liststr1[i] = msfinall[j]
      liststr2[i] = msfinall[j]
  joinedfinal1 = "".join(liststr1)
  joinedfinal2 = "".join(liststr2)
  print(f"\nHere Is Your Extrap : {joinedfinal1}")
  print(f"\nHere Is Your Second Extrap : {joinedfinal2} \n")

  choice = input(Fore.RED + "Do You Want To Make Another Extrap (Y/N)? : ").upper()
  if choice == "Y" or "YES":
    chk()
  else:
    quit()



def maker(ace1, ace2, ace):
    clear()

    #Ace : For Gen1

    lastfrmgen1 = 0
    lisst = [int(x) for x in str(ace1)]
    s = [str(i) for i in lisst[0:12]]
    lastfrmgen1 = int("".join(s))

    #Ace : For Gen2

    lastfrmgen2 = 0
    lisst = [int(x) for x in str(ace2)]
    s1 = [str(i) for i in lisst[0:12]]
    lastfrmgen2 = int("".join(s1))

    #Ace : For Live

    lastfrmlive = 0
    lisst = [int(x) for x in str(ace)]
    s3 = [str(i) for i in lisst[-4:]]
    lastfrmlive = int("".join(s3))

    sjoinedgen1 = str(lastfrmgen1)
    sjoinedgen2 = str(lastfrmgen2)
    sjoinedlive = str(lastfrmlive)

    joinedgen1 = sjoinedgen1 + sjoinedlive
    joinedgen2 = sjoinedgen2 + sjoinedlive

    clear()
    
    print(Fore.MAGENTA + "")
    listgen1 = list(joinedgen1)
    listgen1[7] = "x"
    listgen1[9] = "x"
    listgen1[11] = "x"
    listgen1joined = "".join(listgen1)

    listgen2 = list(joinedgen2)
    listgen2[7] = "x"
    listgen2[9] = "x"
    listgen2[11] = "x"
    listgen2joined = "".join(listgen2)

    print(f"\n\nBasic Extrapped CC 1 : {listgen1joined} \n")
    time.sleep(1)
    print(Fore.BLUE + "")
    print(f"Basic Extrapped CC 2 : {listgen2joined} \n")

    print(Fore.RED + "Now We Can Proceed, \n")
    print(Fore.CYAN + "Copy These And Generate CC Using Them \n")
    time.sleep(1)
    print(Fore.RED + "Opening CC Gen  <3 \n")
    time.sleep(3)
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("www.namso-gen.com")
    print("\n")
    sgen1 = input(Fore.CYAN + "Enter Any CC Number From The Extrap I Gave You To Generate : ")
    sgen2 = input(Fore.CYAN + "Enter Any Other CC Number From The Other Extrap I Gave You : ")
    sgen1list = list(sgen1)
    sgen2list = list(sgen2)
    for digit in sgen1list[-5:]:
      for i in  range(11, 16):
        sgen1list[i] = "x"
    sgen1list[8] = "x"
    stringnew = "".join(sgen1list)

    for digit in sgen2list[-5:]:
      for i in  range(11, 16):
        sgen2list[i] = "x"
    sgen2list[8] = "x"
    stringnew2 = "".join(sgen2list)
    step2(stringnew, stringnew2)

    

def chk():
    clear()

    gen1 = int(input(Fore.RED + "Enter The First Generated CC Number (Only CC Number) : \033[1;32;40m"))
    gen2 = int(input(Fore.RED + "Enter The Second Generated CC Number (Only CC Number) :\033[1;32;40m "))
    livecc = int(input("\033[1;32;40mEnter Any Live CC Number : \033[38;2;255;255;255m"))
    if len(str(gen1)) < 16 or len(str(gen1)) > 16 and len(str(gen2)) < 16 or len(str(gen2)) > 16 and len(str(livecc)) < 16 or len(str(livecc)) > 16:
        clear()
        print("Bruh! Enter Valid CC Numbers...")
        time.sleep(2)
        clear()
        global AceAgain
        AceAgain = True
    else :
        maker(gen1, gen2, livecc)
    while AceAgain==True:
        chk()
    
chk()
