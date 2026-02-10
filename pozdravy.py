print("=== DOBRÉ RÁNO/ODPOLEDNE/VEČER ===")
print("")

hodina = input("Kolik je hodin? (0-23) ")
hodina = int(hodina)

if hodina < 0:
    print("Chyba: Hodina nemůže být záporná!")
elif hodina == 12:
    print("Právě je poledne!")
elif hodina < 6:
    print("Ještě spíš? Dobrou noc!")
elif hodina < 12:
    print("Dobré ráno!")
elif hodina < 18:
    print("Dobré odpoledne!")
elif hodina < 22:
    print("Dobrý večer!")
elif hodina <= 23:
    print("Dobrou noc!")
else:
    print("Chyba: Hodina musí být 0-23!")