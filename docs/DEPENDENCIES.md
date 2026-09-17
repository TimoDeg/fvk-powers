# Was benötigt wird

## Für PMs

| Voraussetzung | Wofür? | Prüfung im Chat |
| --- | --- | --- |
| Assistent mit Zugriff auf dieses Repo und dessen Anweisungen | Arbeitsablauf und PM-Profil lesen | `AGENTS.md` und die gerouteten Dateien sind lesbar |
| Freigegebener Jira-Connector und persönliche Leseberechtigung | Tickets und relevante Ergänzungen lesen | Ein konkret genanntes Ticket tatsächlich abrufen |
| Lesezugriff auf das Rewrite-Produktrepo | Original-Specs und bei Bedarf weitere Quellen lesen | Spec-Einstieg und passende Spec öffnen, Stand festhalten |
| Lokaler beschreibbarer, von Git ausgeschlossener Ordner | Einrichtung über den Chat hinaus behalten | `.local/` prüfen; sonst nur im aktuellen Gespräch fortsetzen |

Jira und Specs können einzeln nutzbar sein; nur mit beiden ist ein vollständiger Ticket-Spec-Abgleich möglich. Ein normaler Chat ohne Datei- und Connector-Zugriff erfüllt diese Voraussetzungen nicht. Die Zuverlässigkeit beim Laden der Anweisungen hängt vom Client ab und muss beim Erststart geprüft werden.

## Nur bei entsprechendem Bedarf

| Werkzeug/Zugang | Wann benötigt? | Gehört zum PM-Grundsetup? |
| --- | --- | --- |
| Git | Lokal klonen, Versionen bestimmen, lokale Speicherung vor Veröffentlichung schützen | Beim lokalen Repo-Weg; kein Produkt-Build nötig |
| Freigegebener Spec-Bot-/Slack-Lesezugriff | Aktueller Spec-Status und Zuständigkeit, wenn die Repo-Dokumentation dorthin verweist | Nein; ohne Zugriff diesen Status offenlassen |
| PDF-/Bild-/Confluence-Lesewerkzeuge | Entscheidungsrelevante verlinkte Quellen | Nur bei solchen Quellen; ungelesene Anhänge benennen |
| Browser und erreichbare Testumgebung | Eine tatsächliche UI-Abnahme ausführen | Nein; eine Abnahme planen geht ohne Browser |
| Dateisuche, optional `rg` | Passende Originale auffinden | Der Client kann die Suche bereitstellen |
| QMD, CodeGraph, Graphify | Vorhandene, aktuelle Suchindizes gezielt nutzen | Nein; nicht enthalten und nicht automatisch installiert |

Für reine PM-Fragen keine Node-, PHP-, Composer-, Docker-, Datenbank- oder Produktinstallation verlangen. Die Abhängigkeiten des Produktrepos gelten erst bei entsprechender Entwickler-/Testarbeit.

## Dieses Repo prüfen und pflegen

- `python3 tools/check.py`: Paketprüfung mit Python 3.11 oder neuer und ausschließlich Standardbibliothek. Getestete Versionen stehen im Prüfbericht; 3.11 ist eine deklarierte Mindestversion, kein Beleg einer getesteten Laufzeit.
- `python3 -m unittest discover -s tests -v`: Regressionen der Paketprüfung.
- `python3 tools/check.py --product-repo <pfad>`: zusätzlich lesender Check der Kontext-Einstiege in einem lokalen Produktrepo. Kein Jira-Aufruf, kein Fetch und keine App-Installation.
- Git für lokale Versionsbelege; `gh` ist nur für Maintainer beim Veröffentlichen und Lesen der GitHub-Checks hilfreich.
- GitHub Actions für die spätere automatische Paketprüfung. Die [inaktive Vorlage](ci/check.yml) verwendet eine auf Commit fixierte [offizielle checkout-Action](https://github.com/actions/checkout/releases/tag/v7.0.1), einen bereitgestellten Python-Interpreter und nur lesende Repo-Rechte. Keine Jira-Zugänge, Produktrepo-Zugänge oder Modellschlüssel in CI. Zum Veröffentlichen unter `.github/workflows/` fehlt dem aktuellen GitHub-OAuth-Zugang die `workflow`-Berechtigung. Sie muss über den vorgesehenen GitHub-Anmeldeweg freigegeben werden; kein Token gehört ins Repo.

Es gibt keine zusätzlich zu installierenden Python-/npm-Pakete und keinen eigenen Modell-API-Client. Der Assistent und seine Connectoren bleiben externe Laufzeitvoraussetzungen; „0 Zusatzpakete“ bedeutet nicht „ohne Zugänge nutzbar“.
