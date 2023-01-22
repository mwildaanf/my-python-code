"""
Semua sintaksis dasar bahasa pemrograman terdiri daari :
1. Sekuensiaal : Langkah berurutan 
2. Percabangam : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu Berkata,"Pergi ke toko"')
print('Budi Menjawab, "Baik, apa yang harus saya beli di toko"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f'Jumlah botol susu, {jumlah_botol_susu} botol')
print(f'Jumlah telur, {jumlah_telur}')

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup.")
    if jumlah_telur == 0:
       print('Budi membeli 1 botol susu')
    else :
        print('Budi membeli 6 botol susu ya')

else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('Menyampaikan hasilnya kepada ibu')