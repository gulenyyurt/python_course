# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
loop = True
while loop:
    eleman = int(input("Lütfen 20 veya 20'den büyük bir eleman giriniz:"))
    if eleman >= 20:
        fibonacci = [1,1]  # İlk iki elemanı 1 olan Fibonacci serisi
        while len(fibonacci) < eleman:  # En az 20 elemanlı olana kadar devam et
                sonraki_fibonacci = fibonacci[-1]+fibonacci[-2] # Son iki elemanın toplamı
                fibonacci.append(sonraki_fibonacci)  # Yeni Fibonacci sayısını listeye ekle
        print(fibonacci)
        loop= False
    else:
        print("girdiğiniz sayı 20den küçüktür.")


# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
a = int(input("Bir Sayıyı Giriniz : "))
toplam= 0
for i in range(1,a+1):
    if a  % i==0:
        toplam += i
        
if 2*a==toplam:
    print(a, ": mükemmel sayıdr")
else:
    print(a, ": mükemmel sayı değildir")
    
# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
a = int(input("Birinci Sayıyı Giriniz : "))
b = int(input("İkinci Sayıyı Giriniz : "))
 
if (a > b):
    kucuksayi = b
else:
    kucuksayi = a
for i in range(1,kucuksayi+1):
    if (a  % i==0) and (b %i ==0):
        ebob = i
        ekok = (a*b)//ebob
        
print ("EBOB:", ebob)
print ("EKOK:", ekok)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
sayi= int(input("Lütfen bir sayı giriniz "))
asal_mi= True
if sayi==1:
    print(sayi,"Girdiğiniz sayı asal değildir")

else :
    for i in range(2,sayi):
    
        if sayi % i==0 :
            asal_mi=False
            break
    if asal_mi:
        print(sayi," :asal sayıdır")
    
    else:
         print(sayi," :asal sayı değildir")



# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
sayi = int(input("Lütfen Bir sayi giriniz: "))
asal_carpanlar=[]
bölen = 2
while sayi!=1:
    if(sayi % bölen == 0):
        asal_carpanlar.append(bölen)
        sayi = sayi / bölen
    else:
        bölen += 1
        
print("Asal çarpanlar: ",asal_carpanlar)
