sayi1=0
sayi2=0
islem='a'
#string olması ıcın a atadım

cıkıs=0


#cıkıs olmadıgı surece devam etsın
while(cıkıs==0):
    #sayıları ve ıslemı aldık
    sayi1=int(input("ilk sayiyi girin= "))
    sayi2=int(input("ikinci sayiyi girin= "))
    islem=input("islemi girin ")
    if islem=='+':
        print('sonuc = ',sayi1+sayi2)
    if islem =='-':
        print('sonuc = ',sayi1-sayi2)

    if islem=='*':
        print('sonuc = ',sayi1*sayi2)

    if islem=='/':
        print('sonuc = ',sayi1/sayi2)

#0 yazılmadıgı surece donguden cıkacak
    cıkıs=int(input("tekrar islem yapmak ıcın 0, cıkmak ıcın 1 yazın "))
    

