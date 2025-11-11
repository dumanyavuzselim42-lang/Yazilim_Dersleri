#Ders 2

                     #python da Sayılar

#Integer-Float-Type fonksiyonları
sayı1 = 3    #Python tam sayıları Int sınıfına alır.
sayi2 = 3.5  #python Virgüllü sayıları float sınıfına alır.
print(type(sayı1))  #Type fonksiyonu kullanarak kodu çalıştırdığımız zaman "<class 'int'>"  çıktmızdada görüldüğü üzere sayı1 ınteger sınıfındadır.
print(type(sayi2))  #Type fonksiyonu kullanarak kodu çalıştırdığımız zaman "<class 'float'>"  çıktmızdada görüldüğü üzere sayı1 Float sınıfındadır.
#-------------------------------------------------------------------------------------------------------------------------------------------------
                     #Pythonda Matematiksel İşlemler

# Toplama = "+"
# Çıkarma = "-"
# Çarpma = "*"
# Bölme = "/"
# Tam Sayılı Bölme = "//"
# Kuvvet Alma = "**"
# Mutlak Değer = "abs"
# Yuvarlama = "round"
# İşlem Önceliği


print(3 + 5)     # 3 artı 5 = 8
print(3 - 4)     # 3 eksi 4 = -1
print(3 * 4)     # 3 çarpı 4 = 12
print(16 / 5)    # 16 / 5 = 3.2
print(16 // 5)   #Tam sayılı bölme,bölme sonucundaki virgülü attığı için burada sonucu 3 olarak görürüz:)
print(3 ** 2)    # 3 kuvvet 2 işlemi 3 çarpı 3 olarak sonuç 9 bulunur.
print(5 ** 4)    # aynı mantıkla 5 kuvvet 4 işleminin sonucu 625 bulunur.
print(abs(-10))  # mutlak değer almak "-" işaretini yok saymaktır.Burada Cevabı 10 buluruz
print(round(5.7))#Yuvarlama işlemi ise virgüllü sayıyı en yakınındaki tam sayıya yuvarlar.

#pythonda İşlem önceliğine verlien önemin örnekleri
#Matematikte ilk parantez içindeki işlem sonra çarpma-bölme işlemleri ve en son toplama-Çıkarma İşemleri Yapılır.
print(3+4*2)  #Burada ilk önce 4*2 = 8 ve daha sonra 3+8 yaparak sonucu 11 bulur.
print((3+2)*4)#sonucu 20 olarak Görebilirsiniz:)

#--------------------------------------------------------------------------------------------------------------------------
                     #Pythonda Karşılaştırma Operatörleri

#Eşittir             "=="  #Pythonda "=" ifadesi sadece atama yapmak için kullanılır(değişken vb)!!
#Büyüktür            ">"
#Küçüktür            "<"
#Küçük veya Eşittir  "<="
#Büyük veya Eşittir  ">="
#Eşit Değildir        "!"      

print(3 == 4) #3 ifadesi 4 e eşit olmadığından Terminalde False çıktısı görülür
print(5 >= 2) #5 ifadesi 2 den büyük olduğu için terminalde True çıktısı verir aynı zamanda 2 yerine 5 koysaydık sonuç değişmez çünkü ">=" operatörünü kullandık
print(7 <= 8) #True
print(10 > 5) #True
print(5 < 10) #True
print(5 != 6) #True

#Terminal Çıktınız BU şekilde Olmalıdıı!!!
#<class 'int'>
#<class 'float'>
#8
#-1
#12
#3.2
#3
#9
#625
#10
#6
#11
#20
#False
#True
#True
#True
#True
#True                                                 Ders Bitmiştir:)   Yavuz Selim Duman
#------------------------------------------------------------------------------------------------------------------------