print('Birim zamanda sabit bir hızla alınan yolu hesaplama botuna hoş geldiniz!')
secenek = input("""
Hangi bilinmeyeni hesaplamak istiyorsunuz? Yazınız:
    
ALINAN YOL
SABIT SURAT
ZAMAN

""")

if secenek.upper() == "ALINAN YOL":
    v = float(input("V (sabit hız) değerimiz kaç olsun? "))
    t = float(input("t (zaman) değerimiz kaç olsun? "))
    x = v * t
    print("Alınan yol (x) {}".format(x))
  
    
if secenek.upper() == "SABIT SURAT":
    x = float(input("X değerimiz kaç olsun? "))    
    t = float(input("t (zaman) değerimiz kaç olsun? ")) 
    v = x / t
    print("Sabit sürat (x) {}".format(x))
  
  
if secenek.upper() == "ZAMAN":
    x = float(input("X değerimiz kaç olsun? "))
    v = float(input("V (sabit hız) değerimiz kaç olsun? "))    
    t = x / v
    print("Zaman (x) {}".format(x))
    

  







