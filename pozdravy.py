print("=== DOBRÉ RÁNO/ODPOLEDNE/VEČER ===")
print("")

hodina = int(input("Kolik je hodin? "))
print(hodina)

if hodina < 0:
    print("Chyba: Hodina nemůže být záporná!")
elif hodina > 23:
    print("Chyba: Hodina musí být 0-23!")
elif hodina == 12:
    print("Právě je poledne!")
elif hodina < 12:
    print("Dobré ráno!")
elif hodina < 18:
    print("Dobré odpoledne!")
elif hodina < 22:
    print("Dobrý večer!")
else:
    print("Dobrou noc!")