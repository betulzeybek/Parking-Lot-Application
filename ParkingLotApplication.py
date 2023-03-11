BIR_TON_GIRIS = 2.5 / 1000
#  Otoparkta kalınan sürelere göre belirtilen ücret değerleri:
AZ_1_TL = 3
TL_1_3 = 5
TL_3_5 = 7
TL_5_10 = 10
TL_10_24 = 14
TL_24 = 15
#  Her sınıf koduna göre süreye bağlı ücretlere uygulanan katsayı değerleri:

KOD_1_KATSAY = 1
KOD_2_KATSAY = 2
KOD_3_KATSAY = 3
KOD_4_KATSAY = 3
KOD_5_KATSAY = 4
KOD_6_KATSAY = 4

#  Saydırma işlemleri için belirlenen değerler:

motosiklet_say = 0
motosiklet_gelir = 0
motosiklet_sure = 0
binek_say = 0
binek_gelir = 0
binek_sure = 0
hafif_binek = 0
minibus_say = 0
minibus_gelir = 0
minibus_sure = 0
otobus_say = 0
otobus_gelir = 0
otobus_sure = 0
kamyon_say = 0
kamyon_gelir = 0
kamyon_sure = 0
tir_say = 0
tir_gelir = 0
tir_sure = 0
ozel_arac_say = 0
agir_arac = 0
az_kalan_arac = 0
cok_kalan_arac = 0
gazi_arac = 0
engelli_arac = 0
yatan_arac = 0
cok_kalan_ozel_arac = 0
max_sure = 0
max_sure_gelir = 0
max_gelir = 0
max_gelir_sure = 0
gazi_arac_sure = 0
engelli_arac_sure = 0
tutar = 0


# Süreye bağlı ücretleri bulmak için kullanılan fonksiyon

def sure_ucret(a):  # a saat değerinden zaman dilimi
    tutar = 0
    if 24 <= a:
        tutar = (a // 24 * TL_24)  # Her 24 saatte bir bir günlük ücret değeriyle çarpma işlemi uygulanıyor.
    a = a % 24  # 24 satten kalan her saat değeri için ücrete ekleme yapılıyor.

    if 0 < a < 1:
        tutar = tutar + AZ_1_TL
    elif 1 <= a < 3:
        tutar = tutar + TL_1_3
    elif 3 <= a < 5:
        tutar = tutar + TL_3_5
    elif 5 <= a < 10:
        tutar = tutar + TL_5_10
    elif 10 <= a < 24:
        tutar = tutar + TL_10_24

    return tutar  # Yazdığımız fonksiyon zamana bağlı ücret değerini buldu.


def zaman(b):  # b dk cinsinden otoparkta kalma süresi
    dakika = b % 60
    saat = b // 60

    if saat >= 24:
        gun = saat // 24
        saat = saat % 24
    else:
        gun = 0
    return f'{gun} gün, {saat} saat, {dakika} dakika'  # Yazdığımız fonksiyon alınan dk değerini gün saat dk cinsine çevirdi.


baska_arac = 'e'

while baska_arac == 'E' or baska_arac == 'e':
    plaka = input('Aracın plakasını giriniz:')

    arac_sinif_kodu = int(input('Aracın sınıf kodunu (1-6) giriniz : '))
    while not 1 <= arac_sinif_kodu <= 6:  # Kullanıcı yanlış girme durumlarını tekrar sorduruyoruz.
        print("!!!! HATALI VERİ !!!!", '\n', "TEKRAR DENEYİNİZ")
        arac_sinif_kodu = int(input('Aracın sınıf kodunu (1-6) giriniz : '))

    arac_agirlik = float(input("Aracınızın ağırlığını giriniz:"))
    while arac_agirlik <= 0:  # Kullanıcı yanlış girme durumlarını tekrar sorduruyoruz.
        print("!!!! HATALI VERİ !!!!", '\n', "TEKRAR DENEYİNİZ")
        arac_agirlik = float(input("Aracınızın ağırlığını (kg) giriniz:"))

    otopark_sure = int(input('Aracınızın otoparkta bulunduğu süreyi dk olarak giriniz: '))
    surucu_isim = input('Adınızı soyadınızı giriniz: ')

    ucret = sure_ucret(otopark_sure / 60)  # Fonksiyon değerimizi parametre atarak değerleri buluyoruz.
    sure = zaman(otopark_sure)

    if arac_sinif_kodu == 1:

        ozel_durum = input("Sürücünün özel durumu nedir? (Y/y G/g E/e)")

        while ozel_durum not in ["Y", "y", "G", "g", "E", "e"]:  # Kullanıcının hatalı veri girme durumlarını tekrar sorduruyoruz.
            print("!!!! HATALI VERİ !!!!", '\n', "TEKRAR DENEYİNİZ")
            ozel_durum = input("Sürücünün özel durumu nedir? (Y/y G/g E/e)")

        katsayi = KOD_1_KATSAY
        arac_sinif_adi = 'Motosiklet'
        motosiklet_say += 1  # Çıktılar için gerekli saydırma işlemleri
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))
        motosiklet_sure += otopark_sure

    elif arac_sinif_kodu == 2:

        ozel_durum = input("Sürücünün özel durumu nedir? (Y/y G/g E/e)")

        while ozel_durum not in ["Y", "y", "G", "g", "E", "e"]:
            print("!!!! HATALI VERİ !!!!", '\n', "TEKRAR DENEYİNİZ")
            ozel_durum = input("Sürücünün özel durumu nedir? (Y/y G/g E/e)")

        katsayi = KOD_2_KATSAY
        arac_sinif_adi = 'Binek'
        binek_say += 1
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))  # Toplam ücrete tanımlamalar yapılıyor
        binek_sure += otopark_sure

        if arac_agirlik < 1000:
            hafif_binek += 1

    elif arac_sinif_kodu == 3:
        katsayi = KOD_3_KATSAY
        arac_sinif_adi = 'Minibüs'
        minibus_say += 1
        ozel_durum = 'y'
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))
        minibus_sure += otopark_sure

    elif arac_sinif_kodu == 4:
        katsayi = KOD_4_KATSAY
        arac_sinif_adi = 'Otobüs'
        otobus_say += 1
        ozel_durum = 'y'
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))
        otobus_sure += otopark_sure

    elif arac_sinif_kodu == 5:
        katsayi = KOD_5_KATSAY
        arac_sinif_adi = 'Kamyon'
        kamyon_say += 1
        ozel_durum = 'y'
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))
        kamyon_sure += otopark_sure

    else:
        katsayi = KOD_6_KATSAY
        arac_sinif_adi = 'Tır'
        tir_say += 1
        ozel_durum = 'y'
        toplam_ucret = ((ucret * katsayi) + (arac_agirlik * BIR_TON_GIRIS))
        tir_sure += otopark_sure

    if (arac_sinif_kodu == 4 or arac_sinif_kodu == 5 or arac_sinif_kodu == 6) and (arac_agirlik > 10000):
        agir_arac += 1

    if (arac_sinif_kodu == 1 or arac_sinif_kodu == 2) and (otopark_sure <= 30):
        az_kalan_arac += 1

    if (arac_sinif_kodu == 3 or arac_sinif_kodu == 4) and (otopark_sure > 1440):
        cok_kalan_arac += 1

    if (otopark_sure > 30 * 1440) or (toplam_ucret > 1000):
        yatan_arac += 1

    if (otopark_sure > 180) and (ozel_durum == 'G' or ozel_durum == 'g' or ozel_durum == 'E' or ozel_durum == 'e'):
        cok_kalan_ozel_arac += 1

    #  Otopark fatura çıktısı
    print("*************************************************")
    print("FATURANIZ")
    print(f'Araç plakası: {plaka}')
    print(f'Araç sınıf adı: {arac_sinif_adi}')
    print(f'Araç ağırlığı: {arac_agirlik} kg')
    print(f'Otoparkta kaldığı süre: {zaman(otopark_sure)}')
    print(f'Sürücü adı ve soyadı: {surucu_isim}')

    if ozel_durum == 'G' or ozel_durum == 'g':
        print('Sürücünün özel durumu: Gazi')
        print('Uygulanan indirim oranı: %100')
        toplam_ucret = 0
        ozel_arac_say += 1
        gazi_arac += 1
        gazi_arac_sure += otopark_sure


    elif ozel_durum == 'E' or ozel_durum == 'e':
        print('Sürücünün özel durumu: Engelli')
        print('Uygulanan indirim oranı: %50')
        toplam_ucret = toplam_ucret / 2
        ozel_arac_say += 1
        engelli_arac += 1
        engelli_arac_sure += otopark_sure

    if arac_sinif_kodu == 1:
        motosiklet_gelir += toplam_ucret

    elif arac_sinif_kodu == 2:
        binek_gelir += toplam_ucret

    elif arac_sinif_kodu == 3:
        minibus_gelir += toplam_ucret

    elif arac_sinif_kodu == 4:
        otobus_gelir += toplam_ucret

    elif arac_sinif_kodu == 5:
        kamyon_gelir += toplam_ucret

    else:
        tir_gelir += toplam_ucret

    if (arac_sinif_kodu == 2) and (toplam_ucret > max_gelir):
        max_gelir = toplam_ucret
        max_gelir_sure = otopark_sure

    print(f'Otopark ücreti: {toplam_ucret:.2f} TL')
    print("*************************************************")

    baska_arac = input('Otoparka giriş yapan başka araç var mı? (E/e/H/h):')

    while baska_arac not in ["E", "e", "H", "h"]:
        print("!!!! HATALI VERİ !!!!", '\n', "TEKRAR DENEYİNİZ") # Kullanıcının hatalı veri girme durumlarını tekrar sorduruyoruz.
        baska_arac = input('Başka araç var mı? (E/e/H/h): ')

    if otopark_sure > max_sure:  # MAX süre ve  MAX gelir değerleri bulunuyor.
        max_sure = otopark_sure
        max_sure_gelir = toplam_ucret

toplam_arac = motosiklet_say + binek_say + minibus_say + otobus_say + kamyon_say + tir_say
toplam_gelir = motosiklet_gelir + binek_gelir + minibus_gelir + otobus_gelir + kamyon_gelir + tir_gelir

print(f'Otoparkı kullanan toplam araç sayısı: {toplam_arac}')
print(f'Otoparkı kullanan motosiklet sayısı: {motosiklet_say}, Tüm araçlar içindeki yüzdesi: %{100 * motosiklet_say / toplam_arac:.2f}')
print(f'Otoparkı kullanan binek sayısı: {binek_say}, Tüm araçlar içindeki yüzdesi: %{100 * binek_say / toplam_arac:.2f}')
print(f'Otoparkı kullanan minibüs sayısı: {minibus_say}, Tüm araçlar içindeki yüzdesi: %{100 * minibus_say / toplam_arac:.2f}')
print(f'Otoparkı kullanan otobüs sayısı: {otobus_say}, Tüm araçlar içindeki yüzdesi: %{100 * otobus_say / toplam_arac:.2f}')
print(f'Otoparkı kullanan kamyon sayısı: {kamyon_say}, Tüm araçlar içindeki yüzdesi: %{100 * kamyon_say / toplam_arac:.2f}')
print(f'Otoparkı kullanan tır sayısı: {tir_say}, Tüm araçlar içindeki yüzdesi: %{100 * tir_say / toplam_arac:.2f}')

print("******************************************************************************************")

print(f'Otopark toplam geliri: {toplam_gelir:.2f} TL')
print(f'Motosiklet araçlarının toplam geliri: {motosiklet_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * motosiklet_gelir / toplam_gelir:.2f}')
print(f'Binek araçlarının toplam geliri:: {binek_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * binek_gelir / toplam_gelir:.2f}')
print(f'Minibüs araçlarının toplam geliri:: {minibus_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * minibus_gelir / toplam_gelir:.2f}')
print(f'Otobüs araçlarının toplam geliri:: {otobus_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * otobus_gelir / toplam_gelir:.2f}')
print(f'Kamyon araçlarının toplam geliri:: {kamyon_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * kamyon_gelir / toplam_gelir:.2f}')
print(f'Tır araçlarının toplam geliri:: {tir_gelir:.2f} TL Tüm gelir içindeki yüzdesi: %{100 * tir_gelir / toplam_gelir:.2f}')

print("******************************************************************************************")

print(f'Motosiklet için araç başına ortalama otoparkta kalma süresi: {zaman(motosiklet_sure // motosiklet_say)}')
print(f'Motosiklet için araç başına ortalama gelir: {motosiklet_gelir / motosiklet_say:.2f} TL')
print(f'Binek için araç başına ortalama otoparkta kalma süresi: {zaman(binek_sure // binek_say)}')
print(f'Binek için araç başına ortalama gelir: {binek_gelir / binek_say:.2f} TL')
print(f'Minibüs için araç başına ortalama otoparkta kalma süresi: {zaman(minibus_sure // minibus_say)}')
print(f'Minibüs için araç başına ortalama gelir: {minibus_gelir / minibus_say:.2f} TL')
print(f'Otobüs için araç başına ortalama otoparkta kalma süresi: {zaman(otobus_sure // otobus_say)}')
print(f'Otobüs için araç başına ortalama gelir: {otobus_gelir / otobus_say:.2f} TL')
print(f'Kamyon için araç başına ortalama otoparkta kalma süresi: {zaman(kamyon_sure // kamyon_say)}')
print(f'Kamyon için araç başına ortalama gelir: {kamyon_gelir / kamyon_say:.2f} TL')
print(f'Tır için araç başına ortalama otoparkta kalma süresi: {zaman(tir_sure // tir_say)}')
print(f'Tır için araç başına ortalama gelir: {tir_gelir / tir_say:.2f} TL')

print("******************************************************************************************")

print(f'Ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranı: %{100 * hafif_binek / binek_say :.2f}')

print("******************************************************************************************")

print(f'Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlara oranı: %{100 * agir_arac / (otobus_say + kamyon_say + tir_say):.2f}')

print("******************************************************************************************")

print(
    f'Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{100 * az_kalan_arac / (motosiklet_say + binek_say):.2f}')

print("******************************************************************************************")

print(f'Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlara oranı: %{100 * cok_kalan_arac / (minibus_say + otobus_say):.2f}')

print("******************************************************************************************")

print(f"Otoparkta 30 günden daha uzun süre kalan veya 1000 TL'den daha yüksek gelir elde eden araçların, tüm araçlar içindeki oranı: %{100 * yatan_arac / toplam_arac:.2f}")

print("******************************************************************************************")

print(f'Sürücüsü gazi olan araçların sayısı:{gazi_arac}')
print(f'Sürücüsü engelli olan araçların sayısı:{engelli_arac}')
print(f'Sürücüsü gazi olan araç sayısısın toplam araç sayısına oranı:%{gazi_arac * 100 / toplam_arac :.2f} ')
print(f'Sürücüsü engelli olan araç sayısının toplam araç sayısına oranı :%{engelli_arac * 100 / toplam_arac :.2f}')
print(f'Sürücüsü gazi olan araçların otoparkta kalma süresi: {zaman(gazi_arac_sure // gazi_arac)}')
print(f'Sürücüsü engelli olan araçların otoparkta kalma süresi: {zaman(engelli_arac_sure // engelli_arac)}')

print("******************************************************************************************")

print(f'Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı %{100 * cok_kalan_ozel_arac / ozel_arac_say:.2f}')

print("******************************************************************************************")

print(f'En uzun süre otoparkta kalan aracın otoparkta kaldığı süre: {zaman(max_sure)}, ücreti: {max_sure_gelir:.2f} TL.')

print("******************************************************************************************")

print(f'En çok gelir elde edilen binek aracın otoparkta kaldığı süre: {zaman(max_gelir_sure)}, ücreti: {max_gelir:.2f} TL')
