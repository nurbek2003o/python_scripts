# kocha = input("Ko'cha nomini  kiriting\n")
# mahalla = input("Mahalla\n")
# tuman = input("Tuman\n")
# viloyat = input("Viloyat\n")
# print(kocha + " " + "ko'chasi,\n", mahalla + " " + "mahallasi,\n", tuman + " " + "tumani,\n", viloyat + " " + "viloyati." )
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())
# print(manzil.lstrip())
# print(manzil.rstrip())
# print(manzil.strip())


#  Sonlar darsi vazifasi

# 1-vazifa

# a =  int(input("Istalgan sonni kiriting\n"))
# b = a**2
# c = a**3
# print(str(a) + ' ' + 'ning kvadrati' + ' ' + str(b) + ' ' +'ga teng')
# print(str(a) + ' ' + 'ning kubi' + ' ' + str(c) + ' ' +'ga teng')

# 2-vazifa
# a = int(input("Yoshingiz nechida?\n"))
# b = 2025 - a
# print("Siz" + " "  + str(b) + " " + "da tug'ilgansiz ")

# 3-vazifa
# a = str(float(input("Birinchi sonni kiriting:")))
# b = str(float(input("Ikkinchi sonni kiriting:")))
# c = str(float(a) + float(b))
# d = str(float(a) - float(b))
# e = str(float(a) * float(b))
# f = str(float(a) / float(b))
#
# print(a + ' ' + '+' + ' ' + b + ' =' + ' ' + c)
# print(a + ' ' + '-' + ' ' + b + ' =' + ' ' + d)
# print(a + ' ' + '*' + ' ' + b + ' =' + ' ' + e)
# print(a + ' ' + '/' + ' ' + b + ' =' + ' ' + f)



# List elementlari
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']
# print("Birinchi meve: ", mevalar[0].title())
# print("Oxirgi meve: ", mevalar[3].upper())

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = narhlar[0] + 1000
# print(narhlar)
# mevalar.append("tarvuz")
# print(mevalar)
# cars = []
# cars.append("Lacetti")
# cars.append("Nexia 3 ")
# cars.append("Cobalt")
# cars.insert(0, "Malibu")
# del cars[1]
# cars.remove("Malibu")
# print(cars)
# bozorlik = ["yog'","piyoz",'banan', "go'sht"]
# mahsulot = bozorlik.pop(2)
# print(f"Men {mahsulot} ni yaxshi ko'raman")
# print(f"Har kim ham {mahsulot} ni olib yeyolmaydi. Odatda bu mahsulot faqat yangi yilda yeyilardi.")

# 1-vazifa
# ismlar = ["Asadbek", "Shavkat aka", "Donyor"]
# print(f"Salom {ismlar[0]}, bugun choyxonaga boramizmi?")
# print(f"{ismlar[1]}, choyxona bormi?")
# print(f"{ismlar[2]}, choyxonaga  kel gaplashib o'tiramiz")
# 2-vazifa
# narxlar = [2000,3000,4000]
# narxlar[2] = narxlar[1] - 1000
# narxlar.append(3000)
# narxlar.insert(2,4000)
# narxlar.remove(2000)
# print(narxlar)
# shaxslar = ['Imom Buxoriy', 'Bill Gates', 'Alisher Navoiy', 'Amir Temur']
# adiblar = shaxslar.pop(0)
#
# print(f"Men tarixiy shaxslardan {adiblar} bilan, zamonaviy shaxslardan {shaxslar[0]} bilan suhbat \nqilishni istardim")
#
friends = []
friends.append("Joe")
friends.append("Bob")
friends.append("Sholibek")
friends.append("Jim")
friends.append("Jucki")
friends.append("Bobik")
friends.remove("Bob")
friends.remove("Sholibek")
friends.append("Jim1")
friends.insert(0, "Jim2")
friends.insert(2, "Jim3")
mehmonlar = friends.pop(0),friends.pop(2),friends.pop(3),friends.pop(1)
print(mehmonlar)
print(friends)