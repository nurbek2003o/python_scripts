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


# a=int((input("Bugun nechta odam bilan suhbat qildingiz:\n")))
# odamlar = []
# for i in range(a):
#     odamlar.append(input(f"{i+1} - suhbat qilgan odamingiz kim edi?\n"))
# print(odamlar)

#   10-dars
# avtolar = ['audi','bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
# ism =  input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutyabmiz")
# else:
#     print("Salom, Ali")
# javob = float(input("12*6 nechchiga teng?>>>"))
# if javob != 72:
#     print("Javob xato!")
# yosh = int(input("Yoshingiz nechchida"))
# if yosh >= 18:
#     print('Xush kelibsiz')
# else:
#     print('Kirish mumkinmas')
# login = input("Yangi loginni tanlang:")
# if len(login) <= 5:
#     print("Login 5ta harfdan ko'proq bo'lishi kerak")
# yil = int(input("Tug'ilgan yilingizni kiriting:" ))
# if 2025-yil<18:
#     print(f"Yoshingiz {2025-yil}da ekan")
#     print("Kirish mumkin emas")
# else:
#     print("Xush kelibsiz")
# yosh = int(input("Yoshingiz nechada?"))
# if yosh > 65: print("Siz covid 19 risk guruhidasiz")
# x, y = 80,50
# print("x>y") if x > y else print("x<y")
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# print("2ta son kiriting!")
# x=float(input("Birinchi sonni kiriting"))
# y=float(input("Ikkinchi sonni kiriting"))
# if x == y:
#     print("Sonlar teng")
# a=input("Ismingizni yozing!")
# print(a)
# if a.lower() == "admin":
#     print("Xush kelibsiz Admin")
# else:
#     print(f"Xush kelibsiz {a.title()}")
# a = int(input("Istalgan sonni kiriting!"))
# print(a)
# if a < 0:
#     print(f"Manfiy son")
# else:
#     print(f"Musbat son")
# son = float(input("Istalgan sonni kiriting."))
# if son >= 0:
#     print(son**(1/2))
# else:
#     print("Musbat sonni kiriting.")

#  11- dars
# yosh =  int(input('Yoshingiz nechida?>>'))
# if yosh<=4:
#     print('Sizga kirish bepul')
# elif yosh <=12:
#     print('Sizga kirish 5000 so\'m')
# else:
    # print('Sizga kirish 10000 so\'m')


# yosh = int(input('Yoshingiz nechida'))
# if yosh<4:
#     price = 0
# elif yosh<12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm ")


# yosh = int(input('Yoshingiz nechchida?'))
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price=5000
# elif yosh<65:
#     price=10000
# elif yosh>=65:
#     price=8000
# print(f"Sizga kirish {price} so'm ")
# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun=input('Bugun nima kun?>>>')
# harorat=float(input('Havo harorati qanday?>>'))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#     print('Cho\'milgani kettik!')
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat<30:
#     print('Uyda o\'tiramiz')
# else:
#     print("Dam olish kuni emas")


# narh = 15000
# choy = True
# salat = True
# if choy and salat:
#     narh = narh +10000
# elif choy or salat:
#     narh = narh +5000
#
# print(f"Jami {narh} so'm")
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assosrti = False
# if choy:
#     print('Mijoz choy oldi.')
#     narh = narh +3000
# if salat:
#     print('Mijoz salat oldi.')
#     narh = narh +5000
# if non:
#     print('Mijoz non oldi.')
#     narh = narh +2000
# if kompot:
#     print('Mijoz kompot oldi.')
#     narh = narh +5000
# if assosrti:
#     print('Mijoz assosrti oldi.')
#     narh = narh +15000
# print(f"Jami {narh} so'm")

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yuq')
# else:
#
#     print('Buyurtma qabul qilindi')
# menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh','somsa','manti', 'shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Menuda {taom} yuq")
# else:
#     print(f"Savatchangiz bo'sh")




# uyga vazifalar
# son = float(input('Juft son kiriting:'))
# if son%2:
#     print('Bu juft emas')
# else:
#     print('Rahmat')

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <+ 4:
#     narh = 0
# elif yosh <= 18:
#     narh = 10000
# elif yosh <= 60:
#     narh = 20000
# else:
#     narh = 0
# print(f"Sizga kirish {narh} so'm")

# mahsulotlar = ['olma', 'anjir', 'anor', 'tarvuz', 'uzum', 'shaftoli', 'kartoshka', 'qovun', 'piyoz', 'tuz']
# savat = []
# print("5ta mahsulotni kiriting")
# savat.append(input('1-mahsulotni kiriting'))
# savat.append(input('2-mahsulotni kiriting'))
# savat.append(input('3-mahsulotni kiriting'))
# savat.append(input('4-mahsulotni kiriting'))
# savat.append(input('5-mahsulotni kiriting'))
# bor_mahsulotni = []
# mavjud_emas = []
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#             bor_mahsulotni.append(mahsulot)
#         else:
#             print(f"Do'konimizda {mahsulot} yuq")
#             mavjud_emas.append(mahsulot)
#     if mavjud_emas:
#         print(f"Do'konimizda quyidagi mahsulotlar yuq:")
#         for mahsulot in mavjud_emas:
#             print(mahsulot)
#     else:
#         print(f"Siz so'ragan barcha mahsulotlar bor")
# else:
#     print("Savatingiz bo'sh")
#
#

# x = float(input('Birinchi sonni kiriting'))
# y = float(input('Ikkinchi sonni kiriting'))
# if x==y:
#     print(f"{x}={y}")
# elif x>y:
#     print(f"{x}>{y}")
# else:
#     print(f"{x}<{y}")


# foydalanuvchilar = ['nurbek', 'sardor', 'katya', 'rohila', 'Azam']
# if foydalanuvchilar.append(input('Yangi login kiriting')) in foydalanuvchilar:
#     print('Login band')
# else:
#     print('Login successful')
# print(foydalanuvchilar)

# a = list(range(2,11))
# print(a)
# b = int(input('Istalgan butun sonni kiriting: '))
# for son in a:
#     if not (b%son):
#         print(f"{b} soni {son} ga qoldiqsiz bo'linadi")

   # 13-dars | Pythonda lug'at
# car_0= {'model':'ferrari', 'rang':'qizil'}
# print(car_0['rang'])
# talaba_0={'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['t_yil']}-yilda tug'ilgan,\
#       {talaba_0['yosh']} yoshda")
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)
# talaba_1 = {}
# talaba_1['ism'] = 'qobil'
# talaba_1['kurs']=3
# talaba_1['yosh']=20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# talaba_1['kurs']=4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# telefonlar={
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }
# print(telefonlar)
# phone=telefonlar.get('hasan')
# print(phone)



# Uyga vazifalar
# otam ={'ism':'zafar', 't_yil':1975, 't_joyi':'Samarqand'}
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, {otam['t_joyi'].title()}da tug'ilgan ")
# sevimli_taom={'otam':'barak','onam':'qatiqli osh', 'Ali akam':'manti', 'Elbek Akam':'shurva','Singlim':'osh'}
# print(f"Otamning sevimli taomi {sevimli_taom['otam']}")
# print(f"Onamning sevimli taomi {sevimli_taom['onam']}")
# print(f"Elbek akamning sevimli taomi {sevimli_taom['Elbek Akam']}")
python_izohli_lugati={
    'integer':'Butun son',
    'float':"O'nlik son",
    'string':'Matn',
    'list':"Ro'yxat",
    'tuple':"O'zgarmas list"
}
# kalit=input("Biror so'z kiriting").lower()
# tarjima=python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas")
# print(tarjima)

kalit=input("Biror so'z kiriting: ").lower()
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjudmas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")