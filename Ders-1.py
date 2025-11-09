#Print komutu ile terminale yazdırma
print("hello world")

#Print komutu ile terminalde alt alta yazma yolları
print("hello\nworld")
#veya
print("""hello
world""")

#Değişken kullanarak terminale yazdırma
mesaj = "Selamün Aleyküm" 
print(mesaj)

#2 Değişken kullanarak Terminale yazdırma
mesaj2 = " yavuz"
print(mesaj + mesaj2)   #Kodu başlatınca Selamün aleyküm ve yavuzu birleşik yazdırmaması için selamün aleyküm değişkeninin sonuna veya yavuz değişkeninin başına boşluk bırakılabilir 

#değişkendeki belirli bir kısmı yazdırma
print(mesaj[0:4])#Bunu Yazdığımızda terminalde "sela" çıktısını alırız.Python değişkendeki ilk elemana her zaman 0 der ve 0:4 yazdığımızda 0 dahil fakat 4 hariç olur:)

#Bazı Fonksiyonlarla terminale yazdırma
#ÖNEMLİ!!!!
#upper=Tüm değişkeni büyük harfle yazar.
#lower=Tüm değişkeni küçük harfle yazar.
#startswith=Değişkenin nasıl başladığını doğru veya yanlış olarak gösterir.
#endswith=Değişkenin nasıl bittiğini doğru veya yanlıi olarak terminalde gösterir.
#capitalize=Değişkenin baş harfini büyük yazar.
#len=Değişkende kaç eleman(harf boşluk sayı vb) olduğunu terminalde gösterir.

#upper-lower kullanım
print(mesaj.upper())
print(mesaj2.lower())

#startswith-endswith kullanım
print(mesaj.startswith("Se"))#Gördüğünüz gibi mesaj değişkeni yanı "Selamün aleyküm" ifadesi Se ilemi başlıyor diye sorduk ve bize true-doğru çıktısını verdi.
print(mesaj.endswith("üm"))#Gördüğünüz gibi mesaj değişkeni yanı "Selamün aleyküm" ifadesi üm ilemi bitiyor diye sorduk ve bize true-doğru çıktısını verdi.
#Bu fonksiyonlar büyük-küçük harfe önem verir.

#capitalize kullanım
print(mesaj.capitalize())#Zaten mesaj değişkenimiz büyük harfle başladığı için burada pek etki etmedi:)

#len kullanım
print(len(mesaj))#kullanımı diğer fonksiyonlardan daha farklıdır.
print(len(mesaj + mesaj2))#İki değişkendeki elemanların toplamını verir:)
#Önemli=Python yazıdaki elemanları saymaya sıfırdan başlar yani ilk eleman sıfırdır.Boşluk sembol yani her şeyi sayar.

#tüm bu kodları yazıp çalıştırdığınızda terminal çıktınız aşağıdaki gibi olmalıdır.
#hello world
#hello
#world
#hello
#world
#Selamün Aleyküm
#Selamün Aleyküm yavuz
#Sela
#SELAMÜN ALEYKÜM
# yavuz
#True
#True
#Selamün aleyküm
#15
#21

#Ders bitmiştir.
#Yavuz Selim Duman.