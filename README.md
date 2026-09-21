# fvk-powers — Entwickler-Variante

Diese Variante wird auf `codex/developer` separat entwickelt und getestet. `main` bleibt vorerst die PM-Version; eine Zusammenführung erfolgt später. Beide Varianten gehören zum selben Repo. Weitere experimentelle Regeln und die inzwischen durchgeführten historischen Echtproben stehen auf [codex/dev-evidence-checks](https://github.com/TimoDeg/fvk-powers/tree/codex/dev-evidence-checks); deren vollständige fachliche Abnahme ist noch offen.

Tickets analysieren, Code umsetzen, Änderungen reviewen und gezielt testen: der Rewrite-Arbeitsablauf für Entwickler und PMs, die Änderungen mit einem Assistenten umsetzen — unabhängig vom KI-Client.

## Starten in drei Schritten

**Zum ersten Mal hier?** [Assistent und Git einrichten, Jira verbinden](docs/DEPENDENCIES.md#einrichtung-von-anfang-an). Wenn dein Assistent und Git bereits eingerichtet sind, starte direkt mit Schritt 1.

Du brauchst **einen Assistenten mit Datei- und Werkzeugzugriff**, **Git** zum Klonen und für den vollständigen Abgleich Lesezugriff auf **Jira und das Rewrite-Produktrepo**. Die Specs sind die fachlichen Beschreibungen im Produktrepo. Für die Quellenanalyse brauchst du keine laufende Produktanwendung. Für Implementierung und Tests gelten zusätzlich die Voraussetzungen des Produktrepos.

### 1. Repo herunterladen

Im Terminal in dem Ordner ausführen, in dem du das Projekt ablegen möchtest:

```sh
git clone --branch codex/developer https://github.com/TimoDeg/fvk-powers.git
```

### 2. Im Assistenten öffnen

Öffne den heruntergeladenen Ordner **fvk-powers** im Assistenten deiner Wahl:

| Client | Einstieg |
| --- | --- |
| Cursor | Ordner öffnen und Agent verwenden; die Regeln stehen in `AGENTS.md`. |
| Claude Code | Im Projektordner starten; `CLAUDE.md` importiert die gemeinsamen Regeln. |
| Codex | Ordner als Projekt öffnen und einen neuen Chat starten. |
| Orca | Repo öffnen und darin den gewünschten Agenten starten. Es gelten die Einstiegsdateien und Jira-Zugänge dieses Agenten. |
| Claude-App oder anderer Client | Repo-Dateien über den verfügbaren Projekt-/Dateizugriff bereitstellen und den Starttext unten verwenden. Datei- und Jira-Zugriff müssen tatsächlich angeboten werden. |

[Einrichtung je Client und Jira-Zugang](docs/DEPENDENCIES.md). Die Aufnahme in diese Liste ist kein Nachweis eines erfolgreichen Tests in jedem Client.

### 3. Einrichtung starten

Schreibe im Projektchat:

```text
Lies AGENTS.md in diesem Projekt und führe das darin beschriebene Setup aus.
Richte fvk-powers für mich ein.
```

Der Assistent prüft vorhandene Zugänge und führt dich durch fehlende Schritte. Halte einen **Link zu einem Rewrite-Ticket** und den **Ordner oder internen Link zum Rewrite-Produktrepo** bereit. Er fragt danach, wenn die Angaben fehlen. Falls die Jira-Verbindung noch fehlt, hilft er dir beim nächsten Verbindungsschritt. Melde dich im jeweiligen Dienst an; Passwörter gehören nicht in den Chat.

**Unterbrochen?** Schreibe „Setup weiter“. Bereits lokal gespeicherte Angaben werden wiederverwendet.

[Voraussetzungen im Detail](docs/DEPENDENCIES.md) · [Ablauf der geführten Einrichtung](SETUP.md)

## Dein erster Auftrag

Füge einen Ticketlink ein und schreibe zum Beispiel:

> Analysiere dieses Ticket: Welche Akzeptanzkriterien gelten, welche Codepfade sind betroffen und wie lässt sich die Änderung testen?

Der Assistent liest die verfügbaren Quellen und antwortet verständlich, mit passenden technischen Details und Quellenlinks. Fehlende Informationen und Widersprüche werden benannt. Vorgeschlagene Abnahmeschritte sind noch keine ausgeführten Tests.

| Du möchtest … | Frage im Chat |
| --- | --- |
| Ein Ticket verstehen | „Was verlangt das Ticket und wo ist der Ablauf implementiert?“ |
| Anforderungen abgleichen | „Passt das Ticket zur Spec? Was fehlt oder widerspricht sich?“ |
| Eine Änderung umsetzen | „Setze dieses Ticket um und prüfe die betroffenen Fälle.“ |
| Änderungen reviewen | „Prüfe diesen Diff auf Fehler und Regressionen.“ |
| Verhalten testen | „Teste diesen Ablauf anhand der Akzeptanzkriterien.“ |
| Eine PM-Abnahme vorbereiten | „Erkläre es für einen PM und nenne konkrete Abnahmesituationen.“ |
| Den Release-Stand klären | „Ist das schon live? Welche Belege gibt es dafür?“ |

Codearbeit ist der Standard. Du musst dafür keine technischen Lösungsanweisungen formulieren: „Ich bin PM. Beim vierten Favoriten verschwindet die Auswahl. Bitte fix das und erklär mir, was ich testen kann.“ reicht als Auftrag, sobald Produktzugriff und Anforderungen geklärt sind. Der Assistent untersucht den Code, setzt die Änderung um, führt die passenden Tests aus und prüft den Diff. Offene Produktentscheidungen fragt er verständlich nach.

Die Qualitätsanforderungen gelten unabhängig von deiner Rolle. Das zusätzliche [PM-Profil](profiles/pm.md) vereinfacht die Erklärung; es ersetzt weder Entwicklerablauf noch Tests. Commit, Push und Deployment sind eigene Aufträge. Die PM-Version auf `main` bleibt vorerst separat; diese Verbesserung führt die Branches noch nicht zusammen.

## Wenn beim Setup etwas fehlt

- **Jira noch nicht verbunden:** Folge der [Anleitung zur Jira-Verbindung](docs/DEPENDENCIES.md#jira-verbinden). Mit erreichbaren Specs kannst du bereits Produktfragen stellen.
- **Rewrite-Repo fehlt:** Nenne den internen Repo-Link oder den lokalen Ordner. Ohne Zugriff auf die Specs kann der Assistent lesbare Tickets erklären, aber keinen Spec-Abgleich bestätigen.
- **Zugriff verweigert:** Lass die benötigte Leseberechtigung intern freischalten. Das öffentliche fvk-powers-Repo gewährt keinen Zugang zu Jira oder zum Produktrepo.

## Was du erwarten kannst

**Stand: Erste ausführbare Dev-Proben bestanden.** Vier isolierte Codeaufträge in PM-Sprache prüfen Umsetzung mit Regressionstest, lesendes Review, fehlende Browserprüfung und ungeklärte Anforderungen. Sie liefen auf einem kleinen synthetischen Produkt; der vollständige Rewrite-Ablauf und native Erststarts je Client stehen noch aus. Ergebnisse einschließlich Fehlversuchen und Grenzen stehen im [Prüfbericht](docs/VALIDATION.md#codeaufträge-von-pms--21092026). Die PM-Pipeline wird erst nach weiterer Dev-Prüfung verbunden.

Fragen beantwortet der Assistent lesend; Implementierung und Tests führt er auf Auftrag aus. Nachrichten und Veröffentlichungen brauchen einen ausdrücklichen Auftrag zur jeweiligen Aktion. Persönliche Quellenangaben bleiben lokal im von Git ausgeschlossenen Ordner `.local/`. Dieses Repo enthält keine privaten Ticketkopien oder Zugangsdaten.

## Für Maintainer

[![Package checks](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml/badge.svg?branch=codex%2Fdeveloper)](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml)

Paket und Dokumentationslinks prüfen, mit Git und Python 3.11 oder neuer; keine zusätzlichen Python-Pakete nötig. Im Repo-Ordner ausführen:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check.py
```

Die Checks prüfen die Paketstruktur. Sie ersetzen keine Prüfung der Jira-Verbindung, der Antwortqualität oder der Produktumsetzung.

[Arbeitsregeln](AGENTS.md) · [Kontext und Originalquellen](CONTEXT.md) · [Entwicklerablauf](profiles/developer.md) · [Optionales PM-Profil](profiles/pm.md) · [Prüfplan](evals/README.md)

## Lizenz

Dieses Paket steht unter der [MIT-Lizenz](LICENSE). Kopieren, Ändern, Weitergeben und kommerzielle Nutzung sind erlaubt; der Urheber- und Lizenzhinweis müssen in allen Kopien oder wesentlichen Teilen erhalten bleiben. Copyright (c) 2026 Timofey Degtyarev.

Die Lizenz gilt für die Inhalte dieses Repos, nicht für externe Rewrite-Produktquellen, Jira-Inhalte oder andere verlinkte Materialien.
