import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('baza_danych.db')
cursor = conn.cursor()

# Funkcja dodająca artykuł do tabeli Artykuly
def dodaj_artykul(tytul, tresc):
    cursor.execute("INSERT INTO Artykuly (tytul, tresc) VALUES (?, ?)", (tytul, tresc))
    conn.commit()
    print("Dodano artykuł:", tytul)

# Funkcja dodająca streszczenie artykułu do tabeli Streszczenia
def dodaj_streszczenie(id_artykulu, streszczenie):
    cursor.execute("INSERT INTO Streszczenia (id_artykulu, streszczenie) VALUES (?, ?)", (id_artykulu, streszczenie))
    conn.commit()
    print("Dodano streszczenie do artykułu o ID:", id_artykulu)

# Przykładowe artykuły
artykul_1 = {
    "tytul": "Przykładowy artykuł 1",
    "tresc": "To jest pełna treść artykułu numer 1."
}

artykul_2 = {
    "tytul": "Przykładowy artykuł 2",
    "tresc": "To jest pełna treść artykułu numer 2."
}

# Dodanie artykułów
dodaj_artykul(artykul_1["tytul"], artykul_1["tresc"])
dodaj_artykul(artykul_2["tytul"], artykul_2["tresc"])

# Przykładowe streszczenia artykułów
streszczenie_1 = "Streszczenie artykułu numer 1."
streszczenie_2 = "Streszczenie artykułu numer 2."

# Dodanie streszczeń
dodaj_streszczenie(1, streszczenie_1)  # Streszczenie artykułu 1
dodaj_streszczenie(2, streszczenie_2)  # Streszczenie artykułu 2

# Zamknięcie połączenia z bazą danych
conn.close()
