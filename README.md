# fvk-powers

Ein Arbeitsablauf für PMs im KI-Assistenten: Rewrite-Tickets verstehen, mit den Specs abgleichen, Abnahmen Schritt für Schritt begleiten und Bug-Entwürfe vorbereiten.

## Warum

Ein KI-Assistent antwortet immer flüssig, auch wenn er die entscheidende Stelle nie gelesen hat. Für PMs ist das gefährlich: Ein falsch übernommenes Limit, ein alter „Done“-Status oder eine erfundene Ursache landen direkt in Abnahme und Planung.

fvk-powers gibt dem Assistenten klare Arbeitsregeln:

- **Nur Gelesenes zählt.** Aussagen stützen sich auf Ticket und Spec, mit Link. Ungelesene Anhänge oder fehlender Zugriff bleiben als Lücke sichtbar.
- **Widersprüche bleiben offen.** Sagt das Ticket drei und die Spec fünf, entscheidet nicht die KI, sondern du erfährst, welche Entscheidung fehlt.
- **Alt ist nicht aktuell.** „Done“ heißt nicht live, ein Test von letzter Woche gilt nicht für die neue Version.
- **Nichts passiert ungefragt.** Der Assistent liest und entwirft; Jira-Tickets, Kommentare oder Nachrichten entstehen nur auf ausdrücklichen Auftrag.

## So sieht das aus

Ein erfundenes Beispiel einer geführten Abnahme:

> **PM:** Führe mich durch die Abnahme.
>
> **Assistent:** Du hast in Vorschau A drei Favoriten markiert. Markiere jetzt ein viertes Angebot. Laut Spec erscheint ein Hinweis und die drei bleiben ausgewählt. Was siehst du?
>
> **PM:** Der Hinweis kommt, aber alle Favoriten sind weg.
>
> **Assistent:** Der Fall ist **abweichend laut deiner Rückmeldung**. Hier ist der **Bug-Entwurf, nicht erstellt**: Titel, Umgebung, Schritte, Erwartung mit Spec-Link, Beobachtung. Offen sind noch Screenshot und Wiederholbarkeit.

Weitere Beispiele: [examples/pm.md](examples/pm.md).

## Starten in drei Schritten

Du brauchst einen **KI-Assistenten mit Datei- und Werkzeugzugriff** (Codex, Claude Code, Claude Desktop oder Cursor), **Git** und Lesezugriff auf **Jira** und das **Rewrite-Produktrepo**, in dem die Specs liegen. Eine laufende Produktanwendung brauchst du nicht. Zum ersten Mal hier? [Assistent und Git einrichten, Jira verbinden](docs/DEPENDENCIES.md#einrichtung-von-anfang-an).

1. **Herunterladen:** Im Terminal in deinem Projektordner ausführen:

   ```sh
   git clone https://github.com/TimoDeg/fvk-powers.git
   ```

2. **Öffnen:** Den Ordner `fvk-powers` im Assistenten als Projekt öffnen. Codex und Cursor lesen `AGENTS.md`, Claude Code liest `CLAUDE.md`.
3. **Einrichten:** Im Chat schreiben: „Richte fvk-powers für mich ein.“ Halte einen **Rewrite-Ticketlink** und den **Ordner oder Link des Rewrite-Repos** bereit. Der Assistent prüft, was schon geht, und führt dich durch den Rest. Unterbrochen? „Setup weiter“.

Passwörter und Tokens gehören nie in den Chat; die Anmeldung läuft im jeweiligen Dienst.

## Was du fragen kannst

| Du möchtest … | Frage im Chat |
| --- | --- |
| Ein Ticket verstehen | „Erkläre mir dieses Ticket: Was ändert sich für Kunden?“ |
| Anforderungen abgleichen | „Passt das Ticket zur Spec? Was fehlt oder widerspricht sich?“ |
| Eine Abnahme vorbereiten | „Welche konkreten Situationen sollte ich prüfen?“ |
| Eine Abnahme durchführen | „Führe mich Schritt für Schritt durch die Abnahme.“ |
| Eine Abweichung festhalten | „Mach daraus einen Bug-Entwurf.“ |
| Den Release-Stand klären | „Ist das schon live? Welche Belege gibt es?“ |
| Später weitermachen | „Speicher den Stand zu FVK-…“, im neuen Chat „Weiter mit FVK-…“ |
| Internes Wissen anbinden | „Nutze diesen internen Wissenseinstieg: …“ |

Vorgeschlagene Prüfschritte sind noch keine ausgeführten Tests, und einzelne bestandene Fälle sind keine Freigabe: Die entscheidest weiterhin du.

## Stand speichern und Wissen anbinden

„Stand speichern“ legt Umfang, Quellenstand, Entscheidungen, deine Beobachtungen (wörtlich, mit Umgebung und Version) und offene Schritte in `.local/tickets/` ab. Ein neuer Chat setzt damit fort; geänderte Anforderungen oder eine neue Version machen alte Tests nicht wieder gültig. Eine interne Wissensbasis bindest du beim Setup als Datei oder Link an; entscheidende Aussagen prüft der Assistent an den Originalen.

`.local/` wird nicht mit Git geteilt: Notizen und Quellenangaben bleiben auf deinem Rechner, Kollegen richten ihren eigenen Zugang ein. [Details](CONTEXT.md#kontext-erhalten).

## Wenn beim Setup etwas fehlt

- **Jira nicht verbunden:** [Jira verbinden](docs/DEPENDENCIES.md#jira-verbinden). Fragen zu den Specs gehen schon vorher.
- **Rewrite-Repo fehlt:** Nenne den Ordner oder den internen Repo-Link. Ohne Specs kann der Assistent Tickets erklären, aber keinen Spec-Abgleich bestätigen.
- **Zugriff verweigert:** Leserechte intern freischalten lassen. Dieses Repo gewährt keinen Zugang zu Jira oder zum Produktrepo.

## Stand und Grenzen

Pilotphase. Die Regeln werden mit 28 synthetischen Fällen automatisch und blind bewertet; Ergebnisse und offene Nachweise stehen im [Prüfstand](docs/VALIDATION.md). Ein echter PM hat den Ablauf noch nicht von Anfang bis Ende genutzt, und native Tests in Claude und Cursor stehen aus. Die Regeln helfen, garantieren aber keine fehlerfreie Antwort.

## Wie das Paket arbeitet

fvk-powers besteht nur aus Projektanweisungen, ohne eigenen KI-Dienst, Index oder Installation:

- [AGENTS.md](AGENTS.md): Belegmodell, Recherche und Grenzen
- [profiles/pm.md](profiles/pm.md): Antwortform, Prüfsituationen, geführte Abnahme
- [CONTEXT.md](CONTEXT.md): welche Originalquelle zu welcher Frage passt, Speichern und Fortsetzen
- [SETUP.md](SETUP.md): der geführte Einrichtungsdialog

Jira- und Dateizugriff stellt dein Client bereit. Persönliche Angaben bleiben im von Git ausgeschlossenen `.local/`; dieses Repo enthält keine Ticketkopien oder Zugangsdaten.

## Für Maintainer

[![Package checks](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml/badge.svg)](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml)

Paketprüfung (Python 3.11+, nur Standardbibliothek) und Antwortqualität (Codex CLI mit Anmeldung, Ergebnisse unter `.local/evals/`):

```sh
python3 -m unittest discover -s tests -v
python3 tools/check.py
python3 evals/run.py --rules . --label mein-lauf --reps 2
```

[Prüfplan](evals/README.md) · [Prüfstand](docs/VALIDATION.md). `main` ist die PM-Version; die Entwickler-Variante entsteht separat auf [codex/developer](https://github.com/TimoDeg/fvk-powers/tree/codex/developer).

## Lizenz

[MIT](LICENSE), Copyright (c) 2026 Timofey Degtyarev. Die Lizenz gilt für dieses Repo, nicht für Rewrite-Produktquellen, Jira-Inhalte oder verlinkte Materialien.
