#Deze functie bepaalt het nulpunt van een polynoom van de vorm ax^2+bx+c.
#Simpele vorm: geeft None als er geen nulpunt is en geeft maar 1 van de 2 nulpunten bij D>0

def vindNulpunt(a,b,c):
    D = b ** 2 - 4*a*c
    if D < 0:
        nulpunt=None
    else:
        nulpunt=(-b + D**0.5)/(2*a)
    return nulpunt

#Geavanceerde vorm: 
#Deze functie gebruikt een lijst om twee antwoorden te geven als D > 0.
def vindNulpunt(a,b,c):
    D = b ** 2 - 4*a*c
    if D < 0:
        nulpunt=None
    elif D == 0:
        nulpunt=(-b + D**0.5)/(2*a)
    elif D > 0:
        nulpunt1=(-b + D**0.5)/(2*a)
        nulpunt2=(-b - D**0.5)/(2*a)
        nulpunt=[nulpunt1,nulpunt2]
    return nulpunt