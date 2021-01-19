# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_Erişme_modu--> dosyayı hangi amaçla açtığımızı belirtir.

# 'w' --> (write) Yazma modu. Dosyayı konumda oluşturur. Önceki veriyi siler. dosya yoksa oluşturur.

file = open("newfile.txt","w",encoding="utf-8")
file.write("\nHamza Yüksel.")
file.close()

# 'r' --> (read) Okuma varsayılan. Dosya konumda yoksa hata verir.
# 'a' --> (append) Ekleme. Dosya konumda yoksa oluşturur. Önceki veriyi korur ardına ekleme yapar.
# 'x' --> (create) Oluşturma. Dosya zaten varsa hata verir.
# 'r+'--> hem yazma hem okuma modu __ güncelleme.