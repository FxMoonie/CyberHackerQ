import time
import os

top_10 = {
    2 * 60: [],
    5 * 60: [],
    10 * 60: []
}

def lue_top_10(kesto):
    tiedoston_nimi = f"top_10_{kesto // 60}min.txt"
    if os.path.exists(tiedoston_nimi):
        with open(tiedoston_nimi, "r") as tiedosto:
            for rivi in tiedosto.readlines()[1:]:
                osio = rivi.strip().split(": ")
                if len(osio) == 2:
                    nimi, pisteet = osio[0], int(osio[1].split()[0])
                    top_10[kesto].append((nimi, pisteet))

def arvioi_suoritus(pisteet, kesto):
    if kesto == 2 * 60:
        if pisteet >= 10:
            return "Erittäin hyvä!"
        elif pisteet >= 8:
            return "Hyvä!"
        elif pisteet >= 5:
            return "Kohtalainen."
        else:
            return "Heikko. Yritä uudestaan."
    elif kesto == 5 * 60:
        if pisteet >= 20:
            return "Erittäin hyvä!"
        elif pisteet >= 16:
            return "Hyvä!"
        elif pisteet >= 10:
            return "Kohtalainen."
        else:
            return "Heikko. Yritä uudestaan."
    elif kesto == 10 * 60:
        if pisteet >= 30:
            return "Erittäin hyvä!"
        elif pisteet >= 24:
            return "Hyvä!"
        elif pisteet >= 15:
            return "Kohtalainen."
        else:
            return "Heikko. Yritä uudestaan."
    else:
        return "Virheellinen kesto."

def paivita_top_10(nimi, pisteet, kesto):
    for i in range(len(top_10[kesto])):
        if top_10[kesto][i][0] == nimi:
            if top_10[kesto][i][1] < pisteet:
                top_10[kesto][i] = (nimi, pisteet)
            return
    top_10[kesto].append((nimi, pisteet))
    top_10[kesto] = sorted(top_10[kesto], key=lambda x: x[1], reverse=True)[:10]
    tallenna_top_10(kesto)

def tallenna_top_10(kesto):
    tiedoston_nimi = f"top_10_{kesto // 60}min.txt"
    with open(tiedoston_nimi, "w") as tiedosto:
        tiedosto.write(f"Top 10 -lista ({kesto // 60} minuutin testi) - Aika: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        for nimi, pisteet in top_10[kesto]:
            tiedosto.write(f"{nimi}: {pisteet} pistettä\n")  

def tulosta_top_10(kesto):
    print(f"\nTop 10 -lista ({kesto // 60} minuutin testi):")
    for i, (nimi, pisteet) in enumerate(top_10[kesto]):
        print(f"{nimi}: {pisteet} pistettä")  
