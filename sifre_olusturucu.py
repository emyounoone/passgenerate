import time
from colorama import Fore, Back, Style, init
import sys
import os
init(autoreset=True)


print(Fore.GREEN+"EMYOUNOONE Tarafından Kodlanmıştır ")
print(Fore.GREEN+"www.siberguvenlikblogu.com ")
input("Şifre Oluşturucu Programına Hoş Geldiniz...\n \nDevam Etmek İçin Enter'e Basınız..\n")
os.system('cls' if os.name=='nt' else 'clear')
print(Fore.RED+"BİLMENİZ GEREKEN HER ŞEY PROGRAMI KURDUĞUNUZ YERDE BENİ OKU.txt DOSYASININ İÇİNDE..\n")

while True:
    f = open("ŞİFRELER.txt", "a")

    import random
    şifre_oluşturucu="""abcdfeghijklmnoprstuvyzxwq\
ABCDEFGHIJKLMNOPRSTUVYZXQW\
1234567890\
!'^+%&/()=?}][{#£><.,-"$*:;|_"""
    print("Şifrenin maximum uzunluğu 30 minimum uzunluğu 8 olmalı.\n")
    
    uzunluk=int(input("Şifreniz için bir uzunluk belirtin :"))
    
    kayıt=input("Şifrenizi Ne Olarak Kayıt Edelim :")

    if uzunluk == (8):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE GÜVENLİKSİZ--- "+" : " + password+"\n" )
    elif uzunluk == (9):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKSİZ--- "+kayıt+" =" + password+"\n" )
    elif uzunluk == (10):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKSİZ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (11):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (12):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" =" + password+"\n" )
    elif uzunluk == (13):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (14):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (15):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE ORTA GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (16):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (17):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (18):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (19):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (20):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (21):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (22):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (23):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (24):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (25):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (26):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (27):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (28):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (29):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    elif uzunluk == (30):
        password="".join(random.sample(şifre_oluşturucu,uzunluk))
        print("\n\nŞifre Oluşturuludu: "+Fore.RED+password)
        f.write("ŞİFRE YÜKSEK GÜVENLİKLİ--- "+kayıt+" : " + password+"\n" )
    else:
        print("Lütfen Geçerli Bir uzunluk Giriniz..")
    soru=int(input("\n\nYeniden Oluşturmak için 1'e, Çıkmak İçin 2'ye Basınız :"))
    if soru == (1):
        continue
    elif soru == (2):
        break
        quit()
    else:
        
        print("Lütfen Geçerli Bir Kod Giriniz")
        input("")
                     
