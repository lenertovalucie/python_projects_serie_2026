line = "======================"
print(line)
print("Restaurace u Pythona")
print(line)
print("")
print("1. Pizza - 150 Kč")
print("2. Hamburger - 120 Kč")
print("3. Salát - 90 Kč")
print("")
print(line) # 

# Získání údajů od zákazníka
objednavka = input("Co si dáte? ")
jmeno = input("Vaše jméno: ")
adresa = input("Doručovací adresa: ")

# Potvrzení objednávky
print("")
print("=============================")
print("Děkujeme, " + jmeno + "!")
print("Vaše objednávka: " + objednavka)
print("Doručíme na: " + adresa)
print("=============================")
