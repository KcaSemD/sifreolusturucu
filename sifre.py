import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifreniz kaç karaktarden oluşsun istersiniz?"))


password = ""      
for i in range(sayi):
    password += random.choice(karakterler)


print("Şifreniz=", password)
