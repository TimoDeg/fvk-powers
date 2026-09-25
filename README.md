# fvk-powers

Ein Arbeitsablauf für PMs im KI-Assistenten: Rewrite-Tickets verstehen, mit den Original-Specs abgleichen, den Umfang klären, Abnahmen Schritt für Schritt begleiten und Bug-Entwürfe vorbereiten.

**Stand: Pilot für einen beobachteten Erststart, keine Teamfreigabe.** Die Tests nutzen überwiegend synthetische Tickets. Ein PM hat den Ablauf noch nicht von Anfang bis Ende mit echtem Jira-Zugang genutzt. [Prüfstand und Grenzen](docs/VALIDATION.md).

## Warum

Ein KI-Assistent kann flüssig antworten, obwohl er die entscheidende Stelle nicht gelesen hat. Für PMs ist das gefährlich: Ein falsch übernommenes Limit, ein alter „Done“-Status oder eine erfundene Ursache landen direkt in Abnahme und Planung.

fvk-powers gibt dem Assistenten klare Arbeitsregeln:

- **Nur Gelesenes zählt.** Aussagen stützen sich auf Ticket und Spec, mit Link. Ungelesene Anhänge oder fehlender Zugriff bleiben als Lücke sichtbar.
- **Widersprüche bleiben offen.** Sagt das Ticket drei und die Spec fünf, entscheidet nicht die KI, sondern du erfährst, welche Entscheidung fehlt.
- **Alt ist nicht aktuell.** „Done“ heißt nicht live, ein Test von letzter Woche gilt nicht für die neue Version.
- **Ticketumfang vollständig lesen.** Ein Fall aus den Akzeptanzkriterien gehört zum Ticket, auch wenn die Kurzbeschreibung ihn nicht erwähnt. Fachliche Rückfragen bleiben produktbezogen und kommen einzeln mit konkreten Optionen.
- **Gezielt merken.** Ein belegter Ticketstand, dauerhafte Angaben zur Person und Fachbegriffe werden bei sicherem lokalem Speicher automatisch für den nächsten Chat gesichert.
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

Du brauchst einen **KI-Assistenten mit Datei- und Werkzeugzugriff**, **Git** und für einen vollständigen Abgleich Lesezugriff auf **Jira** und das **Rewrite-Produktrepo**, in dem die Specs liegen. Für PM-Fragen musst du die Produktanwendung, Docker, Node oder PHP nicht installieren. Zum ersten Mal hier? [Assistent und Git einrichten, Jira verbinden](docs/DEPENDENCIES.md#einrichtung-von-anfang-an).

1. **Herunterladen:** Im Terminal in deinem Projektordner ausführen:

   ```sh
   git clone https://github.com/TimoDeg/fvk-powers.git
   ```

2. **Öffnen:** Den Ordner `fvk-powers` im Assistenten als Projekt öffnen. Codex nutzt `AGENTS.md`, Claude Code lädt die Regeln über `CLAUDE.md`. Bei Claude Desktop, Cursor und anderen Clients müssen Datei-, Regel- und Jira-Zugriff im jeweiligen Projekt geprüft werden; ein vollständiger Erststart ist dort noch nicht nachgewiesen.
3. **Einrichten:** Im Projektchat schreiben: „Richte fvk-powers für mich ein.“ Halte einen **Rewrite-Ticketlink** und den **Ordner oder internen Link des Rewrite-Repos** bereit. Der Assistent prüft, was schon geht, und führt dich durch den Rest. Unterbrochen? „Setup weiter“.

Passwörter und Tokens gehören nie in den Chat; die Anmeldung läuft im jeweiligen Dienst.

Die übliche lokale Struktur ist `fvk-powers/` neben `fvk/`; `fvk-infrastructure/` ist nur für Fragen zum Deployment nötig. Ein installierter Jira-Connector oder ein vorhandener Repo-Ordner allein zählt noch nicht als geprüfter Zugriff. [Geführtes Setup](SETUP.md).

## Was du fragen kannst

| Du möchtest … | Frage im Chat |
| --- | --- |
| Ein Ticket verstehen | „Erkläre mir dieses Ticket: Was ändert sich für Kunden?“ |
| Anforderungen abgleichen | „Passt das Ticket zur Spec? Was fehlt oder widerspricht sich?“ |
| Umfang klären | „Gehört mein beobachteter Fehler zu diesem Ticket?“ |
| Eine Abnahme vorbereiten | „Welche konkreten Situationen sollte ich prüfen?“ |
| Eine Abnahme durchführen | „Führe mich Schritt für Schritt durch die Abnahme von FVK-…“ |
| Eine Abweichung festhalten | „In Vorschau A verschwanden nach dem vierten Favoriten alle drei. Mach daraus einen Bug-Entwurf.“ |
| Den Release-Stand klären | „Ist das schon live? Welche Belege gibt es?“ |
| Später weitermachen | „Weiter mit FVK-…“ – auch in einem neuen Chat desselben Checkouts |
| Gespeichertes korrigieren | „Vergiss meinen Bereich Checkout.“ |
| Internes Wissen anbinden | „Nutze diesen internen Wissenseinstieg: …“ |

Bei einer geführten Abnahme bedienst **du** die Anwendung und meldest, was du gesehen hast. Der Assistent kennzeichnet Vorschläge als noch nicht ausgeführt und hält bestandene, abweichende und offene Fälle getrennt. Er fragt fachlich, möglichst mit konkreten Optionen und nur eine Frage auf einmal. Einzelne bestandene Fälle sind keine Freigabe: Die entscheidest weiterhin du.

## Lokales Gedächtnis und internes Wissen

Nach dem ersten belegten Ticket-Spec-Abgleich legt der Assistent eine Notiz unter `.local/tickets/<TICKET>.md` an. Er hält darin Umfang, Quellenstand, Entscheidungen, offene Schritte und deine Beobachtungen wörtlich mit Umgebung und damaligem Stand fest. Dauerhafte Angaben wie Name, Bereich und „immer kurz“ landen gezielt im Profil; belegte Fachbegriffe mit Originalquelle im Glossar. Jede Speicherung meldet er in einer letzten Zeile „Gemerkt: …“. Ein einmaliges „diesmal ausführlich“ bleibt einmalig; „Vergiss …“ entfernt den benannten Eintrag.

Im neuen Chat liest der Assistent das Profil und **nur die Notiz zum genannten Ticket**, nicht pauschal alle Dateien unter `.local/`. Geänderte Anforderungen oder eine neue Version machen alte Tests nicht automatisch wieder gültig. Eine interne Wissensbasis kannst du beim Setup als Datei oder internen Link anbinden; entscheidende Aussagen werden an Originalquellen geprüft.

`.local/` wird nur beschrieben, wenn der Ordner sicher von Git ausgeschlossen und die Zieldatei nicht getrackt ist. Dort gehören **keine** Passwörter, Tokens oder Ticketkopien hinein. Notizen gelten nur für diesen Checkout und werden nicht mit Git an Kollegen übertragen. [Regeln für Ticketnotizen, Profil und Glossar](CONTEXT.md#lokales-gedächtnis).

## Wenn beim Setup etwas fehlt

- **Jira nicht verbunden:** [Jira verbinden](docs/DEPENDENCIES.md#jira-verbinden). Fragen zu den Specs gehen schon vorher.
- **Rewrite-Repo fehlt:** Nenne den Ordner oder den internen Repo-Link. Ohne Specs kann der Assistent Tickets erklären, aber keinen Spec-Abgleich bestätigen.
- **Zugriff verweigert:** Leserechte intern freischalten lassen. Dieses Repo gewährt keinen Zugang zu Jira oder zum Produktrepo.

## Grenze bei Codearbeit

**Das Setup legt keinen Branch an und ändert keinen Produktcode**, auch wenn das Ticket oder derselbe Setup-Prompt eine Umsetzung verlangt. Die PM-Version auf `main` behandelt einen späteren ausdrücklichen Codeauftrag gesondert. Dieser Übergang ist noch **nicht** als zuverlässiger PM-Ablauf bestätigt: In der Setup-Matrix wurde einmal ein Branch angelegt, ohne die fehlenden Produktregeln zu benennen. Für Codearbeit wird die [Entwickler-Variante](https://github.com/TimoDeg/fvk-powers/tree/codex/developer) separat entwickelt; auch sie ist noch keine vollständige Rewrite-Abnahme. [Befund](docs/VALIDATION.md#bekannte-schwächen).

Jira-Kommentare, neue Tickets, Nachrichten, Commits, Pushes und Deployments brauchen jeweils einen ausdrücklichen Auftrag. Grüne Paketchecks oder einzelne bestandene Prüffälle sind keine Produktfreigabe.

## Prüfstand und Grenzen

| Prüfung auf dem veröffentlichten PM-Stand | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Setup in frischen Wegwerf-Umgebungen | **19/20** Grenzfälle | Synthetisches Rewrite-Repo und Jira-Stub, je Fall ein Lauf; der Code-Folgefall scheiterte. |
| Antwort-Eval | **73/84** gegenüber 74/84 am Vortag; gemeinsame 28 Fälle **52/56** in beiden Ständen | Zwei Wiederholungen pro Fall, Codex bewertet Codex; keine menschliche PM-Abnahme. |
| Gedächtnis-Szenarien | **4/4**; Kontextkette anschließend **11/12** | `context-drift` bleibt offen: Nach Versionswechsel wird eine Prüfung nicht zuverlässig erneut als offen genannt. |
| Aufwand | Rund **19 % mehr Eingabe-Kontext** pro Antwort | Gemessener Mehraufwand der Gedächtnis-Regeln, kein allgemeiner Kostenwert. |

Die Setup-Matrix prüfte unter anderem fehlendes Jira, ein verschobenes oder falsches Produktrepo, Fortsetzung im neuen Chat, nicht ignorierten lokalen Speicher und Anweisungen in einem Ticket. `scenario-draft`, `profile-detail` und `profile-secret` bestehen noch nicht zuverlässig. Die Zahlen gelten nur für diese synthetischen Läufe; daraus folgt keine Zuverlässigkeitsquote für echte PM-Arbeit. Ein vollständiger PM-Erststart, aktuelle native Prüfreihen in Claude Code, Claude Desktop und Cursor sowie drei echte, fachlich bewertete Tickets stehen aus. [Vollständiger Prüfstand](docs/VALIDATION.md) · [Methodik](evals/README.md) · [Ausbauplan](docs/ROADMAP.md).

## Wie das Paket arbeitet

fvk-powers ist ein Regelpaket ohne eigenen KI-Dienst oder Index:

- [AGENTS.md](AGENTS.md): Belegmodell, Recherche und Grenzen
- [profiles/pm.md](profiles/pm.md): Antwortform, Prüfsituationen, geführte Abnahme
- [CONTEXT.md](CONTEXT.md): welche Originalquelle zu welcher Frage passt, Speichern und Fortsetzen
- [SETUP.md](SETUP.md): der geführte Einrichtungsdialog
- [SCENARIOS.md](SCENARIOS.md): optionale Entwürfe für ausführbare Prüfszenarien

Jira- und Dateizugriff stellt dein Client bereit. Dieses Repo enthält keine privaten Ticketkopien oder Zugangsdaten.

## Für Maintainer

[![Package checks](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml/badge.svg)](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml)

Paket und Dokumentationslinks mit Python 3.11+ ohne Zusatzpakete prüfen; für die Modell-Evals ist eine angemeldete Codex CLI nötig:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check.py
python3 evals/setup_run.py
python3 evals/run.py --rules . --label mein-lauf --reps 2
```

Die ersten beiden Befehle prüfen das Paket, die letzten beiden führen Modellfälle aus. Rohantworten und Toolspuren bleiben lokal unter `.local/evals/`. [Arbeitsregeln](AGENTS.md) · [Prüfplan](evals/README.md). `main` ist die PM-Version; die Entwickler-Variante entsteht separat auf [codex/developer](https://github.com/TimoDeg/fvk-powers/tree/codex/developer).

## Lizenz

[MIT](LICENSE), Copyright (c) 2026 Timofey Degtyarev. Die Lizenz gilt für dieses Repo, nicht für Rewrite-Produktquellen, Jira-Inhalte oder verlinkte Materialien.
