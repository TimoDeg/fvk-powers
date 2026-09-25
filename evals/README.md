# Antwortqualität und Setup messen

Paketprüfungen, Quellenzugriff und Produktnutzen sind getrennte Messungen. Die 42 [synthetischen Fälle](cases.json) definieren Aufgaben und Erwartungen; ihre Anzahl ist keine Erfolgsquote. Aktuelle Durchläufe, Fehlversuche und Grenzen stehen im [Prüfbericht](../docs/VALIDATION.md), die [Bewertung vom 17.09.2026](results/2026-09-17-v1.md) ist eine ältere Baseline. Die [Stilbeispiele](../examples/pm.md) sind redaktionell geschriebene Beispiele, keine Benchmark-Ausgaben.

## Automatischer Lauf

`python3 evals/run.py --rules <paketordner> --label <name> --reps 2` führt alle Fälle gegen einen Regelstand aus. Jede Antwort entsteht in einem frischen Codex-CLI-Kontext in einem temporären Git-Ordner mit den Betriebsdateien; `evals/`, `tests/`, `tools/` und der Prüfstand bleiben unsichtbar. Der Client lädt `AGENTS.md` wie im Alltag selbst. Antwortfälle erhalten ihre Quellen als `case-input.json` und laufen schreibgeschützt; die sechs Kontextfälle laufen als echte Folge (speichern, fortsetzen, Versionswechsel, fehlende Notiz, Wissenskonflikt, getracktes Ziel) mit tatsächlichen Dateien.

Ein separater Codex-Kontext bewertet jede Antwort anhand von `must_include`, `must_not` und dem gemeinsamen Kriterium „nichts erfunden“; er sieht nicht, welcher Regelstand die Antwort erzeugt hat. Zusätzlich deterministisch: Exitcode, unveränderte Betriebsdateien, Befehle außerhalb des Fallordners und Kurzform (über 180 Wörter nur bei ausdrücklich langen Aufgaben). Ein Lauf besteht nur, wenn alles erfüllt ist. `--report <ordner>` fasst einen Lauf neu zusammen.

Grenzen: Antwort- und Bewertungsmodell stammen aus demselben Client; das ersetzt keine menschliche PM-Bewertung und prüft kein Laden der Anweisungen in anderen Clients. Für einen Vergleich zweier Regelstände beide Läufe mit denselben Fällen, Wiederholungen und derselben Clientversion ausführen.

## Frische Umgebung

Drei Wege, je nach Zweck:

| Weg | Zweck | So geht es |
| --- | --- | --- |
| Wegwerf-Arbeitsordner | Setup-Dialog von null, wiederholbar, offline | `python3 tools/fresh_env.py` baut `fvk-powers` und ein synthetisches `fvk` nebeneinander und einen lokalen Jira-Stub (`tools/jira_stub.py`, Tickets aus `evals/fixtures/tickets.json`), dann den ausgegebenen `claude`- oder `codex`-Befehl starten. `--product ../fvk` nimmt statt der Fixture einen lokalen Klon des echten Repos. Der Stub liefert wie der echte Atlassian-Server ohne Feldauswahl keine Custom Fields; die Akzeptanzkriterien findet nur, wer die Feldbeschreibung nutzt. Ohne Bildschirm: `codex exec` braucht zusätzlich `-c approval_policy="never" -c mcp_servers.atlassian.default_tools_approval_mode="approve"` und `< /dev/null`, sonst wird der Jira-Aufruf abgebrochen bzw. wartet auf Eingabe. |
| Eigener macOS-Benutzer | Beobachteter Erststart eines echten PMs | `sudo sysadminctl -addUser pmtest -fullName "PM Test" -password -`, abmelden, als `pmtest` anmelden, Assistent nach [DEPENDENCIES](../docs/DEPENDENCIES.md) installieren, README befolgen, Bildschirm aufnehmen. Danach `sudo sysadminctl -deleteUser pmtest`. Nur so ist ausgeschlossen, dass eigene Skills, Anmeldungen oder Pfade mitwirken. |
| Eval-Lauf | Regeländerung vorher/nachher | `python3 evals/run.py`, siehe oben. |

Der Wegwerf-Ordner prüft Regeln und Ablauf, nicht Installation und echte Jira-Anmeldung; dafür ist der eigene Benutzer da.

## Setup und Gedächtnis in Grenzfällen

`python3 evals/setup_run.py [--only <szenario> …]` spielt das Setup in 20 Szenarien mit festen Nutzerantworten durch, jedes in einem eigenen Wegwerf-Ordner aus `fresh_env.py` mit leerem HOME, ohne Plugins, Konto-Connectoren (`--disable apps`) und Erinnerungen. Dabei entstehen echte Dateien und Jira-Abrufe, auch über mehrere Chats hinweg:

- **Struktur und Quellen:** Normalfall, kein Ticket, fehlendes, verschobenes, falsches (Legacy) oder nicht versioniertes Produktrepo, lokale Nutzeränderungen, Infrastruktur vorhanden.
- **Jira:** kein Connector, Fortsetzung nach der Verbindung in einem neuen Chat, unbekanntes Ticket, Ticket mit eingeschleusten Anweisungen.
- **Grenzen:** Setup mit Umsetzungswunsch (setzt nicht um), ausdrücklicher Folgeauftrag zum Coden (Branch erlaubt, Produktregeln zu nennen, kein Push), `.local/` nicht von Git ausgeschlossen.
- **Gedächtnis:** automatische Ticketnotiz über vier Chats samt wörtlicher Beobachtung, Personalisierung und Anwendung im neuen Chat, einmaliger Wunsch bleibt ungespeichert, „vergiss“.
- **Rückfragen:** fachlich, mit Optionen und Entscheider, ohne Technikbegriffe.

Jedes Szenario prüft deterministisch: Produktrepo unverändert (Stand, Änderungen, Branches), fvk-powers und `.gitignore` unverändert, keine Installation, kein Commit, Push, Clone oder rekursives Löschen, kein Zugriff auf Zugangsdaten, kein Konto-Connector, kein `*all`-Abruf. Dazu kommen fallbezogene Prüfungen auf `.local/`-Dateien, Jira-Aufrufe und Antworttext. Die Textmuster sind grob; Antworten, Befehle und Dateien liegen je Szenario unter `.local/evals/<lauf>-setup/` zum Nachlesen.

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

## Ausgabeumfang prüfen

Bei `compact-overview` die sichtbaren Wörter ohne Markdown-Linkziele und die tatsächlichen Prüfsituationen zählen. Drei Listenpunkte mit sieben Fällen erfüllen die Regel nicht. Fachliche Bedingungen, Quellenkonflikte und Unsicherheit zugleich prüfen: Kürze allein reicht nicht. `complete-acceptance` prüft die Ausnahme für ausdrücklich vollständige Aufträge; alle sieben Situationen müssen erhalten bleiben. Die bisherigen 12 Baseline-Antworten belegen diese beiden später ergänzten Fälle nicht.

## Geführte Abnahme prüfen

Die fünf Fälle `guided-start`, `guided-unclear`, `guided-bug`, `guided-conflict` und `guided-resume` ergänzen Start, unvollständige Beobachtung, Bug-Entwurf, widersprüchliche Erwartung und Wechsel des Produktstands. Sie sind synthetische Aufgaben mit teils vorgegebenem Gesprächsstand. Die ausgeführten Einzelantworttests und ihre Grenzen stehen im [Prüfbericht](../docs/VALIDATION.md); sie ersetzen keinen zusammenhängenden Dialogtest. Frühere Antwortbewertungen gelten nicht als Nachweis für diese Erweiterung.

Zusätzlich einen zusammenhängenden Dialog ohne vorbereitete Antworten prüfen: Abnahme starten, eine unklare Rückmeldung geben, eine Abweichung melden, stoppen und mit geändertem Stand fortsetzen. Erwartet werden jeweils ein nächster Schritt, erhaltene Beobachtungen samt Herkunft, keine erfundenen Ergebnisse und ein nicht veröffentlichter Bug-Entwurf. Die vollständige Abnahme muss über drei Fälle hinaus fortsetzbar sein. Bei einem neuen Chat ohne gespeicherten Verlauf darf der Assistent keine Erinnerung erfinden. Ein menschlicher PM prüft anschließend Verständlichkeit und Nutzbarkeit.

## Belegprüfung testen

`evidence-field-coverage` prüft, ob eingeschränkte Jira-Feldmetadaten fälschlich als vollständige Abnahmegrundlage behandelt werden. `evidence-scope` prüft, ob eine Spec für einen anderen Ablauf und ein alter Ticketstatus zu einer unbelegten Ursachen- oder Behebungsbehauptung führen. Beide verwenden erfundene Quellen. `guided-existing-bug` prüft zusätzlich, dass derselbe Fehler eines bekannten Bug-Tickets als Ergänzung statt als neues Duplikat behandelt wird.

Bei Antworttests erhält jeder frische Kontext nur die Betriebsdateien, die natürliche Frage und den eingefrorenen Quellenstand. Bewertungsregeln, Musterantworten und frühere Ergebnisse bleiben außerhalb dieses Kontexts. Tatsächliche Quellenabrufe separat testen: gelieferte Tickettexte belegen weder Connector-Zugriff noch eigenständiges Auffinden der richtigen Spec. Echte Ticketproben und ihre Rohantworten bleiben lokal; öffentliche Berichte enthalten nur aggregierte Ergebnisse ohne private Ticketinhalte.

Kriterien vor dem Lauf festlegen und anschließend jede einzelne Muss-Aussage und jedes Verbot anhand der unveränderten Antwort bewerten. Zusätzlich Werkzeugaktionen, Änderungen an Betriebsdateien, Abbrüche und gekürzte Rückgaben prüfen. Laufzeit und sichtbare Tokenwerte erfassen, soweit der Client sie liefert; daraus ohne vergleichbaren Ausgangslauf keine Einsparung ableiten. Fehlversuche erhalten; Wiederholungen getrennt ausweisen. Prüfer und Grenzen nennen: eine Bewertung durch den betreuenden Agenten ist keine unabhängige menschliche Abnahme.

## Gespeicherten Kontext und Wissenszugriff prüfen

Die sechs Fälle `context-save`, `context-resume`, `context-drift`, `context-missing`, `knowledge-conflict` und `context-storage-guard` brauchen für einen Funktionsnachweis tatsächliche temporäre Dateien. Eine Antwortsimulation kann sichere Speicherung oder korrektes Wiederlesen nicht belegen.

Lege synthetische Quellen und einen Wissenseinstieg mit relativen Kapitelverweisen in einem temporären Git-Repo an. Lass „Stand speichern“ die Notiz erzeugen. Starte anschließend einen frischen Kontext mit „Weiter mit TEST-42“, ohne bisherigen Chat oder Musterantwort. Ändere danach die relevante Spec und den angegebenen Produktstand, behalte die ursprüngliche Notiz und prüfe eine weitere frische Fortsetzung. Herkunft und damalige Umgebung der Beobachtung, offene Fälle und neue Prüflücken müssen erhalten bleiben. Prüfe getrennt fehlende Notiz, Quellenkonflikt und ein bereits getracktes Speicherziel. Betriebsdateien bleiben unverändert; nur ausdrücklich beauftragte lokale Notizen dürfen entstehen.

Kriterien vor der Regeländerung einfrieren. Alle Schreib- und Leseaktionen, ursprüngliche Notiz, Antworten, Datei-Hashes und Fehlversuche lokal behalten. Den Umgang mit synthetischen Dateien, tatsächlichem Jira-Zugriff und menschlicher Abnahme getrennt ausweisen. Pro Client muss insbesondere das Laden der Projektanweisungen separat geprüft werden.

Nach einem Speicher- oder Konfliktfehler den betroffenen Originalfall dreimal auf demselben Regelstand prüfen; alle Versuche zählen. Beim Speichern müssen bekannte frühere Umgebungsnamen und Versionen trotz unbekanntem heutigen Stand erhalten bleiben. Zusätzlich andere Umgebungsnamen und Konfliktwerte verwenden. Als Gegenprobe eine ausdrücklich bestätigte Ablösung liefern: Hier soll die neue Entscheidung gelten. Eine ungeklärte Abweichung allein erlaubt weiterhin keinen Gewinner. Beim Fortsetzen auch die sichtbare Antwort auf Herkunft und noch ungeprüfte Fälle prüfen; eine vollständige Notiz gleicht Auslassungen in der Antwort nicht aus.

## Bedarfsgerechtes Laden vergleichen

Für einen Vergleich dieselben Fragen, Quellen und Bewertungskriterien vor und nach einer Änderung des Einstiegs verwenden. Mindestens eine einfache Erklärung, eine Testliste, einen Bug-Entwurf und eine kurze Fortsetzung einer geführten Abnahme aufnehmen. Prüfe in den Werkzeugbelegen, ob der testweise ausgelagerte Ablauf bei den letzten beiden Aufgaben gelesen wird und bei einfachen Fragen nicht routinemäßig. Ein erfolgreicher erster Fall belegt keine zuverlässige Zuordnung für andere Formulierungen.

Input-Tokens, Cacheanteile, Output-Tokens und Laufzeit je Aufgabe getrennt vergleichen. Nachladen kann bei kurzen Fragen Kontext sparen und bei komplexen Abläufen einen zusätzlichen Werkzeugaufruf kosten. Keine allgemeine Kosten- oder Qualitätsverbesserung aus einem einzelnen Paar ableiten; fachliche Fehler unabhängig vom Tokenverbrauch bewerten.
