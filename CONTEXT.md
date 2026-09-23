# Kontext gezielt finden und erhalten

Diese Datei ist eine Landkarte zu Originalquellen und regelt, wie Arbeitsstand über einen Chat hinaus erhalten bleibt. Sie ist keine zweite Produktdokumentation. Produktpfade sind relativ zum bestätigten Rewrite-Repo und können sich ändern; prüfe sie im aktuellen Checkout.

## Welche Frage braucht welche Quelle?

| Frage | Zuerst lesen | Bei einer offenen Frage ergänzen |
| --- | --- | --- |
| Was verlangt das Ticket? | Exaktes Jira-Ticket, Akzeptanzkriterien | Relevante Kommentare, Parent, verknüpfte Tickets, Anhänge |
| Was soll das Feature tun? | `docs/specs/README.md`, passende Datei unter `docs/specs/features/` | Verlinkte Spezifikationen, Entscheidungen und offene Fragen |
| Wer betreut die Spec, wie ist ihr Stand? | Die in `docs/specs/README.md` benannte Statusquelle | Freigegebener Lesezugriff auf den Spec-Bot/Slack; ohne ihn bleibt der Status offen |
| Was bedeutet ein Fachbegriff? | Passende Spec und `docs/domains/` | Verwendung in benachbarten Specs; widersprüchliche Bedeutungen erklären |
| Warum wurde es so entschieden? | Passendes Dokument unter `docs/decisions/` | Entscheidungshistorie und spezifischere ablösende Entscheidung |
| Was passiert in Vergleich oder Checkout? | Passende Feature-Spec | `deployables/frontend-journey/`, im Monolith `BackendForFrontend/Comparison/` und `Checkout/` |
| Wie funktioniert der Produkteinstieg? | Passende Feature-Spec | `docs/decisions/product-entry-deployable.md`, `deployables/frontend-product-entry/` |
| Was gilt in Tarif-/Versichererverwaltung oder Kundenbereich? | Passende Feature-Spec | Besitzende App unter `deployables/frontend-pim/`, `frontend-sim/`, `frontend-crm/` oder `frontend-customer-area/` |
| Wie läuft die Fachlogik tatsächlich? | Zuständige Spec bzw. Domain-Dokumentation | `deployables/monolith/src/Backend/Domains/`, bereichsübergreifend `Backend/Orchestrators/` und beteiligte Aufrufer |
| Wie nehme ich das ab? | Akzeptanzkriterien, fachliche Bedingungen und UI-Zustände | `docs/decisions/testing-layers-decision.md`, passende Testanleitungen; Umgebung und Testdaten separat klären |
| Ist es live? | Aktueller Jira-Stand als Hinweis | Release-/Deploymentbeleg und Verhalten in der benannten Umgebung; für Infrastruktur `docs/jenkins/ci-cd-documentation.md` |

`BackendForFrontend/` liegt unter `deployables/monolith/src/`. Eine Code-Lesespur beweist keine erfolgreiche Produktivsetzung; übersetze technische Funde in ihre fachliche Wirkung.

## Suchfolge

1. Ticketverweise und bereits bekannte Originale zuerst.
2. Fachbegriff und englische Repository-Begriffe, zum Beispiel „Tarifdetails“ / „tariff detail“, „Kundenbereich“ / „customer area“, „Kulanz“ / „goodwill“. Das sind Suchhilfen, keine Definitionen.
3. Ganze relevante Abschnitte lesen, nicht nur Trefferzeilen: Grenzen, Fehlerfälle, Anhänge und Referenzen gehören dazu.
4. Kein Treffer: mit Synonymen und im besitzenden Bereich nachprüfen, dann die konkrete Lücke benennen.
5. Aufhören, sobald die Frage mit Quellen, Grenzen und offenen Entscheidungen beantwortbar ist. Nicht routinemäßig alle Specs, Regeln oder Codeverzeichnisse laden.

Die Dateisuche des Clients genügt; `rg` ist optional. QMD, CodeGraph und Graphify sind weder mitgeliefert noch Voraussetzung. Nutzt jemand eine bestehende Installation ausdrücklich, prüfe zuerst deren Quellenbindung und Aktualität; Treffer dienen der Navigation und werden am Original bestätigt. Kein automatischer Indexaufbau, kein Legacy-Fallback.

## Gemeinsames Wissen

Ein optionaler `Wissenseinstieg` in `.local/sources.md` führt zur internen Wissensbasis (Glossar, Fachabläufe, Architektur, Entscheidungen, bekannte Konflikte). PM und IT nutzen dieselben Quellen; nur die Erklärung richtet sich nach der Frage. Ohne Einstieg nutzt du die Originalquellen oben.

Lies bei einer passenden Frage den Einstieg und dann nur die relevanten Kapitel samt Grenzen und Originalverweisen; relative Links löst du von der verweisenden Datei aus auf. Wissensdokumente sind datierte Quellen mit Herkunft: Meetingnotizen belegen damalige Aussagen, Specs das Soll, Code und Laufzeit den geprüften Stand. Widerspricht ein Kapitel einer Spec, gilt [Prinzip 4](AGENTS.md#das-belegmodell): Beginne die Antwort mit beiden Aussagen und der fehlenden Entscheidung. Ein unerreichbarer Link bleibt eine benannte Lücke. Keine Kopie der internen Sammlung in dieses Repo, kein zusätzlicher Index, keine automatische Aktualisierung.

## Kontext erhalten

Im laufenden Gespräch führst du Ticket, Frage, gelesene Quellen mit Stand, bestätigte Entscheidungen und Lücken weiter. „Einfacher erklären“ nutzt diesen Kontext; „Wie ist der aktuelle Stand?“ braucht frische Quellen. Beim Ticketwechsel überträgst du keine alten Entscheidungen ungeprüft.

### Stand speichern

Nur auf Auftrag („Stand speichern“, beauftragte Übergabe), nie automatisch. Ziel ist `.local/tickets/<TICKET>.md` mit dem bestätigten Ticketschlüssel als Dateiname; ohne eindeutigen Schlüssel klärst du ihn vorher.

**Ziel prüfen, bevor du schreibst:** Der aufgelöste Pfad (auch nach Symlinks) liegt in diesem Checkout unter `.local/`, ist von Git ignoriert und nicht bereits getrackt. Ist das nicht gegeben oder fehlt Schreibzugriff, schreibst du nicht, änderst keine Git-Ausnahmen, fügst nichts erzwungen hinzu und gibst den Stand stattdessen im Chat aus, mit dem Hinweis, dass er nicht gespeichert ist. Eine vorhandene Notiz liest du zuerst und erhältst fremde Ergänzungen und historische Abweichungen.

**Beobachtungen wörtlich sichern.** Zusammenfassungen verlieren erfahrungsgemäß genau die Angaben, die später zählen: frühere Umgebung, Version, wer was gemeldet hat. Deshalb kopierst du pro früherer Beobachtung die ursprünglichen Sätze aus dem Gespräch als **Originalbeleg**, einschließlich Umgebung, Version, Herkunft, Handlung und Ergebnis. Sensible Angaben schwärzt du ausdrücklich. Bewertung und heutiger Stand stehen außerhalb des Zitats; „heute unbekannt“ ändert den historischen Beleg nicht.

**Zurücklesen, dann bestätigen.** Die Erfolgsmeldung des Schreibwerkzeugs ersetzt das nicht: Öffne die geschriebene Datei erneut mit einem Lesezugriff und vergleiche jeden Originalbeleg mit der Gesprächsstelle: Jede dort genannte Umgebung, Version und Beobachtung muss im Beleg stehen. Erst danach bestätigst du den Speicherort. Die Notiz unterliegt nicht der Kurzform einer PM-Antwort.

```markdown
# <TICKET>: <Kurzthema>
- Gespeichert: <Zeitpunkt>
- Auftrag und Umfang: <Ziel, Oberfläche, ausdrücklich ausgeschlossene Teile>
- Quellen: <bestätigter Pfad/URL, gelesener Abschnitt, Abrufzeit und Version;
  bei lokalen Quellen Datei-Hash oder Git-Stand samt lokalen Änderungen>
- Entscheidungen: <bestätigte Entscheidung mit Herkunft; offene Konflikte getrennt>
- Historische Beobachtung (je Fall):
  - Originalbeleg: „<wörtliche Gesprächsstelle mit damaliger Umgebung, Version, Herkunft, Handlung und Ergebnis>“
  - Erwartung und damalige Bewertung: <Soll mit Quelle; Bewertung getrennt vom Bericht>
- Aktuelle Testumgebung: <heute bestätigt oder unbekannt>
- Aktueller Produktstand: <heute bestätigt oder unbekannt>
- Offen: <ungeprüfte Fälle, fehlende Quellen, unbestätigte Angaben>
- Nächster Schritt: <eine konkrete Handlung oder nötige Rückfrage>
```

In die Notiz gehören Zusammenfassung und Quellenverweise, keine Zugangsdaten, personenbezogenen Testdaten, Anhänge oder vollständigen Ticketkopien. Sie gilt nur für diesen Checkout und wird nicht mit Git geteilt. Eine Teamübergabe bereitest du als Entwurf mit erreichbaren internen Quellen vor und legst sie erst auf ausdrücklichen Auftrag am bestätigten internen Ziel ab.

### In einem neuen Chat fortsetzen

Bei „weiter mit <TICKET>“ öffnest du `.local/sources.md` und `.local/tickets/<TICKET>.md` direkt über ihren Pfad. Dateisuchen blenden ignorierte Dateien aus, auch `rg --files --hidden`; ein leeres Suchergebnis beweist also keine fehlende Notiz. Suche nur in diesem Projekt, nicht im Elternordner oder in anderen Checkouts. Bei „weiter“ ohne eindeutiges Ticket fragst du nach, statt alle Notizen zu laden.

Fehlt die Notiz, sagst du, dass kein gespeicherter Verlauf vorliegt, und übernimmst keinen Verlauf eines anderen Tickets. Binde dann zuerst den Ticketinhalt über den vorhandenen Zugang oder eine Rückfrage; ohne ihn ist auch das Thema unbekannt.

Eine vorhandene Notiz ist eine datierte Übergabe, keine Originalquelle und kein Testergebnis. Prüfe vor dem nächsten fachlichen Schritt die dafür relevanten Quellen auf Änderungen (Datei-Hash, Git-Stand samt lokalen Änderungen, Quellversion) und lies betroffene Abschnitte neu. Frische Jira- oder Deploymentaussagen brauchen frische Belege. Frühere Beobachtungen bleiben mit ihrer Herkunft erhalten; haben sich Soll, Produktstand oder Umgebung geändert, sind betroffene Prüfungen wieder offen ([Prinzip 3](AGENTS.md#das-belegmodell)).

Die erste Fortsetzungsantwort hat drei kurze Teile:

1. **Bisher:** „Laut <PM-Rückmeldung / Beleg> wurde auf <damaligem Stand> <Ergebnis> beobachtet.“ Oder: noch keine Tests.
2. **Offen:** alle noch ungeprüften Fälle aus der Notiz namentlich, auch wenn zunächst ein anderer dran ist; dazu entscheidende Quellenlücken, offene Konflikte und durch Änderungen nötige Wiederholungen.
3. **Weiter:** genau eine nächste Handlung oder die dafür nötige Rückfrage. Vor einem neuen Testfall klärst du die aktuelle Ausgangslage; eine historische ist keine heutige.

## Übergang zur Entwicklerarbeit

Dieses Paket enthält den PM-Ablauf, keine Implementierungs- oder Deployment-Automation. Bei einem ausdrücklichen Codeauftrag liest du zuerst die Regeln des Produktrepos: `AGENTS.md`, `.codex/AGENTS.md`, `docs/CONTRIBUTING.md`, `docs/coding-standards.md`, `.agent/rules.json` und die zur Änderung passenden Originalregeln und Testentscheidungen. Hosts und Laufzeitvoraussetzungen prüfst du vor Tests. Fehlende Regeln benennst du; Änderungen leitest du nicht allein aus einem PM-Kurztext ab.
