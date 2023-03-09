import io

while(True):

  val = input("1. Mata in order: \n2. Skriv ut orderlistan: \n3. Avsluta programmet: \n Välj ett av alternativen här: ")

  
  if(val=="1"):
      
    namn = input("Ange ditt namn: ")
    mail = input("Ange din mail: ")
    produkt = input("Ange din produkt: ")
    mängd = input("Ange mängden du vill köpa av denna produkt: ")
  
    f = io.open("orders.txt", "a", encoding="utf-8")

  
 

    f.write(namn + ";" + mail + ";" + produkt + ";" + mängd + "\n")

    f.close()
  elif(val=="3"):
    break
  elif(val=="2"):
    with io.open("orders.txt", "r") as fil_text:
      for x in fil_text:
        namn, mail, produkt, mängd =x.split(";")
        print("Namn: ",namn , "\nMail: ", mail, "\nProdukt: ", produkt, "\nmängd: ", mängd)
