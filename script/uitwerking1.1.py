#Voorbeelduitwerkingen opgave 1.1


##Input vragen en opschonen
letter = str(input("Welke letter moet ik testen? ")) #vraag om input en sla op als string

letter = letter.strip() #BONUS: haal alle spaties weg
if letter.isalpha(): #BONUS: Check of het een letter is, voer dan uit

  ##Testen op klinker
  if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y": #check voor kleine klinkers
      print(letter + " is een klinker")
  elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "Y": #check voor grote klinkers
      print(letter + " is een klinker")
  else: #anders is het een medeklinker!
      print(letter + " is een medeklinker")

  ##BONUS: andere manier om het te doen (kortere if door gebruik van een set):

  klinkers = {"a","e","i","o","u","y","A","E","I","O","U","Y"}

  if letter in klinkers: #als je letter kan vinden in de set van klinkers dan...
      print(letter + " is een klinker")
  else: 
      print(letter + " is een medeklinker")

else: #BONUS: Als het geen letter is, geef dat aan
    print(letter + " is geen letter.")