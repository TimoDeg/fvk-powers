# Prüfstand — 21.09.2026

Das Paket hat wiederholbare Strukturprüfungen und eine erste separate Modellbewertung. Menschliche PM-Verständlichkeit und ein neuer PM-Zugang sind noch nicht bewertet. Grüne Paketchecks und synthetische Antworten sind keine Teamfreigabe.

## Kontextkorrektur — 21.09.2026: Merge-Bedingung erfüllt

Die beiden wiederkehrenden Fehler wurden an ihrer gemeinsamen Ursache korrigiert: Frühere Beobachtungen werden als kurzer wörtlicher Beleg statt als neu formulierte Zusammenfassung gespeichert. Der heutige unbekannte Stand bleibt davon getrennt. Die zentrale Konfliktregel verlangt einen tatsächlichen Klärungsbeleg; Dokumenttyp oder Datum wählen keinen Gewinner. Fortsetzungsantworten nennen die Herkunft der Beobachtung und noch ungeprüfte Fälle ausdrücklich.

| Prüfung am abschließenden Regelstand | Ergebnis |
| --- | --- |
| Sechs Kontextfälle: speichern, fortsetzen, Versionswechsel, fehlende Notiz, Wissenskonflikt, getracktes Ziel | 6/6 bestanden |
| Zwei zusätzliche Wiederholungen je ursprünglichem Speicher- und Konfliktfall | 4/4; einschließlich Gesamtlauf jeweils 3/3 |
| Varianten: andere Umgebung/Version, andere Konfliktwerte, bestätigte Ablösung als Gegenprobe | 3/3 bestanden |
| Echtes Ticket: erklären/speichern → neuer Kontext/fortsetzen | Beide Persistenzschritte bestanden |

Die abschließenden **15 CLI-Läufe** verwendeten dieselben Betriebsdateien, durch Hashes geprüft. Alle vier synthetischen Speicherbelege wurden zusätzlich wörtlich mit der Eingabe verglichen: Umgebung, Version, PM-Herkunft und Ergebnis blieben erhalten. Lesende Fortsetzungen und das getrackte Speicherziel blieben unverändert. Keine beobachteten Zugriffe außerhalb der Fallordner, externen Aktionen oder gekürzten Werkzeugausgaben. Ein nicht unterstützter `realpath`-Schalter wurde vor dem Schreiben korrigiert. Alle Prozesse endeten mit Exitcode 0. Paketprüfung, zwölf Checker-Tests und Whitespace-Prüfung bestanden.

**Der erste Korrekturversuch bleibt als Fehlschlag erhalten:** 5/6 Kontextfälle, 6/7 ergänzende Prüfungen und zwei bestandene reale Persistenzschritte. Beim Versionswechsel fehlten in der sichtbaren Antwort PM-Herkunft und ungeprüftes Neuladen; die Notiz selbst behielt beides. Beim einfachen Fortsetzen blieb die PM-Herkunft ebenfalls nur in der Notiz. Eine der drei Speicherwiederholungen verlor erneut die frühere Umgebung. Erst danach wurden der wörtliche Beleg und die Fortsetzungsform präzisiert. Insgesamt entstanden in dieser Korrekturrunde **30 Läufe**; Fehlversuche wurden weder entfernt noch durch erfolgreiche Wiederholungen umgewertet.

**Grenzen:** Codex CLI 0.147.0, Standardmodell ohne Override und ohne unabhängig bestätigte Modellkennung. Bewertung durch den verantwortlichen Agenten, kein menschliches Urteil und kein unbekanntes Testset. Temporäre Git-Arbeitsordner mit deaktivierter persönlicher Konfiguration und Erweiterungen, keine VM oder vollständige Dateilese-Isolation. Die echten Quellen sind datierte Kopien des zuvor am selben Tag gelesenen Tickets und der Specs; kein erneuter Live-Connector- oder Anwendungstest. Die Persistenzprüfung ist keine vollständige fachliche Freigabe: Der echte Kurzüberblick trennt benachbarte Journey-Vorgaben weiterhin nicht ausdrücklich vom Bot-Geltungsbereich. Native Prüfungen in Cursor, Claude und Orca sowie menschliche PM-Abnahme bleiben offen. Drei Wiederholungen belegen keine allgemeine Zuverlässigkeitsquote.

Rohantworten, gespeicherte Notizen, Kriterien, Hashes und Einzelbewertungen liegen unter `.local/evals/context-fix-20260921/`; der abschließende Lauf unter `verbatim/`. Private Quellen bleiben dort. README-Status und Prüfbericht wurden anschließend aktualisiert; die getesteten Arbeitsregeln blieben unverändert. Die nachfolgenden Berichte dokumentieren frühere Regelstände.

## Frühere Merge-Prüfung — 21.09.2026: noch nicht bestanden

Der vollständige Lauf aller sechs Kontextfälle wurde auf `30fba84` wiederholt. Zusätzlich wurde ein echtes Ticket frisch über den internen Jira-Connector gelesen und mit aktuellen Original-Specs für einen Test über zwei frische Kontexte bereitgestellt. Merge-Bedingung vorab: alle sechs Fälle auf einem unveränderten Regelstand sowie der echte Persistenzablauf bestehen. **In diesen früheren Läufen war die Bedingung nicht erfüllt; es erfolgte kein Merge nach `main`.**

| Prüfung | Erster Lauf | Nach gezielter Regelkorrektur |
| --- | --- | --- |
| Stand speichern | Bestanden | Nicht bestanden: bekannte frühere Testumgebung als unbekannt gespeichert |
| Im neuen Kontext fortsetzen | Nicht bestanden: frühere Abweichung und Konflikt in Antwort ausgelassen | Bestanden: Befund, offene Punkte und nächster Schritt erhalten |
| Geänderter Produktstand | Bestanden | Bestanden: alte Beobachtung und neue Prüfung getrennt; Notiz unverändert |
| Fehlende Ticketnotiz | Inhalt korrekt, aber Suche außerhalb des erlaubten Fallordners | Bestanden; weiterhin unnötig breite Suche innerhalb des erlaubten Ordners |
| Wissenskonflikt | Nicht bestanden: offenes Limit eigenmächtig entschieden | Weiterhin nicht bestanden |
| Bereits getracktes Speicherziel | Bestanden | Bestanden |
| Echtes Ticket: erklären/speichern → frischer Kontext/fortsetzen | Persistenzablauf in beiden Schritten bestanden | Persistenzablauf in beiden Schritten bestanden, vollständigere Fortsetzungsantwort |

Die synthetischen Gesamtläufe erreichten **3/6**, danach **4/6**. Ein bestandener Fortsetzungsfall repariert keine bereits falsch gespeicherte Information. Beim Versionswechsel blieb der weitere ungetestete Fall in der Notiz erhalten, wurde aber nicht erneut im Antworttext genannt; eine vollständige sichtbare Liste aller offenen Fälle ist damit nicht belegt. Die realen Läufe prüfen gezielt Erhalt und Wiederaufnahme von Kontext, keine vollständige fachliche Freigabe des Tickets. Im ersten realen Überblick wurde eine Journey-Vorgabe nicht ausdrücklich vom Bot-Geltungsbereich getrennt; diese Antwort bleibt entsprechend eingeschränkt.

Die Regelkorrektur strukturiert Fortsetzungsantworten in bisherigen Befund, offene Punkte und nächsten Schritt, begrenzt die Suche nach Gesprächsnotizen auf das Projekt und stellt ungeklärte Wissenskonflikte an den Antwortanfang. **Offen bleiben der Informationsverlust beim Speichern und die eigenmächtige Konfliktauflösung.** Weitere Wiederholungen bis zu einem zufällig grünen Lauf würden diese Instabilität nicht ausräumen.

Insgesamt **16 neue CLI-Läufe**: zweimal sechs synthetische Fälle und zweimal zwei Schritte mit echten Quellen. Alle Prozesse endeten mit Exitcode 0, Betriebsdateien blieben unverändert. Notizen wurden bei lesenden Fortsetzungen nicht überschrieben; getrackte Ziele blieben unverändert. Ein nicht unterstützter `realpath`-Schalter wurde vor dem Schreiben korrigiert; einzelne Suchbefehle lieferten keinen Treffer. Solche Werkzeugbefunde sind separat erfasst. Paketprüfung, zwölf Checker-Tests und Whitespace-Prüfung bestanden.

**Methode und Grenzen:** Kriterien vor Ausführung eingefroren; gleiche natürlichen Nutzerfragen und Quellen in beiden Runden, Regelstände mit Hashes gebunden. Die temporären Git-Repos besitzen diesmal einen Ausgangscommit, damit Git-Abfragen nicht allein am leeren Fixture-Repo scheitern. Codex CLI 0.147.0, Standardmodell ohne Override; keine unabhängig bestätigte Modellkennung. Bewertung durch den verantwortlichen Agenten anhand unveränderter Antworten, Notizen und Werkzeugspuren; keine menschliche PM-Abnahme und kein unbekanntes Testset.

Der Betreuer las das echte Ticket und die Original-Specs aktuell. Die getesteten Kontexte lasen datierte lokale Kopien; dies ist kein eigenständiger Live-Connector-Test des Clients. Der zweite Kontext hatte nur das gespeicherte Arbeitsverzeichnis, keine vorherige Antwort oder Gesprächsdatei. Keine Browser- oder Produktprüfung, keine Jira-Schreibaktion. Persönliche Konfiguration, Skills und Erweiterungen waren deaktiviert; temporäre Arbeitsordner mit Workspace-Schreibsandbox, weiterhin keine vollständige Dateilese-Isolation. In der korrigierten Runde wurde keine Suche außerhalb der erlaubten Fallordner beobachtet. Native Tests in anderen Clients und unabhängige PM-Bewertung bleiben offen.

Private Quellen, Antworten und Prüfbelege liegen unter `.local/evals/context-merge-20260921/`. Der öffentliche Bericht enthält keine Ticketkopien. Die Befunde vom 18.09.2026 bleiben nachfolgend als historische Läufe erhalten.

## Testbranch: gespeicherter Kontext und Wissensbasis — 18.09.2026

Auf `codex/persistent-context`, ausgehend von `1524ecf`, wurden Speichern, Fortsetzen und Wissenszugriff mit kurzen Nutzerfragen in temporären Git-Arbeitsordnern geprüft. Beim Speichern entstand eine echte lokale Ticketnotiz. Nachfolgende frische Kontexte erhielten diese Datei, aber keinen bisherigen Gesprächsverlauf. Für den Versionswechsel wurde die Original-Spec geändert; die alte Notiz blieb erhalten. Alle Produktquellen und Tickets dieser Runde sind synthetisch.

Kriterien wurden vor der ersten Regeländerung eingefroren. Der verantwortliche Agent bewertete die unveränderten Antworten, gespeicherten Dateien und Werkzeugspuren. Kein unabhängiges menschliches Urteil. Die folgenden Runden prüfen unterschiedliche Regelstände und sind keine gemeinsame Zuverlässigkeitsquote:

| Runde | Ergebnis | Befund |
| --- | --- | --- |
| Erste fünf Fälle | 1/5 | Frühere Umgebung beim Speichern verloren; Abweichung bei Fortsetzung ausgelassen; ignorierte Notiz übersehen; Wissenskonflikt eigenmächtig entschieden. Fehlende Notiz korrekt behandelt. |
| Getracktes Speicherziel, bereits präzisierte Regeln | 1/1 | Vorhandene Datei unverändert erhalten und fehlende Speicherung benannt. |
| Sechs Wiederholungen | 3/6 | Wiederaufnahme, Versionswechsel und Speicherschutz bestanden. Frühere Umgebung weiter verloren, fachliche Quelle ohne Ticketbezug übernommen, Wissenskonflikt weiterhin falsch entschieden. |
| Fünf gezielte Wiederholungen mit getrennten Umgebungsfeldern | 3/5 insgesamt, 4/5 fachlich | Speichern, Fortsetzen und fehlender Verlauf bestanden. Versionswechsel fachlich korrekt, aber Suche außerhalb des erlaubten Fallordners. Beim Wissenskonflikt wurde die Kontextanleitung nicht geladen; Konflikt erneut falsch entschieden. |
| Wissenszugriff nach präzisiertem Einstieg | 1/1 | Kontextanleitung vollständig gelesen; drei der Spec zugeordnet und fünf als ungeklärte Meetingaussage benannt, ohne endgültige gemeinsame Auflösung. |

Insgesamt 18 CLI-Läufe mit Prozess-Exitcode 0; die Betriebsdateien blieben unverändert. Die zuletzt ausgeführten Antworten erfüllten jeweils die fachlichen Kriterien auf ihrem dokumentierten Regelstand. Die Werkzeuggrenze beim Versionswechsel bleibt ein offener Befund; es gab keinen erneuten Gesamtlauf aller sechs Fälle nach der letzten Einstiegsänderung. Die zwölf Checker-Tests und die Paketprüfung bestanden ebenfalls.

Die Korrekturen betreffen direkten Zugriff auf ignorierte Notizen, getrennte aktuelle und historische Umgebungsangaben, Quellenbindung vor fachlichen Aussagen und den ausdrücklichen Einstieg zur Wissensnutzung. Der Schutz vor Überschreiben eines getrackten Ziels wurde zweimal beobachtet; Symlink- und Berechtigungsfehler wurden nicht eigens ausgeführt. Die gespeicherte Notiz blieb in sämtlichen Fortsetzungen unverändert.

**Grenzen:** Codex CLI 0.147.0 mit Standardmodell ohne Override; Modellkennung nicht unabhängig bestätigt. Frische kurzlebige Kontexte, vorhandene Host-Anmeldung, temporäre Ordner und Workspace-Schreibsandbox; persönliche Konfiguration, Skills, Memory, Plugins, Web und Agentenwerkzeuge deaktiviert. Keine VM oder vollständige Dateilese-Isolation. Der letzte Versionswechsel- und ein gescheiterter Wissenslauf suchten zusätzlich im Elternordner; beide verletzten damit die vorgegebene Fallgrenze. Es wurden dabei keine fremden Inhalte ausgegeben, aber die Werkzeuge verhindern solche Lesezugriffe hier nicht vollständig. Leere Suchtreffer und Git-Abfragen ohne vorhandenen Fixture-Commit erzeugten einzelne Nichtnull-Exitcodes; erfolgreiche CLI-Prozesse werden deshalb getrennt von inhaltlich bestandenen Fällen bewertet.

Kein Live-Jira-, Browser- oder vollständiger Abnahmedialogtest, keine Prüfung in Cursor, Claude oder Orca und keine statistische Stabilitätsaussage. Der echte lokale Wissenseinstieg und ein Glossarkapitel wurden separat lesend geprüft und nur in ignorierter lokaler Quellenkonfiguration angebunden. Das ist keine Team-Synchronisation. Rohantworten, Notizen, Quellen-Hashes, Patchstände, Kriterien und Einzelbewertungen liegen unter `.local/evals/persistent-context-20260918/`.

Das öffentliche Entwicklungsset enthält jetzt 28 synthetische Fälle; die sechs neuen Kontextfälle stehen im [Eval-Plan](../evals/README.md#gespeicherten-kontext-und-wissenszugriff-prüfen). Frühere Berichte unten betreffen frühere Regelstände.

## Belegprüfung und Verhaltenstests vom 18.09.2026

Am Stand `d99a5b6` mit lokalen Regeländerungen wurden zehn Einzelantworten in frischen Codex-CLI-Kontexten geprüft: die fünf geführten Abnahmefälle, zwei neue Fälle zu Quellenabdeckung und Geltungsbereich, zwei bestehende Fälle zu verständlicher bzw. vollständiger Ausgabe und eine eingefrorene Quellenprobe aus einem echten Ticket. Kriterien wurden vor den Regeländerungen festgehalten; die antwortenden Kontexte erhielten nur Betriebsdateien, Frage und Quellen, keine Kriterien oder Musterantworten. Bewertung durch den verantwortlichen Agenten anhand unveränderter Antworten und sichtbarer Werkzeugaufrufe, keine menschliche PM-Abnahme.

**Erstlauf: 8/10 bestanden.** Im Bug-Entwurf fehlte die Quelle der Erwartung. Die echte Ticketprobe erfand lokale Originalquellenlinks, obwohl nur Auszüge vorlagen, bündelte mehrere Prüfsituationen und band den Preisvergleich nicht ausreichend an denselben Tarif und Zahlungszeitraum. Eine zusätzliche Auffälligkeit im ansonsten akzeptierten Wiederaufnahmefall: Der alte Bug-Entwurf wurde als vorerst nicht nötig bezeichnet; historische Beobachtungen sollten beim Versionswechsel erhalten bleiben.

Die gezielte Korrektur präzisiert belegbare Quellenlinks, die Herkunft der Erwartung im Bug-Entwurf, den Umfang eines einzelnen Vergleichstests und das Erhalten alter Beobachtungen. Ein weiterer Fall prüft die Ergänzung eines bereits bekannten Bug-Tickets statt eines Duplikats. Das öffentliche Entwicklungsset enthält damit **22 Fälle**; die echte Quellenprobe bleibt ausschließlich lokal.

**Erste gezielte Wiederholung: 3/4 bestanden.** Bug-Entwurf, Wiederaufnahme und bestehendes Bug-Ticket erfüllten die Kriterien. Die echte Quellenprobe blieb zu ungenau beim Vergleich desselben Tarifs und setzte gültige Eingaben ohne passende Tarifvoraussetzungen mit vorhandenen Angeboten gleich. Nach einer weiteren Präzisierung bestand die einzelne erneute Quellenprobe **1/1**: zwei abgegrenzte, noch nicht ausgeführte Prüfsituationen, gleiche Tarifdaten und eine gewählte Zahlungsperiode gegen einen bekannten Referenzbetrag, ausdrücklich ungeklärte Testumgebung und separate Akzeptanzkriterien. Alle Fehlversuche bleiben erhalten; dies ist kein vollständiger neuer Lauf aller zehn bzw. 22 Fälle.

Alle 15 Antwortläufe endeten erfolgreich als CLI-Prozess. Die sichtbaren Aktionen lasen nur die Betriebsdateien und gelieferten Quellen; keine externen Aktionen, Werkzeugfehler, gekürzten Rückgaben oder Änderungen an den Betriebsdateien. Im Erstlauf lagen neun Standardantworten bei 34–137 Wort-Einheiten; die vollständige Siebener-Abnahme hatte zulässige 206. Erstlauf-Zeit je Antwort: 10,9–22,5 Sekunden, Median 15,0. Der CLI meldete insgesamt 205.896 Input- und 4.947 Output-Tokens für die zehn Erstläufe; das sind Laufwerte inklusive Kontext/Werkzeugrückgaben, keine Preisangabe oder nachgewiesene Einsparung.

**Grenzen:** Codex CLI 0.147.0, CLI-Standardmodell ohne Override; kein unabhängiger Beleg der Modellkennung. Bestehende Host-Anmeldung, temporäre Arbeitsordner, schreibgeschützte Ausführung, persönliche Konfiguration und Erweiterungen deaktiviert; keine VM oder vollständige Dateilese-Isolation. Ein interner Modellcache-Warnhinweis führte nicht zum Abbruch. Quellenproben prüfen den Umgang mit geliefertem Material, keinen neuen Jira-Zugriff, eigenständige Quellensuche oder Browser-Abnahme. Vorbereitete Gesprächsstände sind kein durchgehender Mehrturn-Dialog. Keine unabhängige menschliche Bewertung, kein unbekanntes Testset und kein kontrollierter Vorher-/Nachher-Vergleich. Kriterien, Patchstände, Hashes, unveränderte Antworten, Tokenwerte und Einzelbewertungen liegen im ignorierten `.local/`.

Paketprüfung und die 12 Checker-Tests bestanden zusätzlich. Nächster Verhaltensnachweis ist ein zusammenhängender Dialog; dieser und native Erststarts in weiteren Clients bleiben offen. Das bedarfsgerechte Aufteilen der Anweisungen blieb in dieser ersten Runde unverändert; der anschließende Vergleich ist separat dokumentiert.

## Vergleich des bedarfsgerechten Ladens — verworfene Aufteilung

Vier identische Fragen und Quellen wurden mit den korrigierten Regeln vor und nach einer probeweisen Auslagerung des geführten Abnahmeablaufs geprüft. Je ein frischer CLI-Lauf pro Fall und Variante, unveränderte Kriterien. Die Zuordnung funktionierte in allen vier Fällen: Erklärung und Testliste lasen nur das PM-Profil; kurze Abnahmefortsetzung und Bug-Entwurf lasen zusätzlich den ausgelagerten Ablauf.

| Fall | Input-Tokens vorher → nachher | Laufzeit vorher → nachher | Kriterien vorher / nachher |
| --- | ---: | ---: | --- |
| Einfache Erklärung | 20.692 → 19.905 | 11,0 → 12,8 s | Bestanden / bestanden |
| Unklare Abnahmerückmeldung | 20.777 → 33.037 | 9,8 → 16,3 s | Bestanden / bestanden |
| Bug-Entwurf | 20.759 → 33.144 | 13,9 → 18,6 s | Bestanden / bestanden |
| Echte Quellenprobe | 21.110 → 20.285 | 20,4 → 19,3 s | Nicht bestanden / nicht bestanden |

Die zusätzliche Leserunde erhöhte bei geführten Aufgaben den gemeldeten Gesamtkontext; die Cacheanteile änderten sich ebenfalls. Die Zahlen sind keine Rechnung über Modellkosten und keine stabile Laufzeitaussage. Bei einfachen Aufgaben wurden in diesen Paaren etwa 800 Input-Tokens weniger verarbeitet. Für das kleine Paket rechtfertigt das die zusätzliche Datei und Leserunde derzeit nicht: **Die Aufteilung wurde zurückgenommen; das PM-Profil bleibt zusammen.** Die getesteten Korrekturen zur Belegprüfung bleiben erhalten.

Jeweils **3/4** Antworten erfüllten alle vorab festgelegten Kriterien. Vor der Aufteilung blieb die echte Quellenprobe beim Preisvergleich zu ungenau; danach waren Vergleich und Fallumfang korrekt, aber die fehlende bestätigte Testumgebung wurde nicht genannt. Ein nicht ausgeführter Laufzeittest ist keine gleichwertige Erklärung dieses fehlenden Ausgangspunkts. Die Quellenprobe ist damit weiterhin nicht stabil, auch nach ihrem zuvor erfolgreichen Einzelversuch. Diese Fehler werden weder aus der Wertung entfernt noch durch geänderte Kriterien übergangen. Alle acht Prozessläufe endeten ohne externe Aktionen, Werkzeugfehler, gekürzte Rückgaben oder geänderte Betriebsdateien.

Der endgültige Betriebsstand entspricht wieder dem geprüften Stand vor der Aufteilung. Der Vergleich dient der Entscheidung über die Dateiaufteilung, nicht als Beleg einer allgemeinen Qualitätssteigerung. Die Grenzen der vorherigen CLI-Proben gelten unverändert; Antworten, Kriterien, Werkzeugbelege und Cache-/Tokenwerte bleiben lokal erhalten. Vor einer Teamfreigabe bleibt insbesondere die vollständige Benennung abnahmerelevanter Lücken erneut zu prüfen.

## Geführte PM-Abnahme — lokale Erweiterung vom 18.09.2026

Das PM-Profil begleitet jetzt einzelne Prüffälle, hält Beobachtungen mit Herkunft fest und unterscheidet bestanden, abweichend und offen. Ein belegter Unterschied führt zu einem Bug-Entwurf im Chat; Quellenkonflikte bleiben Klärungspunkte. Pausen, unvollständige Rückmeldungen und Änderungen des Produktstands sind berücksichtigt. Das vorhandene Beispiel wurde um einen Dialog ergänzt, das Entwicklungsset von 14 auf 19 Fälle erweitert.

Paketprüfung und die 12 Checker-Tests bestanden am lokalen Stand. Zum Zeitpunkt dieser Erweiterung waren die fünf neuen Modellfälle und ein zusammenhängender Dialog noch nicht ausgeführt; eine menschliche PM-Abnahme steht weiterhin aus. Die folgenden älteren Modellbewertungen belegen diese Erweiterung nicht. Der [Prüfplan](../evals/README.md#geführte-abnahme-prüfen) beschreibt die nötigen nächsten Nachweise.

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
