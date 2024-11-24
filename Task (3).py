list = ["Alisafa" , "Cavid" , "Ali"]
secim = input("Ad daxil etmek isteyirsinizse (1), silmek isteyirsinizse (2) daxil edin: ")
if secim == "1":
    secim1 = input("Ad elave edin: ")
    if secim1 == "":
        print("Ad daxil etmediniz: ")
    elif len(secim1) >= 15:
       print("Ad cox uzundur,maksimum 15 herf")
    else:
      list.append(secim1)
      print(list)
elif secim == "2":
    secim2 = input("Silmek istediyiniz adi yazin: ")
    if secim2 == "":
        print("Ad daxil etmediniz: ")
    elif len(secim2) >= 15:
       print("Ad cox uzundur,maksimum 15 herf")
    else:
      list.remove(secim2)
      print(list)
print("Siyahida", len(list), "eded ad var")