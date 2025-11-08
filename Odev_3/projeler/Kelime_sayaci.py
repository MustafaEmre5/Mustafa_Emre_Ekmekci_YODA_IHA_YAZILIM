def kelime_sayaci_analiz(metin):
    # Fonksiyonun büyük/küçük harf duyarlılığı hakkında açıklama:
    # Program, kelimeleri sayarken ve tekrarları bulurken büyük/küçük harf duyarsız olacaktır.
    # Örneğin, "Elma" ve "elma" aynı kelime olarak kabul edilecektir.
    # Bunun için, analize başlamadan önce tüm metni küçük harfe çeviriyoruz.

    print("--- Analiz Başlatılıyor ---")
    print(f"Orijinal Metin: '{metin}'\n")

    # 1. Toplam Karakter Sayısı (Boşluklar dahil)
    # len() fonksiyonu ile metindeki tüm karakterlerin sayısını hesaplıyoruz.
    toplam_karakter_sayisi = len(metin)

    # 2. Metni Hazırlama ve Kelimelere Ayırma
    # Tüm metni küçük harfe çeviriyoruz.
    kucuk_harf_metin = metin.lower()

    # Kelimeleri ayırmadan önce, noktalama işaretlerini boşlukla değiştiriyoruz.
    # Bu, "kitap." ve "kitap" kelimelerinin ayrı sayılmasını engeller.
    noktalama_isaretleri = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    temiz_metin = kucuk_harf_metin
    for karakter in noktalama_isaretleri:
        temiz_metin = temiz_metin.replace(karakter, ' ')

    # Metni boşluklara göre ayırarak bir kelime listesi oluşturuyoruz.
    # list(filter(None, ...)) ifadesi, boş stringleri ("") listeden çıkarır.
    # Bu, ardışık boşlukların veya noktalama işaretlerinin bıraktığı gereksiz boşlukları temizler.
    kelimeler = list(filter(None, temiz_metin.split()))

    # 3. Toplam Kelime Sayısı
    # Kelimeler listesinin uzunluğu, toplam kelime sayısını verir.
    toplam_kelime_sayisi = len(kelimeler)

    # 4. En Uzun Kelimenin Uzunluğu
    en_uzun_kelime_uzunlugu = 0
    if kelimeler: # Eğer listede kelime varsa bu işlemi yap
        # max() fonksiyonu ile kelimeler listesindeki en uzun kelimeyi buluyoruz, key=len ile uzunluğa bakılmasını sağlıyoruz.
        en_uzun_kelime = max(kelimeler, key=len)
        en_uzun_kelime_uzunlugu = len(en_uzun_kelime)
    # Not: Eğer metin tamamen boş veya sadece noktalama işareti içeriyorsa uzunluk 0 kalır.

    # 5. Kelime Tekrar Sayıları (Frekans)
    # Kelime frekanslarını tutmak için bir sözlük (dictionary) kullanıyoruz.
    kelime_frekanslari = {}
    for kelime in kelimeler:
        # Eğer kelime sözlükte daha önce varsa, sayısını 1 artır.
        if kelime in kelime_frekanslari:
            kelime_frekanslari[kelime] += 1
        # Eğer kelime sözlükte yoksa, yeni bir giriş oluştur ve başlangıç değerini 1 yap.
        else:
            kelime_frekanslari[kelime] = 1

    # Sonuçları Ekrana Yazdırma
    print("--- İstatistikler ---")
    print(f"1. Toplam Kelime Sayısı: **{toplam_kelime_sayisi}**")
    print(f"2. Toplam Karakter Sayısı (Boşluklar dahil): **{toplam_karakter_sayisi}**")
    print(f"3. En Uzun Kelimenin Uzunluğu: **{en_uzun_kelime_uzunlugu}**")
    if en_uzun_kelime_uzunlugu > 0:
        print(f"   (En uzun kelime(ler)den biri: '{en_uzun_kelime}')")

    print("\n4. Kelime Tekrar Sayıları (Frekans Listesi):")
    # Sözlükteki kelimeleri alfabetik sıraya göre ekrana yazdırıyoruz.
    for kelime, sayi in sorted(kelime_frekanslari.items()):
        print(f"   - '{kelime}': {sayi} kez")

    print("\n--- Analiz Tamamlandı ---\n")

# --- Programın Çalıştırılması İçin Örnek Kullanım ---
# Kullanıcıdan bir metin girmesini istiyoruz.
kullanici_metni = input("Lütfen analiz etmek istediğiniz bir cümle veya paragraf girin: ")

# Fonksiyonu, kullanıcıdan alınan metin ile çağırıyoruz.
kelime_sayaci_analiz(kullanici_metni)
