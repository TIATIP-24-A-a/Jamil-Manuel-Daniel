Problem: 
Sortieren von Zahlen aus einer Liste

Gewünschtes Resultat:
Zahlen in aufsteigender Reihenfolge ausgeben

Funktionsweise:
flowchart TD
    A[input array] --> B{len array}
    B -->|if n<=1|Z[return array]
    B --> C[for i in 1-len array]
    C --> D[key = array i
               j = i-1]
    D --> E[while j >= 0
            key < array j]
    E --> F[array j +1 = array j 
            j-=1]
    F --> G[array j+1=key]
    G -->|repeat til i=n|C
    G --> Z

![Folwchart insertionsort.png](Folwchart%20insertionsort.png)

Quellen:
https://docs.python.org/3/howto/sorting.html
https://www.w3schools.com/python/ref_list_sort.asp