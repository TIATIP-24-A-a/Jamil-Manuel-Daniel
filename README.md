# Jamil-Manuel-Daniel  
## Python Sortierfunktionen  

Dieses Projekt implementiert einfache Sortieralgorithmen in Python und ermöglicht die Eingabe von Zahlen, um diese zu sortieren.  

---

## Dateien  

- **`sortFunction.py`**  
  Beinhaltet die Implementierung von zwei Sortierfunktionen:  
  - `sort(a)`: Nutzt die eingebaute `sorted`-Funktion, um eine Liste effizient zu sortieren.  
  - `insertionsort(b)`: Implementiert den Insertion Sort Algorithmus, um eine Liste manuell zu sortieren.  

- **`UserInput.py`**  
  Ermöglicht Benutzern, eine Liste von Zahlen einzugeben und diese mit beiden Sortierfunktionen zu sortieren.  

- **`test_insertions.py`**  
  Testet die `insertionsort`-Funktion anhand von vordefinierten Testfällen.  

- **`test_sort.py`**  
  Testet die `sort`-Funktion mit vordefinierten Datensätzen.  

- **`Recherche.md`**  
  Enthält die Projektdokumentation, einschließlich theoretischer Hintergründe und Ressourcen.  

---

## Voraussetzungen  

1. Installieren Sie [Python 3](https://www.python.org/downloads/).  
2. (Optional) Verwenden Sie eine IDE wie [PyCharm](https://www.jetbrains.com/pycharm/) oder [Visual Studio Code](https://code.visualstudio.com/).  

---

## Nutzung  

1. Klonen Sie das Repository oder laden Sie die Dateien herunter:  
   ```bash  
   git clone <https://github.com/TIATIP-24-A-a/Jamil-Manuel-Daniel.git>

2. Führen Sie die Datei `UserInput.py` aus:
   ```bash
   python UserInput.py
3. Geben Sie eine Liste von Zahlen ein, die durch Kommas getrennt sind, z. B.: 
5,3,8,6,2  

4. Das Programm gibt die sortierten Listen aus, einmal mit sort und einmal mit insertionsort.

## Beispielausgabe

Zahlen mit Komma getrennt eingeben:
5,3,8,6,2
Sortierte Liste (sort): [2, 3, 5, 6, 8]
Sortierte Liste (insertionsort): [2, 3, 5, 6, 8]

## Tests
Die Dateien test_insertions.py und test_sort.py enthalten Unit-Tests, um die Sortierfunktionen zu validieren. Führen Sie die Tests wie folgt aus:

   python -m unittest test_insertions.py  

   python -m unittest test_sort.py  

## Anmerkungen
Die Funktion sort nutzt die eingebaute Python-Funktion sorted und bietet eine schnelle und einfache Lösung.
Der Algorithmus insertionsort dient als Beispiel für eine manuelle Implementierung eines klassischen Sortieralgorithmus.
