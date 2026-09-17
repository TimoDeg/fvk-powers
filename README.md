# fvk-powers

**Rewrite verstehen. Tickets schärfen. Abnahmen vorbereiten.**

[![Package checks](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml/badge.svg)](https://github.com/TimoDeg/fvk-powers/actions/workflows/check.yml)

Ein Assistent für PMs, der Jira mit den passenden Original-Specs verbindet und verständlich antwortet. Kundenwirkung und fachliche Entscheidungen stehen im Vordergrund. Technische Keywords werden nur verwendet, wenn sie helfen, und kurz erklärt.

> **Stand: Vorbereitung für den PM-Pilot.** Der Quellenzugriff wurde am bestehenden Arbeitsplatz geprüft. Ein frisches PM-Setup und unabhängig bewertete Antworten stehen noch aus. Der grüne Workflow prüft das Paket, nicht die Qualität der KI-Antworten.

## In einem Satz starten

Dieses private Repo lokal klonen, als Projekt in Codex öffnen und im Chat schreiben:

> **Richte fvk-powers für mich ein.**

Der Assistent erklärt den nächsten Schritt, prüft vorhandene Quellen und fragt nur nach fehlenden Angaben. Anmeldung erfolgt im vorgesehenen Dienst; keine Passwörter im Chat. „Setup weiter“ setzt bei der offenen Stelle fort. [So funktioniert der Setup-Dialog](SETUP.md).

Du brauchst einen Assistenten mit Dateizugriff, einen freigegebenen Jira-Lesezugang und Zugriff auf das Rewrite-Repo. Für PM-Fragen ist keine laufende Produktanwendung nötig. [Alle Voraussetzungen und optionalen Werkzeuge](docs/DEPENDENCIES.md).

## Die Pipeline

```mermaid
flowchart LR
    A[Frage oder Ticket] --> B[Jira und Original-Specs]
    B --> C[Passenden Kontext ergänzen]
    C --> D[Anforderungen und Konflikte prüfen]
    D --> E[Verständliche PM-Antwort]
    E --> F[Abnahme, Entscheidung oder Idee]
```

| Du fragst | Du bekommst |
| --- | --- |
| „Was bedeutet dieses Ticket?“ | Fachliches Ziel, Kundenwirkung und wichtige Bedingungen |
| „Passt das zur Spec?“ | Übereinstimmungen, Widersprüche und fehlende Entscheidungen mit Quellen |
| „Was muss ich abnehmen?“ | Konkrete Ausgangslagen, Schritte und erwartete Ergebnisse |
| „Welche Verbesserung wäre sinnvoll?“ | Begründete Ideen, erkennbar getrennt von verbindlichen Anforderungen |
| „Ist das schon live?“ | Den belegbaren Stand und die noch fehlenden Release-/Laufzeitnachweise |

Die [Kontextlandkarte](CONTEXT.md) führt zu fachlichen Beschreibungen, Architekturentscheidungen, passenden Codebereichen und Testquellen. Specs bleiben im Produktrepo gepflegt. Persönliche Skills, private Wissenskopien und Suchindizes sind keine Voraussetzung. Der vollständige Implementierungs- und Deployment-Ablauf ist nicht portiert; [enthaltene und offene Teile](docs/VALIDATION.md).

## Zahlen mit klarer Bedeutung

Momentaufnahme vom **17.09.2026**. Details und Grenzen stehen im [Prüfbericht](docs/VALIDATION.md).

| Kennzahl | Stand | Was sie belegt |
| --- | ---: | --- |
| Regressionstests des Paketprüfers | **12 / 12 bestanden** | Beschädigte Links, private Dateien, fehlende Einstiege und ungültige Eval-Fälle werden erkannt |
| Automatische Paket-Prüfgruppen | **5** | Wiederholbare Offline-Prüfung; aktueller Lauf über das Badge oben |
| Kontext-Einstiege im lokalen Produktrepo | **17 / 17 vorhanden** | Die geprüften Pfade existieren; kein Vollständigkeitsversprechen |
| Live-Quellenchecks Jira + Spec | **1** | Zugriff und begrenzter Abgleich am bestehenden Arbeitsplatz |
| Vorbereitete Antwort-Eval-Fälle | **12** | Entwicklungsset für Fakten, Konflikte, Setup, Sicherheit und Sprache |
| Unabhängig bewertete Modellfälle | **0 / 12** | Antwortqualität noch nicht gemessen |
| Frische PM-Setups vollständig beobachtet | **0** | Pilotabnahme noch offen |
| Zusätzliche Python-/npm-Pakete | **0** | Paketchecker nutzt Standardbibliothek; externe Client- und Quellenzugänge bleiben nötig |

Keine erfundene Erfolgsquote: Vorbereitete Fälle und redaktionelle Beispiele zählen nicht als bestandene KI-Tests. [So messen wir Qualität, Verständlichkeit und Setup-Aufwand](evals/README.md).

## So sollen Antworten aussehen

Die Beispiele sind **erfunden und redaktionell geschrieben**, keine beobachteten Benchmark-Ausgaben. In echten Antworten stehen Links zu den tatsächlich gelesenen Quellen.

### Ein Ticket verstehen

**PM:** „Was sollen die Favoriten können, und was fehlt noch?“

> Kunden sollen bis zu drei Angebote als Favoriten markieren können. Wählen sie ein viertes aus, erscheint laut Beispiel-Spec ein Hinweis; die bisherigen drei bleiben erhalten.
>
> Offen ist, ob die Auswahl nach dem Schließen und erneuten Öffnen der Seite noch vorhanden sein soll. Das sollten wir vor der Abnahme klären. Ob die Funktion schon umgesetzt ist, ist hier nicht geprüft.

### Einen Widerspruch erkennen

**PM:** „Kann ich das Auswahl-Limit so abnehmen?“

> Das Ticket nennt drei Favoriten, die Spec fünf. Damit fehlt für diesen Punkt ein eindeutiges Abnahmekriterium. Klärt zuerst, welches Limit gelten soll. Die widersprüchlichen Angaben allein beweisen noch keinen Fehler in der Anwendung.

<details>
<summary><strong>Abnahme und Verbesserungsidee ansehen</strong></summary>

**PM:** „Was sollte ich testen? Gibt es eine kleine Verbesserung?“

> Wähle zunächst drei Favoriten aus und versuche, ein viertes Angebot hinzuzufügen. Erwartung laut Beispiel-Spec: Ein Hinweis erscheint, die ursprünglichen drei bleiben ausgewählt. Diese Prüfung ist vorgeschlagen, noch nicht ausgeführt.
>
> **Idee:** Ein Zähler wie „2 von 3 ausgewählt“ könnte das Limit früher verständlich machen. Das ist ein zusätzlicher Vorschlag. Prüft vorher, ob Kunden mit dem bisherigen Hinweis bereits zurechtkommen.

</details>

[Weitere Beispiele und Setup-Abnahmefälle](examples/pm.md).

## Prüfen und weiterentwickeln

Für Maintainer, ohne zusätzliche Pakete:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check.py
# Optional: nur lesend gegen den eigenen Produktcheckout
python3 tools/check.py --product-repo ../fvk
```

Die nächsten Schritte sind ein **frisches PM-Setup**, die **12 Antwortfälle** und **drei echte Tickets mit PM-Bewertung**. Setup-Zeit, Rückfragen, fachliche Fehler und Verständlichkeit werden dabei getrennt erfasst. [Prüfplan und Freigabekriterien](evals/README.md).

| Datei | Zweck |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Gemeinsamer Ablauf und Quellenregeln |
| [SETUP.md](SETUP.md) | Geführte Einrichtung im Chat |
| [CONTEXT.md](CONTEXT.md) | Die passende Originalquelle finden und Kontext fortführen |
| [PM-Profil](profiles/pm.md) | Verständliche Antworten, klare Unsicherheit, hilfreiche Ideen |
| [Dependencies](docs/DEPENDENCIES.md) | Nötige Zugänge und optionale Werkzeuge |
| [Prüfbericht](docs/VALIDATION.md) | Ausgeführte Checks, Grenzen und offene Arbeit |
| [Eval-Plan](evals/README.md) | Messdefinitionen und Testfälle |

Standardmäßig arbeitet der Assistent lesend. Jira-Änderungen, Nachrichten an andere, Produktänderungen und Veröffentlichungen brauchen den jeweiligen ausdrücklichen Auftrag. Lokale Quellenangaben und private Belege bleiben unter dem ausgeschlossenen `.local/`; dieses Repo verteilt keine Ticketkopien oder Zugangsdaten.
