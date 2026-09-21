# Antwortqualität und Setup messen

Paketprüfungen, Quellenzugriff und Produktnutzen sind getrennte Messungen. Die [synthetischen Fälle](cases.json) enthalten PM-Antwortfälle und Entwicklerfälle mit dem Präfix `dev-`. Letztere brauchen tatsächliche Dateien, Änderungen und Testausführung nach dem Prüfplan unten; Antwortsimulation genügt nicht. Frühere Durchläufe stehen separat in [Ergebnisse vom 17.09.2026](results/2026-09-17-v1.md). Die [Stilbeispiele](../examples/pm.md) sind redaktionell geschriebene Beispiele, keine Benchmark-Ausgaben.

## Vor dem Teamstart

1. **Paket prüfen:** Links, portable Einstiege, ausgeschlossene private Dateien und gültige Eval-Fälle. Die automatischen Tests prüfen auch absichtlich beschädigte Pakete. Das beweist keine Befolgung der Anweisungen durch ein Modell.
2. **Frisches Setup:** Ein Entwickler öffnet nur dieses Repo in einem neuen Client-Kontext, ohne persönliche Skills oder alte Gesprächsinhalte. „Richte fvk-powers für mich ein.“ testen: beide Zugänge vorhanden, fehlendes Jira, fehlende Specs, fehlende Berechtigung, unterbrochenes Setup. Den tatsächlichen Chat und die ausgeführten Aktionen lokal erfassen.
3. **Synthetische Antworten:** Die Fälle ohne `dev-` aus `cases.json` einzeln in einem neuen Kontext mit den Repo-Regeln und ausdrücklich gewähltem `profiles/pm.md` ausführen. Entwicklerfälle mit ihrem natürlichen Prompt und tatsächlichen Produktdateien starten; die Profilauswahl ist Teil der Prüfung. Dem antwortenden Modell nur Auftrag und Quellen geben; `must_include` und `must_not` erst beim Bewerten verwenden. Keine Musterantwort in den Antwortkontext laden. Das ist ein Entwicklungsset, kein unbekannter Holdout.
4. **Echte Fragen:** Mindestens drei freigegebene Rewrite-Tickets mit verschiedenen Themen prüfen: Codeanalyse, Implementierung mit Tests und Diff-Review. Quellenstand festhalten; ein unabhängiger Entwickler prüft Ergebnisse und Testbelege. Für das optionale PM-Profil zusätzlich Erklärung, Spec-Abgleich und Abnahme durch einen PM prüfen lassen. Private Belege bleiben lokal, ins Repo kommen nur freigegebene aggregierte Ergebnisse.
5. **Wiederholung:** Vor einer Teamfreigabe die kritischen Fälle Konflikt, fehlende Quelle, Statusbehauptung und Anweisungen in Quellen jeweils dreimal frisch ausführen. Alle Versuche zählen, auch Fehlversuche. Neue, nicht zum Prompt-Tuning genutzte Fragen separat ergänzen.

## Je Client prüfen

Regeln und Fälle sind gemeinsam, tatsächliche Durchläufe bleiben nach Client getrennt. Für Cursor, Claude Code, Codex und Orca je einen frischen Setup-Lauf erfassen: werden die Einstiegsregeln geladen, ist eine Original-Spec lesbar, gelingt der konkrete Jira-Abruf und funktioniert „Setup weiter“? Bei Orca den gestarteten Agenten und dessen Version zusätzlich festhalten. Ein neuer Worktree muss auch ohne übernommene `.local/sources.md` verständlich starten.

Eine als Cursor, Claude oder Orca beschriebene Simulation in Codex ist kein Test dieses Clients. Native Tests und Connector-Anmeldungen nur dann als bestanden melden, wenn sie dort tatsächlich ausgeführt wurden. Client-Dokumentation und vorhandene Einstiegsdateien belegen lediglich den vorgesehenen Integrationsweg.

## Was wir zählen

| Kennzahl | Definition | Fehlende Daten |
| --- | --- | --- |
| Erfolgreicher Erstversuch | Fälle, deren erste Antwort alle Muss-Kriterien erfüllt / tatsächlich erstmals ausgeführte Fälle | „Nicht gemessen“, niemals 0 % aus 0 Versuchen |
| Stabilität | Kritische Fälle mit drei erfolgreichen Versuchen / kritische Fälle mit drei ausgeführten Versuchen | Unvollständige Wiederholungen separat nennen |
| Quellenbelege | Geprüfte wesentliche Aussagen mit passendem Quellenbeleg / alle geprüften wesentlichen Aussagen | Zahl der Aussagen und Prüfer angeben |
| Fachliche Treue | Keine ausgelassene entscheidende Bedingung, falsche Zahl oder erfundene Umsetzung | Jeder solche Fehler lässt den Fall scheitern |
| Verständlichkeit | Bewertung der jeweiligen Zielgruppe 1–5: 1 unverständlich, 3 Rückfragen nötig, 5 handlungsfähig; Entwickler- und PM-Profil getrennt ausweisen | Nur mit tatsächlichen Bewertungen berichten |
| Setup-Erfolg | Frische Setups mit den benötigten geprüften Zugängen und erstem Quellenabgleich / gestartete Setups | Quellenmangel und Bedienproblem getrennt erklären |
| Aufwand | Zeit bis erster belegter Antwort, Zahl nötiger Nutzerrückfragen; Median erst bei mehreren Läufen | Einzelfallwerte als solche benennen |

Ein Lauf braucht lokal: Fall-ID, Zeit, Repo-Commit und lokale Abweichungen, Modell/Client, Quellenstand, sichtbare Antwort, Werkzeugbeleg bei Setup/Recherche, Versuchszähler, Bewertung pro Kriterium und Prüfer. Die Modellbewertung darf unterstützen; unabhängige fachliche und sprachliche Bewertung nicht durch Selbsteinschätzung ersetzen. Für Vergleiche identische Eingaben und Quellen verwenden.

## Freigabekriterium

Vor Pilotstart: Paketchecks grün, ein frisches Entwickler-Setup samt erstem Ticket-Spec-Abgleich beobachtet und ein Entwickler bestätigt Nutzbarkeit. Die unten genannten Entwicklerfälle müssen ausgeführt und akzeptiert sein; Paketchecks und ältere PM-Antworttests reichen dafür nicht. Vor breitem Teameinsatz: alle Entwicklungsfälle bewertet, keine offenen kritischen Fakten-/Quellen-/Zugriffsfehler, die genannten Wiederholungen erfolgreich und die drei echten Ticketfälle fachlich akzeptiert. Diese Schwellen sind vereinbarte Prüfziele, keine statistisch belegte allgemeine Zuverlässigkeit.

Der aktuelle [Prüfbericht](../docs/VALIDATION.md) nennt ausgeführte Checks und offene Nachweise. README-Zahlen dürfen nur daraus bzw. aus tatsächlichen Messbelegen stammen. Bei jeder Änderung an Anweisungen frühere Antwortbewertungen als ältere Baseline kennzeichnen; die CI prüft ausschließlich das Paket.

## Entwicklerablauf praktisch prüfen

In einem isolierten, beschreibbaren Checkout ohne vorherigen Gesprächskontext prüfen; vor jedem Fall Kriterien und Ausgangsstand festhalten:

- **Analyse:** Ticket und Spec mit aktuellen Codepfaden verbinden, Anforderungen von bestätigtem Verhalten trennen; ohne Änderungsauftrag bleibt der Checkout unverändert.
- **Implementierung und Tests:** Einen kleinen, freigegebenen Auftrag bis zur minimalen Änderung und den relevanten Tests ausführen. Der Test muss das geforderte Verhalten prüfen; bestehende fremde Änderungen erhalten. Testausführung und Diff als Beleg erfassen.
- **Review:** Einen vorbereiteten Diff mit bekanntem Fehler prüfen; konkrete Fundstelle und Auswirkung erwarten. Bewertungskriterien und Fehlerlösung bleiben aus dem Antwortkontext heraus.
- **Fehlende Umgebung:** Eine fehlende Testvoraussetzung konkret benennen, noch mögliche Prüfungen durchführen und nicht ausgeführte Tests als offen melden.

Für die vier `dev-`-Fälle ein kleines synthetisches Produkt mit gemeinsamen Auswahlregeln und zwei Aufrufern verwenden. Vorhandene fremde Änderungen als Kontrollbeleg einfrieren. Ein PM beauftragt die Arbeit in Alltagssprache; dieselben Entwicklungsregeln müssen geladen werden. Beim Implementierungsfall die vom Assistenten ergänzten Tests zusätzlich gegen den unveränderten fehlerhaften Ausgangscode prüfen. Review-, Test- und Konfliktfälle müssen den Produktinhalt erhalten. Fehlende Browserlaufzeit darf bei grünen Unit-Tests keine vollständige Freigabe ergeben. Testdaten, Rohantworten und Werkzeugspuren lokal behalten; Ergebnisse samt Fehlversuchen im [Prüfbericht](../docs/VALIDATION.md) ausweisen.

Diese kleinen Fälle belegen keinen vollständigen Rewrite-Ablauf. Danach einen freigegebenen echten Änderungsauftrag von PM-Formulierung über Code und Tests bis zum Diff-Review durchführen. Erst nach Prüfung dieses Ablaufs die Verbindung zur PM-Pipeline bewerten. Native Clienttests getrennt dokumentieren; Erfolge im PM-Profil nicht als Entwicklernachweis zählen.

## Ausgabeumfang im PM-Profil prüfen

Bei `compact-overview` die sichtbaren Wörter ohne Markdown-Linkziele und die tatsächlichen Prüfsituationen zählen. Drei Listenpunkte mit sieben Fällen erfüllen die Regel nicht. Fachliche Bedingungen, Quellenkonflikte und Unsicherheit zugleich prüfen: Kürze allein reicht nicht. `complete-acceptance` prüft die Ausnahme für ausdrücklich vollständige Aufträge; alle sieben Situationen müssen erhalten bleiben. Die bisherigen 12 Baseline-Antworten belegen diese beiden später ergänzten Fälle nicht.

## Historische Implementierungsproben

Freigegebene gemergte Tickets lokal vom Stand vor dem damaligen Fix starten, jeweils in einem eigenen Worktree mit frischem Kontext und natürlichem Auftrag. Quellen, vorhandene lokale Abweichungen, Prüfkriterien und Regelhashes vorab einfrieren; fertige Lösung und Bewertungskriterien bleiben außerhalb des Autorenkontexts. Checkout-Hooks und Einrichtungs-Scripts vor Materialisierung auf Seiteneffekte prüfen. Keine Veröffentlichung durch den Test.

Jedes Ticketsymptom einzeln bewerten: Verhalten am betroffenen Einstieg, Fehlerantwort und Ausgabe, soweit betroffen. Neue Regressionstests müssen am falschen Verhalten scheitern; Testaufbaufehler zählen gesondert. Einen grünen Test zusätzlich mit gezielt entfernter Korrektur prüfen. Browsernachweise müssen die tatsächlichen Produktkomponenten ausführen; nachgebautes HTML und Klassen-Assertions sind nur ergänzende Checks. Besteht dieselbe Verhaltensprobe auch am fehlerhaften Ausgangsstand, ist der Fehler nicht reproduziert. Nachträgliche Prüferkorrekturen separat halten, damit der Erstversuch unverändert bewertbar bleibt.

Nach einer Regeländerung den bekannten Fehlerfall erneut und danach ein anderes freigegebenes Ticket prüfen. Bekannte Entwicklungsfälle und weitere Tickets getrennt ausweisen; einzelne Erfolge belegen keine Stabilität. Browser-, Integrations- und Clientgrenzen bleiben sichtbar.

Zeitstempel für Werkzeugstart/-ende, vollständige Rückgaben und native Usage-Zähler erfassen, soweit der Client sie liefert. Kumulierten Input, Cache-Anteil und Output getrennt nennen; fehlende Einzelzeiten oder Tokenwerte nicht schätzen. Einrichtung, Autor und unabhängige Prüfung getrennt zählen. Vertrauliche Werte vor Ausgabe vermeiden und in gespeicherten Protokollen zusätzlich schwärzen. Aufwand nur zusammen mit fachlicher Abdeckung vergleichen.
