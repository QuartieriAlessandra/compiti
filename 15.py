nazioni = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia"]
capitali = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi" ] 

nazione = input("inserisci nazione")
if nazione in nazioni:
    print(capitali[nazioni.index(nazione)])
else:
    print("errore")