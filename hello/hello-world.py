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
# print(f"Men tarixiy shaxslardan {adiblar} bilan, zamonaviy shaxslardan {shaxslar.pop(0)} bilan suhbat \nqilishni istardim")
#
# friends = []
# friends.append("Joe")
# friends.append("Bob")
# friends.append("Sholibek")
# friends.append("Jim")
# friends.append("Jucki")
# friends.append("Bobik")
# friends.remove("Bob")
# friends.remove("Sholibek")
# friends.append("Jim1")
# friends.insert(0, "Jim2")
# friends.insert(2, "Jim3")
# mehmonlar = friends.pop(0),friends.pop(2),friends.pop(3),friends.pop(1)
# print(mehmonlar)
# print(friends)

# 8-dars
# cars = ['bmv', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort() # A-Z gacha tartiblaydi
# print(cars)
# cars.sort(reverse=True)  # Z-A gacha tartiblaydi
# print(cars)
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# cars.reverse()
# print(len(cars))
# sonlar = list(range(0,10))
# print(sonlar)
# juft_sonlar = list(range(0,20,2))
# print(juft_sonlar)
# print(cars[2:5])
# print(cars[:4])
# print(cars[::-1])

#  Vazifalar

#davlatlar = ['Uzb', 'AQSH', 'Rus', 'German', 'France']
# davlatlar.sort(reverse=True)
# print(davlatlar)
# juft_sonlar = list(range(120,1201,2))
# sum(juft_sonlar)
# print(len(juft_sonlar))
# print(juft_sonlar[:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[520:])

# taomlar = ['osh', 'bishtex', 'shurbo', 'manti', 'xonim']
# nonushta = taomlar[0:5]
# nonushta.remove('osh')
# nonushta.remove('bishtex')
# nonushta.append('shirinlik')
# nonushta.append('cofe')
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non'
# print(tuple(nonushta))


#  9-vazifa
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorgi oshga taklif qilamiz")
#     print("Hurmat bilan, Sanaqulovlar oilasi")
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son ** 2)
# print(sonlar)
# print(sonlar_kvadrati)
# dostlar = []
# print("5ta eng yaqin do'stingizni kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:\n "))
# print(dostlar)


# ismlar = ['Ali','Vali', 'Hasan', 'Husan', 'Olim' ]
# for n in ismlar:
#     print(f"Hello, {n}!")
# print(f"Kod {len(ismlar)} marta takrorlandi.")
# toq_sonlar = list(range(11,100,2))
# for i in toq_sonlar:
#     print(f"{i} ning kubi {i**3} ga teng ")

# kinolar = []
# print("5ta eng sevimli kinolaringizni kiriting\n")
# for i in range(5):
#     kinolar.append(input(f"{i + 1}-kino nomini kiriting\n"))
# print(kinolar)


a=int((input("Bugun nechta odam bilan suhbat qildingiz:\n")))
odamlar = []
for i in range(a):
    odamlar.append(input(f"{i+1} - suhbat qilgan odamingiz kim edi?\n"))
print(odamlar)