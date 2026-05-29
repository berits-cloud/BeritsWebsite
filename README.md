# Berits Webdesign — Django-Website

Eine ruhige, elegante Website im Stil von jessiandmarkus.com — gebaut mit Django 4.2.

## Setup

```bash
# (einmalig) Migrationen anwenden
python3 manage.py migrate

# Entwicklungsserver starten
python3 manage.py runserver
```

Anschließend: http://127.0.0.1:8000/

## Struktur

```
berits_webdesign/          # Django-Projekt (Settings, URLs)
core/                      # App mit Views, Forms, Templates
  templates/core/          # Alle HTML-Templates
  static/core/css/         # styles.css mit der Farbpalette
```

## Farbpalette

| Farbe       | Hex      | Verwendung                   |
|-------------|----------|------------------------------|
| Burgundy    | #3e0d17  | Akzente, Überschriften       |
| Forest      | #4e584c  | Text, dunkle Flächen         |
| Sage        | #7a8775  | Mid-Tone, Kicker             |
| Mist        | #b7c1b2  | Helle Flächen, Tiles         |
| Cream       | #faf9f6  | Body-Hintergrund             |
| Sand        | #cec7b5  | Warmer Beige-Akzent          |

## Seiten

- `/` Startseite
- `/leistungen/` Leistungen & Prozess
- `/portfolio/` Projekte
- `/ueber-mich/` Über mich
- `/kontakt/` Kontaktformular (mit Honeypot)
- `/impressum/`, `/datenschutz/` Platzhalter — bitte ergänzen

## Was noch zu tun ist

- Bilder & echte Projekt-Screenshots ins Portfolio einbauen
- Impressum & Datenschutz mit echten Angaben füllen
- Für Produktion: `DEBUG = False`, eigener `SECRET_KEY`, echtes `EMAIL_BACKEND` (z. B. SMTP)
