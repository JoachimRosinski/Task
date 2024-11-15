# Task  
  
Aplikacja do konwersji artykułów tekstowych do formatu HTML, zachowując odpowiednią strukturę HTML, dodając miejsca na obrazy z sugestiami dotyczącymi generowania obrazów oraz dodając do nich podpisy. Aplikacja korzysta z OpenAI GPT-4 do generowania treści HTML na podstawie podanych artykułów.  
  
## Wymagania  
  
Aby uruchomić aplikację, potrzebujesz:  
  
- **Python 3.6+**  
- Zainstalowane biblioteki:  
  - `openai`  
  - `os`

## Opis działania aplikacji  
Aplikacja wykonuje następujące kroki:  

Pobieranie klucza API OpenAI i tworzenie instancji klasy OpenAI.

Odczyt artykułu – Aplikacja odczytuje artykuł z pliku tekstowego (np. `art.txt`).  

Generowanie HTML – Na podstawie treści artykułu aplikacja generuje odpowiednią strukturę HTML, stosując ustalone w promptach zasady.

Zapisanie wygenerowanego HTML - Aplikacja zapisuje wygenerowany kod HTML do pliku (domyślnie `artykul.html`) za pomocą funkcji `save_html`:

## Instrukcja uruchomienia  
### Krok 1: Ustawienie klucza API OpenAI  
Aby korzystać z aplikacji, musisz posiadać klucz API OpenAI. 
  
Po uzyskaniu klucza API, ustaw go jako zmienną środowiskową w systemie. Możesz to zrobić w terminalu, wpisując:  
  
```powershell
setx OPENAI_API_KEY "<your_api_key_here>"
```  

Alternatywnie zakomentuj:
```pyton
openaiapi_key = os.getenv("OPENAI_API_KEY")
```
I odkomentuj: 
```pyton
# openaiapi_key = "<your_api_key>"
```
Po czym wpisz swój api_key w miejsce <your_api_key> 


### Krok 2: Przygotowanie artykułu  
Upewnij się, że masz plik tekstowy (domyślnie: `art.txt`), który zawiera artykuł, który chcesz przekształcić do formatu HTML.  
  
### Krok 3: Uruchomienie aplikacji  
Po przygotowaniu pliku artykułu i ustawieniu klucza API, można uruchomić aplikację za pomocą poniższego polecenia będąc w odpowiednim katalogu:  
  
```bash
python task.py
```  

Aplikacja odczyta artykuł, przekształci go do formatu HTML i zapisze wynik w pliku `artykul.html`.  
  
### Krok 4: Sprawdzanie wyników  
Po uruchomieniu aplikacji, sprawdź plik `artykul.html`, który zawiera wygenerowany artykuł w formacie HTML.  


### Szablon HTML do podglądu artykułu `szablon.html`
W celu umożliwienia wizualizacji artykułu po wklejeniu jego kodu do sekcji <body>, stworzono pusty szablon HTML.
### Pełny podgląd artykułu `podglad.html`
Aby umożliwić pełny podgląd artykułu, stworzono osobny plik HTML, w którym wklejona treść artykułu jest automatycznie wizualizowana w przygotowanej sekcji <body>. 
