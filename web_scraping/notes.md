# Web scrpaing using OpenAI models STARTS WITH ARTICLES

`pipreqs /to/path/`

IDEA1 - Stworzenie bota na twittera ktory streszcza wszytkie artykuly

## Scrapowanie przy pomocy modelu GPT

1. Połączneie z GPT-3.5
2. Jak dobrze scrapowac?

Pobieranie tesktu html ze znacnzikami ze strony

Przy pomocy modelu GPT-3.5 wyodrebnienie calego tekstu ze wzgledu na:
    - naglowki
    - znacnziki tekstu jak <p>, <b>, itd.

Przy pomocy wyboru funkcji czy podac streszczony tekst czy podac pelny tekst artykulu

### Pełny schemat scrapowania artykulow przy pomocy mdoeli GPT

1. Wczytanie strony
2. Sprawdzenie czy mozna scrapowac tekst z tej strony (w poznijeszym etapie na razie tak bo wszytko jest do uzytku wlasnego)
3. Sprawdzenie czy mozna dokonoac dobrego scrapownaia
4. Wyslanie tekstu do modelu GPT zeby zescrapowac tekst
5. Dodanie scrapowanego tekstu do durgiego modelu GPT zeby sprawdzic czy scrapowanie zostalo wykonane dobrze
6. Streszczneie artykulu przez model GPT
7. Wyslanie tekstu do bazy danych calego i streszczonego oznaczonego odpoiwienidnimi naglowkami

