CHARACTERS = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random

def sifreleri_kaydet(sifre, hesap):
    with open("şifreler.txt", "a", encoding="utf8") as doc:
        doc.write(f"{hesap}:   {sifre}\n")

def sifre_olustur(karakter_sayisi):
    sifre = ""
    for i in range(karakter_sayisi):
        sifre += random.choice(CHARACTERS)
    return sifre
if __name__ == "__main__":
    karakter_sayisi = int(input("kaç karakterli bir şifre istersin?"))
    yeni_sifre = sifre_olustur(karakter_sayisi)
    print(f"Yeni şifreniz: {yeni_sifre}")

    hesap = input("bu hangi hesabın şifresi olsun")
    sifreleri_kaydet(yeni_sifre, hesap)