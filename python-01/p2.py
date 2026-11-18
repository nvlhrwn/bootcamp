apel = 10000
mangga = 15000
uang_dimiliki = 100000


jumlah_apel = int(input("Masukkan jumlah apel yang dibeli: "))
jumlah_mangga = int(input("Masukkan jumlah mangga yang dibeli: "))

sisa_uang = uang_dimiliki - (apel * jumlah_apel) - (mangga * jumlah_mangga)


print("Sisa uang Anda adalah:", sisa_uang)