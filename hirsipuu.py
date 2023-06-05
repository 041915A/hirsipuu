import random

# Kysytään pelaajalta, haluaako hän pelata peliä.
def kysy_pelataanko():
    while True:
        pelataanko_vastaus = input("Haluatko pelata Hirsipuuta? (Kyllä/Ei): ").lower()
        # Palautetaan True, jos pelaaja haluaa pelata.
        if pelataanko_vastaus == "kyllä":
            return True
        
        # Palautetaan False, jos pelaaja ei halua pelata.
        elif pelataanko_vastaus == "ei":
            return False
        else:
            print("Antamasi vastaus oli epäselvä. Kokeile uudelleen.")

# Tiedostosta valitaan satunnainen sana.
def valitse_sana():
    # Avataan tiedosto sanalista.txt 
    with open ("sanalista.txt") as tiedosto:
        # Luetaan tiedosto ja jaetaan rivit listaksi.
        rivit = tiedosto.read().split()
        # Valitaan sana.
        valittu_sana = random.choice(rivit)
    return valittu_sana


# Pelataan hirsipuuta.
def hirsipuu():

    # Tallennetaan valitse_sana() -funktion palautusarvo muuttujaan.
    arvattava_sana = valitse_sana()

    # Määritellään arvattavan sanan pituus.
    sanan_pituus = len(arvattava_sana)

    # Alustetaan arvausten määrä.
    arvausten_maara = 0 

    # Alustetaan lista virheellisille arvauksille.
    virheelliset_arvaukset = [] 

    # Alustetaan lista oikeille arvauksille alaviivoilla sanan pituuden mukaan.
    oikeat_arvaukset = ["_"] * sanan_pituus


    # Pelaajalta pyydetään arvausta kunnes peli päättyy.
    while True:

        # Pelaajalle näytetään pelitilanne.
        print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset)

        arvaus = input("Arvaa kirjain tai sana: ").lower()

        # Jos pelaaja arvaa kirjaimen.
        if len(arvaus) == 1:

            # Jos sama kirjain arvataan.
            if arvaus in virheelliset_arvaukset or arvaus in oikeat_arvaukset:
                print("Olet jo arvannut tuon kirjaimen!")
                # Jatketaan seuraavalle kierrokselle.
                continue 

            # Jos arvaus löytyy sanasta.
            if arvaus in arvattava_sana:

                # Asetetaan kirjain listan oikeille paikoille.
                for i in range(sanan_pituus):
                    if arvattava_sana[i] == arvaus:
                        oikeat_arvaukset[i] = arvaus

                # Jos kaikki kirjaimet on arvattu oikein.
                if "_" not in oikeat_arvaukset:
                    print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset)
                    # Peli päättyy voittoon.
                    print("Onneksi olkoon, voitit pelin!")
                    break 

            # Jos arvaus on väärä.
            else:

                # Päivitetään virheelliset arvaukset ja arvausten määrää.
                virheelliset_arvaukset.append(arvaus)
                arvausten_maara += 1

                # Jos arvausten määrä ylittää sallitun määrän.
                if arvausten_maara == 6:
                    print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset)
                    # Peli päättyy häviöön.
                    print("Hävisit pelin! Arvattava sana oli", arvattava_sana)
                    break

        # Jos pelaaja arvaa sanan.
        elif len(arvaus) > 1:

            # Jos arvaus on oikea.
            if arvaus == arvattava_sana:

                # Arvattava sana muutetaan listaksi, jossa jokainen kirjain on erillinen alkio.
                oikeat_arvaukset = list(arvattava_sana)  
                print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset)
                # Peli päättyy voittoon.
                print("Onneksi olkoon, voitit pelin!")
                break 

            # Jos arvaus on väärä.
            else:

                # Päivitetään virheelliset arvaukset ja arvausten määrää.
                virheelliset_arvaukset.append(arvaus)
                arvausten_maara += 1

                # Jos arvausten määrä ylittää sallitun määrän.
                if arvausten_maara == 6:
                    print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset)
                    # Peli päättyy häviöön.
                    print("Hävisit pelin! Arvattava sana oli", arvattava_sana)
                    break 

        # Jos pelaaja ei anna arvausta.
        else:
            print("Syötä vähintään yksi kirjain tai koko sana!")


# Tulostetaan pelitilanne.
def print_hirsipuu(arvausten_maara, virheelliset_arvaukset, oikeat_arvaukset):

    # Hirsipuun eri vaiheet listassa monirivisinä merkkijonoina.
    hirsipuu_kuvat = [
        """
          +---+
              |
              |
              |
             ===
        """,
        """
          +---+
          O   |
              |
              |
             ===
        """,
        """
          +---+
          O   |
          |   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         /    |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         / \\  |
             ===
        """
    ]

    # Tulostetaan hirsipuu sen mukaan, montako virheellistä arvausta on tehty.
    print(hirsipuu_kuvat[arvausten_maara])

    # Tulostetaan tehdyt virheelliset arvaukset.
    print("Virheelliset arvaukset:", ", ".join(virheelliset_arvaukset))

    # Tulostetaan arvattavan sanan tilanne.
    print("Oikeat arvaukset:", " ".join(oikeat_arvaukset)) 

    # join()-funktio yhdistää listan merkkijonot yhdeksi merkkijonoksi.
    # join()-funktion kutsussa määritellään erotinmerkki.


# Kysytään pelaajalta, haluaako hän pelata uudelleen.
def uusi_peli():
    while True:
        uusi_peli_vastaus = input("Haluatko pelata uudelleen? (Kyllä/Ei): ").lower()
        # Palautetaan True, jos pelaaja haluaa pelata uudelleen.
        if uusi_peli_vastaus == "kyllä":
            return True 
    
        # Palautetaan False, jos pelaaja ei halua pelata uudelleen.
        elif uusi_peli_vastaus == "ei":
            return False 
        
        else:
            print("Antamasi vastaus oli epäselvä. Kokeile uudelleen.")


# Pääohjelma alkaa.
print("---------------------------------------------")
print("| Hei! Tervetuloa pelaamaan Hirsipuu-peliä! |")
print("---------------------------------------------")
print()

# Pyöritetään hirsipuu-peliä, jos pelaaja haluaa pelata.
if kysy_pelataanko():
    while True:
        hirsipuu()

        # Silmukka päättyy, jos pelaaja ei halua aloittaa uutta peliä.
        if not uusi_peli():
            print("Kiitos pelaamisesta!")
            break
else:
    print("Ehkä pelaat seuraavalla kerralla.")