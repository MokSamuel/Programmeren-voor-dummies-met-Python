import pandas as pd #deze regel importeert een pakket met functies, komen we later op terug

uur = pd.datetime.now().hour #sla het huidige uur op als variabele

if uur > 17: #is uur 18 of hoger?
    print("Het is avond")
elif uur > 11: #anders: is het uur 12 of hoger?
    print("Het is middag")
else: #de rest van de uren zijn voor 12 uur
    print("Het is ochtend")
