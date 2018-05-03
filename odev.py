import hashlib
oku = open("dosya.txt","r")
okunan = oku.read()
oku.close
random = []
uzunluk =int(input("uzunlugu giriniz: "))
for k in range(0,uzunluk):
    okunan=hashlib.md5(okunan.encode('utf-8')).hexdigest()
    random.append(okunan[7])
hexa = ""
for i in range(0,len(random)):
    hexa = hexa+random[i] 
print("hexadecimal: ",hexa)
print("decimal: ",int(hexa,16))
