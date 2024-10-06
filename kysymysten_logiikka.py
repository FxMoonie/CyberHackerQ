import time
import random
from kysymykset import kysymykset
from top_10 import paivita_top_10, arvioi_suoritus, tulosta_top_10

def kysy_kysymykset(kesto):
    pisteet = 0
    kysymys_lista = list(kysymykset.items())
    random.shuffle(kysymys_lista)

    kysymys_laskuri = 0  
    aloitusaika = time.time()

    try:
        for kysymys, data in kysymys_lista:
            if time.time() - aloitusaika >= kesto:
                print("\nAikaraja ylitetty.")
                break
            
            print(f"\033[92m{kysymys}\033[0m")
            print()
            for vaihtoehto in data["vaihtoehdot"]:
                print(vaihtoehto)
            vastaus = input("\033[92mValitse oikea vastaus (a, b, c, d): \033[0m").strip().lower()

            if vastaus == data["oikea"]:
                print("Oikein!\n")
                pisteet += 1
                time.sleep(0.5)
            else:
                print(f"Väärin! Oikea vastaus oli {data['oikea']}.\n")
                time.sleep(0.5)

            kysymys_laskuri += 1

    except KeyboardInterrupt:
        print("\nOhjelma keskeytetty.")
    
    print(f"Sait {pisteet}/{kysymys_laskuri} oikein.")
    arvio = arvioi_suoritus(pisteet, kesto)
    print(arvio)

    aikaraja_ylitetty = time.time() - aloitusaika >= kesto

    if aikaraja_ylitetty:
        nimi = input("Anna nimesi tallentaaksesi pisteesi top 10 -listalle: ").strip()
        paivita_top_10(nimi, pisteet, kesto)
        tulosta_top_10(kesto)
        print()
    else:
        print("Aikaraja ei ylitetty, top 10 -lista ei päivity.")
