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
    for c in itertools.cycle(['Made By : AceDommete '' | XGOLD', ' JOIN : @thegoldcc']):
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

  
  .   . .    .  .    .  .    .  .    . .:.   .  .    .  .    .  .    .  .       
    .     .    .  .    .  .    .  .    :8  .  .   .    .  .    .  .    .  . .  .
  .    .   .       .       .       . :t: %8    .   .       .       .            
     .   .   .  .    .  .    .  .  .S88 S S88:   .   .  .    .  .    .  .  . .  
  .    .   .:  .  .   .   .   .   :8X8;88@@88Xt     .    .    .   . :: .       .
    .     .;tS.     .   .   .   .S8@tX@%8@@8S888t .   .    .    .  88X   . .    
  .   .     ;8:8.         .   .S@.St88888@88X88@88. .   .   .    8@88;.      .  
    .   .   S8@8;. .  .       %@ 8888S88888888@8:88       .   . @@tX :   .    . 
  .      .  S8%S@S%  .  .  .   8S8X8 8@888888@8@88t .  .    . t:8S888. .   .    
     . .   .:X@8888 t     .  ... @888888@888@88;t:       .  :%8888@8S.       .  
  .         .:888888@% .      .X%  8X88@88:S8 @ ;;. . .    ;S88888@ : .  .     .
    .  . .   8888888S88:  ..%88 @88%@8SS8S888X;888S8t.  . 8888@8%88S   .   .    
  .        . :88888X@;@ .SS88888.:X8; t;88@%:%888. % 8;%. %S888:888S .       .  
    . .  .   . 8888S.  S8 %888888@8@.: :t:   ;888888@8.8X%.  X %88X.    . .    .
  .         ..%8@88.:@X88S888@8 8%;;S8S   t88%;t@8888S88@88@:% 888:.  .     .   
     . .  .   :@t;S8@8X:8;88 8%%%8@@888X88888@8 @: 8@888;88 8.@..X%     .     . 
  .             t88888@;8@8t.:: :88X88888888888SX..: :88888;.888S   .  .  .     
    .  . .  .  S8888888S88;%888.: SX888@88 @8@8S.888%S::@S88:88888.         .  .
  .          . S88@8X:8%%88888:;S8: %888888888;88 88%@S8;:88888888.. .  . .     
    . .  .     %@X8S8..t8888@;88@88; ;t@8888X 888.%8@888X8..@8888S..         .  
  .       .  . .;88t:t8888888@X88@88@;;@888.t8888;8@888888X8;.888%.  . .  .     
     . .      . %:.:8888888888X;88@S;::%S%;tS88@@ @8.8888  888  X           .  .
  .      . .    ..:%88 @88888888888888888888@888@8@ 8t888@% 88:   .  .  . .     
    .  .     . ..8S88 88X%  8 8 88888X%tS@@8888  8.8t%@88X8.@88S:  .         .  
  .       .     .S888SS@S88888888888888888@8@888888888 8t888XS88:    . .  .     
    . . .     .  ;X:t88t:S;t:%t%;St%;;:::.;:t%;t;%%; ;:;.:S S8@S  .         .  .
  .        .     .  888@XSX%%%%;.    .     .   .;tttttttX88SS;;    .  .  .      


                                    
""")
time.sleep(1)
print(Fore.CYAN + "\nWelcome To Ace Extrap Maker by @thegoldcc!! \n")
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
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://t.me/thegoldcc")
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

    print(Fore.CYAN + """
   █████████     ███████    █████       ██████████     █████████    █████████                                     
  ███░░░░░███  ███░░░░░███ ░░███       ░░███░░░░███   ███░░░░░███  ███░░░░░███                                    
 ███     ░░░  ███     ░░███ ░███        ░███   ░░███ ███     ░░░  ███     ░░░                                     
░███         ░███      ░███ ░███        ░███    ░███░███         ░███                                             
░███    █████░███      ░███ ░███        ░███    ░███░███         ░███                                             
░░███  ░░███ ░░███     ███  ░███      █ ░███    ███ ░░███     ███░░███     ███                                    
 ░░█████████  ░░░███████░   ███████████ ██████████   ░░█████████  ░░█████████                                     
  ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░ ░░░░░░░░░░     ░░░░░░░░░    ░░░░░░░░░                                      
                                                                                                                  
                                                                                                                  
                                                                                                                  
   █████████                     ██████████                                                      █████            
  ███░░░░░███                   ░░███░░░░███                                                    ░░███             
 ░███    ░███   ██████   ██████  ░███   ░░███  ██████  █████████████   █████████████    ██████  ███████    ██████ 
 ░███████████  ███░░███ ███░░███ ░███    ░███ ███░░███░░███░░███░░███ ░░███░░███░░███  ███░░███░░░███░    ███░░███
 ░███░░░░░███ ░███ ░░░ ░███████  ░███    ░███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███████   ░███    ░███████ 
 ░███    ░███ ░███  ███░███░░░   ░███    ███ ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░    ░███ ███░███░░░  
 █████   █████░░██████ ░░██████  ██████████  ░░██████  █████░███ █████ █████░███ █████░░██████   ░░█████ ░░██████ 
░░░░░   ░░░░░  ░░░░░░   ░░░░░░  ░░░░░░░░░░    ░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░     ░░░░░   ░░░░░░  
                                                                                                                  
                                                                                                                  




    """)
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
    print(Fore.CYAN + """
   █████████     ███████    █████       ██████████     █████████    █████████ 
  ███░░░░░███  ███░░░░░███ ░░███       ░░███░░░░███   ███░░░░░███  ███░░░░░███
 ███     ░░░  ███     ░░███ ░███        ░███   ░░███ ███     ░░░  ███     ░░░ 
░███         ░███      ░███ ░███        ░███    ░███░███         ░███         
░███    █████░███      ░███ ░███        ░███    ░███░███         ░███         
░░███  ░░███ ░░███     ███  ░███      █ ░███    ███ ░░███     ███░░███     ███
 ░░█████████  ░░░███████░   ███████████ ██████████   ░░█████████  ░░█████████ 
  ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░ ░░░░░░░░░░     ░░░░░░░░░    ░░░░░░░░░  
                                                                              
        -------JOIN TELEGRAM FOR MORE HQ TOOLS : @thegoldcc -------                                                                    
                                                                                                                                  
                                                                              
    """)
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