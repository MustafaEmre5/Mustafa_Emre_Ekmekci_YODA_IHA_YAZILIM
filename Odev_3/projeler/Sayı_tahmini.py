import random
sayi=random.randint(0,100)
#rastgele sayı oluşturduk


kalanhak=10
tahmin=0

#kalan hak sayısı 0'dan büyük olduğu sürece devam edecek bir döngü
while kalanhak>0:
    kalanhak-=1
    tahmin=int(input("tahmininizi girin= "))

    #sayının durumuna göre ip ucu verecek
    if tahmin==sayi:
        print("dogru")
        break
    elif tahmin<sayi:
        print("cok kucuk")
    elif tahmin>sayi:
        print("cok buyuk")

    
    print(kalanhak, "hakkınız kaldı")
if kalanhak==0:
    print("haklarınız tukendi")


