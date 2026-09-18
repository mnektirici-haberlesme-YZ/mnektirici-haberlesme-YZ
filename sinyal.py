# Fiber sinyal kaybı hesaplayıcı - İlk projem
mesafe = float(input("Mesafe km: "))
kayip = mesafe * 0.35
print(f"Toplam kayip: {kayip} dB")
if kayip > 20:
    print("Guclendirici gerekli")
else:
    print("Sinyal normal")