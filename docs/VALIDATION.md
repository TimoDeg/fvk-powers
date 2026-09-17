# Prüfstand — 17.09.2026

Das Paket hat wiederholbare Strukturprüfungen und eine erste separate Modellbewertung. Menschliche PM-Verständlichkeit und ein neuer PM-Zugang sind noch nicht bewertet. Grüne Paketchecks und synthetische Antworten sind keine Teamfreigabe.

## Ausgeführt

| Prüfung | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Regressionen des Paketprüfers | 12/12 bestanden, lokal mit Python 3.14.4 | Prüft den Checker gegen gültige und absichtlich fehlerhafte Pakete |
| Paketprüfung | 5/5 Prüfgruppen lokal bestanden | Einstiegsdateien, private Dateipfade, lokale Markdown-Dateilinks, portable Dokumentation, Eval-Datenstruktur |
| Isolierter Clone | Paketchecker und 12 Tests bestanden, Aufruf aus fremdem Arbeitsverzeichnis funktioniert | Keine persönlichen Dateien oder Produktquellen erforderlich; kein frischer PM-Chat |
| GitHub Actions | [Erster Lauf bestanden](https://github.com/TimoDeg/fvk-powers/actions/runs/35212239595): 12 Tests und 5 Prüfgruppen, Ubuntu / Python 3.12.3 | Geprüfter Commit `0886026`; ausschließlich Paketchecks, keine Jira-Zugänge oder Modellantworten |
| Kontextpfade im lokalen Produktrepo | 17/17 vorhanden; beide Spec-Einstiege lesbar | Keine vollständige Code-/Dokumentabdeckung und kein Beleg der jüngsten Remote-Version |
| Jira-Lesezugriff | 7 unterschiedliche Tickets in ausgewerteten Durchläufen erfolgreich gelesen; reine Kandidatensichtung nicht mitgezählt | Nur der aktuelle Maintainer-Zugang, nicht der Zugang eines anderen PMs |
| Begrenzter Ticket-Spec-Abgleich | 7 durchgeführt, mit sichtbaren Quellenlücken und einem Konflikt zwischen Bewertungstabellen | Durch den verantwortlichen Agenten geprüft, keine unabhängige PM-Abnahme |
| Frisches PM-Setup | 0 vollständig beobachtet | Noch offen |
| Tatsächlicher Setup-Test in frischem Agentkontext | 2 Durchläufe vor/nach Eingrenzung der Jira-Felder; Jira, Original-Spec und lokale Speicherung jeweils erfolgreich | Derselbe Einstieg in zwei neuen Clones mit vorhandenen Host-Zugangsdaten; kein neuer menschlicher PM-Account |
| Modell-Evaluation auf dem Entwicklungsset | 12/12 Erstantworten separat modellbewertet und akzeptiert | Frische Agentkontexte, eingefrorene Quellen; keine menschliche PM-Abnahme |
| Wiederholung kritischer Fälle | 4/4 Fälle jeweils 3/3 akzeptiert; insgesamt 8 weitere Antworten | Kein unbekanntes Testset, keine allgemeine Zuverlässigkeitsquote |

Vollständige Antworten, Bewertungen und geprüfter Regelstand: [Modelltest vom 17.09.2026](../evals/results/2026-09-17-v1.md). Die Testagenten sahen keine Bewertungskriterien. Zwei kleine Hinweise bleiben: die Quellenbezeichnung beim Spec-Status und eine zu indirekte Erklärung der bereits möglichen Spec-Arbeit ohne Jira.

Der tatsächliche Setup-Test zeigte einen unnötig breiten Jira-Abruf (`*all`). Anschließend wurde die gemeinsame Regel auf gezielte Anfangsfelder und bedarfsgerechtes Nachladen begrenzt. Die 20 synthetischen Antworten gehören ausdrücklich zum vorherigen Regelstand. Die Änderung wurde in einem zweiten frischen Agentkontext mit tatsächlichem Quellenzugriff geprüft.

## Nachschärfung der Antwort- und Rechercheregeln

Nach den oben genannten Modell- und Setup-Läufen wurden vier Punkte präzisiert: kurze Ticketüberblicke mit zunächst drei priorisierten Abnahmefällen, konkrete Entscheidungen bei unklarem Umfang, kein breiter Jira-Folgeabruf als Ersatz für fehlende Feldmetadaten und eine klare Trennung zwischen Spec-Hinweis und bestätigter Fehlerursache. Entscheidende Bedingungen bleiben auch in kurzen Antworten erhalten; vollständige Abnahmeaufträge bleiben vollständig.

Ein frischer Testagent hat anschließend einen synthetischen Ticketüberblick und eine simulierte Entscheidung bei fehlendem Jira-Feldzugriff bearbeitet. Die Sichtprüfung durch den verantwortlichen Agenten bestätigte drei priorisierte Abnahmefälle, die offene Umfangsentscheidung, eine ausdrücklich ungeklärte Ursache und den Verzicht auf den breiten Folgeabruf. Das ist eine begrenzte Modellprobe ohne tatsächliche Jira-Aufrufe und ohne unabhängige PM-Bewertung; sie wird nicht zu den früheren Erfolgsquoten addiert.

Ein erneuter tatsächlicher Ticketdurchlauf unter Commit `480cb04` nutzte zwei gezielte Ticketabrufe und einen Feldmetadatenabruf ohne wiederholte Beschreibung oder breiten Fallback. Die PM-Ausgabe verfehlte das Kürzungsziel: ungefähr 434 statt 307 Wort-Einheiten, mit sieben Prüfsituationen in drei nummerierten Punkten. Die Quellenbasis war erweitert und die Kontexte unterschiedlich; das ist kein kontrollierter A/B-Vergleich. Private Antworten und Werkzeugbelege bleiben lokal.

Daraufhin wurde ausschließlich das PM-Ausgabeprofil weiter präzisiert: Standardantworten meist 100–160, höchstens 180 Wörter ohne Linkziele; maximal drei tatsächliche Prüfsituationen statt bloß drei Überschriften. Weitere Details bleiben im Arbeitskontext, sofern sie die Antwort nicht entscheidend verändern. Ausdrücklich vollständige Aufträge bleiben vollständig. Zwei zusätzliche synthetische Regressionsfälle prüfen Kürze und diese Ausnahme. Die bisherigen Erfolgszahlen gehören weiterhin zu den jeweils dokumentierten älteren Regelständen.

## Gezielte Tests des gekürzten Ausgabeprofils

Zwei frische Testagenten prüften das neue Profil getrennt vom Quellenabruf. Eine Antwort auf Basis ausgewählter, unveränderter Werkzeugrückgaben des vorherigen echten Ticketdurchlaufs hatte **166 Wörter und drei konkrete Prüfsituationen**. Die Sichtprüfung durch den verantwortlichen Agenten bestätigte beide gemeldeten Symptome samt Zahlen, den Unterschied der Preisangaben in den Quellen, die ungeklärte Ursache, die Umfangsentscheidung und die Kennzeichnung nicht ausgeführter Prüfungen. Es erfolgte kein neuer Jira-Abruf und kein vollständiger erneuter Pipeline-Test; der Vergleich mit der älteren Antwort ist kein kontrolliertes A/B-Experiment.

Ein ausdrücklich vollständiger synthetischer Abnahmeauftrag erhielt **alle sieben geforderten Fälle in 212 Wörtern**, einschließlich unverändertem gespeichertem Stand bei Speicherfehlern. Damit griff im Test die Ausnahme von Wort- und Falllimit. Wortzählung: durch Leerraum getrennte Einheiten, Markdown-Links auf Labels reduziert. Die Ausgaben wurden unverändert lokal aufbewahrt. Diese zwei Modellproben sind keine menschliche PM-Abnahme und keine neue Bewertung der 20 Baseline-Antworten. Der zusätzlich vorbereitete Fall `compact-overview` wurde noch nicht separat ausgeführt; für die Kürzeprobe diente das gespeicherte echte Quellenmaterial.

## Drei neue echte Ticketfragen unter `6e74a65`

Drei bisher in dieser Testreihe nicht verwendete Tickets wurden vor den Antwortläufen anhand von Thema und Original-Spec-Verweisen ausgewählt. Je ein frischer Agent bearbeitete Erklärung, Spec-Abgleich und Abnahme mit tatsächlichem Jira-Lesezugriff und lokalen Original-Specs. Ein vierter Agent bewertete die unveränderten Antworten separat anhand vorab festgelegter Kriterien und Quellen. Hostmodell: `gpt-6-astra`, Einstellung `high`. Kein Gesprächswissen aus den früheren Testläufen; vorhandene Host-Zugänge und Workspace-Regeln blieben verfügbar. Keine Zufallsstichprobe und keine allgemeine Erfolgswahrscheinlichkeit.

| Falltyp | Wörter ohne Linkziele | Modellurteil | Befund |
| --- | ---: | --- | --- |
| Einfache Erklärung | 164 | Akzeptiert | Entscheidende Regeln und Quellenlücken erhalten; keine behauptete Live-Prüfung |
| Spec-Abgleich | 164 | Akzeptiert | Konkrete Unterschiede fachlich belegt; zwei Zeilenverweise könnten präziser sein |
| Abnahme | 151 | Nicht akzeptiert | Genau drei Situationen, aber eine nötige Ausgangsbedingung für ein erwartetes Ergebnis fehlt |

**2/3 akzeptiert, 3/3 unter dem Längenlimit.** Alle 27 Einzelkriterien und unveränderten Antworten bleiben lokal protokolliert. Das Ergebnis wurde nicht durch Nachbessern oder die Auswahl eines besseren Wiederholungsversuchs ersetzt. Wortzählung wie bei den Formatter-Proben: Leerraumtrennung nach Reduktion von Markdown-Links auf Labels. Die fehlende Ausgangsbedingung ist ein fachlicher Mangel trotz korrekter Länge. Die Ausgabeanweisungen wurden während dieser Messung nicht verändert.

Jeder Antwortlauf nutzte zwei gezielte Ticketabrufe, einen Feldmetadatenabruf und eine Atlassian-Werkzeug-Discovery. Kein wiederholtes Beschreibungsfeld, kein `*all` und kein breiter `evidence`-Fallback. Beim umfangreicheren Spec-Abgleich gab es fünf Kürzungshinweise in Ausführungsrückgaben; die entscheidenden Passagen wurden danach gezielt gelesen. Lokale Such- und Ausgabeökonomie bleibt verbesserbar.

Der Produktcheckout änderte sich durch andere Arbeit während der Testphase. Die für die Bewertung relevanten sechs Spec-Dateien blieben nach Hash-Abgleich unverändert. Paketregeln ebenfalls unverändert; gespeicherte Antworten stimmen mit den finalen Agentenantworten überein. Keine Produkt-, Jira- oder sonstigen externen Mutationen durch die Testagenten, keine Anwendungstests. Private Ticketinhalte und Rohbelege wurden nicht in dieses Verteilungsrepo übernommen.

Der menschliche PM-Erststart wurde auf Nutzerwunsch zurückgestellt; diese Runde umfasst ausschließlich Agententests. Alle älteren Baseline-Zahlen bleiben getrennt und sind kein Nachweis für diesen Regelstand.

## Einrichtung praktisch geprüft

Der erste Durchlauf nutzte Baseline `348ab8fca2f4d2e55c50c5c2c9902d83329cdf42`. Der zweite nutzte denselben Stand mit der gezielten `AGENTS.md`-Änderung, SHA-256 `d270202c19db31e66617d76000b01ae29db6b60102b519ba58b176ed8ef57bd3`. Beide starteten ohne lokale Quellenkonfiguration. Repo-Pfad und Ticketlink waren in der Testanfrage ausdrücklich vorgegeben; ihre Ermittlung durch einen unerfahrenen PM wurde damit nicht getestet.

Im zweiten Lauf wurde der Ticketzugriff am 17.09.2026 um 09:53 UTC mit genau `summary`, `description`, `status`, `updated` durchgeführt. Für die gezielte Prüfung verfügbarer Feldmetadaten kam ein weiterer Abruf nur mit `issuetype` hinzu. Kein `*all`, kein wiederholter Abruf der Beschreibung. Die verfügbare Create-Feldmetadatenliste ist kein vollständiger Nachweis aller möglichen Jira-Feldkontexte.

Die passende Original-Spec wurde gelesen und abgeglichen; `.local/sources.md` wurde geschrieben, erneut gelesen und als von Git ausgeschlossen und nicht getrackt geprüft. Ergebnis jeweils: Zugriff, erster begrenzter Quellenabgleich und Speicherung funktionieren mit dem bestehenden Hostzugang. Die zweite PM-Antwort benennt auch einen ungeklärten fachlichen Grenzwert. Bildanhang, UI, Remote-Aktualität und menschliche Verständlichkeit sind weiterhin nicht geprüft. Private Protokolle bleiben lokal.

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
2. **Antwortqualität:** Die erzeugten Antworten von einem PM beurteilen lassen und neue unbekannte Fragen ergänzen. Die ersten 12 Entwicklungsfälle und acht Wiederholungen wurden bereits separat modellbewertet. Bekannte redaktionelle Beispiele nicht als neue Messergebnisse zählen.
3. **Echte Aufgaben:** Drei echte Ticketabgleiche von einem PM fachlich prüfen lassen. Die vorhandenen begrenzten Quellenchecks betreffen Tarifdetails, Tarifbewertung und Auszahlungen; sie ersetzen diese Abnahme nicht.
4. **Weitere Kontextzugänge:** Spec-Statusquelle und typische Anhänge erst anhand konkreter Fragen erproben. QMD/Graph-Werkzeuge nur ergänzen, wenn die direkte Suche an einer beobachteten Aufgabe nicht ausreicht.

Messdefinitionen und Freigabekriterien: [Eval-Plan](../evals/README.md). Neue Ergebnisse immer mit Datum, geprüftem Stand, Stichprobengröße und Bewertungsart ergänzen. Aus „noch nicht gemessen“ keine Prozentzahl berechnen.

## Umfang der übernommenen Pipeline

| Baustein | Stand in fvk-powers |
| --- | --- |
| Geführter PM-Einstieg, Quellenbindung, lokale Fortsetzung | In frischem Agentkontext mit echten Quellen und lokaler Speicherung geprüft; menschlicher PM-Erststart offen |
| Jira plus Original-Specs, Konflikte, Aktualität, Quellenbelege | Enthalten; sieben begrenzte Live-Quellenchecks durchgeführt |
| Fachliche Kontextwahl, Entscheidungen, Code-Einstiege, Release-Grenzen | Portable Landkarte in `CONTEXT.md`; aktuelle lokale Pfade geprüft |
| PM-Formatierung, Ideen, Abnahmeplanung | Profil, redaktionelle Beispiele und 20 separat modellbewertete Antworten enthalten; PM-Abnahme offen |
| Paketprüfungen und wiederholbare Regressionen | Lokaler Checker und GitHub-Workflow für Pushes und Pull Requests enthalten |
| Persönliche Wissenssammlung, private Läufe und alte Ticket-Historie | Keine Abhängigkeit und nicht kopiert; Originalquellen jeweils neu binden |
| QMD, CodeGraph, Graphify und Legacy-Harness | Nicht mitgeliefert; optionaler Suchweg beschrieben |
| Produktimplementierung, App-Tests, Deployment | Keine portierte Automation; expliziter Übergang zu den Regeln des Produktrepos |
