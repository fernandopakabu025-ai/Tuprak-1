menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#masing masing subtotal
sub_KopiSusu = harga[0] * jumlah[0]     #total = 72000
sub_MatchaLatte = harga[1] * jumlah[1]  #total = 66000
sub_Americano = harga[2] * jumlah[2]    #total = 75000

subtotal_pendapatan = [sub_KopiSusu, sub_MatchaLatte, sub_Americano]

total_seluruh = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000

pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_semua = sum(jumlah)

target_tercapai = total_seluruh > 20000 and jumlah_semua > 10

print("Subtotal Pendapatan:", subtotal_pendapatan)
print("Subtotal Kopisusu:", sub_KopiSusu)
print("Subtotal MatchaLatte:", sub_MatchaLatte)
print("Subtotal Americano:", sub_Americano)
print("Total Pendapatan:", total_seluruh)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Jumlah Semua Barang:", jumlah_semua)
print("Target Tercapai:", target_tercapai)







