
#class tanımla
class Banka_hesabi:
    isim='a'
    hesap_numarasi=1234
    bakiye=0

#hesap 1 oluştur
hesap1=Banka_hesabi()
islem=0

#cıkıs verene kadar döngü çalışsın
while(islem!=4):
    islem=int(input('yapmak istediginiz islemi girin  1: para yatirma, 2: para çekme, 3 bakiye görüntüleme, 4:cikis '))

    if islem==1:
        para=int(input('kaç tl '))
        hesap1.bakiye+=para
    if islem==2:
        para=int(input('kaç tl '))
        hesap1.bakiye-=para
    if islem==3:
        print(hesap1.bakiye)


