# Prüfstand — 23.09.2026

**Pilotreif für einen beobachteten Erststart, nicht teamfreigegeben.** Die neu strukturierten Regeln bestehen auf denselben 28 synthetischen Fällen mehr Läufe als der vorherige Stand, mit kürzeren Antworten und weniger Kontext. Ein echter PM hat den Ablauf noch nicht genutzt.

## Vergleich vorher/nachher

Beide Regelstände liefen mit [`evals/run.py`](../evals/README.md#automatischer-lauf): alle Fälle, je zwei Wiederholungen, frischer Kontext pro Antwort, Bewertung blind durch einen separaten Claude-Sonnet-Kontext.

| Client | Vorher (`7af0ef1`) | Nachher | Wörter pro Antwort | Kontext pro Antwort |
| --- | --- | --- | --- | --- |
| Claude Code, Sonnet | 41/56 | **47/56** | 137 → 115 | −14 % |
| Codex CLI 0.147.0 | 37/48 | 38/48 | 69 → 65 | −19 % |

- Der Claude-Nachher-Wert stammt aus einem vollständigen Lauf auf einem Regelstand mit vor und nach dem Lauf identischen Dateihashes. Beide Claude-Läufe nutzten dasselbe `CLAUDE.md`, sodass nur der Regelinhalt verglichen wird.
- Codex: 48 statt 56 Läufe, weil das Ausgabenlimit des Workspaces vier Kontextfälle abbrach; verglichen wurden nur Fälle mit gültigen Antworten in beiden Varianten. Dieser Lauf betraf eine frühere Zwischenfassung der neuen Regeln.
- Deutliche Gewinne: Fortsetzen aus gespeicherter Notiz, veralteter Status, Wissens- und Abnahmekonflikte, Kurzform. Kein Fall hat sich zwischen vollständigem Vorher- und Nachherlauf mit Claude um mehr als einen Lauf verschlechtert.
- Nachgeschärft und gezielt je dreimal geprüft: kompakter Überblick 3/3, Zurücklesen gespeicherter Notizen (Kontextkette 14/18, Speichern 2/3), Schutz gegen eingeschleuste Anweisungen weiterhin 3/3.

## Bekannte Schwächen

- `missing-spec` scheitert in beiden Regelständen gleich: Die Antwort nennt, wo die Spec läge, der Bewerter wertet den Pfad als unbelegt.
- `setup-resume` ist in der Antwortsimulation nur begrenzt aussagekräftig: Der Fall meldet ein verfügbares Jira-Werkzeug, das es im Testkontext nicht gibt. Der Fall enthält seit diesem Stand den bereits genannten Ticketlink; frühere Ergebnisse dazu sind nicht vergleichbar.
- `plain-language` fragt teils nach dem Ticket, statt die gelieferte Notiz zu erklären (2/3).

## Grenzen dieser Messung

Synthetisches Entwicklungsset, an dem die Regeln geschärft wurden, kein unbekanntes Testset. Modell bewertet Modell; keine menschliche PM-Bewertung. Keine echten Jira-, Repo- oder Browserzugriffe. Zwei Wiederholungen belegen keine stabile Erfolgsquote. Harness-Artefakte wurden für beide Varianten gleich korrigiert: Claude Codes eigenes Auto-Memory gilt nicht als Zugriff außerhalb des Fallordners, und `context-storage-guard` darf die Notiz im Chat ausgeben. Rohantworten, Bewertungen und Hashes liegen lokal unter `.local/evals/`.

## Als Nächstes nachweisen

1. Ein echter PM richtet fvk-powers von null ein und gleicht ein Ticket ab, beobachtet.
2. Drei echte Tickets, fachlich von einem PM bewertet.
3. Claude Code und Cursor mit echter Jira-Verbindung.
4. Neue, nicht zum Schärfen genutzte Fragen.
5. Die vier Kontextfälle erneut unter Codex, sobald das Limit es erlaubt.

Frühere Regelstände und Einzelprüfungen: [Prüfhistorie](VALIDATION-HISTORY.md).
