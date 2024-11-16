from sort import sort

#Eingabe von Zahlen durch User
print("Zahlen mit Komma getrennt eingeben:")
s = input()
zahlen = [int(x) for x in s.split(',') if x != '']

# Sortiere die Liste in aufsteigender Reihenfolge
sortierteZahlen = sort(zahlen)

# Ausgabe der sortierten Liste
print("Sortierte Liste (aufsteigend):", sortierteZahlen)

# Sortieren in umgekehrter Reihenfolge
#zahlen.sort(reverse=True)

# Ausgabe der sortierten Liste
#print("Sortierte Liste (absteigend):", zahlen)