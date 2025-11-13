#Ders-3

            #Liste nedir.Nasıl oluşturulur?
Renkler = ["Beyaz","Sarı","Mavi","Yeşil","Turuncu"]  #Yandaki gördüğünüz İsmi Renkler olan bir listedir
print(Renkler)   #Listeinin içini terminale yazdırmak
print(type(Renkler))  #Bu komutu kullnarak terminalde Renkler değişkeninin bir liste olduğunu görebiliriz

            #Len Fonksiyonu kullanımı
print(len(Renkler))  #Listede kaç eleman olduğunu gösterir

            #listeyi Terminale Yazdırma
print(Renkler[1:4])   #Bu komut ile Listenin içindeki istediğimiz aralıktaki elemanlara kolayca ulaşırız.Python en baştaki elemanı sıfır olarak belirler.
print(Renkler[:4])    #En Baştan yazdırmasını istedik.Python sondaki sayıyı dahil etmez.!!
print(Renkler[2::4])  #Aynı şekilde burada 2. ve 4. elemanı yazmasını istedik ama Python sondaki elemanı dahil etmediği için bize sadece 2. elemanı yani maviyi verdi
            
            #Listedeki elemanlara erişme 

print(Renkler[3])    #Listedeki 3. elemanı yazdırır.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


#insert = İstediğimiz sıraya eklememizi sağlayan metoddur
#remove = Listedeki elemanları silmemizi sağlayan metoddur
#extend = 2 listemiz var ise 2. listedeki elemanları,1. listeye taşımamızı sağlayan metodddur
#pop = listenin en sonundaki elemanı siler
#reverse = Lİsteyi en sondan başlayarak yazar
#sort = Listedeki elemanları Alfabetik olarak büyükten küçüğe yazar
#sorted = sort komutu listeyi değiştirir fakat bu komut yeni bir listeye kaydeder


#append kullanımı
Renkler.append("Mor")           
print(Renkler)

#insert kullanımı
Renkler2 = ["mavi","sarı","mor","turuncu"]
Renkler2.insert(2,"kırmızı")                                      
print(Renkler2)

#remove kullanımı                                                                                  
Renkler2.remove("mor")
print(Renkler2)

#extend kullanımı
liste1 = ["Mercedes","BMW"]
liste2 = ["Audi","Tesla"]
liste1.extend(liste2)
print(liste1)

#pop kullanımı
Renkler2.pop()
print(Renkler2)

#reverse kullanımı
Renkler2.reverse()
print(Renkler2)

#sort kullanımı
Renkler2.sort()
print(Renkler2)

#sorted kullanımı
Renkler3 = sorted(Renkler2)
print(Renkler3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#min-max-in komutlarını kullanma
sayılar = [1,3,6,3,6,4,56]
harfler = ["A","B","C","G"]
print(min(sayılar))    #listedeki en küçük değeri verir
print(max(sayılar))    #listedeki en büyük değeri verir
print(min(harfler))    #listedeki en küçük değeri verir(Alfabetik)
print(max(harfler))    #listedeki en büyük değeri verir(Alfabetik)
print("f"in harfler)   #istediğimiz bir şeyin listede olup olmadığını kontrol eder

#sum kullanımı
print(sum(sayılar))    #Listedeki elemanların toplamını verir(Stringlerde kullanılmaz)

#For döngüsü kullanımı
for i in harfler:
    print(i)           #Listedeki elemanları alt alta verir

#enumerate kullanımı
print(list(enumerate(harfler)))    #listedeki elemanları numaralandırır.

#listeyi stringe cevirme-join komutu
stringrenkler = "-".join(harfler)
print(stringrenkler)

#stringi listeye çevirme-split komutu
renkler4 = stringrenkler.split("-")
print(renkler4)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ders bitmiştir Yavuz Selim Duman.Termianl çıktısı aşağıdaki gibidir:)
#['Beyaz', 'Sarı', 'Mavi', 'Yeşil', 'Turuncu']
#<class 'list'>
#5
#['Sarı', 'Mavi', 'Yeşil']
#['Beyaz', 'Sarı', 'Mavi', 'Yeşil']
#['Mavi']
#Yeşil
#['Beyaz', 'Sarı', 'Mavi', 'Yeşil', 'Turuncu', 'Mor']
#['mavi', 'sarı', 'kırmızı', 'mor', 'turuncu']
#['mavi', 'sarı', 'kırmızı', 'turuncu']
#['Mercedes', 'BMW', 'Audi', 'Tesla']
#['mavi', 'sarı', 'kırmızı']
#['kırmızı', 'sarı', 'mavi']
#['kırmızı', 'mavi', 'sarı']
#['kırmızı', 'mavi', 'sarı']
#56
#A
#G
#False
#79
#A
#B
#C
#G
#[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'G')]
#A-B-C-G
#['A', 'B', 'C', 'G']
#-------------------------------------------------------------------------------------------