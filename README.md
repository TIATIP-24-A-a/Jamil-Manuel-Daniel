# Jamil-Manuel-Daniel
# Python Sortierfunktionen

Dieses Projekt implementiert einfache Sortieralgorithmen in Python und ermöglicht die Eingabe von Zahlen, um diese zu sortieren. Es enthält Dateien:

- **`sortFunction.py`**: Enthält die Implementierung von zwei Sortierfunktionen:
  - `sort(a)`: Verwendet die eingebaute `sorted`-Funktion, um eine Liste zu sortieren.
  - `insertionsort(b)`: Implementiert den Insertion Sort Algorithmus, um eine Liste manuell zu sortieren.

- **`UserInput.py`**: Ermöglicht es dem Benutzer, eine Liste von Zahlen einzugeben und diese mit beiden Sortiermethoden zu sortieren. 

- **`test_insertions.py`**: Testet die Insertionsort Algorithmus Funktion. 

- **`test_sort.py`**: Testet die Sort Algorithmus Funktion.

- **`Recherche.md`**: Die Dokumentation des Projekts. 
- 
## Voraussetzungen

Stellen Sie sicher, dass Python 3 installiert ist, bevor Sie das Projekt ausführen.

Alternativ können Sie eine integrierte Entwicklungsumgebung wie PyCharm oder Visual Studio Code verwenden.

## Nutzung

1. Klonen Sie das Repository oder laden Sie die Dateien herunter.
2. Öffnen Sie ein Terminal oder eine Eingabeaufforderung im Verzeichnis der Dateien.
3. Führen Sie die Datei `UserInput.py` aus:
   ```bash
   python UserInput.py
4. Geben Sie eine Liste von Zahlen ein, die durch Kommas getrennt sind, z. B.: 5,3,8,6,2
5. Die Anwendung gibt die sortierten Listen aus, einmal mit sort und einmal mit insertionsort.

## Beispielausgabe

Zahlen mit Komma getrennt eingeben:
5,3,8,6,2
Sortierte Liste (sort): [2, 3, 5, 6, 8]
Sortierte Liste (insertionsort): [2, 3, 5, 6, 8]

## Dateien
sortFunction.py: Enthält die Sortierlogik.
UserInput.py: Verbindet die Sortierfunktionen mit Benutzereingaben.

## Anmerkungen
Die Funktion sort nutzt die eingebaute Python-Funktion sorted und bietet eine schnelle und einfache Lösung.
Der Algorithmus insertionsort dient als Beispiel für eine manuelle Implementierung eines klassischen Sortieralgorithmus.
