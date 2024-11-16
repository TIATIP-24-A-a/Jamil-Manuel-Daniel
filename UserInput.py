from sort import sort
from sort import insertionsort

#Eingabe von Zahlen durch User
#print("Zahlen mit Komma getrennt eingeben:")
#s = input()
#zahlen = [int(x) for x in s.split(',') if x != '']
zahlen = [1,3,2]

# Sortiere die Liste in aufsteigender Reihenfolge
sortierteZahlen = sort(zahlen)
sortierteZahlen2 = insertionsort(zahlen)

# Ausgabe der sortierten Liste
print("Sortierte Liste (sort):", sortierteZahlen)
print("Sortierte Liste (insertionsort):", sortierteZahlen2)

# Sortieren in umgekehrter Reihenfolge
#zahlen.sort(reverse=True)

# Ausgabe der sortierten Liste
#print("Sortierte Liste (absteigend):", zahlen)