# Was benötigt wird

Für den hier ausführlich beschriebenen Einstieg installierst du **die Desktop-App mit Codex und Git**; Claude Code, Claude Desktop und Cursor funktionieren mit denselben Projektanweisungen ([andere Clients](#andere-clients)). Dazu kommen dein freigegebener ChatGPT-Zugang, die Jira-Verbindung und Lesezugriff auf das Rewrite-Produktrepo. Python brauchst du nur, wenn du als Maintainer die Paketchecks ausführen möchtest.

## Einrichtung von Anfang an

Diese Anleitung führt durch macOS und Windows. Bereits erledigte Schritte kannst du überspringen. Auf einem verwalteten Firmenrechner nutze das Softwareportal bzw. die IT, falls eine Installation oder Verbindung gesperrt ist.

### Codex einrichten

1. Öffne die [offizielle Desktop-Anleitung mit Download](https://learn.chatgpt.com/docs/app); für Windows gibt es eine [eigene Installationsseite](https://learn.chatgpt.com/docs/windows/windows-app). Wähle den Download für dein Betriebssystem und öffne die Installationsdatei bzw. den dort verlinkten Store.
2. Folge der Installation und öffne die App. Die aktuelle OpenAI-Dokumentation nennt sie **ChatGPT-Desktop-App**; darin wählst du **Codex**. Bei einer bestehenden Codex-App kannst du diese verwenden.
3. Melde dich mit dem für deine Arbeit freigegebenen ChatGPT-Konto an und wähle den vorgesehenen Workspace. Wenn Codex dort fehlt, kläre den Zugang mit dem Workspace-Administrator.
4. Lass die App geöffnet. Den lokalen Projektordner fügst du nach dem Download des Repos hinzu.

Für diesen Einstieg brauchst du keinen separat angelegten OpenAI-API-Schlüssel. Die Anleitung verwendet die Anmeldung mit deinem ChatGPT-Konto.

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

Öffne danach ein neues Terminal bzw. PowerShell-Fenster und prüfe erneut mit `git --version`. Falls die bereits geöffnete Codex-App Git nicht findet, starte sie neu.

### Repo öffnen und Setup starten

1. Wechsle im Terminal in einen Ordner, in dem du das Projekt speichern möchtest. Führe dort `git clone https://github.com/TimoDeg/fvk-powers.git` aus. Das legt den Unterordner `fvk-powers` an. Existiert er schon, verwende die vorhandene Kopie; überschreibe sie nicht.
2. Öffne in der Desktop-App die Projektansicht und füge den heruntergeladenen Ordner als **lokales Projekt** hinzu. Bei einem vorhandenen Projekt: Projektmenü → **Edit project** → **Add folder**. Wähle `fvk-powers`; bei mehreren Ordnern setze ihn über **Make primary** als Hauptordner. So werden seine Projektanweisungen geladen. [Offizielle Projektanleitung](https://learn.chatgpt.com/docs/projects)
3. Starte in diesem Projekt einen neuen Codex-Chat und schreibe: **„Richte fvk-powers für mich ein.“**

Der Assistent prüft die Projektdateien und vorhandenen Quellen. Halte einen lesbaren Rewrite-Ticketlink und den Ordner oder internen Link zum Rewrite-Produktrepo bereit. Der öffentliche Download von fvk-powers benötigt keine Jira-Anmeldung und gewährt keine internen Zugriffsrechte.

### Jira verbinden

Wenn der Assistent bereits ein Ticket lesen kann, ist keine neue Verbindung nötig. Andernfalls:

1. Öffne in der Desktop-App **Plugins** und suche nach **Atlassian Rovo** bzw. dem für eure Organisation freigegebenen Jira-Plugin. Der Name kann je nach Workspace abweichen.
2. Öffne den Eintrag, prüfe den angebotenen Jira-Zugriff und installiere ihn über **+** bzw. die angezeigte Installationsschaltfläche. Ist er bereits installiert, fahre mit der Verbindung fort.
3. Folge der Aufforderung zum Verbinden und melde dich im geöffneten Anmeldedialog mit deinem Arbeitskonto bei Atlassian an. Verwende die Jira-Site, zu der dein Ticket gehört. Die Anmeldung kann bei der Installation oder bei der ersten Nutzung erscheinen.
4. Starte nach der Installation einen neuen Codex-Chat im Projekt `fvk-powers`. Schreibe **„Setup weiter. Prüfe den Jira-Zugriff auf dieses Ticket: …“** und füge den echten Ticketlink ein. Noch nicht gespeicherte Angaben aus dem alten Chat bei Bedarf erneut nennen.
5. Erst wenn der Assistent das konkrete Ticket gelesen hat, ist der Zugriff geprüft. Ein installiertes Plugin allein reicht nicht.

Fehlt das Plugin oder ist die Verbindung gesperrt, bitte den Workspace-Administrator um den freigegebenen Jira-Zugang. Ist nur das Ticket nicht lesbar, prüfe zunächst, ob du es mit demselben Konto im Browser öffnen kannst, und kläre die Ticketberechtigung intern. Passwörter und Tokens gehören nicht in den Chat.

Der Installationsablauf und die anschließende neue Sitzung sind in der [offiziellen Plugin-Anleitung](https://learn.chatgpt.com/docs/plugins) beschrieben. Menünamen können je nach App-Version und Sprache abweichen; diese Anleitung ist keine Bestätigung, dass das Plugin in jedem Firmenkonto verfügbar ist.

**Wenn du bereits die Codex CLI nutzt:** Gib in der laufenden Codex-Sitzung `/plugins` ein. Wähle dort das freigegebene Jira-/Atlassian-Plugin und folge der Installation bzw. Anmeldung. Starte anschließend Codex im Projektordner neu und schreibe „Setup weiter“ mit deinem Ticketlink. Fehlt der Eintrag, kläre das verfügbare Jira-Plugin mit eurem Workspace-Administrator. Die CLI ist für den oben beschriebenen Desktop-Einstieg nicht zusätzlich erforderlich.

### Andere Clients

Die Projektanweisungen stehen in `AGENTS.md`; Claude Code lädt sie über `CLAUDE.md`. Jira verbindest du über den offiziellen [Atlassian-MCP-Server](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/) mit deinem Arbeitskonto (Stand 23.09.2026):

| Client | Projekt öffnen | Jira verbinden |
| --- | --- | --- |
| Claude Code | Im Ordner `fvk-powers` `claude` starten | `claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp`, dann in der Sitzung `/mcp` und anmelden |
| Claude Desktop | Ordner als Projekt bzw. Arbeitsordner wählen | Atlassian-Connector hinzufügen, falls euer Workspace ihn freigibt; sonst Server-URL wie oben laut Atlassian-Anleitung |
| Cursor | Ordner öffnen, Agent verwenden | Im Cursor-Marketplace „Atlassian“ suchen, **Add to Cursor**, anmelden |

Danach wie oben einen neuen Chat starten und „Setup weiter“ mit dem Ticketlink schreiben. In diesen Clients ist der vollständige Ablauf noch nicht nativ geprüft; [Prüfstand](VALIDATION.md).

### Ordner und Selbstcheck

Lege `fvk-powers` neben das Rewrite-Repo `fvk` (und optional `fvk-infrastructure`) in denselben Arbeitsordner; die Struktur steht in [SETUP](../SETUP.md#arbeitsordner). `python3 tools/doctor.py` prüft anschließend Ordner, Repos, lokalen Speicher, Profil und Glossar, ohne etwas zu ändern.

### Rewrite-Specs anbinden

Nenne dem Assistenten den vorhandenen Produktrepo-Ordner oder den internen Repo-Link. Liegt noch keine lokale Kopie vor, prüft er zuerst verfügbaren Lesezugriff. Wenn ein Download nötig ist, klärt er mit dir den Zielordner und führt den beauftragten Schritt aus. Interne Berechtigungen muss gegebenenfalls das Team freischalten.

Der Assistent prüft eine Original-Spec und versucht den ersten Ticket-Spec-Abgleich. Er zeigt zum Abschluss getrennt, ob **Jira**, **Specs** und **lokale Speicherung** geprüft oder noch offen sind. Bei einer fehlenden Quelle bleibt die Arbeit mit der anderen möglich. Mit **„Setup weiter“** setzt du die Einrichtung fort.

**Für die PM-Nutzung musst du kein Node, PHP, Docker, keine Datenbank und keine zusätzlichen npm-/Python-Pakete installieren.** Auch ein zusätzlicher Editor oder die Codex CLI sind für diesen Desktop-Weg nicht nötig.

Installationsquellen geprüft am **17.09.2026**. Ein vollständiger Erststart auf einem neuen PM-Rechner ist weiterhin offen; [Prüfstand](VALIDATION.md).

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
- GitHub Actions für die automatische Paketprüfung. Der [Workflow](../.github/workflows/check.yml) verwendet eine auf Commit fixierte [offizielle checkout-Action](https://github.com/actions/checkout/releases/tag/v7.0.1), einen bereitgestellten Python-Interpreter und nur lesende Repo-Rechte. Keine Jira-Zugänge, Produktrepo-Zugänge oder Modellschlüssel in CI. Zum Veröffentlichen von Workflow-Änderungen benötigt ein GitHub-OAuth-Zugang die `workflow`-Berechtigung; kein Token gehört ins Repo.

Es gibt keine zusätzlich zu installierenden Python-/npm-Pakete und keinen eigenen Modell-API-Client. Der Assistent und seine Connectoren bleiben externe Laufzeitvoraussetzungen; „0 Zusatzpakete“ bedeutet nicht „ohne Zugänge nutzbar“.
