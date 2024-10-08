import time
from top_10 import lue_top_10, paivita_top_10, tulosta_top_10
from kysymysten_logiikka import kysy_kysymykset

RED = "\033[31m"  
GREEN = "\033[32m"
RESET = "\033[0m"  


cyberhackerq_logo = f"""
{RED}  ______      __              __  __           __             ____  
 / ____/_  __/ /_  ___  _____/ / / /___ ______/ /_____  _____/ __ \\ 
/ /   / / / / __ \\/ _ \\/ ___/ /_/ / __ \` ___/ //_/ _ \\/ ___/ / / / 
/ /___/ /_/ / /_/ /  __/ /  / __  / /_/ / /__/ ,< /  __/ /  / /_/ /  
\\____/\\__, /_.___/\\___/_/  /_/ /_/\\__,_/\\___/_/|_|\\___/_/   \\___\\_\\  
     /____/                                                           {RESET}
"""

author_info = f"{RED}By: Juho K. Leppänen  |  Versio: 0.1{RESET}"
tervetuloa = f"{GREEN}CyberHackerQ auttaa sinua kehittämään ja kertaamaan kyberturvallisuustaitojasi.\nOta haaste vastaan ja paranna osaamistasi!{RESET}\n"

print(cyberhackerq_logo)
print(author_info)
print()
print(tervetuloa)

def main():
    print()
    print("Valitse testin kesto:")
    print()
    print("1. 2 minuutin testi")
    print("2. 5 minuutin testi")
    print("3. 10 minuutin testi")
    print()
    valinta = input("Valintasi (1, 2, tai 3): ").strip()
    
    if valinta == "1":
        kesto_sek = 2 * 60
        print()
        print("Valitsit 2 minuutin testin, yritä vastata mahdollisimman moneen kysymykseen oikein")
        print()
        time.sleep(1.2)
    elif valinta == "2":
        kesto_sek = 5 * 60
        print()
        print("Valitsit 5 minuutin testin, yritä vastata mahdollisimman moneen kysymykseen oikein")
        print()
        time.sleep(1.2)
    elif valinta == "3":
        kesto_sek = 10 * 60
        print()
        print("Valitsit 10 minuutin testin, yritä vastata mahdollisimman moneen kysymykseen oikein")
        print()
        time.sleep(1.2)
    else:
        print("Virheellinen valinta.")
        return
    
    kysy_kysymykset(kesto_sek)

if __name__ == "__main__":
    lue_top_10(2 * 60)
    lue_top_10(5 * 60)
    lue_top_10(10 * 60)
    main()
