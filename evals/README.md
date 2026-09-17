# Antwortqualität und Setup messen

Paketprüfungen, Quellenzugriff und Produktnutzen sind getrennte Messungen. Die [synthetischen Fälle](cases.json) definieren Aufgaben und Erwartungen; tatsächliche Durchläufe stehen separat in [Ergebnisse vom 17.09.2026](results/2026-09-17-v1.md). Die [Stilbeispiele](../examples/pm.md) sind redaktionell geschriebene Beispiele, keine Benchmark-Ausgaben.

## Vor dem Teamstart

1. **Paket prüfen:** Links, portable Einstiege, ausgeschlossene private Dateien und gültige Eval-Fälle. Die automatischen Tests prüfen auch absichtlich beschädigte Pakete. Das beweist keine Befolgung der Anweisungen durch ein Modell.
2. **Frisches Setup:** Ein PM öffnet nur dieses Repo in einem neuen Client-Kontext, ohne persönliche Skills oder alte Gesprächsinhalte. „Richte fvk-powers für mich ein.“ testen: beide Zugänge vorhanden, fehlendes Jira, fehlende Specs, fehlende Berechtigung, unterbrochenes Setup. Den tatsächlichen Chat und die ausgeführten Aktionen lokal erfassen.
3. **Synthetische Antworten:** Jeden Fall aus `cases.json` einzeln in einem neuen Kontext mit den Repo-Regeln ausführen. Dem antwortenden Modell nur `prompt` und `sources` geben; `must_include` und `must_not` erst beim Bewerten verwenden. Keine Musterantwort in den Antwortkontext laden. Das ist ein Entwicklungsset, kein unbekannter Holdout.
4. **Echte Fragen:** Mindestens drei freigegebene Rewrite-Tickets mit verschiedenen Themen prüfen: erklären, Spec-Abgleich, Abnahme/Ideen. Quellenstand festhalten; unabhängiger PM prüft die Antworten. Private Belege bleiben lokal, ins Repo kommen nur freigegebene aggregierte Ergebnisse.
5. **Wiederholung:** Vor einer Teamfreigabe die kritischen Fälle Konflikt, fehlende Quelle, Statusbehauptung und Anweisungen in Quellen jeweils dreimal frisch ausführen. Alle Versuche zählen, auch Fehlversuche. Neue, nicht zum Prompt-Tuning genutzte Fragen separat ergänzen.

## Was wir zählen

| Kennzahl | Definition | Fehlende Daten |
| --- | --- | --- |
| Erfolgreicher Erstversuch | Fälle, deren erste Antwort alle Muss-Kriterien erfüllt / tatsächlich erstmals ausgeführte Fälle | „Nicht gemessen“, niemals 0 % aus 0 Versuchen |
| Stabilität | Kritische Fälle mit drei erfolgreichen Versuchen / kritische Fälle mit drei ausgeführten Versuchen | Unvollständige Wiederholungen separat nennen |
| Quellenbelege | Geprüfte wesentliche Aussagen mit passendem Quellenbeleg / alle geprüften wesentlichen Aussagen | Zahl der Aussagen und Prüfer angeben |
| Fachliche Treue | Keine ausgelassene entscheidende Bedingung, falsche Zahl oder erfundene Umsetzung | Jeder solche Fehler lässt den Fall scheitern |
| Verständlichkeit | PM-Bewertung 1–5: 1 unverständlich, 3 Rückfragen nötig, 5 ohne Entwicklerwissen handlungsfähig | Nur mit tatsächlichen Bewertungen berichten |
| Setup-Erfolg | Frische Setups mit den benötigten geprüften Zugängen und erstem Quellenabgleich / gestartete Setups | Quellenmangel und Bedienproblem getrennt erklären |
| Aufwand | Zeit bis erster belegter Antwort, Zahl nötiger Nutzerrückfragen; Median erst bei mehreren Läufen | Einzelfallwerte als solche benennen |

Ein Lauf braucht lokal: Fall-ID, Zeit, Repo-Commit und lokale Abweichungen, Modell/Client, Quellenstand, sichtbare Antwort, Werkzeugbeleg bei Setup/Recherche, Versuchszähler, Bewertung pro Kriterium und Prüfer. Die Modellbewertung darf unterstützen; unabhängige fachliche und sprachliche Bewertung nicht durch Selbsteinschätzung ersetzen. Für Vergleiche identische Eingaben und Quellen verwenden.

## Freigabekriterium

Vor Pilotstart: Paketchecks grün, ein frisches PM-Setup samt erstem Ticket-Spec-Abgleich beobachtet und ein PM bestätigt Verständlichkeit. Vor breitem Teameinsatz: alle Entwicklungsfälle bewertet, keine offenen kritischen Fakten-/Quellen-/Zugriffsfehler, die genannten Wiederholungen erfolgreich und die drei echten Ticketfälle fachlich akzeptiert. Diese Schwellen sind vereinbarte Prüfziele, keine statistisch belegte allgemeine Zuverlässigkeit.

Der aktuelle [Prüfbericht](../docs/VALIDATION.md) nennt ausgeführte Checks und offene Nachweise. README-Zahlen dürfen nur daraus bzw. aus tatsächlichen Messbelegen stammen. Bei jeder Änderung an Anweisungen frühere Antwortbewertungen als ältere Baseline kennzeichnen; die CI prüft ausschließlich das Paket.
