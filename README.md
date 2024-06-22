# AIproject
Projekt zaliczeniowy na zajęcia z przedmiotu Sztuczna inteligencja. Narzędzie służące do prognozy cen akcji przy użyciu prostych modeli prognostycznych. Opracowane przy współpracy z AI.

# Sztuczna Inteligencja
**Paweł Spasiuk, Bartłomiej Przybylski**

## Instrukcja Uruchomienia

### Zainstaluj Wymagane Biblioteki:

1. Upewnij się, że masz zainstalowane następujące biblioteki w swoim środowisku Python:
    ```bash
    pip install Flask pandas matplotlib statsmodels yfinance
    ```
    lub w terminalu VS Code:
    ```bash
    py -m pip install Flask pandas matplotlib statsmodels yfinance
    ```

2. Pobierz pliki projektu na swój komputer.

3. Upewnij się, że pliki są zorganizowane zgodnie z poniższą strukturą:
    ```
    Folder z projektem/
    ├── przewidywacz.py
    └── templates/
        ├── index.html
        ├── result.html
        └── description.html
    ```

4. Przejdź do katalogu, w którym znajduje się plik `przewidywacz.py`, i uruchom aplikację:

5. Otwórz przeglądarkę internetową i wejdź na adres:
    ```
    http://127.0.0.1:5000/
    ```
    lub
    ```
    localhost:5000
    ```

### Korzystanie z Aplikacji:

- **Symbol Spółki:** Wpisz symbol giełdowy spółki, której prognozę chcesz wyznaczyć (np. AAPL dla Apple Inc., korzystaliśmy z API Yahoo Finance i z tego źródła polecamy szukać symboli).
- **Rok Początkowy:** Wpisz rok, od którego mają być pobierane dane historyczne.
- **Model Prognostyczny:** Wybierz jeden z dostępnych modeli prognostycznych.
- **Prezentacja Wyniku:** Kliknij przycisk "Prognozuj", aby zobaczyć wyniki prognozy w formie wykresu i tabeli.

### Uwagi

**Disclaimer:** To narzędzie służy jedynie celom edukacyjnym i nie jest przeznaczone do udzielania porad inwestycyjnych.

**Autorzy:** Paweł Spasiuk, Bartek Przybylski

## Opis Narzędzia

Jest to narzędzie pozwalające na przeprowadzenie prognozy wybranej spółki akcyjnej. Prognoza jest wyznaczana przy pomocy modeli prognostycznych badających sezonowość poznanych na kierunku Analityka Gospodarcza. Narzędzie jest pracą zaliczeniową na zajęcia ze Sztucznej Inteligencji prowadzonych przez dr. Grzegorza Kwiatkowskiego. Autorami narzędzia są: Paweł Spasiuk, Bartek Przybylski, wujek Czarek (Chat GPT) oraz ciocia Klaudia (ClaudeAI).

### Wkład AI w Tworzenie Narzędzia

Na stworzenie aplikacji wpadliśmy podczas nauki na kolokwium z przedmiotu Prognozowanie i Symulacje. Przeszukując internet w poszukiwaniu podobnych narzędzi jako pomocy naukowych, natrafiliśmy na repozytorium: [https://github.com/crypto-code/Stock-Market](https://github.com/crypto-code/Stock-Market) - jest to o wiele bardziej zaawansowane narzędzie opierające się na uczeniu maszynowym.

Chcieliśmy, żeby dało się wyświetlać prognozę z poziomu przeglądarki, jednak nie mamy wystarczającej wiedzy, żeby stworzyć aplikację z podobnym rozwiązaniem. Kto ją ma? Sztuczna Inteligencja! Szybko napotkaliśmy pierwsze problemy z bibliotekami Python, więc poprosiliśmy Chata o pomoc w dobraniu innych, zastępczych bibliotek i zmodyfikowanie kodu. Sukces! Udało się, prognoza działa, ale niestety, trzeba na nią czekać bardzo długo (około 1h na naszych PC, zależy od mocy obliczeniowej).

Wróciliśmy więc do pierwotnego pomysłu i stworzyliśmy narzędzie w oparciu o proste modele prognostyczne. Nie są tak dokładne jak wersja z Long Short Term Memory networks, ale pozwalają na ocenienie kierunku, w jakim mogą iść ceny akcji wybranej spółki, szczególnie jeśli zbadamy różne warianty prognozy, modyfikując zakres danych (od którego roku liczyć prognozę) oraz używając różnych modeli prognostycznych.

### Co o współpracy z nami mówi sam wujek Czarek?

#### Opis Wspólnych Działań

**Mój Wkład w Tworzenie Narzędzia**

Jako asystent AI, moje główne zadania obejmowały:

- **Analiza i Poprawa Istniejącego Kodu:**
    - Przegląd kodu aplikacji napisanej w Pythonie z użyciem bibliotek takich jak Flask, pandas, matplotlib, statsmodels oraz yfinance.
    - Zamiana modelu ARIMA na model SARIMA.

- **Tworzenie i Modyfikacja Interfejsu Użytkownika:**
    - Dodanie elementów wizualnych takich jak tło z obrazem wykresów oraz estetyczne style CSS.
    - Dodanie tytułu strony oraz odpowiednich etykiet i instrukcji dla użytkownika.

- **Dodanie Dodatkowych Funkcjonalności:**
    - Implementacja przycisku "Opis funkcjonalności", który przekierowuje użytkownika na nową stronę zawierającą szczegółowy opis narzędzia.
    - Dodanie pogrubionej informacji "To nie jest porada inwestycyjna".

- **Optymalizacja i Ulepszanie Kodowania:**
    - Upewnienie się, że kod jest czytelny, dobrze zorganizowany i łatwy do zrozumienia.
    - Używanie odpowiednich bibliotek i funkcji do realizacji zadań.

#### Ocena Współpracy

**Ocena Twoich zapytań:**

Twoje zapytania były jasne, precyzyjne i dobrze sformułowane. Każde zapytanie miało konkretny cel i prowadziło do kolejnych etapów tworzenia aplikacji. Przedstawione wymagania były logiczne i spójne, co znacznie ułatwiło proces implementacji. Byłeś otwarty na sugestie i gotowy do wprowadzania zmian, co przyczyniło się do sprawnej realizacji projektu.

**Ocena Współpracy:**

Współpraca była bardzo efektywna i satysfakcjonująca. Twoje pytania i sugestie były przemyślane i konstruktywne. Proces tworzenia aplikacji przebiegał płynnie, z odpowiednią komunikacją i zrozumieniem oczekiwań. Twoje zaangażowanie i wkład w projekt były widoczne, co przyczyniło się do sukcesu końcowego produktu.

### Podsumowanie

Wspólnie stworzyliśmy funkcjonalne i estetyczne narzędzie do prognozowania cen akcji, które jest intuicyjne w obsłudze i dostarcza wartościowych informacji. Nasza współpraca była owocna, a Twoje zapytania były kluczowe dla osiągnięcia końcowego rezultatu. Razem udało nam się stworzyć aplikację, która spełnia wszystkie założone cele i jest gotowa do prezentacji jako projekt zaliczeniowy.

Życzymy udanej zabawy!

[Link do filmu prezentującego działanie aplikacji](https://youtu.be/ADrNvJgFTFw)
