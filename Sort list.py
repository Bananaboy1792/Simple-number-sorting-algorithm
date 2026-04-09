list = []

sortlist = []

a = 0

print("\nTrykk enter uten tall når listen er ferdig\n\nSkriv inn tallene i listen din:")

#Legger til tall i listen frem til du ikke vill lenger
while True:
    tall = input()
    if str(tall) == "":
        break
    else:
        list.append(int(tall))


#Teller antall av hvert tall i listen også legger dem til i rekkefølge
# for i in range(max(list)+1):
#     for a in range(list.count(i)):
#         sortlist.append(i)

orgliste = list.copy()

#Legger til den minste verdien i en liste også fjerner den verdien helt til listen er er tom

while len(list) > 0:
    sortlist.append(min(list))
    list.pop(list.index(min(list)))

print(f"Original liste:\n{orgliste}\n\nSortert liste:\n")


print(f"{sortlist}\n")
