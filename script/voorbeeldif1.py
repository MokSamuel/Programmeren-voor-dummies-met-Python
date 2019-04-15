y= 30 #stel een getal in


print("Y is gelijk aan " +str(y)) #geef aan de gebruiker aan welk getal er ingesteld is
x = float(input("Welk nummer wil je vergelijken met Y?")) #vraag de gebruik om een getal en sla op als x

if x > y: #als x groter is dan y...
    print("X is groter dan Y!")
elif x == y: #anders als x gelijk is aan y...
    print("Y is gelijk aan X!")
else:  #en anders is x kleiner dan y...
    print("X is kleiner dan Y!")
