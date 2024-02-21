
# # # 1-Verilen sayının basamakları toplamını veren kodu yazınız?
# sayi=int(input("Lütfen bir sayı giriniz"))
# basamaklar=[]

# while sayi !=0:
#     basamak=sayi %10 #Mod alır
#     sayi=sayi//10 # bölümü alır .Eğer sonuç floatsa Tam kısmını alır.
#     basamaklar.append(basamak)  #diziye ekleyerek gidiyor
# basamaklar=basamaklar[::-1] # dizinin tersini alıyor
# toplam=sum(basamaklar)
# print(toplam)

# # 2-Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
# # ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# # ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.
# devamMi ="e"
# ogrenciler=[]

# while (devamMi=="e"):
#     ogrenciNo=input("ogrenci no girin: ")
#     ogrenciAdi=input("Ogrenci adi girin: ")
#     ogrenciSoyad=input('ogrenci soyad girin: ')

#     ogrenciler.append( {
#         "ogrenciNo":ogrenciNo,
#         "ogrenciAdi":ogrenciAdi,
#         "ogrenciSoyad":ogrenciSoyad
#     }
#     )
#     devamMi=input( "devam mi? (e/h): ")

# for ogrenci in ogrenciler:
#     print(f"{ogrenci["ogrenciNo"]} numarali ogrencinin adi soyadi: {ogrenci["ogrenciAdi"]} {ogrenci["ogrenciSoyad"]}  ")
# ------------
# devamMi="e"
# ogrenciler=[]
# while(devamMi=="e"):
#     ogrenciNo=input("Lütfen öğrenci numarasını giriniz")
#     ogrenciAdi=input("Lütfen öğrenci adını giriniz")
#     ogrenciSoyadi=input("Lütfen öğrenci soyadını giriniz")
#     ogrenciler.append( {
#         "OgrenciNo":ogrenciNo
#         "OgrenciAdi":ogrenciAdi
#         "OgrenciSoyadi":ogrenciSoyadi
#     }
#     )
#     devamMi=input(devam mı e/h)
#     for ogrenci in ogrenciler:
#         print(f"{ogrenci["ogrenciNo"]} numarali ogrencinin adi soyadi: {ogrenci["ogrenciAdi"]} {ogrenci["ogrenciSoyad"]}  ")
        
# #3-Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
# baslangic=0
# bitis=0
# sayiBir=int(input("sayi degeri girin:"))
# sayiİki=int(input("sayi degeri girin: "))
# dizi=[]

# if (sayiBir >sayiİki):
#     baslangic=sayiİki
#     bitis=sayiBir
# else:
#     baslangic=sayiBir
#     bitis=sayiİki

#     # 20 21 22 .... 49  50 
# i=baslangic
# while(i<(bitis+1)):
#     if (i%2==0):
#       dizi.append(i)
#     i+=1
# print(dizi)

# 4-Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

# benzin =39.35
# dizel  = 41.71
# lpg    = 20.28
# sonuc=0
# yakitTipi=input("Yakit tipi girin (benzin,dizel,lpg)")
# gidilecekYol=float(input("Gidilen mesafe: "))
# ortalamaYakit=float(input("1 km' deki ortalama yakit tüketimi: "))

# masraf=gidilecekYol*ortalamaYakit

# if (yakitTipi== "benzin"):
#     sonuc=masraf*benzin
# elif(yakitTipi=="dizel"):
#     sonuc=masraf*dizel
# elif (yakitTipi=="lpg"):
#     sonuc=masraf*lpg
# else:
#     print('yanlis')

# print(sonuc)

# 5-Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve
#hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

# 0 -24  => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3
# 70-84  => 4
# 85-100 =>5

# vizeNotu=int(input("Lütfen vize notunuzu giriniz"))
# finalNotu=int(input("Lütfen final notunuzu giriniz"))
# sozluNotu=int(input("Lütfen sözlü notunuzu giriniz"))

# ort=(vizeNotu+finalNotu+sozluNotu)/3
# if(0<=ort and ort<=24):
#     print(f"ortamanız:{ort} notunuz 0'dır.")
# elif (25<=ort and ort<=44):
#     print(f"ortamanız:{ort} notunuz 1'dir")
# elif (45<=ort and ort<=54):
#     print(f"ortamanız:{ort} notunuz'2'dir.")
# elif (55<=ort and ort<=69):
#     print(f"ortamanız:{ort} notunuz'3'dir.")
# elif (70<=ort and ort<=84):
#     print(f"ortamanız:{ort} notunuz'4'dir.")
# elif (85<=ort and ort<=100):
#     print(f"ortamanız:{ort} notunuz'5'dir.")

import math
a=math.sin(90)
print(a)

