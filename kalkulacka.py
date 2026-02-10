print("=== KALKULAČKA SPROPITNÉHO ===")
print("")

ucet = int(input("Kolik byl účet? "))
spropitne_procent = int(input("Kolik procent spropitného? "))
pocet_lidi = int(input("Kolik vás bylo? "))

spropitne = ucet * spropitne_procent / 100
celkem = ucet + spropitne
na_osobu = round(celkem / pocet_lidi, 2)

print("")
print(f"Účet: {ucet} Kč")
print(f"Spropitné ({spropitne_procent}%): {spropitne} Kč")
print(f"Celkem: {celkem} Kč")
print(f"Každý platí: {na_osobu} Kč")