# mnektirici-hsberlesme-YZ
# Gelismis fiber hesaplayici v2
mesafe = float(input("Mesafe km: "))
fiber_tipi = input("Fiber tipi (single/multi): ")

if fiber_tipi == "single":
    kayip_orani = 0.35
else:
    kayip_orani = 2.5

toplam_kayip = mesafe * kayip_orani
print(f"Toplam kayip: {toplam_kayip} dB")

if toplam_kayip > 20:
    print("UYARI: Guclendirici gerekli!")
    print(f"Gerekli guclendirici sayisi: {int(toplam_kayip // 20)}")
else:
    print("Sinyal normal, ek ekipman gerekmez.")
