import random

# Sessiz harf listesi (21 harf)
sessiz_harfler = [
    "B", "C", "Ç", "D", "F", "G", "Ğ", "H", "J", "K",
    "L", "M", "N", "P", "R", "S", "Ş", "T", "V", "Y", "Z"
]

# Gruplar ve n değerleri
gruplar = {
    1: [3, 6, 9],
    2: [4, 8, 3, 7, 2, 6, 1, 5, 9],
    3: [2, 4, 6, 8, 1, 3, 5, 7, 9],
}

def deney_ve_bul(max_deneme=10000):
    """
    Gruplar için rastgele a, b değerleri dener.
    Tekrarsız sonuçlar bulursa döner, max_deneme kadar dener.
    """
    for _ in range(max_deneme):
        tum_sonuclar = {}
        kullanilan_numaralar = set()

        for grup_no, n_listesi in gruplar.items():
            # a: 1-20, b: 0-20
            a = random.randint(1, 20)  
            b = random.randint(0, 20)

            grup_sonuclari = []

            for n in n_listesi:
                sonuc = (a * n + b) % 21
                # 0 çıktığında, 21 olarak kabul et
                sonuc = 21 if sonuc == 0 else sonuc

                if sonuc in kullanilan_numaralar:
                    break  # Bu grup geçersiz, tekrar dene

                grup_sonuclari.append(sonuc)
                kullanilan_numaralar.add(sonuc)
            else:
                # Bu grup tamam, kaydet
                tum_sonuclar[grup_no] = {
                    "a": a,
                    "b": b,
                    "sonuclar": grup_sonuclari
                }
                continue  # Diğer gruba geç

            # Grup tamamlanamadı, baştan dene
            break

        if len(tum_sonuclar) == 3:
            return tum_sonuclar

    # Hâlâ bulunamadıysa:
    raise ValueError("Yeterli denemede tekrarsız sonuç bulunamadı!")

# Çalıştır ve sonucu al
sonuclar = deney_ve_bul()

# Sonuçları yazdır
for grup_no, detay in sonuclar.items():
    a, b, sonuclar_list = detay["a"], detay["b"], detay["sonuclar"]
    harfler = [sessiz_harfler[s-1] for s in sonuclar_list]

    print(f"Grup {grup_no}: f(n) = ({a}*n + {b}) mod 21")
    for n, s, h in zip(gruplar[grup_no], sonuclar_list, harfler):
        print(f"  n={n:<2} => Sonuç: {s:<2} => Harf: {h}")
    print("")
