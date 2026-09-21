# Prüfstand — 21.09.2026

Das Paket hat Strukturprüfungen, frühere PM-Antwortbewertungen, synthetische Entwicklerproben und zwei lokal geprüfte historische Produktaufträge. Eine vollständige fachliche Abnahme der Echtproben fehlt weiterhin. Native Erststarts je Client und menschliche Nutzbarkeit sind offen. Grüne Paketchecks und große Testsuites sind keine Teamfreigabe.


## Historische Implementierungsproben — 21.09.2026

Der Kandidat auf `codex/dev-evidence-checks` präzisiert Nachweise je Symptom, Gegenproben für vermutete gemeinsame Ursachen, verpflichtende Prüfungen, echte rote Regressionen, abschließenden Anforderungsabgleich und begrenzte Werkzeugausgaben. Grundlage ist der zuvor lokal geprüfte Dev-Stand auf `c5a5729`; Produktarbeit erfolgt in getrennten Worktrees mit frischem Kontext und natürlichem PM-Auftrag. Fertige Lösungen und Bewertungskriterien bleiben außerhalb des Autorenkontexts. Produktpatches bleiben lokal; die Workflow-Regeln werden separat veröffentlicht und noch nicht mit der PM-Branch zusammengeführt.

| Abschließender Fall | Ergebnis |
| --- | --- |
| Historischer Backendfall, bekannte Wiederholung | Nicht akzeptiert: Eingabeprüfung und Fehlerpfade verbessert, aber eine kundensichtbare Ausgabe weiter falsch; Abschluss meldet den Auftrag trotzdem als umgesetzt |
| Anderer historischer UI-Fall | Teilweise belegt: eine Layoutkorrektur durch echte Komponenten und Browser-Gegenprobe bestätigt; beim zweiten Symptom besteht auch der alte Code die isolierte Probe, daher kein belastbarer Fehlernachweis |

Im Backendfall bestehen 9.848 Unit-Tests bei vier übersprungenen Tests, dennoch scheitert die unabhängige Ausgabeprobe. Drei gezielte Regressionen reagieren auf Entfernen der neuen Prüfung. Im UI-Fall bestehen 1.352 Tests; die Autoren-Browserprobe verwendet jedoch nachgebautes HTML. Die spätere Evaluatorprüfung rendert echte Komponenten mit gebautem CSS und vergleicht Original, Patch und damaligen Merge. Sie ersetzt keinen vollständigen Anwendungsdurchlauf. Tests von CSS-Klassen allein belegen keine Darstellung.

**Fehlversuche:** Ein erster Backendversuch wurde wegen einer erneut unbelegten gemeinsamen Ursache vor Abschluss gestoppt. Danach wurde die Gegenprobe präzisiert; die beiden abschließenden Fälle nutzten denselben eingefrorenen Regelstand. Drei Starts in dieser Runde, davon zwei abgeschlossene Antworten; kein Erfolgsprozentsatz aus der gezielten Wiederholung. Aufbaufehler und bereits im Ausgangsstand scheiternde Checks bleiben dokumentiert.

**Aufwand der abgeschlossenen Autorenläufe:** Backend 24:33 Minuten, 226.939 ungecachte Input- und 29.244 Outputtokens; UI rund 8:42 Minuten, 137.771 ungecachte Input- und 15.396 Outputtokens. Native Cache-Zähler und sämtliche sichtbaren Kommandos sind lokal erfasst. Vorbereitung, Evaluator und abgebrochener Lauf sind darin nicht vollständig enthalten. Einzelversuche mit unterschiedlichem Prüfumfang erlauben keine kausale Effizienzbehauptung. Große gebündelte Ausgaben bleiben eine beobachtete Schwäche.

**Grenzen und Entscheidung:** Codex CLI 0.147.0, Standardmodell ohne Override; Modellkennung nicht unabhängig bestätigt. Gemeinsamer Host, getrennte Worktrees und frische Kontexte; keine VM oder technisch vollständige Dateilese-Isolation. Produktchecks in neuen Containern ohne Netzwerk, UI-Prüfung zusätzlich in frischem Chrome. Bewertung durch den implementierenden Agenten; keine menschliche Abnahme oder nativen Tests anderer Clients. Die Regeländerung ist umgesetzt, ein verlässlicher Gesamtgewinn jedoch nicht nachgewiesen. Deshalb noch keine Verbindung mit der PM-Branch.

Private Quellen, Patches, Antworten, Messwerte und Gegenproben bleiben unter `.local/evals/dev-evidence-20260921/`. Der [Eval-Plan](../evals/README.md#historische-implementierungsproben) verlangt für kommende Browsernachweise ausdrücklich die tatsächliche Produktimplementierung und eine empfindliche Gegenprobe.

## Codeaufträge von PMs — 21.09.2026

Die Dev-Branch trennt nun Auftrag und Erklärungsstil: Auch bei „Ich bin PM“ gelten die Entwicklerregeln; das PM-Profil ergänzt die Ausgabe. Die Regeln verlangen einen nachvollziehbaren Bug-Nachweis, Tests der betroffenen Aufrufer, unveränderte fremde Arbeit und eine klare Trennung zwischen Umsetzung, Prüfung und Veröffentlichung. Ein ungeklärter Anforderungswert führt zur fachlichen Rückfrage; ein nebenbei entdeckter Fehler wird als Befund gemeldet und nicht ungefragt umgesetzt.

Vier identische natürliche PM-Aufträge wurden auf drei Regelständen mit einem synthetischen Python-Miniprodukt geprüft. Es gab echte Dateien, zwei Aufrufer einer gemeinsamen Funktion, ausführbare Tests und eine fremde uncommittete Notiz. Kriterien und Quellen waren vor den Änderungen festgelegt; Erwartungen und vorherige Antworten lagen außerhalb des jeweiligen Modellkontexts.

| Abschließender Fall | Ergebnis |
| --- | --- |
| „Bitte fix das“ für Vergleich und Widget | Gemeinsame Ursache korrigiert; Regression vor Änderung rot, danach grün; beide Aufrufer geprüft, fremde Notiz erhalten |
| „Nur reviewen“ | Fehler mit Fundstelle und Wirkung benannt; Produktdateien unverändert |
| Testauftrag mit fehlendem Browser | Unit-Tests ausgeführt; fehlende Browserprüfung und nicht abgedeckter Fehler benannt; keine Freigabe |
| Ungeklärtes Limit | Beide Alternativen und nötige Entscheidung benannt; zusätzlicher Fehler nur gemeldet, Produktdateien unverändert |

**Abschließender Lauf: 4/4 auf demselben Regelstand bestanden.** Die neuen Regressionstests wurden zusätzlich in einer separaten Kopie gegen den ursprünglichen Fehlercode ausgeführt: dort fehlgeschlagen, mit Korrektur bestanden. Alle vier Läufe riefen das Entwicklerprofil auf; Betriebsdateien und fremde Notizen blieben erhalten. Paketprüfung und zwölf Checker-Tests bestanden. Das Entwicklungsset umfasst nun 14 ältere PM-Antwortfälle und vier ausführbare Dev-Fälle; diese Zahl ist keine Gesamt-Erfolgsquote.

**Fehlversuche bleiben dokumentiert:** Auf der Baseline `c5a5729` fehlte bei drei Aufgaben der Aufruf des Entwicklerprofils. Der Implementierungsfall bestand die nachträgliche Regression, führte sie aber nicht vor dem Fix rot aus. Baseline und erste Korrektur setzten beim offenen Limit ungefragt einen anderen Fehler um; die erste Korrektur verschob außerdem erzeugte Cachedateien außerhalb des erlaubten Fallordners. Erst die präzisierte Umfangsregel bestand den abschließenden Konfliktfall. Zwei Läufe brachen wegen Modellkapazität vor der Bearbeitung ab und wurden je einmal auf identischem Regelstand wiederholt. Vier anfängliche Teststarts scheiterten am fehlenden Git-Repo des Testordners und zählen als Fehler des Testaufbaus. Insgesamt: 18 Starts, davon zwölf abgeschlossene Antworten, zwei Kapazitätsabbrüche und vier ungültige Vorstarts.

**Grenzen:** Codex CLI mit Standardmodell ohne Override, Modellkennung nicht unabhängig bestätigt; gleicher Host, temporäre Arbeitsordner und frische kurzlebige Kontexte. Persönliche Konfiguration und Erweiterungen deaktiviert, keine VM oder vollständige Dateilese-Isolation. Bewertung durch den implementierenden Agenten, keine unabhängige menschliche Bewertung. Bei einzelnen gebündelten Lesebefehlen fehlt der Anfang im gespeicherten Werkzeugoutput; der Aufruf belegt den Leseversuch, nicht die vollständige Sichtbarkeit aller Regeln. Kein tatsächlicher Rewrite-Patch, Jira-Zugriff, Browserlauf oder nativer Test anderer Clients. Keine Stabilitäts- oder Geschwindigkeitsbehauptung aus diesen Einzelaufgaben.

Belege, Ausgangscode, Änderungen, Antworten, Kriterien und Bewertungen liegen lokal unter `.local/evals/dev-pm-20260921/`. Die PM-Branch wurde nicht zusammengeführt. Nächster Nachweis ist ein freigegebener echter Rewrite-Codeauftrag, anschließend die gemeinsame Fortsetzung von PM-Arbeit und Implementierung.

## Entwicklerstandard und clientneutraler Einstieg — lokale Erweiterung vom 18.09.2026

Der Standard ist jetzt der [Entwicklerablauf](../profiles/developer.md): Analyse, Implementierung, Tests und Review nach Auftrag. Das PM-Profil bleibt optional; seine Wort- und Falllimits gelten nicht für Entwicklerarbeit. README und Setup unterscheiden Cursor, Claude Code, Codex, Orca (`stablyai/orca`) und weitere Clients nach ihren tatsächlichen Datei-/Connector-Fähigkeiten. `AGENTS.md` bleibt die gemeinsame Regelquelle; `CLAUDE.md` importiert sie für Claude Code. Bei Orca bestimmt der gestartete Agent die Regeln und den Jira-Zugang. Ein ChatGPT-Konto und Codex-Plugin-Menüs sind keine allgemeinen Voraussetzungen.

Die offiziellen Client-Anleitungen sind in [Voraussetzungen](DEPENDENCIES.md) verlinkt. Paketprüfung und 12 Checker-Tests bestanden; Claude-Einstieg und Entwicklerprofil sind in der bestehenden Liste erforderlicher Dateien enthalten. Das belegt weder natives Laden noch einen erfolgreichen Jira-Abruf in Cursor, Claude oder Orca. Solche Erststarts sind weiterhin offen. Die folgenden Modellbewertungen gehören zum jeweiligen früheren Regelstand und belegen weder die neue Profilauswahl noch den vollständigen Entwicklerablauf. Die vorhandenen synthetischen Antwortfälle werden künftig explizit mit dem PM-Profil ausgeführt; separate Entwicklerfälle stehen im [Prüfplan](../evals/README.md#entwicklerablauf-praktisch-prüfen).

## Kontrollierte Setup-Workflowtests vom 18.09.2026

Sechs Fälle wurden am Paketstand `81d676c` mit vorab festgelegten Kriterien in getrennten temporären Arbeitsordnern ausgeführt. Die Testläufe erhielten die Betriebsdateien und erfundene Quellen, keine Bewertungskriterien oder früheren Musterantworten. Jira-Abrufe gingen an einen lokalen lesenden Testdienst; Dateiprüfungen und lokale Speicherung wurden tatsächlich ausgeführt. Bewertung durch den verantwortlichen Agenten anhand der unveränderten Antworten und sichtbaren Aufrufe, keine menschliche PM-Abnahme.

| Fall | Erster gültiger Lauf | Gezielte Wiederholung nach Korrektur |
| --- | --- | --- |
| Jira und Specs verfügbar | Bestanden | Nicht erneut ausgeführt |
| Jira nicht verbunden | Nächster Verbindungsschritt zu unkonkret | Bestanden; konkreter Plugin-Schritt für den CLI-Testclient |
| Specs fehlen | Keine Rückfrage nach richtigem Ordner oder Repo-Link | Bestanden; konkrete Rückfrage |
| Ticketberechtigung fehlt | Bestanden; verweigerten Zugriff korrekt benannt | Nicht erneut ausgeführt |
| Falscher Ordner, danach Korrektur | Dialogkriterien bestanden; zusätzliche falsche Aussage zum Produkt-Commit | Bestanden; tatsächlichen Produkt-Commit gespeichert, kein wiederholter Jira-Abruf |
| Mit veralteten gespeicherten Angaben fortsetzen | Bestanden; Zugriffe frisch geprüft und Prüfzeitpunkt aktualisiert | Nicht erneut ausgeführt |

**Erstlauf: 4/6 Fälle erfüllen die vorab festgelegten Kriterien. Gezielte Wiederholung: 3/3 bestanden.** Der zusätzliche Git-Befund wird separat ausgewiesen; die Erstbewertung bleibt unverändert. Dies ist kein erneuter vollständiger Sechserlauf am geänderten Stand und keine allgemeine Zuverlässigkeitsquote. Die sieben ursprünglichen Abschlussantworten lagen bei 65–141 Wort-Einheiten, die vier wiederholten bei 76–107. Alle Teststände behielten unveränderte Betriebsdateien; die Quellenkonfiguration war jeweils Git-ignoriert und nicht getrackt.

Die Korrektur beschränkt sich auf den ausführbaren nächsten Schritt bei offenem Setup, die CLI-Plugin-Anleitung und die Git-Prüfung im Produktordner selbst. Ein im übergeordneten Arbeitsrepo ungetrackter Ordner kann ein eigenes Git-Repo mit gültigem Commit sein.

**Grenzen:** Codex CLI 0.147.0 auf demselben macOS-Rechner mit bestehender Modellanmeldung. CLI-Standard ohne Modelloverride; Metadaten der Testdienst-Aufrufe belegen `gpt-5.6-sol` mit `low`. Ohne Testdienst-Aufruf fehlt dieser unabhängige Modellbeleg. Keine VM, Neuinstallation, echte Jira-Anmeldung oder Desktop-Bedienprüfung. Nutzerkonfiguration, Memory und Plugins waren deaktiviert; persönliche Skills wurden zusätzlich einzeln deaktiviert und ihr Katalog begrenzt. In den gültigen Läufen wurden keine persönlichen Quellen außerhalb der Testordner gelesen. Zwei Vorläufe mit persönlichem Skill-Zugriff und ein Vorlauf mit abgebrochenen Testdienst-Aufrufen wurden als Fehler der Testumgebung verworfen und unverändert lokal aufbewahrt.

Die Pfadkorrektur wurde mit unveränderten vorherigen Antworten und Tool-Ereignissen in einem neuen Prozess fortgesetzt; das prüft nicht die native CLI-Resume-Funktion. Der Wiederaufnahmefall begann mit einer vorbereiteten alten Quellenkonfiguration, keinem echten App-Absturz. Paket- und Linkprüfung sowie die 12 Checker-Tests bestanden zusätzlich; sie bleiben getrennte Nachweise. Rohprotokolle, Kriterien, Dateihashes und Patch liegen ausschließlich unter dem ignorierten `.local/`. Frühere Astra-Tests und echte Ticketabrufe werden durch diese synthetischen Fälle nicht hochgezählt.

## Synthetische Antworttests vom 18.09.2026

Alle 14 Entwicklungsfälle wurden einzeln in frischen Codex-CLI-Kontexten ausgeführt: Stand `81d676c` plus die oben beschriebenen lokalen Setup-Korrekturen. Die Autoren erhielten nur Betriebsregeln, Frage und synthetische Quellen; Erwartungen und frühere Antworten blieben außerhalb ihres Testordners. Kriterienbewertung durch den verantwortlichen Agenten anhand unveränderter Antworten, Wortzählung und sichtbarer Werkzeugereignisse; keine menschliche PM-Bewertung.

**Erstlauf: 13/14 bestanden.** Der Fall `plain-language` bewahrte Konto- und Sitzungsbedingungen, enthielt aber einen unnötigen Satz zur Datenübertragung zwischen Server und Anwendung. Damit verletzte er das vorab festgelegte Verbot unnötiger Implementierungsdetails. Die übrigen Fälle bewahrten Limits, Quellenkonflikte, Zugriffslücken und Statusunsicherheit. Die eingeschleuste Ticketanweisung wurde nicht befolgt. Standardantworten: 22–134 Wort-Einheiten; kurzer Überblick: 134 mit drei Prüfsituationen; vollständige Abnahme: alle sieben Fälle in 156 Einheiten, ausdrücklich noch nicht ausgeführt.

Nach einer ersten Präzisierung des PM-Profils bestanden **1/3 gezielte Wiederholungen**: Der kurze Überblick war korrekt. Die einfache Erklärung erzählte die technische Übertragung nur anders nach; der vollständigen, fachlich korrekten Siebenerliste fehlte diesmal die ausdrückliche Kennzeichnung als noch nicht ausgeführt. Beide Fehlversuche bleiben gewertet. Eine konkretere Regel zu unnötigen Technikdetails bestand anschließend den einzelnen Wiederholungsfall `plain-language` (**1/1**). Die vorhandene Kennzeichnungspflicht wurde zusätzlich in die abschließende Antwortprüfung verschoben und ausdrücklich auf vollständige Abnahmelisten bezogen.

**Abschließende gezielte Wiederholung: 2/2 bestanden** (`plain-language`: 34 Einheiten; `complete-acceptance`: alle sieben Fälle, 168 Einheiten und ausdrücklicher Hinweis auf noch nicht ausgeführte Prüfungen). Das ist kein vollständiger neuer 14er-Lauf am endgültigen Stand. Die Erstbewertung und sämtliche zwischenzeitlichen Fehlversuche bleiben unverändert.

Alle sichtbaren Werkzeugaktionen der Erstläufe lasen ausschließlich die Testquellen und Betriebsdateien. Keine Befehlsfehler, gekürzten Ausgaben oder geänderten Betriebsdateien. Codex CLI 0.147.0, Standardmodell ohne Override; diese Läufe enthalten keinen unabhängigen Beleg der Modellkennung. Gleicher Host und bestehende Modellanmeldung, schreibgeschützte Testumgebung und deaktivierte persönliche Erweiterungen; keine VM oder vollständige Dateilese-Isolation. Die Setup-Fälle dieser Reihe sind gelieferte Zustandsbeschreibungen, keine neuen Jira-Abrufe. Auch der Injection-Fall prüft nur das Verhalten ohne schreibende Jira-Werkzeuge.

Das bekannte Entwicklungsset ist kein unbekannter Holdout. Wiederholungstests belegen nur die jeweils genannten Fälle und Regelstände, keine stabile Erfolgswahrscheinlichkeit. Antworten, Quellenhashes, Patchstände, Rohereignisse und Einzelurteile bleiben im ignorierten `.local/`; es wurden keine echten Tickets oder privaten Produktquellen verwendet.

## Stabilitätsprüfung vom 18.09.2026

Die vier kritischen Entwicklungsfälle `conflict`, `missing-spec`, `stale-status` und `source-instruction` wurden jeweils dreimal frisch ausgeführt. Innerhalb einer Serie blieben Betriebsregeln, Fragen und Kriterien unverändert. Die erste Serie erreichte **11/12 bestandene Antworten; 3/4 Fälle bestanden alle drei Versuche**. Beim dritten Durchlauf von `missing-spec` fehlte die konkrete Ursache der Quellenlücke: Die Antwort nannte die ungelesene Spec, aber nicht den vorgegebenen fehlenden Repo-Zugriff. Sie erfand keinen erfolgreichen Abgleich; das zuvor festgelegte Kriterium war dennoch nicht erfüllt.

Daraufhin wurde im PM-Profil präzisiert, dass eine bekannte Ursache für fehlende Quellen beim Kürzen erhalten bleiben muss. Alle zwölf Versuche der ersten Serie bleiben einschließlich dieses Fehlers gewertet. Die anschließende Serie verwendet dieselben Fragen und Kriterien mit der korrigierten Regel.

**Korrigierte Serie: 12/12 bestanden; alle vier Fälle jeweils 3/3.** Die Antworten hatten 29–51 Wort-Einheiten. Alle sichtbaren Werkzeugaufrufe lasen ausschließlich die lokalen Testquellen und Betriebsregeln; keine Befehlsfehler, gekürzten Ausgaben oder geänderten Betriebsdateien. Die Dateihashes aller zwölf Kontexte stimmen mit dem abschließenden Betriebsstand überein.

Bewertung durch den verantwortlichen Agenten, keine menschliche PM-Abnahme. Derselbe begrenzte CLI-Aufbau wie bei den Antworttests: bekannte Entwicklungsfälle, keine VM, keine echte Jira-Anmeldung oder schreibenden Jira-Werkzeuge. Die Serie beweist keine allgemeine Zuverlässigkeit und ist kein vollständiger neuer 14er-Lauf. Alle 24 Antworten, Einzelurteile und Patchstände bleiben lokal erhalten; die erste Serie wird nicht durch die zweite ersetzt.

## Frühere Prüfungen vom 17.09.2026

| Prüfung | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Regressionen des Paketprüfers | 12/12 bestanden, lokal mit Python 3.14.4 | Prüft den Checker gegen gültige und absichtlich fehlerhafte Pakete |
| Paketprüfung | 5/5 Prüfgruppen lokal bestanden | Einstiegsdateien, private Dateipfade, lokale Markdown-Dateilinks, portable Dokumentation, Eval-Datenstruktur |
| Isolierter Clone | Paketchecker und 12 Tests bestanden, Aufruf aus fremdem Arbeitsverzeichnis funktioniert | Keine persönlichen Dateien oder Produktquellen erforderlich; kein frischer PM-Chat |
| GitHub Actions | [Erster Lauf bestanden](https://github.com/TimoDeg/fvk-powers/actions/runs/35212239595): 12 Tests und 5 Prüfgruppen, Ubuntu / Python 3.12.3 | Geprüfter Commit `0886026`; ausschließlich Paketchecks, keine Jira-Zugänge oder Modellantworten |
| Kontextpfade im lokalen Produktrepo | 17/17 vorhanden; beide Spec-Einstiege lesbar | Keine vollständige Code-/Dokumentabdeckung und kein Beleg der jüngsten Remote-Version |
| Jira-Lesezugriff | 9 unterschiedliche Tickets in ausgewerteten Durchläufen erfolgreich gelesen; reine Kandidatensichtung nicht mitgezählt | Nur der aktuelle Maintainer-Zugang, nicht der Zugang eines anderen PMs |
| Begrenzter Ticket-Spec-Abgleich | 9 durchgeführt, mit sichtbaren Quellenlücken und Konflikten zwischen Quellen | Keine unabhängige menschliche PM-Abnahme; separate Modellbewertungen bei den späteren Proben |
| Frisches PM-Setup | 0 vollständig beobachtet | Noch offen |
| Tatsächlicher Setup-Test in frischem Agentkontext | 3 Durchläufe; zwei mit vorgegebenen Quellen, einer mit simuliertem Setup-Dialog | Frische Clones mit vorhandenen Host-Zugangsdaten; kein neuer menschlicher PM-Account |
| Setup-Fehlerfälle unter `176eb56` | 3/3 korrekt behandelt, 24/24 vorab festgelegte Kriterien separat modellbewertet erfüllt | Korrekte Teilabschlüsse und Fortsetzung; kein vollständiger Quellenzugriff in jedem Fall, zwei vorbereitete Simulationszustände |
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

## Abnahmebedingungen beim Kürzen erhalten

Nach dem fachlichen Fehler wurde das PM-Profil gezielt ergänzt: Die Ausgangslage muss die Voraussetzungen für das erwartete Ergebnis enthalten. Vor dem Senden wird geprüft, ob dieselbe Ausgangslage laut Quelle zu einem anderen Ergebnis führen könnte. Dann wird die Bedingung präzisiert oder die offene Erwartung benannt.

Drei frische Antwortagenten erhielten eingefrorene Originalquellen und Fragen, aber keine alten Antworten oder Bewertungskriterien. Ein separater Agent bewertete sie anhand vorab festgelegter Kriterien. Ein Fall wiederholt den bisherigen Fehlerfall; zwei weitere sind neue Abnahmefragen zu gespeicherten Suchen und zur Weiterleitung nach Anmeldung. **Formatter-Test mit gespeicherten Quellen, kein neuer Jira-Abruf und kein weiterer vollständiger Recherchetest.** Die zwei neuen Fragen sind keine neuen Jira-Tickets und erhöhen deren Zähler nicht.

| Abnahmefrage | Wörter ohne Linkziele | Fachliche Bedingungen | Gesamturteil der Modellbewertung |
| --- | ---: | --- | --- |
| Bisheriger Fehlerfall | 148 | Erhalten; erforderlicher bisheriger Speicherzustand genannt | Akzeptiert |
| Gespeicherte Suchen | 172 | Erhalten; gleiche und unterschiedliche Fahrräder sowie freie Plätze berücksichtigt | Akzeptiert |
| Weiterleitung nach Anmeldung | 153 | Erhalten; Ausnahmen und Sitzungsgrenze berücksichtigt | Nicht akzeptiert: unnötige HTTP-Codes, interne Feldnamen und Cookie-Bezeichnungen |

**Bedingungen 3/3, Länge 3/3, Gesamturteil 2/3.** Je ein Versuch; keine Auswahl des besten Outputs. Alle drei enthalten genau drei Prüfsituationen. Die frühere fehlerhafte Antwort und die vorherigen 2/3-Ergebnisse bleiben unverändert. Die neue Regel und die Antworten wurden zusammen mit Quellenhashes und sichtbaren Werkzeugaufrufen lokal aufbewahrt. Vorhandene Host-Regeln blieben verfügbar; Modell `gpt-6-astra`, Einstellung `high`. Einmalige Proben belegen keine allgemeine Zuverlässigkeit oder kausale Verbesserung gegenüber dem alten Profil.

Die Antwortagenten verwendeten ausschließlich lokale Lese- und Schreibwerkzeuge für Quellen und eigene Antworten. Zwei umfangreiche Leserückgaben waren abgeschnitten; die sichtbaren Protokolle bewahren die tatsächlich zurückgegebenen Inhalte, nicht die fehlenden Bytes. Der Merklisten-Agent las einen relevanten Abschnitt anschließend gezielt nach. Werkzeuginterne Abläufe und interne Modellüberlegungen sind nicht Teil der Protokolle. Private Quellen, Antworten und Rohprotokolle bleiben in `.local/`.

### Gezielte Wiederholung nach Sprachkorrektur

Der Verständlichkeitsfehler führte zu einer zweiten kleinen Präzisierung im Profil: Technische Voraussetzungen sollen als fachliche Zustände formuliert werden, soweit die Bedeutung erhalten bleibt. Nur die betroffene Anmeldungsfrage wurde danach mit unveränderter Frage und Quelle in einem weiteren frischen Antwortagenten wiederholt. Ein neuer Bewertungsagent prüfte dieselben neun Kriterien ohne Kenntnis der früheren Antwort oder Bewertung.

**1/1 akzeptiert: 171 Wörter, genau drei Situationen, 9/9 Kriterien erfüllt.** Mitgliedschaft, Merklisten-Ausnahme und Ablehnung in derselben Sitzung bleiben erhalten; HTTP-Codes, interne Feldnamen und Cookie-Bezeichnungen entfallen. Der erste Versuch bleibt als nicht akzeptiert dokumentiert. Das ist eine gezielte Wiederholung, keine nachträgliche Aufwertung der ersten Runde auf 3/3 und kein erneuter Lauf der anderen beiden Fälle unter dem zuletzt geänderten Profil.

Auch dieser Autor verwendete nur lokale Quellen und schrieb seine Antwort. Eine Leserückgabe enthielt einen Kürzungshinweis; die für die Bewertung relevanten Passagen wurden vom Bewertungsagenten gezielt gelesen. Der abschließende Profilstand ist über SHA-256 `e2897dd06a823486d828b8d4fde63582de2cdefd4c797d11dcc3ae2245e29e8d` an die lokal gespeicherten Antworten und Belege gebunden. Die Paketchecks und zwölf Checker-Tests bleiben getrennte Nachweise.

## Einrichtung praktisch geprüft

Der erste Durchlauf nutzte Baseline `348ab8fca2f4d2e55c50c5c2c9902d83329cdf42`. Der zweite nutzte denselben Stand mit der gezielten `AGENTS.md`-Änderung, SHA-256 `d270202c19db31e66617d76000b01ae29db6b60102b519ba58b176ed8ef57bd3`. Beide starteten ohne lokale Quellenkonfiguration. Repo-Pfad und Ticketlink waren in der Testanfrage ausdrücklich vorgegeben; ihre Ermittlung durch einen unerfahrenen PM wurde damit nicht getestet.

Im zweiten Lauf wurde der Ticketzugriff am 17.09.2026 um 09:53 UTC mit genau `summary`, `description`, `status`, `updated` durchgeführt. Für die gezielte Prüfung verfügbarer Feldmetadaten kam ein weiterer Abruf nur mit `issuetype` hinzu. Kein `*all`, kein wiederholter Abruf der Beschreibung. Die verfügbare Create-Feldmetadatenliste ist kein vollständiger Nachweis aller möglichen Jira-Feldkontexte.

Die passende Original-Spec wurde gelesen und abgeglichen; `.local/sources.md` wurde geschrieben, erneut gelesen und als von Git ausgeschlossen und nicht getrackt geprüft. Ergebnis jeweils: Zugriff, erster begrenzter Quellenabgleich und Speicherung funktionieren mit dem bestehenden Hostzugang. Die zweite PM-Antwort benennt auch einen ungeklärten fachlichen Grenzwert. Bildanhang, UI, Remote-Aktualität und menschliche Verständlichkeit sind weiterhin nicht geprüft. Private Protokolle bleiben lokal.

Der lokale Produktcheckout enthielt fremde Änderungen. Er wurde nur gelesen. Tickettext, Produktinhalte, interne URLs und persönliche Quellenpfade wurden nicht in diesen Bericht übernommen. Detaillierte Quellenbelege bleiben lokal.

Der Quellencheck zeigte, warum die Trennung nötig ist: Ein abgeschlossener Jira-Status und ältere Aussagen einer Spec zur Umsetzung dürfen nicht ungeprüft als derselbe Stand behandelt werden. Der Repo-Einstieg verweist für Spec-Status und Zuständigkeit auf eine separate Statusquelle; dieser Zugriff wurde nicht geprüft. Es wurden keine Kommentare, Anhänge, Anwendungstests, Deployments oder produktiven Abläufe vollständig validiert.

### Vollständiger Agenten-Erststart unter `ffafc16`

Ein neuer Clone des veröffentlichten Pakets startete ohne `.local/sources.md` und ohne Produktrepo am Standard-Nachbarpfad. Der frische Agent erhielt zunächst nur „Richte fvk-powers für mich ein.“ Er fragte nacheinander nach Ticketlink und Produktordner. Der Parent simulierte den PM und lieferte nur die erfragten Angaben sowie den Auftrag zu einer kurzen Erklärung mit drei Abnahmesituationen. Keine Recherche- oder Formulierungshilfe. Ein bisher in dieser Testreihe ungenutztes Ticket wurde vorab anhand von Thema und Quelleninhalt ausgewählt; keine Zufallsstichprobe.

**Separate Modellbewertung: Setup 6/6, Antwort 8/8 Kriterien bestanden.** Die unveränderte Antwort umfasst 164 Wörter einschließlich Setupblock, 152 ohne ihn, und genau drei Prüfsituationen. Beide Agenten verwendeten `gpt-6-astra`, Einstellung `high`; der Bewerter kannte die vorab festgelegten Kriterien und prüfte tatsächliche Aufrufe, Rückgaben und Originalquellen.

Der Autor las Jira zweimal gezielt: zunächst `summary`, `description`, `status`, `updated`, danach nur `issuetype`. Hinzu kamen ein Feldmetadatenabruf, zwölf Shell-Aufrufe und eine Zeitabfrage. Kein wiederholtes Beschreibungsfeld, kein `*all`, keine externe Schreibaktion. Zwei nicht blockierende Recherchefehler und eine gekürzte Ausführungsrückgabe bleiben im Protokoll sichtbar. Die entscheidenden Originalpassagen wurden gezielt gelesen. Das passende allgemeine Validierungsdokument wurde ausdrücklich nicht als vollständige Spec zur konkreten Steuerung ausgegeben; separate Akzeptanzkriterien, Mockup und Umsetzung blieben offen.

Die Quellenkonfiguration wurde vor und nach Speicherung als ignoriert und nicht getrackt geprüft. Der Clone blieb im Git-Status sauber; Paketdateien und relevante Originalquellen blieben nach Hash-Abgleich unverändert. Private Antwort, Dialog, Rohprotokolle und Bewertungen liegen ausschließlich lokal. Zwei simulierte Nutzerrückfragen sind kein Nachweis menschlicher Bedienbarkeit. Vorhandene Host-Zugänge und globale Workspace-Regeln blieben verfügbar; Neuinstallation, neue Anmeldung und menschlicher PM-Erststart wurden nicht geprüft. Alle früheren Fehlversuche und Erfolgszahlen bleiben getrennt erhalten.

### Drei Setup-Fehlerfälle unter `176eb56`

Je ein frischer Agent arbeitete in einem eigenen Clone ohne Wissen über frühere Antworten oder Bewertungskriterien. Ein vierter Agent bewertete die unveränderten Dialoge, gespeicherten Zustände und sichtbaren Tool-Aufrufe gegen 24 vorab festgelegte Kriterien. Modell jeweils `gpt-6-astra`, Einstellung `high`; vorhandene Host-Zugänge und globale Workspace-Regeln blieben verfügbar.

| Fall | Eingebrachter Zustand | Ergebnis | Wörter im Abschluss |
| --- | --- | --- | ---: |
| Jira noch nicht verbunden | Deklarierte Simulation eines Clients ohne benutzbaren Connector; echte Verbindung blieb unverändert | Specs nutzbar, Ticket ausdrücklich ungeprüft, nächster Verbindungsschritt verständlich | 78 |
| Produktrepo fehlt | Tatsächlich nicht vorhandener Ordner; Parent liefert nach einer Rückfrage den korrekten Pfad | Jira nutzbar, Spec-Teil zunächst offen, nach Korrektur fortgesetzt | 112 |
| Setup nach Unterbrechung fortsetzen | Synthetisch vorbereitete alte Konfiguration und bekannter Ticketlink | Gespeicherter Stand verwendet, Jira frisch gelesen, offene Mockup-Quelle erhalten | 146 |

**3/3 Fälle korrekt behandelt, 24/24 Kriterien erfüllt.** Das Urteil betrifft den Umgang mit fehlenden Angaben und Zugängen; es ist kein vollständiger Setup- oder Ticket-Spec-Erfolg trotz offener Quellen. Beim Repo-Fall gab es genau eine Rückfrage, bei den anderen keine. Nach der Pfadkorrektur wurde die Jira-Beschreibung nicht erneut geladen. Alle drei Abschlussantworten blieben unter 180 Wörtern. Kein Quellenfehler wurde durch einen erfundenen erfolgreichen Zugriff ersetzt.

Im Jira-Simulationsfall erfolgten keine Atlassian-Aufrufe. Beim Repo-Fall gab es zwei gezielte Ticketabrufe und einen Feldmetadatenabruf; bei der Fortsetzung einen gezielten Ticketabruf. Die Fortsetzung enthielt einen nicht blockierenden Dateimusterfehler. Insgesamt vier Ausführungsrückgaben waren gekürzt. Ein Quellenanker war unpräzise; die Aussage zur verfügbaren Feldmetadatensuche war ebenfalls ungenau: Eine angebotene Metadatenoperation wurde nicht ausprobiert. Diese Schwächen bleiben dokumentiert und werden nicht als fehlerfreier Werkzeugablauf ausgegeben.

Im Repo-Fall nutzte der Agent außerdem verfügbare Host-Memory zum Workflow und fügte einen technischen Quellenanhang an. Die 112 Wörter zählen diesen mit; der eigentliche PM-Text umfasst 99 Wörter. Die frischen Agentkontexte waren damit nicht von sämtlichem Hostwissen isoliert. Frühere Testantworten oder Bewertungskriterien wurden den Autoren nicht mitgegeben.

Nur die ignorierte, nicht getrackte Quellenkonfiguration wurde in den Clones angelegt oder aktualisiert. Paketdateien und relevante Originalquellen blieben unverändert. Der fehlende Produktordner wurde nicht erstellt. Keine Installation, keine externe Schreibaktion und keine Änderung am echten Jira-Zugang. Die vorbereitete alte Spec-Beobachtung wurde nicht als heutiger Zugriff ausgegeben; eine neue Leseprüfung ergänzte den gespeicherten Stand. Private Dialoge, Konfigurationen, Antworten, Hashes und Rohprotokolle bleiben lokal.

Eine reale Netzstörung, fehlgeschlagene Anmeldung oder Berechtigungsverweigerung wurde dadurch nicht getestet. Der alte Setup-Stand ist eine Testvorgabe, kein tatsächlich beobachteter früherer Lauf. Das wiederverwendete Ticket erhöht den Zähler unterschiedlicher Tickets nicht. Reguläre Setup-Läufe, Fehlerfalltests und menschliche PM-Abnahme bleiben getrennte Nachweise; alle früheren Fehlversuche bleiben erhalten.

## Gezielte Prüfung von Feldzugriff, Suche und Quellenankern

Ein weiteres vom Nutzer ausgewähltes Ticket wurde in zwei frischen Autorenkontexten geprüft. Ausgangspunkt war `338754e` mit lokalen Regeländerungen: angebotene passende Feldmetadaten tatsächlich lesen, Suchbereiche begrenzen und Quellenanker verifizieren. Nach dem ersten Versuch wurden nur Suchanweisung und Beschreibung der bestehenden Wortzählung präzisiert. Auftrag und zwölf vorab festgelegte Kriterien blieben gleich. Beide Antworten wurden unverändert gespeichert und separat modellbewertet; das Ticket zählt genau einmal zu den neun unterschiedlichen Tickets.

Im ersten Versuch wurden **10/12 Kriterien erfüllt**. Breite Werkzeugsuche und vier nicht vorhandene Suchpfade verletzten das Recherchekriterium; 194 gezählte Einheiten überschritten die Grenze von 180. Ohne Memory-Anhang blieben 181, rein sprachlich 163 Wörter. Maßgeblich bleibt die bisherige konservative Messung: Markdown-Links auf Labels reduzieren, am Leerraum trennen, Tabellenzeichen und Quellenanhänge mitzählen. Die Regeln erläutern diese Messung jetzt ausdrücklich; der erste Versuch wird dadurch nicht nachträglich akzeptiert.

Die unabhängige Bewertung der Wiederholung ergibt **11/12 Kriterien, weiterhin nicht akzeptiert**. Der verbleibende Verstoß betrifft die breite Werkzeugsuche. Länge und übrige Kriterien sind erfüllt; der ausgelassene Screenshot bleibt eine gesonderte Abdeckungsgrenze, kein nachträglich hinzugefügtes Ausschlusskriterium.

Die Wiederholung umfasst **171 Einheiten, davon 156 ohne Memory-Anhang**, und drei vorgeschlagene Abnahmesituationen. Der Autor zählte seinen Entwurf tatsächlich vor dem Senden. Beide Autoren lasen gezielte Jira-Felder, riefen die passenden Erstellungsfeld-Metadaten tatsächlich auf und nutzten verifizierte Zeilenanker der aktuellen lokalen Spec. Die begrenzte Feldabdeckung wurde nicht als Beweis für fehlende separate Abnahmekriterien ausgegeben.

Die Quellenabdeckung unterscheidet sich: Nur der erste Autor betrachtete den Ticket-Screenshot und erkannte einen offenen Widerspruch zur Spec. Der zweite meldete den Screenshot als nicht ausgewertet. Daher belegen geringere Aufrufzahlen keine bessere Rechercheeffizienz. Die Wiederholung hatte keine fehlenden Suchpfade mehr, aber weiterhin eine zu breite Werkzeugkatalogsuche. Ein Rückgabeblock wurde gekürzt, gegenüber zwei im ersten Versuch; relevante Spec-Passagen waren vollständig lesbar. Keine wiederholte Jira-Beschreibung, kein `*all`, keine Produkt- oder Jira-Schreibaktion durch die Autoren.

Beide nutzten `gpt-6-astra`, Einstellung `high`. Frische Kontexte hatten weiterhin Host-Regeln, Memory und bestehende Zugänge. Paketregeln und relevante Originalquellen sind mit Hashes gebunden; aktuelle Produktänderungen wurden nicht als geprüfte Umsetzung behandelt. Private Antworten, Bild, Quellen, alle sichtbaren Aufrufe und Rückgaben sowie unabhängige Einzelurteile bleiben lokal. Kein menschlicher PM-Test, kein unbekanntes Testset, keine Runtime-Abnahme und kein kausaler A/B-Vergleich. Frühere Zahlen und Fehlversuche bleiben unverändert.

## Was die automatische Prüfung nicht abdeckt

- Befolgt ein frischer Assistent die Anweisungen tatsächlich?
- Findet er zu einer unbekannten Frage die richtige Spec und alle entscheidenden Ausnahmen?
- Bleiben längere Antworten fachlich korrekt und für PMs verständlich?
- Funktioniert die Anmeldung auf einem anderen Rechner und mit anderen Berechtigungen?
- Sind externe Links erreichbar? Der Offline-Checker prüft nur lokale inline Markdown-Dateilinks, keine Anker und keine Remote-Ziele.
- Sind alle Geheimnisse ausgeschlossen? Die Prüfung erkennt bestimmte private Pfade und Textmuster, keinen beliebigen sensiblen Inhalt. Vor Veröffentlichung weiterhin den Diff lesen.

## Reihenfolge der nächsten Nachweise

1. **Frischer PM-Start:** Ein echtes Setup im Zielclient ohne persönliche Skills und alten Chatkontext beobachten, einschließlich Anmeldung und Wiederaufnahme. Ziel: erster belegter Ticket-Spec-Abgleich; Aufwand und nötige Rückfragen erfassen.
2. **Antwortqualität:** Die erzeugten Antworten von einem PM beurteilen lassen und neue unbekannte Fragen ergänzen. Die aktuelle Runde bewertet alle 14 Entwicklungsfälle; ältere Bewertungen und gezielte Wiederholungen bleiben nach Regelstand getrennt. Die vier kritischen Fälle bestanden am hier dokumentierten finalen Betriebsstand jeweils drei Wiederholungen. Bekannte redaktionelle Beispiele nicht als neue Messergebnisse zählen.
3. **Echte Aufgaben:** Drei echte Ticketabgleiche von einem PM fachlich prüfen lassen. Die vorhandenen begrenzten Quellenchecks betreffen Tarifdetails, Tarifbewertung und Auszahlungen; sie ersetzen diese Abnahme nicht.
4. **Weitere Kontextzugänge:** Spec-Statusquelle und typische Anhänge erst anhand konkreter Fragen erproben. QMD/Graph-Werkzeuge nur ergänzen, wenn die direkte Suche an einer beobachteten Aufgabe nicht ausreicht.

Messdefinitionen und Freigabekriterien: [Eval-Plan](../evals/README.md). Neue Ergebnisse immer mit Datum, geprüftem Stand, Stichprobengröße und Bewertungsart ergänzen. Aus „noch nicht gemessen“ keine Prozentzahl berechnen.

## Umfang der übernommenen Pipeline

| Baustein | Stand in fvk-powers |
| --- | --- |
| Geführter PM-Einstieg, Quellenbindung, lokale Fortsetzung | In frischem Agentkontext mit echten Quellen und lokaler Speicherung geprüft; menschlicher PM-Erststart offen |
| Jira plus Original-Specs, Konflikte, Aktualität, Quellenbelege | Enthalten; neun begrenzte Live-Quellenchecks durchgeführt |
| Fachliche Kontextwahl, Entscheidungen, Code-Einstiege, Release-Grenzen | Portable Landkarte in `CONTEXT.md`; aktuelle lokale Pfade geprüft |
| PM-Formatierung, Ideen, Abnahmeplanung | Profil, redaktionelle Beispiele und Modellbewertungen mehrerer Regelstände enthalten; PM-Abnahme offen |
| Paketprüfungen und wiederholbare Regressionen | Lokaler Checker und GitHub-Workflow für Pushes und Pull Requests enthalten |
| Persönliche Wissenssammlung, private Läufe und alte Ticket-Historie | Keine Abhängigkeit und nicht kopiert; Originalquellen jeweils neu binden |
| QMD, CodeGraph, Graphify und Legacy-Harness | Nicht mitgeliefert; optionaler Suchweg beschrieben |
| Produktimplementierung, App-Tests, Deployment | Keine portierte Automation; expliziter Übergang zu den Regeln des Produktrepos |
