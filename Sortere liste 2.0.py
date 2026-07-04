liste = []

sortlist = []


def gjennomsnitt(x: list):
    total = 0
    for i in x:
        total += i
    return total / len(x)

print("\nTrykk enter uten tall når listen er ferdig\n\nSkriv inn tallene i listen din:")

#Legger til tall i listen frem til du ikke vill lenger
while True:
    try:
        tall = input()
        if tall == "":
            break
        elif float(tall).is_integer() == True:
            liste.append(int(tall))
        else:
            liste.append(float(tall))
    except ValueError:
        pass

konstantliste = liste.copy()

#Teller antall av hvert tall i listen også legger dem til i rekkefølge
# for i in range(max(liste)+1):
#     for a in range(liste.count(i)):
#         sortlist.append(i)

orgliste = liste.copy()

telleliste = liste.copy()

# Legger til den minste verdien i en liste også fjerner 
# den verdien helt til listen er er tom
while len(liste) > 0:
    sortlist.append(min(liste))
    liste.pop(liste.index(min(liste)))
    

print(f"Original liste:\n{orgliste}\n\nSortert liste:\n{sortlist}\n\n")

typetall_dict = {}

while len(telleliste) > 0:

    # Lager en dict med "Tall"(int):"Antall av tall"(int) som key:value pairs 
    # for å kunne finne typetallet
    typetall_dict.update({min(telleliste):telleliste.count(min(telleliste))})

    antall = konstantliste.count(min(telleliste))
    
    print(F"Nummer: {min(telleliste)}\tAntall: {antall}")

    #Fjerner tallene i listen som den akkurat har telt
    for i in range(telleliste.count(min(telleliste))):
        telleliste.pop(telleliste.index(min(telleliste)))

print(F"\nGjennomsnittet av listen er: {gjennomsnitt(konstantliste):.2f}")

# Lager en liste med Key verdiene som har lik Value verdi som antallet av typetallet, 
# altså typetallene
typetallene = [key for key,value in typetall_dict.items() if value == max(typetall_dict.values())]

print("\nTypetall: ",end="")

for i in range(len(typetallene)):
    print(typetallene[i],end=", ")