# Was benötigt wird

Du brauchst **einen freigegebenen KI-Assistenten mit Datei- und Werkzeugzugriff**, Zugang zu Jira und den Rewrite-Specs sowie beim lokalen Klonen Git. Cursor, Claude Code, Codex und andere passende Clients verwenden dieselbe Pipeline. Ein ChatGPT-Konto ist nur für entsprechende OpenAI-Anmeldewege relevant, keine allgemeine Voraussetzung. Python brauchst du nur für die Paketchecks als Maintainer.

## Einrichtung von Anfang an

Verwende deinen vorhandenen Assistenten. Falls er noch fehlt, installiere den von eurem Team freigegebenen Client nach dessen offizieller Anleitung. Konto und Lizenz richten sich nach diesem Client. Auf Firmenrechnern hilft das Softwareportal bzw. die IT, wenn Installation oder Verbindung gesperrt sind.

### Assistent wählen und Regeln laden

| Client | Einrichtung und Projektregeln |
| --- | --- |
| Cursor | [Offizielle Anleitung](https://cursor.com/docs). Öffne den Repo-Ordner im Agent-Modus. Cursor unterstützt `AGENTS.md` als Projektregel: [Regeldokumentation](https://cursor.com/docs/rules). |
| Claude Code | [Offizieller Einstieg](https://code.claude.com/docs/en/quickstart). Starte Claude Code im Repo-Ordner. Die mitgelieferte `CLAUDE.md` importiert `AGENTS.md`: [Import-Dokumentation](https://code.claude.com/docs/en/memory). |
| Codex | [Offizielle App-Anleitung](https://learn.chatgpt.com/docs/app). Füge den Repo-Ordner als lokales Projekt hinzu und starte darin Codex; siehe [Projektanleitung](https://learn.chatgpt.com/docs/projects). Ein bereits eingerichteter CLI-Client ist ebenfalls nutzbar. |
| Claude-App | Nutze einen Modus mit Zugriff auf die benötigten Projektdateien und einen freigegebenen Jira-Connector. Automatisches Laden der Claude-Code-Regeln nicht voraussetzen; verwende den expliziten Starttext unten. |
| Orca (`stablyai/orca`) | [Orca](https://github.com/stablyai/orca) startet andere CLI-Agenten in eigenen Arbeitsordnern. Öffne fvk-powers in Orca und starte den gewünschten Agenten darin. Für Claude Code gilt `CLAUDE.md`, für Codex bzw. Cursor deren `AGENTS.md`-Einstieg. [Unterstützte Agenten](https://www.onorca.dev/docs/agents/supported) |
| Weitere Clients | Stelle Projekt-/Dateizugriff her und verwende den Starttext unten. Automatische Regelerkennung erst als vorhanden behandeln, wenn sie für genau diesen Client geprüft ist. |

Ein neuer Git-Worktree enthält die ignorierte `.local/sources.md` nicht automatisch; bestätigte Quellenpfade gegebenenfalls erneut angeben. Den Produktordner explizit binden, wenn er neben dem neuen Arbeitsordner nicht vorhanden ist.

Ein Client muss die verlinkten Regeln und Originalquellen tatsächlich lesen können. Ein gewöhnlicher Textchat ohne diese Zugriffe ermöglicht keinen vollständigen Ablauf. Dass ein Client ein bestimmtes Modell anbietet, sagt noch nichts über seine Dateirechte oder Jira-Werkzeuge aus.

### Git installieren

Öffne auf macOS **Terminal** über die Spotlight-Suche, auf Windows **PowerShell** über das Startmenü. Gib ein:

```sh
git --version
```

Erscheint `git version …`, ist Git vorhanden. Andernfalls nutze den passenden Weg:

| Betriebssystem | Installation |
| --- | --- |
| macOS | Im Terminal `xcode-select --install` eingeben und den Installationsdialog abschließen. Die Apple Command Line Tools enthalten Git; die vollständige Xcode-App ist dafür nicht nötig. [Offizielle Git-Anleitung](https://git-scm.com/install/mac) |
| Windows | In PowerShell `winget install --id Git.Git -e --source winget` ausführen. Ohne `winget` den passenden Installer über [Git für Windows](https://git-scm.com/install/windows) herunterladen und ausführen. |

Öffne danach ein neues Terminal bzw. PowerShell-Fenster und prüfe erneut mit `git --version`. Falls dein bereits geöffneter Assistent Git nicht findet, starte ihn neu.

### Repo öffnen und Setup starten

1. Klone im gewünschten Ordner `git clone --branch codex/developer https://github.com/TimoDeg/fvk-powers.git`. Existiert die Kopie schon, verwende sie; überschreibe sie nicht. Prüfe mit `git branch --show-current`, welche Variante aktiv ist: `codex/developer` für Entwickler, `main` für die bisherige PM-Version. Vor einem Wechsel lokale Änderungen sichern.
2. Öffne den Ordner `fvk-powers` im gewählten Client. Gib ihm Zugriff auf die Repo-Dateien. Die Ordnerfunktionen unterscheiden sich je Client; ein Projektname allein belegt keinen Dateizugriff.
3. Starte einen neuen Chat bzw. eine neue Sitzung im Projekt und schreibe:

```text
Lies AGENTS.md in diesem Projekt und führe das darin beschriebene Setup aus.
Richte fvk-powers für mich ein.
```

Damit ist der Einstieg auch ohne automatische Erkennung des Dateinamens eindeutig. Kann der Assistent die Datei nicht öffnen, richte zuerst den Projekt-/Dateizugriff ein. Halte einen lesbaren Rewrite-Ticketlink und den Ordner oder internen Link zum Produktrepo bereit. Der öffentliche Download gewährt keine internen Zugriffsrechte.

### Jira verbinden

Eine vorhandene funktionierende Verbindung weiterverwenden. Fehlt sie, nutze den zum Client passenden Weg. **MCP** ist ein Standard, über den ein Assistent externe Werkzeuge wie Jira aufrufen kann; manche Clients nennen solche Zugänge Plugins oder Connectoren.

| Client | Nächster Schritt bei fehlendem Jira-Zugang |
| --- | --- |
| Cursor | Öffne die MCP-Verwaltung des Clients und füge den von eurem Team freigegebenen Jira-/Atlassian-Zugang nach [Cursor-MCP-Anleitung](https://cursor.com/docs/mcp) hinzu. Fehlt die Serveradresse oder Freigabe, frage den Workspace-Administrator. |
| Claude Code | Öffne `/mcp`, um konfigurierte Verbindungen und deren Anmeldung zu prüfen. Fehlt der Jira-Server, binde den freigegebenen Zugang anhand der [MCP-Anleitung](https://code.claude.com/docs/en/mcp) ein; Serveradresse und Freigabe kommen vom Team. |
| Codex in der Desktop-App | Öffne **Plugins**, suche das freigegebene Jira-/Atlassian-Plugin und folge Installation und Anmeldung nach der [Plugin-Anleitung](https://learn.chatgpt.com/docs/plugins). Falls die Installation eine neue Sitzung verlangt, starte einen neuen Projektchat. |
| Codex CLI | Öffne `/plugins` und wähle das freigegebene Jira-/Atlassian-Plugin. Folge Installation und Anmeldung und starte die Sitzung bei Bedarf neu. |
| Orca | Richte Jira im tatsächlich gestarteten Agenten ein, etwa über `/mcp` in Claude Code oder den passenden Codex-Zugang. Anschließend das Ticket in genau dieser Orca-Sitzung abrufen; ein funktionierender Zugang in einer anderen App beweist ihn nicht. |
| Claude-App oder anderer Client | Prüfe die tatsächlich angebotenen Connector-/MCP-Einstellungen und die offizielle Anleitung genau dieses Produkts. Ohne passenden Zugang den Administrator nach dem freigegebenen Weg fragen; keine Menünamen eines anderen Clients übernehmen. |

Melde dich ausschließlich im vorgesehenen Anmeldedialog an; Passwörter und Tokens gehören nicht in den Chat oder ins Repo. Wir liefern keine Zugangsdaten oder verbindliche firmenspezifische Serverkonfiguration mit. Nach der Einrichtung schreibe **„Setup weiter. Prüfe den Jira-Zugriff auf dieses Ticket: …“** mit dem echten Ticketlink. Lade die Werkzeuge so neu, wie der Client es verlangt; bestätigte lokale Quellenangaben werden weiterverwendet.

Erst der erfolgreiche Abruf dieses Tickets bestätigt den Zugriff. Fehlt nur dessen Berechtigung, prüfe, ob du es mit demselben Konto im Browser öffnen kannst, und kläre die Leserechte intern. Ein installiertes Plugin oder erreichbarer MCP-Server allein ist kein erfolgreicher Ticketabruf. Bis dahin sind Fragen zu zugänglichen Specs bereits möglich.

### Rewrite-Specs anbinden

Nenne dem Assistenten den vorhandenen Produktrepo-Ordner oder den internen Repo-Link. Liegt noch keine lokale Kopie vor, prüft er zuerst verfügbaren Lesezugriff. Wenn ein Download nötig ist, klärt er mit dir den Zielordner und führt den beauftragten Schritt aus. Interne Berechtigungen muss gegebenenfalls das Team freischalten.

Der Assistent prüft eine Original-Spec und versucht den ersten Ticket-Spec-Abgleich. Er zeigt zum Abschluss getrennt, ob **Jira**, **Specs** und **lokale Speicherung** geprüft oder noch offen sind. Bei einer fehlenden Quelle bleibt die Arbeit mit der anderen möglich. Mit **„Setup weiter“** setzt du die Einrichtung fort.

**Die Pipeline selbst benötigt kein Node, PHP, Docker, keine Datenbank und keine zusätzlichen npm-/Python-Pakete.** Der gewählte Client kann eigene Installationsvoraussetzungen haben. Eine zweite KI-App oder zusätzliche CLI ist für die Pipeline nicht erforderlich.

Client-Dokumentation geprüft am **18.09.2026**. Ein vollständiger Erststart je Client ist damit noch nicht nachgewiesen; [Prüfstand](VALIDATION.md).

## Grundsetup für Quellenarbeit

| Voraussetzung | Wofür? | Prüfung im Chat |
| --- | --- | --- |
| Assistent mit Zugriff auf dieses Repo und dessen Anweisungen | Arbeitsablauf und gewähltes Profil lesen | `AGENTS.md` und die gerouteten Dateien sind lesbar |
| Freigegebener Jira-Connector und persönliche Leseberechtigung | Tickets und relevante Ergänzungen lesen | Ein konkret genanntes Ticket tatsächlich abrufen |
| Lesezugriff auf das Rewrite-Produktrepo | Original-Specs und bei Bedarf weitere Quellen lesen | Spec-Einstieg und passende Spec öffnen, Stand festhalten |
| Lokaler beschreibbarer, von Git ausgeschlossener Ordner | Einrichtung über den Chat hinaus behalten | `.local/` prüfen; sonst nur im aktuellen Gespräch fortsetzen |

Jira und Specs können einzeln nutzbar sein; nur mit beiden ist ein vollständiger Ticket-Spec-Abgleich möglich. Ein normaler Chat ohne Datei- und Connector-Zugriff erfüllt diese Voraussetzungen nicht. Die Zuverlässigkeit beim Laden der Anweisungen hängt vom Client ab und muss beim Erststart geprüft werden.

## Nur bei entsprechendem Bedarf

| Werkzeug/Zugang | Wann benötigt? | Gehört zum Grundsetup? |
| --- | --- | --- |
| Git | Lokal klonen, Versionen bestimmen, lokale Speicherung vor Veröffentlichung schützen | Beim lokalen Repo-Weg; kein Produkt-Build nötig |
| Freigegebener Spec-Bot-/Slack-Lesezugriff | Aktueller Spec-Status und Zuständigkeit, wenn die Repo-Dokumentation dorthin verweist | Nein; ohne Zugriff diesen Status offenlassen |
| PDF-/Bild-/Confluence-Lesewerkzeuge | Entscheidungsrelevante verlinkte Quellen | Nur bei solchen Quellen; ungelesene Anhänge benennen |
| Browser und erreichbare Testumgebung | Eine tatsächliche UI-Abnahme ausführen | Nein; eine Abnahme planen geht ohne Browser |
| Dateisuche, optional `rg` | Passende Originale auffinden | Der Client kann die Suche bereitstellen |
| QMD, CodeGraph, Graphify | Vorhandene, aktuelle Suchindizes gezielt nutzen | Nein; nicht enthalten und nicht automatisch installiert |

Für Quellenanalyse und Erklärungen keine Node-, PHP-, Composer-, Docker-, Datenbank- oder Produktinstallation verlangen. Für Implementierung und Tests prüft der Assistent die benötigten Versionen, Installationsschritte und Testbefehle in der aktuellen Anleitung des Produktrepos. Diese Abhängigkeiten werden nicht von fvk-powers mitgeliefert; das Grundsetup allein bestätigt keine lauffähige Produktumgebung.

## Dieses Repo prüfen und pflegen

- `python3 tools/check.py`: Paketprüfung mit Python 3.11 oder neuer und ausschließlich Standardbibliothek. Getestete Versionen stehen im Prüfbericht; 3.11 ist eine deklarierte Mindestversion, kein Beleg einer getesteten Laufzeit.
- `python3 -m unittest discover -s tests -v`: Regressionen der Paketprüfung.
- `python3 tools/check.py --product-repo <pfad>`: zusätzlich lesender Check der Kontext-Einstiege in einem lokalen Produktrepo. Kein Jira-Aufruf, kein Fetch und keine App-Installation.
- Git für lokale Versionsbelege; `gh` ist nur für Maintainer beim Veröffentlichen und Lesen der GitHub-Checks hilfreich.
- GitHub Actions für die automatische Paketprüfung. Der [Workflow](../.github/workflows/check.yml) verwendet eine auf Commit fixierte [offizielle checkout-Action](https://github.com/actions/checkout/releases/tag/v7.0.1), einen bereitgestellten Python-Interpreter und nur lesende Repo-Rechte. Keine Jira-Zugänge, Produktrepo-Zugänge oder Modellschlüssel in CI. Zum Veröffentlichen von Workflow-Änderungen benötigt ein GitHub-OAuth-Zugang die `workflow`-Berechtigung; kein Token gehört ins Repo.

Es gibt keine zusätzlich zu installierenden Python-/npm-Pakete und keinen eigenen Modell-API-Client. Der Assistent und seine Connectoren bleiben externe Laufzeitvoraussetzungen; „0 Zusatzpakete“ bedeutet nicht „ohne Zugänge nutzbar“.
