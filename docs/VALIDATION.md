# Prüfstand — 24.09.2026

**Pilotreif für einen beobachteten Erststart, nicht teamfreigegeben.** Neu gegenüber dem 23.09.: realistischer Jira-Stub, erstmals isolierte Erststarts in einer frischen Umgebung, Paket B (Umfang und Dev-Frage), Profil, Glossar und Scenario-Entwürfe mit Eval-Fällen. Ein echter PM hat den Ablauf weiterhin nicht genutzt; Claude Code lief heute nicht (Nutzungslimit).

## Erststart in frischer Umgebung

`tools/fresh_env.py` baut `fvk-powers` neben einem synthetischen `fvk` und einem lokalen Jira-Stub. Codex 0.147.0 lief ohne Bildschirm, in einem leeren HOME (nur der Login verlinkt), ohne persönliche Skills, Plugins oder Erinnerungen. Aufgabe: „Richte fvk-powers für mich ein. Mein Ticket: …“.

| Regelstand | Ticket | Ergebnis |
| --- | --- | --- |
| neu | TEST-42 (Spec vorhanden, Akzeptanzkriterium widerspricht der Spec) | Ein Zug bis zum Abgleich. Akzeptanzkriterien-Feld über die Feldbeschreibung gefunden und gespeichert, Widerspruch als Produktentscheidung benannt, Profilfrage erst am Ende. |
| neu | TEST-43 (keine passende Spec) | Ein Zug. Keine Spec erfunden, leeres Akzeptanzkriterien-Feld gemeldet, ein Abnahmeschritt aus dem Ticket. |
| `affa5b4` | TEST-42 | Ebenfalls ein Zug, Feld gefunden, Widerspruch benannt; ohne Profil und Feldspeicherung, die es dort nicht gibt. |

Je ein Lauf, Codex ohne Bildschirm, synthetische Specs, Stub statt echter Jira-Anmeldung. Frühere Erststarts desselben Tages sind ungültig: Codex hatte trotz Deaktivierung einen persönlichen FVK-Skill des Betreuers geladen. Der am Morgen beobachtete Fehlschlag („passt vollständig“ ohne gelesene Akzeptanzkriterien) ging vor allem auf diesen Skill und einen Stub ohne Feldbeschreibung zurück; die neue Regel zum Akzeptanzkriterien-Feld ist durch diese Läufe nicht als notwendig belegt.

## Eval-Lauf vorher/nachher

[`evals/run.py`](../evals/README.md#automatischer-lauf), je zwei Wiederholungen, frischer Kontext pro Antwort, Codex antwortet und bewertet blind (Claude war wegen Nutzungslimit nicht verfügbar), beide Varianten in leerem HOME.

| | Vorher (`affa5b4`) | Nachher |
| --- | --- | --- |
| Gemeinsame 28 Fälle | 50/56 | **52/56** |
| Neue 14 Fälle | – | 22/28 |
| Wörter pro Antwort (gemeinsame Fälle) | 66 | 68 |
| Eingabe-Tokens pro Antwort (gemeinsame Fälle) | ~36.600 | ~46.200 (+26 %) |
| Verständlichkeit, Modellurteil 1–5 | 4,93 | 4,96 |

- Besser: `setup-resume` 0/2 → 2/2, `stale-status` und `setup-no-jira` je 1/2 → 2/2. Schlechter: `context-storage-guard` und `guided-existing-bug` je 2/2 → 1/2. Bei zwei Wiederholungen ist ein Unterschied von einem Lauf kein belastbarer Effekt.
- Mehr Kontext: Die zusätzlichen Abschnitte (Profil, Glossar, Umfang, Szenarien) kosten Eingabe-Tokens bei jeder Antwort.
- 13 Antworten des Nachher-Laufs brachen wegen eines Netzwerkausfalls nach fünf Minuten ohne Antwort ab. Sie gelten jetzt als ungültig statt als Fehlschlag und wurden einmal nachgeholt (12/13 bestanden); die Tabelle zählt die Nachholläufe.
- Zwei Kriterien wurden nach Sicht erster Ergebnisse präzisiert: `ticket-spec-match` verlangte zuvor, die Jira-Feldbeschreibung in der PM-Antwort zu nennen (widerspricht dem PM-Profil); `scenario-draft` wertete eine tatsächlich geprüfte JSON-Syntax als verbotenes Prüfergebnis.

## Bekannte Schwächen

- `context-storage-guard` 1/2: Einmal wurde die bereits getrackte Notiz zuerst geschrieben, dann geprüft und zurückgesetzt. Das Endergebnis war richtig, die Reihenfolge verletzt „erst prüfen, dann schreiben“. Kontrolllauf mit drei Wiederholungen: 3/3, ohne Schreibzugriff.
- `context-drift` scheitert in beiden Regelständen (0/2, im Kontrolllauf 0/3): Nach einem Versionswechsel bleibt die neue Prüfung nicht ausdrücklich offen.
- `scenario-draft` 0/2: Die Suche nach Engine-Originalen greift auf den Elternordner (`../fvk`) zu, obwohl `.local/sources.md` eine andere Produktquelle nennt.
- Je 1/2: `glossary-save` (einmal eine Definition zum Gewinner erklärt), `profile-detail`, `profile-secret`, `setup-layout-missing`.

## Grenzen dieser Messung

Synthetisches Entwicklungsset, an dem die Regeln geschärft wurden. Modell bewertet Modell desselben Anbieters; keine menschliche Bewertung. Die Zahlen sind nicht mit dem 23.09. vergleichbar (anderer Client und Bewerter, damals ohne leeres HOME). Rohantworten, Bewertungen und Hashes liegen lokal unter `.local/evals/`.

## Als Nächstes nachweisen

1. Ein echter PM richtet fvk-powers von null ein und gleicht ein Ticket ab, beobachtet (eigener macOS-Benutzer).
2. Derselbe isolierte Erststart und A/B-Lauf mit Claude Code; vorher prüfen, ob `--setting-sources project` persönliche Skills ausblendet.
3. Zwei Dev-Frage-Entwürfe an echten Tickets von einem Entwickler bewerten lassen.
4. Drei echte Tickets, fachlich von einem PM bewertet; neue, nicht zum Schärfen genutzte Fragen.

Frühere Regelstände und Einzelprüfungen: [Prüfhistorie](VALIDATION-HISTORY.md).
