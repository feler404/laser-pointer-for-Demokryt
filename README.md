# laser-pointer-for-Demokryt

Sterownik do wskaźników laserowych XY na bazie M5Stack i serwo-napędów

## Opis

Projekt ma na celu stworzenie sterownika do wskaźników laserowych XY, które będą wykorzystywane w ramach projektu Demokryt. Sterownik ma za zadanie zarządzać dwoma serwomechanizmami, odpowiedzialnymi za ruch wskaźnika w płaszczyźnie XY. Wykorzystuje on platformę M5Stack Core2 lub Core2 Basic z dodatkowym nakładanym modułem M5Stack Servo Kit.

Sterownik otwiera gniazdo (socket) na porcie 5000 (domyślnie) i nasłuchuje komend w formacie JSON. Komendy mogą być wysyłane z dowolnego urządzenia, które potrafi wysłać instrukcje w formacie JSON.

Przykładowa komenda:

```json
{"X_POINT": 90, "Y_POINT": 120}
```

Komunikację z serwerem można testować za pomocą narzędzi takich jak Postman, curl, itp.

## Wymagania

### Sprzęt
- M5Stack Core2 lub Core2 Basic
- Moduł M5Stack Servo Kit

### Oprogramowanie
- M5Stack IDE: https://flow.m5stack.com/
  - Przy programowaniu należy skonfigurować M5Stack Core2 tak, aby łączył się do sieci i wyświetlił API Key, który jest potrzebny do komunikacji ze zdalnym IDE.
- M5Burner (do aktualizacji firmware'u): https://docs.m5stack.com/en/uiflow/m5burner/intro
  - UI bazuje na pierwszej wersji, czyli M5flow.

## Konfiguracja i uruchomienie

1. W razie potrzeby zaktualizuj firmware M5Stack Core2 za pomocą M5Burner.
2. Otwórz M5Stack IDE i skonfiguruj urządzenie do połączenia z lokalną siecią.
3. Zanotuj API Key wyświetlony na ekranie M5Stack Core2 do komunikacji z zdalnym IDE.
4. Wgraj kod projektu na urządzenie M5Stack Core2.
5. Upewnij się, że serwomechanizmy są prawidłowo podłączone i zasilane.

## Użytkowanie

1. Włącz urządzenie M5Stack Core2.
2. Połącz się z tą samą siecią lokalną co urządzenie.
3. Wysyłaj komendy JSON na adres IP urządzenia na port 5000 (domyślny).

## Rozwiązywanie problemów

### Problemy z komunikacją UDP
- Sprawdź adres IP urządzenia (wyświetlony na ekranie M5Stack Core2) i upewnij się, że jest on dostępny w sieci lokalnej.
- Sprawdź, czy port 5000 jest otwarty na urządzeniu (zobacz konfigurację w pliku `init_config.py`).
- Upewnij się, że Twój host jest w tej samej sieci co urządzenie.
- Sprawdź, czy nie masz firewalla na swoim hoście, który blokuje komunikację z urządzeniem.
- Przejrzyj logi na ekranie LCD M5Stack Core2.

### Problemy z ruchem wskaźników
- Spróbuj poruszyć wskaźnikami za pomocą interfejsu użytkownika M5Stack Core2 i sprawdź, czy reagują na ruchy.
- Upewnij się, że serwomechanizmy są prawidłowo podłączone i zasilane.
- Sprawdź, czy nie wysyłasz współrzędnych poza zakresem serwomechanizmów (patrz konfiguracja w pliku `init_config.py`).
- Sprawdź logi na ekranie LCD M5Stack Core2.
