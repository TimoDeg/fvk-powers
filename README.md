# fvk-powers

Jira-Tickets verstehen, mit den Rewrite-Specs abgleichen und Abnahmen vorbereiten — ein Arbeitsablauf für PMs im KI-Assistenten.

## Starten in drei Schritten

Du brauchst **Codex oder einen vergleichbaren Assistenten mit Dateizugriff**, **Git** zum Klonen und für den vollständigen Abgleich Lesezugriff auf **Jira und das Rewrite-Produktrepo**. Die Specs sind die fachlichen Beschreibungen im Produktrepo. Eine laufende Produktanwendung brauchst du nicht.

### 1. Repo herunterladen

Im Terminal in dem Ordner ausführen, in dem du das Projekt ablegen möchtest:

```sh
git clone https://github.com/TimoDeg/fvk-powers.git
```

### 2. Im Assistenten öffnen

Öffne den heruntergeladenen Ordner **fvk-powers** als Projekt in Codex. Bei anderen Assistenten muss der Client die Projektanweisungen aus `AGENTS.md` lesen können.

### 3. Einrichtung starten

Schreibe im Projektchat:

```text
Richte fvk-powers für mich ein.
```

Der Assistent prüft vorhandene Zugänge und führt dich durch fehlende Schritte. Halte einen **Link zu einem Rewrite-Ticket** und den **Ordner oder internen Link zum Rewrite-Produktrepo** bereit. Er fragt danach, wenn die Angaben fehlen. Falls die Jira-Verbindung noch fehlt, hilft er dir beim nächsten Verbindungsschritt. Melde dich im jeweiligen Dienst an; Passwörter gehören nicht in den Chat.

**Unterbrochen?** Schreibe „Setup weiter“. Bereits lokal gespeicherte Angaben werden wiederverwendet.

[Voraussetzungen im Detail](docs/DEPENDENCIES.md) · [Ablauf der geführten Einrichtung](SETUP.md)

## Deine erste Frage

Füge einen Ticketlink ein und schreibe zum Beispiel:

> Erkläre mir dieses Ticket: Was soll sich für Kunden ändern und was muss ich abnehmen?

Der Assistent liest die verfügbaren Quellen und antwortet kurz, verständlich und mit Quellenlinks. Fehlende Informationen und Widersprüche werden benannt. Vorgeschlagene Abnahmeschritte sind noch keine ausgeführten Tests.

| Du möchtest … | Frage im Chat |
| --- | --- |
| Ein Ticket verstehen | „Was soll sich für Kunden ändern?“ |
| Anforderungen abgleichen | „Passt das Ticket zur Spec? Was fehlt oder widerspricht sich?“ |
| Eine Abnahme vorbereiten | „Welche konkreten Situationen sollte ich prüfen?“ |
| Eine Verbesserung finden | „Welche Verbesserung wäre sinnvoll und warum?“ |
| Den Release-Stand klären | „Ist das schon live? Welche Belege gibt es dafür?“ |

[Beispielantworten ansehen](examples/pm.md)

## Wenn beim Setup etwas fehlt

- **Jira noch nicht verbunden:** Verbinde den freigegebenen Jira-/Atlassian-Zugang in deinem Assistenten. Mit erreichbaren Specs kannst du bereits Produktfragen stellen.
- **Rewrite-Repo fehlt:** Nenne den internen Repo-Link oder den lokalen Ordner. Ohne Zugriff auf die Specs kann der Assistent lesbare Tickets erklären, aber keinen Spec-Abgleich bestätigen.
- **Zugriff verweigert:** Lass die benötigte Leseberechtigung intern freischalten. Das öffentliche fvk-powers-Repo gewährt keinen Zugang zu Jira oder zum Produktrepo.

## Was du erwarten kannst

**Stand: Vorbereitung für den PM-Pilot.** Paketprüfungen und begrenzte Modelltests wurden durchgeführt; die menschliche PM-Abnahme steht noch aus. Ergebnisse und Grenzen stehen im [Prüfbericht](docs/VALIDATION.md), die [Modelltest-Ergebnisse](evals/results/2026-09-17-v1.md) sind separat dokumentiert.

Standardmäßig liest und erklärt der Assistent. Änderungen, Nachrichten und Veröffentlichungen brauchen einen ausdrücklichen Auftrag. Persönliche Quellenangaben bleiben lokal im von Git ausgeschlossenen Ordner `.local/`. Dieses Repo enthält keine privaten Ticketkopien oder Zugangsdaten.

## Für Maintainer

[![Package checks](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml/badge.svg)](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml)

Paket und Dokumentationslinks prüfen, mit Git und Python 3.11 oder neuer; keine zusätzlichen Python-Pakete nötig. Im Repo-Ordner ausführen:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check.py
```

Die Checks prüfen die Paketstruktur. Sie ersetzen keine Prüfung der Jira-Verbindung, der Antwortqualität oder der Produktumsetzung.

[Arbeitsregeln](AGENTS.md) · [Kontext und Originalquellen](CONTEXT.md) · [PM-Ausgabeprofil](profiles/pm.md) · [Prüfplan](evals/README.md)

## Lizenz

Dieses Paket steht unter der [MIT-Lizenz](LICENSE). Kopieren, Ändern, Weitergeben und kommerzielle Nutzung sind erlaubt; der Urheber- und Lizenzhinweis müssen in allen Kopien oder wesentlichen Teilen erhalten bleiben. Copyright (c) 2026 Timofey Degtyarev.

Die Lizenz gilt für die Inhalte dieses Repos, nicht für externe Rewrite-Produktquellen, Jira-Inhalte oder andere verlinkte Materialien.
