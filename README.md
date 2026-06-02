# Vendi ku dua të jetoj — New York City

Projekt **Gjuhe Shqipe** — **Harvard Zani**, Klasa IX, SHKA "26 Nëntori", Tiranë.  
30 faqe me temën *Vendi ku dua të jetoj* për **New York City**.

## Si ta hapni

1. Hapni dosjen `new-york-projekt`
2. Klikoni dy herë mbi `index.html` ose hapeni me shfletuesin (Chrome, Edge, Firefox)

Për navigim më të mirë, mund të nisni një server lokal:

```bash
cd new-york-projekt
py -3 -m http.server 8080
```

Pastaj shkoni te: http://localhost:8080

## Struktura

| Faqja | Skedari |
|-------|---------|
| 1 | index.html — Hyrja |
| 2–7 | Hyrje, historia, gjeografi, klima, popullsia |
| 8–12 | Manhattan, Brooklyn, Queens, Bronx, Staten Island |
| 13–19 | Transporti, metro, shkolla, universitete, karrierë, kosto, banesa |
| 20–28 | Kultura, muze, atraksione, sport, gastronomi, festivale |
| 29–30 | Siguria, konkluzioni |

## Personalizim

Në `index.html`, seksioni **Informacione për projektin** — vendosni emrin tuaj, klasën dhe shkollën.

Për të rigjeneruar faqet pas ndryshimeve në përmbajtje:

```bash
py -3 generate_pages.py
```
