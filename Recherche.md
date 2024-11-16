Problem: 
Sortieren von Zahlen aus einer Liste

Gewünschtes Resultat:
Zahlen in aufsteigender Reihenfolge ausgeben

Mögliche Lösungen:
[Zahlen].sort()
sorted([Zahlen])

Funktionsweise:
flowchart TD
    A[input numbers] -->|write in list| B(write numbers in list)
    B --> C{Pick N Number}
    C -->|interieren| D{value of number and position in list}
    D -->|first number| E{write number in new sorted list at position}
    D -->|value of new number|E
    E -->|get next number| C
    E -->|wirte number| F[list]

Quellen:
https://docs.python.org/3/howto/sorting.html
https://www.w3schools.com/python/ref_list_sort.asp