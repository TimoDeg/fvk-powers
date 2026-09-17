# Prüfstand — 17.09.2026

Das Paket hat wiederholbare Strukturprüfungen. Die Antwortqualität und ein frisches PM-Onboarding sind noch nicht unabhängig gemessen. Grüne Paketchecks sind keine Teamfreigabe.

## Ausgeführt

| Prüfung | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Regressionen des Paketprüfers | 12/12 bestanden, lokal mit Python 3.14.4 | Prüft den Checker gegen gültige und absichtlich fehlerhafte Pakete |
| Paketprüfung | 5/5 Prüfgruppen lokal bestanden | Einstiegsdateien, private Dateipfade, lokale Markdown-Dateilinks, portable Dokumentation, Eval-Datenstruktur |
| Isolierter Clone | Paketchecker und 12 Tests bestanden, Aufruf aus fremdem Arbeitsverzeichnis funktioniert | Keine persönlichen Dateien oder Produktquellen erforderlich; kein frischer PM-Chat |
| GitHub Actions | Vorlage vorbereitet, Aktivierung blockiert | GitHub lehnt Workflow-Veröffentlichung mit dem aktuellen OAuth-Zugang ohne `workflow`-Berechtigung ab; kein CI-Erfolg behauptet |
| Kontextpfade im lokalen Produktrepo | 17/17 vorhanden; beide Spec-Einstiege lesbar | Keine vollständige Code-/Dokumentabdeckung und kein Beleg der jüngsten Remote-Version |
| Jira-Lesezugriff | 1 exaktes, aus einer Original-Spec verlinktes Ticket erfolgreich gelesen | Nur der aktuelle Maintainer-Zugang, nicht der Zugang eines anderen PMs |
| Begrenzter Ticket-Spec-Abgleich | 1 durchgeführt, mit sichtbaren Quellenlücken | Selbst durchgeführter Quellencheck, keine unabhängige Bewertung der Antwortqualität |
| Frisches PM-Setup | 0 vollständig beobachtet | Noch offen |
| Modell-Evaluation auf dem Entwicklungsset | 0/12 Fälle ausgeführt und unabhängig bewertet | Die 12 Fälle sind vorbereitet, nicht bestanden |

Der lokale Produktcheckout enthielt fremde Änderungen. Er wurde nur gelesen. Tickettext, Produktinhalte, interne URLs und persönliche Quellenpfade wurden nicht in diesen Bericht übernommen. Detaillierte Quellenbelege bleiben lokal.

Der Quellencheck zeigte, warum die Trennung nötig ist: Ein abgeschlossener Jira-Status und ältere Aussagen einer Spec zur Umsetzung dürfen nicht ungeprüft als derselbe Stand behandelt werden. Der Repo-Einstieg verweist für Spec-Status und Zuständigkeit auf eine separate Statusquelle; dieser Zugriff wurde nicht geprüft. Es wurden keine Kommentare, Anhänge, Anwendungstests, Deployments oder produktiven Abläufe vollständig validiert.

## Was die automatische Prüfung nicht abdeckt

- Befolgt ein frischer Assistent die Anweisungen tatsächlich?
- Findet er zu einer unbekannten Frage die richtige Spec und alle entscheidenden Ausnahmen?
- Bleiben längere Antworten fachlich korrekt und für PMs verständlich?
- Funktioniert die Anmeldung auf einem anderen Rechner und mit anderen Berechtigungen?
- Sind externe Links erreichbar? Der Offline-Checker prüft nur lokale inline Markdown-Dateilinks, keine Anker und keine Remote-Ziele.
- Sind alle Geheimnisse ausgeschlossen? Die Prüfung erkennt bestimmte private Pfade und Textmuster, keinen beliebigen sensiblen Inhalt. Vor Veröffentlichung weiterhin den Diff lesen.

## Reihenfolge der nächsten Nachweise

1. **Frischer PM-Start:** Ein echtes Setup im Zielclient ohne persönliche Skills und alten Chatkontext beobachten, einschließlich Anmeldung und Wiederaufnahme. Ziel: erster belegter Ticket-Spec-Abgleich; Aufwand und nötige Rückfragen erfassen.
2. **Antwortqualität:** Die 12 Entwicklungsfälle in getrennten Kontexten ausführen und pro Muss-Kriterium bewerten; ein PM beurteilt die Verständlichkeit. Bekannte redaktionelle Beispiele nicht als neue Messergebnisse zählen.
3. **Echte Aufgaben:** Drei fachlich verschiedene Tickets von einem PM prüfen lassen. Kritische Konflikt-/Quellenfälle dreimal wiederholen und anschließend neue unbekannte Fragen ergänzen.
4. **Weitere Kontextzugänge:** Spec-Statusquelle und typische Anhänge erst anhand konkreter Fragen erproben. QMD/Graph-Werkzeuge nur ergänzen, wenn die direkte Suche an einer beobachteten Aufgabe nicht ausreicht.

Messdefinitionen und Freigabekriterien: [Eval-Plan](../evals/README.md). Neue Ergebnisse immer mit Datum, geprüftem Stand, Stichprobengröße und Bewertungsart ergänzen. Aus „noch nicht gemessen“ keine Prozentzahl berechnen.

## Umfang der übernommenen Pipeline

| Baustein | Stand in fvk-powers |
| --- | --- |
| Geführter PM-Einstieg, Quellenbindung, lokale Fortsetzung | Als Chat-Anweisungen enthalten; frisches Setup offen |
| Jira plus Original-Specs, Konflikte, Aktualität, Quellenbelege | Enthalten; ein begrenzter Live-Quellencheck durchgeführt |
| Fachliche Kontextwahl, Entscheidungen, Code-Einstiege, Release-Grenzen | Portable Landkarte in `CONTEXT.md`; aktuelle lokale Pfade geprüft |
| PM-Formatierung, Ideen, Abnahmeplanung | Profil und Beispiele enthalten; unabhängige Qualitätsmessung offen |
| Paketprüfungen und wiederholbare Regressionen | Lokaler Checker und inaktive GitHub-Workflow-Vorlage enthalten; Workflow-Berechtigung fehlt |
| Persönliche Wissenssammlung, private Läufe und alte Ticket-Historie | Keine Abhängigkeit und nicht kopiert; Originalquellen jeweils neu binden |
| QMD, CodeGraph, Graphify und Legacy-Harness | Nicht mitgeliefert; optionaler Suchweg beschrieben |
| Produktimplementierung, App-Tests, Deployment | Keine portierte Automation; expliziter Übergang zu den Regeln des Produktrepos |
