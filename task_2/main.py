word = str(input("Введіть довільне слово: "))
count = word.count("_")
if count > 0 :
    print("В заданому слові символи «_» з'являються %d разів" % (count))
else: print("В заданому слові символ «_» відсутній")