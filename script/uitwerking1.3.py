#Voorbeelduitwerking 1.3

y=input("Geef een geheel getal. ")
if y.isnumeric():
  y=int(y)
  if y % 2 == 0:
      print("Het getal is even")
  else:
	  print("Het getal is oneven")
else:
	print("Dit is geen getal!")
