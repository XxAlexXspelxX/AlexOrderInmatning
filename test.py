import io
#Mata in personuppgifter
förnamn = input("mata in ditt förnamn: ")
efternamn = input("Mata in ditt efternamn: ")

#öppna fil
f = io.open("minfil.txt", "a", encoding="utf-8")
#skapa sträng för att skriva till fil

print(f.read())
text = förnamn + ";" + efternamn + "\n"
#skriv till filen
f.write(text)

for x in f:
  firstname, lastname =x.split(";")
  print("förnamn: ", firstname, "n\efternamn:", lastname)

#Stäng filen
f.close()