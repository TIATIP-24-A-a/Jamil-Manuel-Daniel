#Eingabe von Zahlen durch User
print("Zahlen mit Komma getrennt eingeben:")
s = input()
zahlen = [int(x) for x in s.split(',') if x != '']

# Eine Liste von Zahlen
#zahlen: list[int] = [34, 1, 56, 23, 89, 12, 7, 13, 99, 0]

# Sortiere die Liste in aufsteigender Reihenfolge
zahlen.sort()

# Ausgabe der sortierten Liste
print("Sortierte Liste (aufsteigend):", zahlen)

# Sortieren in umgekehrter Reihenfolge
zahlen.sort(reverse=True)

# Ausgabe der sortierten Liste
print("Sortierte Liste (absteigend):", zahlen)