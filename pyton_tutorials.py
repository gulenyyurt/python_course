
# # 1-Verilen sayının basamakları toplamını veren kodu yazınız?
sayi=int(input("Lütfen bir sayı giriniz"))
basamaklar=[]

while sayi !=0:
    basamak=sayi %10 #Mod alır
    sayi=sayi//10 # bölümü alır .Eğer sonuç floatsa Tam kısmını alır.
    basamaklar.append(basamak)  #diziye ekleyerek gidiyor
basamaklar=basamaklar[::-1] # dizinin tersini alıyor
toplam=sum(basamaklar)
print(toplam)