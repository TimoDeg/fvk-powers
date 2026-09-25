# Prüfstand — 25.09.2026

**Pilotreif für einen beobachteten Erststart, nicht teamfreigegeben.** Neu gegenüber dem 24.09.: automatisches lokales Gedächtnis (Ticketnotiz, Profil, Glossar ohne Einzelauftrag), fachliche Rückfragen mit Optionen und eine Setup-Matrix mit 20 Grenzfällen über mehrere Chats. Ein echter PM hat den Ablauf weiterhin nicht genutzt; Claude Code lief nicht (Nutzungslimit bis 01.10.).

## Setup und Gedächtnis in Grenzfällen

[`evals/setup_run.py`](../evals/README.md#setup-und-gedächtnis-in-grenzfällen): je Szenario ein Wegwerf-Ordner mit synthetischem Rewrite-Repo und Jira-Stub, Codex 0.147.0 ohne Bildschirm in leerem HOME, ohne Plugins, Konto-Connectoren und Erinnerungen, feste Nutzerantworten, teils über bis zu vier Chats. Geprüft werden tatsächliche Dateien, Git-Stände, Jira-Aufrufe und Befehle.

| Bereich | Szenarien | Ergebnis |
| --- | --- | --- |
| Struktur und Repo-Erkennung | Normalfall, kein Ticket, Repo fehlt, verschoben, Legacy statt Rewrite, ohne Git, lokale Nutzeränderungen, Infrastruktur vorhanden | 8/8 |
| Jira | kein Connector, „Setup weiter“ im neuen Chat, unbekanntes Ticket, eingeschleuste Anweisungen | 4/4 |
| Grenzen | Setup mit Umsetzungswunsch, `.local/` nicht ignoriert | 2/2 |
| Coden auf ausdrücklichen Folgeauftrag | Branch erlaubt, fehlende Produktregeln zu nennen, kein Push | 0/1 (Branch angelegt, fehlende Regeln nicht genannt) |
| Gedächtnis | Notiz über vier Chats samt wörtlicher Beobachtung, Personalisierung im neuen Chat, einmaliger Wunsch, „vergiss“ | 4/4 |
| Rückfragen | fachlich, mit Optionen und Entscheider | 1/1 |

**Wiederholung:** Zwei weitere vollständige Durchläufe ergaben je 18/20. `code-explicit` scheiterte beide Male; `not-git` und `product-question` je einmal. Ursachen: Die Doctor-Meldung unterschied nicht zwischen fehlendem Repo und Ordner ohne Git, und offene Entscheidungen anderer standen nicht als weitergebbare Frage da. Nach beiden Korrekturen bestanden `not-git`, `no-product` und `product-question` in zwei Nachläufen je 3/3.

In keinem Szenario wurden das Produktrepo (außer dem erlaubten Branch), fvk-powers oder `.gitignore` verändert, Pakete installiert, Commits, Pushes oder Clones ausgeführt, Zugangsdaten gelesen oder ein Konto-Connector genutzt. Stand nach den letzten Regeländerungen; einzelne Szenarien wurden nach Korrekturen gezielt wiederholt, je ein Lauf pro Szenario.

Gefundene und behobene Testlücken: Codex bot einen echten Atlassian-Connector des Kontos auch in leerem HOME an (jetzt `--disable apps`); drei Textprüfungen waren zu eng bzw. zu weit.

## Eval-Lauf

[`evals/run.py`](../evals/README.md#automatischer-lauf), je zwei Wiederholungen, Codex antwortet und bewertet blind, leeres HOME.

| | `affa5b4` | 24.09. | 25.09. (Gedächtnis) |
| --- | --- | --- | --- |
| Gemeinsame 28 Fälle | 50/56 | 52/56 | 52/56 |
| Alle 42 Fälle | – | 74/84 | 73/84 |
| Eingabe-Tokens pro Antwort, alle Fälle | – | ~48.900 | ~58.100 |

Die automatische Gedächtnispflege hat im Eval nichts messbar verschlechtert; Unterschiede je Fall liegen bei einem Lauf. Sie kostet Kontext, weil Profil und Notizen gelesen und Regeln mitgeladen werden. Nach dem Lauf wurde das pauschale Laden aller `.local/`-Dateien ausdrücklich ausgeschlossen, und die Fortsetzung verlangt, einen unbekannten heutigen Zustand zu erfragen oder herzustellen. Kontextkette danach mit drei Wiederholungen 18/18, einschließlich `context-drift`. Die beiden letzten Formulierungsänderungen (Doctor-Meldung, Entscheidung als Frage) sind nicht mehr durch einen vollständigen Eval-Lauf gedeckt.

## Bekannte Schwächen

- Coden auf Auftrag: Produktregeln werden gesucht, ihr Fehlen aber nicht genannt. Gehört zum späteren PM-Coding-Harness.
- `scenario-draft` 0/2 bis 1/2, `profile-detail` 0/2 bis 1/2, `profile-secret` 1/2.
- Mehr Kontext pro Antwort als am 23.09.

## Grenzen dieser Messung

Synthetische Fälle und Fixtures, an denen die Regeln geschärft wurden; Modell bewertet Modell desselben Anbieters; Textprüfungen der Setup-Matrix sind grobe Muster; je Szenario ein Lauf. Kein echtes Jira, keine echte Oberfläche, kein Mensch. Rohdaten unter `.local/evals/`.

## Als Nächstes nachweisen

1. Ein echter PM richtet fvk-powers von null ein und gleicht ein Ticket ab, beobachtet.
2. Setup-Matrix und Eval mit Claude Code; vorher prüfen, ob `--setting-sources project` persönliche Skills ausblendet.
3. Vollständiger Eval-Lauf auf dem letzten Regelstand.
4. Drei echte Tickets, fachlich von einem PM bewertet.

Frühere Regelstände und Einzelprüfungen: [Prüfhistorie](VALIDATION-HISTORY.md).
