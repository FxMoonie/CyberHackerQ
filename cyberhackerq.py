import time
from top_10 import lue_top_10, paivita_top_10, tulosta_top_10
from kysymysten_logiikka import kysy_kysymykset

def main():
    print()
    print("Valitse testin kesto:")
    print()
    print("1. 2 minuutin testi")
    print("2. 5 minuutin testi")
    print("3. 10 minuutin testi")
    
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
