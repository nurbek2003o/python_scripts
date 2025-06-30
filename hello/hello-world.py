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
from cloudinit.config.cc_ntp import install_ntp_client

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
# python_izohli_lugati={
#     'integer':'Butun son',
#     'float':"O'nlik son",
#     'string':'Matn',
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas list"
# }
# kalit=input("Biror so'z kiriting").lower()
# tarjima=python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas")
# print(tarjima)

# kalit=input("Biror so'z kiriting: ").lower()
# tarjima=python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjudmas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")


# 15-dars

# talaba_0={
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
# }
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# telefonlar={
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
# }
# for k,q in telefonlar.items():
#     print(f"{k.title()} ning telefoni {q}")

# mahsulotlar={
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000,
# }
# print(mahsulotlar.keys())
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# bozorlik=['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# print(telefonlar.values())
# print('Foydalanuvchilarni quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


# Uyga vazifalar:

# python_izohli_lugati={
#     'integer':'Butun son',
#     'float':"O'nlik son",
#     'string':'Matn',
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas list",
#     'for':'Biror amalni qayta-qayta bajarish sikli',
#     'if':'Shartlarni tekshirish operatori',
#     'Boolean':'Mantiqiy qiymat',
#     'type':'Malumot turini aniqlash',
#     'get':'Lug\'atdan elementni olish'
# }
# for k, q in sorted(python_izohli_lugati.items()):
#     print(f"{k.title()}-{q}")
# dunyo_davlatlari={
#     'aqsh':'washington',
#     'italiya':'rim',
#     'malayziya':'kuala-lumpur',
#     'uzbekistan':'toshkent',
#     'qirg\'iziston':'bishker',
#     'qozog\'iston':'nursulton',
#     'rossiya':'moskva',
#     'singapur':'singapur',
#     'tojikiston':'dushanbe'
# }
# for value in sorted(dunyo_davlatlari.values()):
#     print(value.title())
# country=input("Qaysi davlatning poytaxtini bilishni istaysiz: ")
# capital = dunyo_davlatlari.get(country)
# if capital==None:
#     print("kechirasiz,bizda malumot yuq")
# else:
#     print(f"{country}ning poytaxti {capital}ga teng")


# taomlar={'osh':20000,'shurvo':30000,'shashlik':6000,'non':5000,'salat':6000,'choy':2000,'kompot':15000,'bushteks':3000,'mastava':35000}
# print("3ta ovqat nomini kiriting.")
# buyurtmalar=[]
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom").lower())
# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"{buyurtma.title()} {taomlar[buyurtma]}")
#     else:
#         print(f"Kechirasiz, {buyurtma} bizda yuq.")



# 16-dars
# car0={
#     'model':'lacetti',
#     'rang':'oq',
#     'yil':2018,
#     'narx':13000,
#     'km':50000,
#     'korobka':'avtomat'
# }
# car1={
#     'model':'nexia 3',
#     'rang':'qora',
#     'yil':2015,
#     'narx':9000,
#     'km':89000,
#     'korobka':'mexanika'
# }
# car2={
#     'model':'gentra',
#     'rang':'qizil',
#     'yil':2019,
#     'narx':15000,
#     'km':20000,
#     'korobka':'mexanika'
# }
# car =car0
# print(f"{car['model'].title()}.\
#     {car['rang']} rang,\
#     {car['yil']}-yil, {car['narx']}$")
# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang']} rang,"
#           f"{car['yil']}-yil, {car['narx']}$")
# print(cars[0]['model'].title())

# malibus=[]
# for n in range(10):
#     new_car={
#         'model':'malibu',
#         'rang':None,
#         'yil':2025,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narx']=40000
#     else:
#         malibu['narx']=30000
# print(malibus)
# dasturchilar={
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f'{til.upper()}', end=' ')

# hamkasblar={
#     'ali':{
#         'familiya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python','c++']
#         },
#     'vali':{
#         'familiya':'aliyev',
#         'tyil':2001,
#         'malumot':'o\'rta-maxsis',
#         'tillar':['html','css','js']
#         },
#     'hasan':{
#         'familiya':'husanov',
#         'tyil':1999,
#         'malumot':'maxsus',
#         'tillar':['python','php']
#     }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

# Vazifalar
# shaxslar={
#   'Abu Abdulloh Muhammad ibn Ismoil':{
#       'tyil':810,
#       'tjoy':'Buxoro',
#       'yosh':60,
#       'asarlar':['Al-jome as-sahih', 'Al-adab al-mufrad','At-tarix al-kabir']
#         },
#   'Abdulla Qodiriy':{
#       'tyil':1894,
#       'tjoy':'Toshkent',
#       'yosh':44,
#       'asarlar':["o'tkan kunlar",'Mehrobdan cahyon','obid ketmon']
#     },
#   'Erkin Vohidov':{
#       'tyil':1936,
#       'tjoy':"Farg'ona",
#       'yosh':80,
#       'asarlar':['tong nafasi',"qo'shiqlarim sizga","o'zbegim",'qiziquvchan matmusa']
#     },
#   'Alisher Navoiy':{
#       'tyil':1441,
#       'tjoy':"Xirot",
#       'yosh':60,
#       'asarlar':['xamsa','lison ut-tayr','mahbub al-qulub','munojat']
#   }
# }
# for shaxs, info in shaxslar.items():
#     print(f"{shaxs.title()} {info['tyil']}-yilda "
#           f"{info['tjoy']}da tavallud topgan."
#           f" {info['yosh']} yil umr ko'rgan\n"
#           f"{shaxs.title()}ning eng mashhur asarlari: ")
#     for asar in info['asarlar']:
#         print(asar.title())
# print("3ta sevimli kinoyingizni kiriting")
# akamlar={
#     'ali':['Terminator','rambo','titanic'],
#     'vali':['tenet','inception','interstellar'],
#     'hasan':['abdullajon','bomba','shaytanat'],
#     'husan':['mahallada duv-duv gap','john wick']
# }
# for ism, info in akamlar.items():
#     print(f"{ism.title()}ning sevimli kinolari:")
#     for kino in info:
#         print(kino)

davlatlar={
    "o'zbekiston":{
        'poytaxt':'toshkent',
        'hudud':448978,
        'aholi':33000000,
        'puli':"so'm"
      },
    'rossiya':{
        'poytaxt':'moskva',
        'hudud':17098246,
        'aholi':144000000,
        'puli':'rubl'
     },
    'aqsh':{
        'poytaxt':'vashington',
        'hudud':9631418,
        'aholi':327000000,
        'puli':'dollar'
        },
    'malayziya':{
        'poytaxt':'kuala-lumpur',
        'hudud':329750,
        'aholi':25000000,
        'puli':'rinngit'
    }
}
# for davlat, info in davlatlar.items():
#     print(f"{davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
#           f"Hududi: {info['hudud']} kv.km\n"
#           f"Aholisi: {info['aholi']}\n"
#           f"Pul birligi: {info['puli']}\n")
#
# a=(input('Davlat nomini kiriting'))
# b=davlatlar.get(a)
# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"{davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
#           f"Hududi: {info['hudud']} kv.km\n"
#           f"Aholisi: {info['aholi']}\n"
#           f"Pul birligi: {info['puli']}\n")
# else:
#     print("Bizda bu davlat haqida ma'lumot yuq" )



# 17-dars
# son=1
# while son<=5:
#     print(son, end=' ')
#     son=son+1
# print("kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol='istalgan son kiriting'
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#          print(float(qiymat)**2)

# son=0
# while son<10:
#     son += 1
    # if son%2!=0:
    #     continue
    # else:
    #     print(son)
    # son += 1


# Vazifalar
# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
#
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')

# savol ='Yoshingizni kiriting: '
# while True:
#     qiymat=input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh=int(qiymat)
#     if yosh<7:
#         narx=2000
#     elif 7<=yosh<=18:
#         narx=3000
#     elif 18<=yosh<=65:
#         narx=10000
#     else: narx=0
#     if narx==0:
#         print("Sizga tekin")
#     else:
#         print(f"Sizga chipta narxi: {narx} so'm")
#

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")



# 18-dars
# ismlar=[]
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1
# while True:
#     savol=f"{n}-do'stingiz ismini kiriting:"
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasiz? (ha/yoq)")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingiz ismini kiriting: ")
#     yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#
#     javob=input("Yana ma'lumot qo'shasizmi? (ha/yoq)")
#     if javob=="yoq":
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} yoshi {yosh}-yoshda")

# cars=['lacetti','nexia','toyota','nexia','malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar=['hasan','husan','olim','botir']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()}ning baholandi")
#     baholangan_talabalar[talaba]=(baho)
# print(baholangan_talabalar)


# Uyga vazifalar
# buyurtmalar=[]
# n=1
# while True:
#     buyurtma=input(f"{n}-buyurtmangizni kiriting: ")
#     buyurtmalar.append(buyurtma)
#     javob=input("Yana buyurtma berasizmi? (ha/yoq)")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Buyurtmalaringiz:")
# for buyurtma in buyurtmalar:
#     print(buyurtma.lower())


# mahsulotlar={}
# while True:
#       mahsulot=input("Mahsulot nomini kiriting: ")
#       narx=input(f"{mahsulot.title()}ning narxini kiriting: ")
#       mahsulotlar[mahsulot]=narx
#       javob=input("yana mahsulot kiritishni xohlaysizmi? (ha/yoq)")
#       if javob =='yoq':
#           break
# buyurtmalar=['olma', 'anjir','uzum', 'qovun']
# mahsulotlar={
#     'olma':20000,
#     'shaftoli':25000,
#     'tarvuz':40000,
#     'uzum':22000
# }
# while buyurtmalar:
#     buyurtma=buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx=mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()}-{narx} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")





# 19-dars
# def salom_ber(ism):
#     """Salom beruvchi funksiya """
#     print(f"Assalomu alaykum!, hurmatli {ism.title()}")
# salom_ber('hasan')
# salom_ber('boja')
# print(salom_ber.__doc__)
# def toliq_sim(ism, familiya):
#     """Foydalanuvchi ism va familyasini ko'rsatadi"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familyasi: {familiya.title()}")
# toliq_sim('hasan', 'olimov')

# def yosh_hisobla(tugilgan_yil,joriy_yil=2025):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f" {joriy_yil-tugilgan_yil} yoshda")
# yosh_hisobla('olim', 2003)
# yosh_hisobla(tugilgan_yil=2003)
# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
#
#
# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tugilgan_yil)

# uyga vazifalar
# def tugilgan_yil(ism,yosh,joriy_yil=2025):
#     """Foydalanuvchi tug'olgan yilini hisoblaydi"""
#     print(f"{ism.title()} {joriy_yil-yosh}-yilda tug'ilgan.")
# tugilgan_yil(ism='olim',yosh=22)

# def son_kvadrati(son):
#     son=int(input("Ixtiyoriy biror butun son kiriting: "))
#     print(f"{son}ning kvadrati {son**2}ga, kubi {son**3}ga teng.")
# son_kvadrati(son=-1)

# def sonning_juft_tekshirish(son):
#     son=int(input("Istalgan son kiriting: "))
#     if son%2:
#         print("Toq son")
#     else:
#         print("Juft son")
# sonning_juft_tekshirish(son=1)


# def son_ol(son1, son2):
#     """Foydalanuvchi sonlari ustida amallar"""
#     print("2ta son kiriting!")
#     son1=int(input("1-sonni kiriting: "))
#     son2=int(input("2-sonni kiriting: "))
#     if son1 > son2:
#         print(f"{son1} katta {son2}dan ")
#     elif son1==son2:
#         print("Sonlar teng")
# son_ol(1,2)

# def son_daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y}ga teng")
# son_daraja(9)

def son_bolinish(son):
    son=int(input("Ixtiyoriy sonni kiriting: "))
    for n in range(2,10):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
son_bolinish(5)
