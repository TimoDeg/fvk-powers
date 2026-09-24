# Ausbauplan — Stand 23.09.2026

Ausgangspunkt ist der Pilotstand auf `optimize/pm-rules`: ein Belegmodell, blinder A/B-Eval-Lauf, 47/56 bestandene Fälle mit Claude. Dieser Plan bündelt das Feedback vom 23.09. in sieben Arbeitspakete. Jedes Paket nennt, was gebaut wird, wie es geprüft wird und wovon es abhängt. Zwei Regeln gelten für alle: Jede neue Fähigkeit läuft durch das Belegmodell, und nichts, was nach außen wirkt (Jira, Slack, Bestellungen), passiert ohne ausdrücklichen Auftrag.

| # | Paket | Wert für PMs | Aufwand | Phase |
| --- | --- | --- | --- | --- |
| A | Setup mit fester Struktur und Repo-Landkarte | Jeder weiß, wo was liegt | S | 1 |
| B | Scope-Karte, Stopp-Hinweis, Dev-Frage | Weniger Blindflug, bessere Fragen an Devs | M | 1 |
| C | Personalisierung | Antworten passen zur Person | S | 1 |
| D | Frische Testumgebung | Setup wirklich von null prüfbar | S–M | 1 |
| E | Glossar: Fachbegriffe automatisch sichern | Gemeinsame Sprache wächst mit | M | 2 |
| F | Abnahme mit Scenario-Engine und Testkonto | Beobachtungen aus echtem Browserlauf | M–L | 2–3 |
| G | Slack-Bot | Zugang ohne eigenes Setup, Dev-Fragen im Kanal | L | 3 |

Phase 1 ist in etwa zwei Wochen zu zweit machbar; sie enthält alles, was der beobachtete PM-Erststart braucht.

**Stand 24.09.2026** (Belege im [Prüfstand](VALIDATION.md)):

| # | Stand |
| --- | --- |
| A | Gebaut: `tools/doctor.py`, festes `sources.md`-Schema samt Akzeptanzkriterien-Feld, Repo-Landkarte. Isolierter Codex-Erststart ok. |
| B | Gebaut: „Umfang und Dev-Frage“ im PM-Profil, drei Eval-Fälle 2/2. Dev-Bewertung an echten Tickets offen. |
| C | Gebaut: Profil mit zwei Setup-Fragen nach dem ersten Abgleich. `profile-detail` und `profile-secret` je 1/2. |
| D | D2 und D3 (ohne Container) gebaut: `fresh_env.py`, realistischer Jira-Stub, leeres HOME. D1 mit echtem PM offen. |
| E | Gebaut, Eval 1/2 bzw. 2/2. Zehn-Ticket-Durchsicht offen. |
| F | Stufe 1 als Regel (`SCENARIOS.md`), Eval `scenario-draft` 0/2. Stufe 2 und echte Tickets offen. |
| G | Nicht begonnen; hängt an den Entscheidungen unten. |

## A. Setup mit fester Struktur und Repo-Landkarte

**Problem:** Heute rät der Assistent den Produktpfad (`../fvk`) und der PM weiß nicht, welcher Ordner wofür da ist.

**Bauen**

- Eine feste Arbeitsstruktur unter einem frei wählbaren Root, Standard `~/fvk-work/`:

  ```text
  fvk-work/
  ├── fvk-powers/          # dieses Paket, Projektordner im Assistenten
  ├── fvk/                 # Rewrite-Monorepo: Specs, Domains, Entscheidungen, Code
  └── fvk-infrastructure/  # optional: Jenkins, Deployment, „ist es live?“
  ```

- `.local/sources.md` bekommt ein festes Schema statt Freitext: Root, je Repo Pfad und geprüfter Git-Stand, Jira-Site, Wissenseinstieg, Profil. Der Assistent liest es bei jedem Start, kein Raten mehr.
- Eine Repo-Landkarte in `CONTEXT.md`: welches Repo welche Frage beantwortet (Specs und Fachlogik im Rewrite-Repo, Rollout in der Infrastruktur, Anforderungen in Jira). Ergänzt die bestehende Quellenlandkarte um die Ebene „welches Repo“.
- `tools/doctor.py` (nur Standardbibliothek): prüft Ordnerstruktur, Git-Stand jedes Repos, `.local/` ignoriert und nicht getrackt, Spec-Einstieg lesbar. Gibt eine Zeile pro Punkt aus. Der Assistent führt es im Setup aus und übersetzt das Ergebnis für den PM.

**Prüfen:** Setup-Fälle im Eval erweitern (falscher Root, fehlendes Infrastruktur-Repo, Repo ohne Commit). Danach der Erststart aus Paket D.

## B. Scope-Karte, Stopp-Hinweis und Dev-Frage

**Problem:** PMs merken nicht, wann eine Frage den Ticketrahmen verlässt oder nur ein Entwickler sie beantworten kann. Die KI antwortet dann trotzdem.

**Bauen**

- **Scope-Karte** beim ersten Ticketkontakt, gespeichert in der Ticketnotiz: *Im Umfang* (laut Ticket und Spec), *Nicht im Umfang* (angrenzende Features, Ursachenanalyse im Code, Rollout), *Unklar* (braucht Entscheidung). Kurz, drei Listen, mit Quellen.
- **Stopp-Hinweis:** Verlässt eine Frage den Umfang, antwortet der Assistent zuerst mit einer markierten Zeile („Außerhalb des Tickets: …“), nennt warum, und bietet den passenden Weg: anderes Ticket, Klärung mit dem PO, oder eine Dev-Frage. Danach beantwortet er, was innerhalb des Umfangs belegbar ist. Kein stilles Weiterreden.
- **Dev-Frage als Entwurf.** Auslöser ist Prinzip 1 und 3 des Belegmodells: Die Lücke lässt sich nur mit Code- oder Laufzeitbelegen schließen, die der PM nicht hat. Der Assistent erzeugt dann einen Entwurf in fester Form:

  ```text
  Ticket: FVK-… · Bereich: Vergleichsseite
  Beobachtung: <was, wo, wann, laut wem>
  Erwartung laut Spec: <Satz + Link>
  Frage: <eine konkrete, mit Ja/Nein oder Auswahl beantwortbare Frage>
  Warum ich das nicht selbst klären kann: <fehlender Beleg>
  Antwort bitte als: <Bestätigung / Codeverweis / Reproduktionsstand>
  Dringlichkeit: <blockiert Abnahme / vor Release / später>
  ```

  Der Entwurf wird nur auf Auftrag versendet (Paket G) oder kopiert. Er landet in der Ticketnotiz unter „Offen“.

**Regeln:** Neue Sektion „Scope und Dev-Frage“ in `profiles/pm.md`; Trigger im Belegmodell in `AGENTS.md` (eine Zeile). **Prüfen:** Drei neue Eval-Fälle: Frage außerhalb des Umfangs, Frage die nur ein Dev beantworten kann, Scope-Karte aus Ticket plus Spec mit einem Unklar-Punkt. Danach an zwei echten Tickets von einem Dev bewerten lassen: Ist die Frage so gestellt, dass er sie in zwei Minuten beantworten kann?

## C. Personalisierung

**Bauen**

- `.local/profile.md` mit wenigen Feldern: Anrede und Name, Rolle (PM, Dev, QA), Bereiche (Journey, Kundenbereich, PIM …), Detailgrad (kurz oder ausführlich), bevorzugte Testumgebung, Testkonto-Alias (ohne Passwort), Sprache.
- Das Setup fragt höchstens zwei Dinge (Name, Bereiche); der Rest hat Standardwerte. „Merk dir: ich will immer die Prüfschritte sehen“ aktualisiert das Profil.
- `profiles/pm.md` liest das Profil: Detailgrad steuert die Antwortform, Bereiche steuern, welche Specs zuerst gesucht werden, die Testumgebung füllt Prüfsituationen vor.
- Grenze: Profil enthält niemals Zugangsdaten, und es überschreibt keine Belegregeln.

**Prüfen:** Zwei Eval-Fälle mit derselben Frage und zwei Profilen; Antworten müssen sich in Länge und Vorbelegung unterscheiden, nicht in den Fakten.

## D. Frische Testumgebung

Drei Wege, für drei Zwecke. Alle brauchen kein neues Werkzeug.

**D1 · Eigener macOS-Benutzer (für den beobachteten Erststart).** Am realistischsten, weil nichts von deinem Rechner durchsickert: keine Skills, keine Anmeldungen, keine gespeicherten Pfade.

```sh
sudo sysadminctl -addUser pmtest -fullName "PM Test" -password -
```

Dann über den schnellen Benutzerwechsel anmelden, Codex oder Claude Code nach `docs/DEPENDENCIES.md` installieren, README befolgen, Bildschirm aufnehmen. Danach den Benutzer löschen (`sysadminctl -deleteUser pmtest`). Aufwand: ein Nachmittag, zu zweit.

**D2 · Wegwerf-HOME für jede Regeländerung (existiert).** `evals/run.py` startet jeden Fall in einem leeren Ordner mit `--ignore-user-config` bzw. `--setting-sources project`. Das prüft die Regeln, nicht die Installation.

**D3 · Container mit Jira-Stub (für wiederholbare Setup-Tests).** `node:22` mit Codex- oder Claude-CLI, `fvk-powers` und eine lesbare Kopie der Specs eingehängt, Anmeldung per Gerätecode. Weil die Atlassian-OAuth-Anmeldung im Container keinen Browser hat, liefert ein kleiner lokaler MCP-Stub drei synthetische Tickets. Damit wird der komplette Setup-Dialog bis zum ersten Ticket-Spec-Abgleich offline prüfbar. Aufwand M; der Stub ist auch die Grundlage für neue Setup-Eval-Fälle.

Empfehlung: D1 einmal jetzt mit dem Kollegen als erstem PM, D2 weiter bei jeder Änderung, D3 wenn mehr als zwei Leute das Setup pflegen.

## E. Glossar: Fachbegriffe automatisch sichern

**Problem:** Begriffe wie Kulanz, Tarifdetails oder Wiedervorlage werden pro Gespräch neu erklärt, und Definitionen weichen zwischen Spec, Meeting und Jira ab.

**Bauen**

- Beim Lesen von Spec, Ticket oder Wissensbasis hält der Assistent neue Fachbegriffe fest: Begriff, Definition laut Quelle, Quelle mit Anker, Datum, Bereich. Ziel: `.local/glossary.md`, eine Tabelle, ein Eintrag pro Begriff und Quelle.
- Das ist die einzige Schreibaktion ohne Einzelauftrag, weil sie lokal, ignoriert und rein additiv ist. Die Antwort nennt sie in einer Zeile („2 Begriffe ins Glossar aufgenommen“).
- Widersprüchliche Definitionen stehen nebeneinander mit beiden Quellen, nach Prinzip 4. Kein Gewinner ohne Entscheidung.
- Beim nächsten Gespräch liest der Assistent das Glossar vor der Spec-Suche; ein Begriff mit bekannter Quelle spart die Suche.
- `docs/domains/` im Rewrite-Repo bleibt die primäre Quelle; das Glossar ist der Index darauf. Auf Auftrag exportiert der Assistent Einträge als Vorschlag für die interne Wissensbasis.

**Prüfen:** Drei Eval-Fälle: neuer Begriff wird gesichert, widersprüchliche Definition bleibt doppelt, bekannter Begriff wird ohne neue Suche wiederverwendet. Zusätzlich: Glossar nach zehn echten Tickets von einem PM durchsehen lassen.

## F. Abnahme mit Scenario-Engine und Testkonto

**Grundlage:** Der Journey-Adapter der `@fvk/e2e`-Engine unter `deployables/frontend-journey/e2e-scenario-engine/` kann heute schon: typisierte Szenario-Dokumente, Umgebungen `local`/`test`/`preview`/`live`, ein Login pro Lauf, Fake-Order-Schutz vor jeder Bestellung, Manifest mit Preisen, Links und Fehlerbündeln, `--plan-only` ohne Browser und ohne Zugangsdaten. Wir bauen keinen Playwright-Code, wir nutzen die Engine.

**Stufe 1 · Prüfplan als Szenario (Phase 2).** Der Assistent übersetzt Akzeptanzkriterien in ein Szenario-Dokument nach `schema/scenario.schema.json` und validiert es mit `npm run scenario -- --plan-only`. Der PM sieht den aufgelösten Plan: Eingaben, Auswahl, Erwartung. Das ersetzt die Prosa-Prüfsituation durch etwas Ausführbares, braucht aber noch kein Konto.

**Stufe 2 · Lauf auf `test` oder `preview` mit eigenem Testkonto (Phase 3).** Jeder PM legt sich ein eigenes Testkonto an; die Engine erkennt Testbestellungen nur über die CHECK24-Plus-Adresse oder die Namenskonvention „Max … Pecu“, also gilt das als Konvention für PM-Konten. Zugangsdaten stehen ausschließlich in der `.env.local` der Engine, nie im Chat, nie in einer Notiz. Der Assistent startet einen Lauf nur auf ausdrücklichen Auftrag, liest danach `manifest.json` und die Fehlerbündel und berichtet Beobachtungen mit Herkunft „Engine-Lauf <run-id>“. Was das Manifest nicht zeigt, bleibt offen.

**Harte Grenzen:** `--allow-live-convert` und Live-Bestellungen sind im PM-Ablauf verboten; `mode: convert` nur auf `test`/`preview`. Ein grüner Lauf ist eine Beobachtung, keine Freigabe.

**Voraussetzungen:** Node, `npm install` und `npx playwright install chromium` in dem Paket. Das widerspricht „PM braucht keine Entwicklerumgebung“, deshalb ist das ein optionales Modul „Abnahme mit Browser“ mit eigenem Setup-Schritt, nicht Teil des Grundsetups.

**Prüfen:** Stufe 1: Für drei echte Tickets Szenarien erzeugen, `--plan-only` muss ohne Korrektur durchlaufen, ein Dev prüft die Plausibilität. Stufe 2: ein Dry-Run auf `test`, Manifest gegen die manuelle PM-Beobachtung desselben Falls vergleichen.

## G. Slack-Bot

Zwei Funktionen, eine Reihenfolge:

1. **Dev-Frage im Kanal (zuerst).** Der PM bestätigt einen Dev-Frage-Entwurf aus Paket B, der Bot postet ihn in den Dev-Kanal, verfolgt den Thread und legt die Antwort mit Link in die Ticketnotiz. Kleiner Umfang, klarer Nutzen, klare Freigabe pro Nachricht.
2. **Fragen im PM-Kanal beantworten (danach).** Derselbe Regelsatz, lesend auf Jira und Specs, Antworten im Thread.

**Technik:** Slack-App (Bolt) plus Agent SDK auf einem internen Host, Projektregeln aus diesem Repo als Systemkontext. **Offene Fragen vorab:** Jira-Rechte laufen dann über ein Bot-Konto statt über den einzelnen PM; ein Bot darf nur lesen, was jeder im Kanal lesen dürfte. Wo läuft der Host, wer verwaltet die Secrets, wie wird der Kanal begrenzt? Ohne Antworten darauf startet G nicht.

**Prüfen:** Testkanal mit zwei Personen, zehn Dev-Fragen, Bewertung durch die Devs: beantwortbar ohne Rückfrage?

## Querschnitt: Evals und Qualität

- Jedes Paket bringt seine Eval-Fälle mit; Ziel sind etwa 40 Fälle plus ein kleiner Holdout aus echten, anonymisierten Fragen, der nicht zum Schärfen benutzt wird.
- `evals/run.py` läuft vor jedem Merge mit beiden Regelständen; das Ergebnis landet in `docs/VALIDATION.md`.
- Menschliche Bewertung: eine einfache Tabelle (Fall, verständlich 1–5, richtig ja/nein, hilfreich ja/nein) für die drei echten Tickets und den Erststart.

## Entscheidungen, die vorher fallen müssen

1. Bleibt das Repo öffentlich? Es beschreibt interne Produktstruktur. Alternativ internes Git.
2. Konvention für PM-Testkonten (Plus-Adresse oder Pecu-Name) und wer sie anlegt.
3. Ablageort für ein teamweites Glossar und für Übergaben (Wissensbasis, Confluence, Repo).
4. Host und Verantwortliche für den Slack-Bot.

## Nächste zwei Wochen

| Wann | Was | Wer |
| --- | --- | --- |
| Woche 1 | Paket A und C bauen, Eval-Fälle ergänzen, A/B-Lauf | Timofey |
| Woche 1 | Entscheidungen 1–2 klären | beide |
| Woche 2 | Paket B bauen, zwei Dev-Fragen von einem Dev bewerten lassen | Timofey + Kollege |
| Woche 2 | D1: Kollege als erster PM, beobachteter Erststart mit drei echten Tickets | beide |
