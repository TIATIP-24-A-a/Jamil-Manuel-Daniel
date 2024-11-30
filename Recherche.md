# Sortierfunktion Projekt

## Problemstellung

Das Ziel dieses Projekts ist das Sortieren von Zahlen aus einer Liste.

## Gewünschtes Resultat

Die Zahlen sollen in **aufsteigender Reihenfolge** ausgegeben werden.

## Funktionsweise

### Ablaufdiagramm (Flowchart)

Das folgende Ablaufdiagramm visualisiert die Funktionsweise des verwendeten Sortieralgorithmus (Insertion Sort):

```mermaid
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