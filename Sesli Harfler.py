import random

# Sesli harf listesi (1-8 numaralı)
sesli_harfler = ["A", "E", "I", "İ", "O", "U", "Ü", "Ö"]

# Gruplar ve n değerleri
gruplar = {
    1: [6, 9],
    2: [6, 9],
    3: [3, 9],
    4: [3, 9],
}

def deney_ve_bul():
    while True:
        tum_sonuclar = {}
        kullanilan_numaralar = set()

        for grup_no, n_listesi in gruplar.items():
            # Rastgele katsayı ve sabit (1-20 arası)
            a = random.randint(1, 20)
            b = random.randint(0, 20)

            grup_sonuclari = []

            for n in n_listesi:
                sonuc = (a * n + b) % 8
                sonuc = 8 if sonuc == 0 else sonuc

                # Eğer bu numara daha önce çıktıysa, başarısız
                if sonuc in kullanilan_numaralar:
                    break

                grup_sonuclari.append(sonuc)
                kullanilan_numaralar.add(sonuc)

            else:
                # Tüm n'ler için benzersiz sonuç bulunduysa kaydet
                tum_sonuclar[grup_no] = {
                    "a": a,
                    "b": b,
                    "sonuclar": grup_sonuclari
                }
                continue  # diğer gruplara geç
            break  # tekrar baştan dene

        # Eğer 4 grup da tamamsa sonuçları döndür
        if len(tum_sonuclar) == 4:
            return tum_sonuclar

# Çalıştır ve sonucu al
sonuclar = deney_ve_bul()

# Sonuçları yazdır
for grup_no, detay in sonuclar.items():
    a, b, sonuclar_list = detay["a"], detay["b"], detay["sonuclar"]
    harfler = [sesli_harfler[s-1] for s in sonuclar_list]

    print(f"Grup {grup_no}: f(n) = ({a}*n + {b}) mod 8")
    for n, s, h in zip(gruplar[grup_no], sonuclar_list, harfler):
        print(f"  n={n} => Sonuç: {s} => Harf: {h}")
    print("")

