mesafe = float(input("Mesafe km: "))
fiber = input("Fiber tipi single/multi: ")
if fiber == "single":
    oran = 0.35
else:
    oran = 2.5
kayip = mesafe * oran
print(f"Toplam kayip: {kayip} dB")
if kayip > 20:
    print("Guclendirici gerekli!")
else:
    print("Sinyal normal")