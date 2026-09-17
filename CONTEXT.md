# Kontext gezielt finden

Diese Datei ist eine Landkarte zu Originalquellen, keine zweite Produktdokumentation. Alle Produktpfade sind relativ zum bestätigten Rewrite-Repo. Lies nur die für die Frage passenden Quellen, einschließlich relevanter Ausnahmen und Konflikte. Prüfe Pfade im aktuellen Checkout; sie können sich ändern.

## Welche Frage braucht welche Quelle?

| Frage | Zuerst lesen | Bei einer offenen Frage ergänzen |
| --- | --- | --- |
| Was verlangt das Ticket? | Exaktes Jira-Ticket, Akzeptanzkriterien | Relevante Kommentare, Parent, verknüpfte Tickets, Anhänge |
| Was soll das Feature tun? | `docs/specs/README.md`, passende Datei unter `docs/specs/features/` | Verlinkte Spezifikationen, Entscheidungen und offene Fragen |
| Wer betreut die Spec, wie ist ihr Stand? | Die in `docs/specs/README.md` benannte Statusquelle | Aktueller freigegebener Lesezugriff auf den Spec-Bot/Slack; ohne diesen Zugriff Status offenlassen |
| Was bedeutet ein Fachbegriff? | Passende Spec und `docs/domains/` | Begriffsverwendung in benachbarten Specs; widersprüchliche Bedeutungen erklären |
| Warum wurde es so entschieden? | Passendes Dokument unter `docs/decisions/` | Entscheidungshistorie und spezifischere ablösende Entscheidung |
| Was passiert in Vergleich oder Checkout? | Passende Feature-Spec | `deployables/frontend-journey/`, zuständige Bereiche `BackendForFrontend/Comparison/` und `Checkout/` im Monolith |
| Wie funktioniert der Produkteinstieg? | Passende Feature-Spec | `docs/decisions/product-entry-deployable.md`, `deployables/frontend-product-entry/` |
| Was gilt in Tarif-/Versichererverwaltung oder Kundenbereich? | Passende Feature-Spec | Besitzende App unter `deployables/frontend-pim/`, `frontend-sim/`, `frontend-crm/` oder `frontend-customer-area/` |
| Wie läuft die Fachlogik tatsächlich? | Zuständige Spec bzw. Domain-Dokumentation | `deployables/monolith/src/Backend/Domains/`, bei bereichsübergreifenden Abläufen `Backend/Orchestrators/` und beteiligte Aufrufer |
| Wie nehme ich das ab? | Akzeptanzkriterien, fachliche Bedingungen und UI-Zustände | `docs/decisions/testing-layers-decision.md`, passende Testanleitungen; tatsächliche Umgebung und Testdaten separat prüfen |
| Ist es live? | Aktueller Jira-Stand als Hinweis | Release-/Deploymentbeleg und Verhalten in der benannten Umgebung; bei Infrastrukturfragen `docs/jenkins/ci-cd-documentation.md` als Einstieg |

`BackendForFrontend/` liegt unter `deployables/monolith/src/`. Eine Code-Lesespur beweist keine erfolgreiche Produktivsetzung. Technische Quellen werden in der Antwort in ihre fachliche Wirkung übersetzt.

## Suchfolge

1. Ticketverweise und bereits bekannte Originale zuerst.
2. Fachbegriff und passende englische Repository-Begriffe gezielt suchen, zum Beispiel „Tarifdetails“ / „tariff detail“, „Kundenbereich“ / „customer area“, „Kulanz“ / „goodwill“. Diese Wörter sind Suchhilfen, keine Definitionen.
3. Ganze relevante Abschnitte lesen, nicht nur Trefferzeilen. Grenzen, Fehlerfälle, Anhänge und Referenzen berücksichtigen.
4. Bei keinem Treffer mit Synonymen und dem besitzenden Bereich nachprüfen. Dann die konkrete Quellenlücke benennen, statt Vollständigkeit zu behaupten.
5. Aufhören, wenn die Frage mit Quellen, Grenzen und offenen Entscheidungen beantwortbar ist. Nicht routinemäßig alle Specs, Regeln und Codeverzeichnisse laden.

Dateisuche des Clients genügt; `rg` ist eine optionale lokale Hilfe. QMD, CodeGraph und Graphify sind nicht mitgeliefert und keine Voraussetzung. Wenn eine bestehende Installation ausdrücklich genutzt wird, zuerst ihre dokumentierte Quellenbindung und Aktualität prüfen. Treffer dienen der Navigation und müssen am Original bestätigt werden. Kein automatischer Indexaufbau oder Legacy-Fallback.

## Kontext im Gespräch erhalten

Führe Ticketidentität, konkrete Frage, gelesene Quellen mit Stand, bestätigte Entscheidungen und verbleibende Lücken im selben Gespräch fort. „Einfacher erklären“ verwendet den vorhandenen Kontext; „Wie ist der aktuelle Stand?“ braucht frische relevante Quellen. Beim Ticketwechsel alte Entscheidungen nicht ungeprüft übertragen.

Wenn eine dauerhafte Übergabe beauftragt ist, fasse diese Punkte unter `.local/` zusammen und prüfe vorher den Git-Ausschluss wie beim Setup. Private Quelleninhalte bleiben lokal. Gespeicherte Zusammenfassungen ersetzen bei neuen fachlichen Entscheidungen nicht die Originale.

## Übergang zur Entwicklerarbeit

Dieses Paket besitzt den PM-Ablauf. Es enthält keine portierte Implementierungs- und Deployment-Automation. Bei einem ausdrücklichen Codeauftrag zuerst Produktrepo-Regeln lesen: `AGENTS.md`, `.codex/AGENTS.md`, `docs/CONTRIBUTING.md`, `docs/coding-standards.md`, `.agent/rules.json` und die zur Änderung passenden Originalregeln und Testentscheidungen. Abweichende Hosts und Laufzeitvoraussetzungen vor Tests prüfen. Fehlende Regeln oder Quellen benennen; Änderungen nicht allein aus dem PM-Kurztext ableiten.
