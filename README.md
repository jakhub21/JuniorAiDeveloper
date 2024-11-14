# ZadanieRektutacyjneOxido

## Opis aplikacji

Aplikacja łączy się z API OpenAI, aby przekształcić artykuł w pliku tekstowym na kod HTML. Proces obejmuje:

1. Odczytanie zawartości artykułu z pliku tekstowego.
2. Przesłanie treści do API OpenAI, które przekształca ją na strukturę HTML z odpowiednimi tagami i miejscami na grafiki.
3. Wygenerowanie kodu HTML, który jest zapisywany w pliku `.html`.

Aplikacja pozwala na:
- Generowanie kodu HTML artykułu.
- Wstawianie grafik w odpowiednich miejscach w artykule.
- Wstawianie tagów `<img>` z atrybutem `src="image_placeholder.jpg"` oraz odpowiednim atrybutem `alt`, który zawiera prompt do wygenerowania grafiki.

## Wymagania

- Python 3.7+
- Zainstalowane biblioteki:
  - `openai` – do łączenia z API OpenAI
  - `python-dotenv` – do zarządzania zmiennymi środowiskowymi

## Instrukcja uruchomienia

### Krok 1: Ustawienie klucza API

1. Zarejestruj się na stronie [OpenAI](https://platform.openai.com/signup) i uzyskaj swój klucz API.
2. Utwórz plik `.env` w katalogu głównym projektu i dodaj do niego swój klucz API:

    ```
    GPT_API="twój_klucz_api"
    ```

### Krok 2: Instalacja zależności

Zainstaluj wymagane biblioteki za pomocą `pip`. W terminalu przejdź do katalogu głównego projektu i uruchom:

```bash
pip install openai os
```

### Krok 3: Przygotowanie pliku artykułu

Przygotuj plik tekstowy artykul.txt, który będzie zawierał artykuł do przetworzenia. Artykuł powinien być zapisany w formacie czystego tekstu (np. .txt).

### Krok 4: Uruchomienie aplikacji

W terminalu przejdź do katalogu głównego projektu i uruchom aplikację:

```bash
python app.py
```

Lub:

```bash 
python3 app.py
```

### Krok 5: Wynik

Po uruchomieniu aplikacji w katalogu głównym projektu zostaną utworzone dwa kluczowe pliki:

1. **`artykul.html`** – Ten plik zawiera przekształcony artykuł w formacie HTML, wygenerowany przez API OpenAI. Kod HTML zawiera treść artykułu, poprawnie ustrukturyzowaną przy użyciu tagów HTML oraz oznaczenia miejsc na grafiki z tagami `<img>` i odpowiadającymi im opisami w atrybucie `alt`. Jest to surowy kod HTML przeznaczony do osadzenia w szablonie, bez nagłówków czy stylizacji.

2. **`podglad.html`** – Jest to gotowy podgląd artykułu w pełnym szablonie HTML. Aplikacja automatycznie podmienia sekcję `<body>` w pliku szablonowym `szablon.html` na wygenerowaną treść z `artykul.html` i zapisuje wynikowy dokument jako `podglad.html`. Dzięki temu `podglad.html` jest kompletnym plikiem, gotowym do wyświetlenia w przeglądarce, oferującym pełen, sformatowany widok artykułu.

#### Podsumowanie wyników:

- **`artykul.html`** – surowa treść artykułu w HTML, przeznaczona do osadzenia w szablonie.
- **`podglad.html`** – pełen podgląd artykułu gotowy do otwarcia w przeglądarce.

Teraz możesz otworzyć `podglad.html` w dowolnej przeglądarce, aby zobaczyć gotowy artykuł w pełnym szablonie HTML.
