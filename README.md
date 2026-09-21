# fvk-powers

Jira-Tickets verstehen, mit den Rewrite-Specs abgleichen, Abnahmen begleiten und Bug-Entwürfe vorbereiten — ein Arbeitsablauf für PMs im KI-Assistenten.

## Starten in drei Schritten

**Zum ersten Mal hier?** [Codex und Git installieren, Jira verbinden](docs/DEPENDENCIES.md#einrichtung-von-anfang-an). Wenn Codex und Git bereits eingerichtet sind, starte direkt mit Schritt 1.

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
| Eine Abnahme durchführen | „Führe mich Schritt für Schritt durch die Abnahme dieses Tickets.“ |
| Eine Abweichung beschreiben | „Mach daraus einen Bug-Entwurf mit Erwartung, Beobachtung und Prüfschritten.“ |
| Eine Verbesserung finden | „Welche Verbesserung wäre sinnvoll und warum?“ |
| Den Release-Stand klären | „Ist das schon live? Welche Belege gibt es dafür?“ |
| Später im neuen Chat weitermachen | „Speicher den Stand zu FVK-…“ und später „Weiter mit FVK-…“ |
| Internes Wissen anbinden | „Nutze diesen internen Wissenseinstieg: …“ |

Bei der geführten Abnahme führst du jeweils einen Prüffall aus und meldest deine Beobachtung zurück. Der Assistent hält fest, was bestanden, abweichend oder noch offen ist, und formuliert bei Bedarf einen Bug-Entwurf im Chat. Ist derselbe Fehler bereits im besprochenen Bug-Ticket erfasst, bereitet er eine Ergänzung dazu vor. Ein Jira-Ticket wird dadurch nicht automatisch erstellt.

[Beispielantworten ansehen](examples/pm.md)

## Wissen und Ticketstand behalten

Eine interne Wissensbasis kannst du beim Setup als Datei oder internen Link anbinden. Der Assistent liest passende Kapitel und prüft entscheidende Aussagen an ihren Originalquellen. PM und IT können dieselbe Wissensbasis verwenden; zusätzliche Suchdienste sind dafür nicht nötig.

Mit „Stand speichern“ hält der Assistent Umfang, Quellenstand, Entscheidungen, tatsächliche Beobachtungen und offene Schritte lokal fest. Ein neuer Chat im selben Checkout kann damit fortsetzen. Geänderte Anforderungen oder eine neue Testversion machen frühere Tests nicht automatisch wieder gültig. Ohne gespeicherte Notiz fehlt der bisherige Verlauf.

**Lokal bedeutet nicht teamweit:** `.local/` wird nicht mit Git übertragen. Kollegen richten ihren eigenen Zugang zur internen Wissensbasis ein. Eine gemeinsame Übergabe braucht einen bestätigten internen Ablageort. [Speichern und Fortsetzen im Detail](CONTEXT.md#kontext-im-gespräch-erhalten).

## Wenn beim Setup etwas fehlt

- **Jira noch nicht verbunden:** Folge der [Anleitung zur Jira-Verbindung](docs/DEPENDENCIES.md#jira-verbinden). Mit erreichbaren Specs kannst du bereits Produktfragen stellen.
- **Rewrite-Repo fehlt:** Nenne den internen Repo-Link oder den lokalen Ordner. Ohne Zugriff auf die Specs kann der Assistent lesbare Tickets erklären, aber keinen Spec-Abgleich bestätigen.
- **Zugriff verweigert:** Lass die benötigte Leseberechtigung intern freischalten. Das öffentliche fvk-powers-Repo gewährt keinen Zugang zu Jira oder zum Produktrepo.

## Was du erwarten kannst

**Stand: Testbranch `codex/persistent-context`, noch nicht bereit für den Merge.** Im vollständigen Kontextlauf bestanden zuletzt 4 von 6 Fällen. Eine bekannte frühere Testumgebung ging beim Speichern verloren; ein ungeklärter Wissenskonflikt wurde eigenmächtig entschieden. Ein echtes Ticket ließ sich über zwei frische Kontexte speichern und fortsetzen. [Ergebnisse und Grenzen](docs/VALIDATION.md#merge-prüfung--21092026-noch-nicht-bestanden).

Der PM-Grundablauf bleibt in Vorbereitung für den Pilot. Die frühere echte Ticketprobe war noch nicht stabil: Preisvergleiche oder die fehlende bestätigte Testumgebung wurden teilweise zu ungenau beschrieben. Menschliche PM-Abnahme, ein vollständiger Abnahmedialog und Prüfungen in weiteren Clients stehen weiterhin aus. [Frühere Modellbewertung vom 17.09.2026](evals/results/2026-09-17-v1.md).

Vor einer Antwort soll der Assistent prüfen, ob die entscheidenden Quellen vollständig gelesen wurden, zum betroffenen Ablauf passen und den angefragten Stand belegen. Fehlende Inhalte bleiben als Lücke sichtbar; ein alter Ticketstatus bestätigt keinen aktuellen Rollout. Diese Regeln unterstützen die Arbeit, garantieren aber keine fehlerfreie Antwort.

Standardmäßig liest und erklärt der Assistent. Änderungen, Nachrichten und Veröffentlichungen brauchen einen ausdrücklichen Auftrag. Persönliche Quellenangaben bleiben lokal im von Git ausgeschlossenen Ordner `.local/`. Dieses Repo enthält keine privaten Ticketkopien oder Zugangsdaten.

## Wie das Paket arbeitet

`fvk-powers` liefert Projektanweisungen für deinen Assistenten. [AGENTS.md](AGENTS.md) steuert die Quellenarbeit, [CONTEXT.md](CONTEXT.md) verweist auf passende Originalquellen, und das [PM-Profil](profiles/pm.md) beschreibt Antworten und Abnahmedialoge. Jira- und Dateizugriff stellt dein Client bereit. Das Paket enthält keinen eigenen KI-Dienst und trainiert kein Modell.

`main` enthält die PM-Version. Die [Entwickler-Variante](https://github.com/TimoDeg/fvk-powers/tree/codex/developer) wird auf `codex/developer` separat weiterentwickelt.

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
