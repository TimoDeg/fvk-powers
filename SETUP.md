# Geführtes Setup im Chat

Diese Anleitung richtet sich an den Assistenten. Führe die Schritte selbst aus, soweit Werkzeuge und Auftrag das erlauben. Lass den Nutzer nur Angaben, Anmeldung oder Zugriffsentscheidungen übernehmen, die du nicht selbst erledigen kannst. Ein Link auf diese Datei allein erfüllt keinen Setup-Auftrag.

## 1. Begrüßen und vorhandene Quellen prüfen

Beginne etwa so:

> Ich richte fvk-powers für dich ein. Dafür prüfe ich den Zugriff auf Jira und auf die Rewrite-Specs. Ich schaue zuerst, was schon vorhanden ist, und führe dich dann durch die fehlenden Schritte. Du brauchst keine Entwicklerumgebung.

Verwende Deutsch und das PM-Profil als Standard. Frage nicht zuerst nach Rolle, Modell, technischen Einstellungen oder Antwortlänge. Explizite Wünsche des Nutzers übernehmen.

Lies vorhandene Angaben aus `.local/sources.md`, falls vorhanden, und berücksichtige den laufenden Chat. Prüfe die tatsächlich verfügbaren Datei- und Jira-Werkzeuge; suche gegebenenfalls in den angebotenen Connector-Werkzeugen. Erfinde keine Toolnamen. Prüfe den bekannten Produktpfad oder den Kandidaten `../fvk` auf lesbare Specs. Suche nicht pauschal auf dem gesamten Rechner.

Kündige bevorstehende Schritte kurz mit ihrem Zweck an. Zeige relevante Ergebnisse, keine Befehlsausgaben und internen Diagnosepakete. Ein gespeicherter Erfolgsstatus ist eine alte Beobachtung und muss für einen erneuten Setup-Check frisch geprüft werden.

## 2. Fehlendes nacheinander klären

Stelle im Normalfall nur eine kurze, konkrete Frage auf einmal. Erkläre jeweils, wofür die Angabe benötigt wird. Nutze Antworten sofort und wiederhole bereits beantwortete Fragen nicht. Arbeite an unabhängigen Prüfungen weiter, während eine Antwort aussteht.

### Jira

- Ist ein Ticketlink bereits bekannt, übernimm Site und exakten Schlüssel daraus. Sonst frage: „Schick mir einen Link zu einem Rewrite-Ticket, das du lesen kannst. Daran prüfe ich den Jira-Zugriff.“ Keine zusätzliche Frage nach der Site, wenn der Link sie schon eindeutig enthält.
- Lies das genannte Ticket über den vorhandenen internen Connector. Prüfe, dass das zurückgegebene Ticket übereinstimmt und Beschreibung und Status zugänglich sind. Halte die Abrufzeit fest. Ein vorhandenes Werkzeug allein beweist keinen Zugriff.
- Fehlt der Connector, erkläre: „Für Jira fehlt noch die Verbindung in deinem Client. Verbinde dort den freigegebenen Jira-/Atlassian-Zugang und melde dich mit deinem Arbeitskonto an. Danach kann ich den Ticketzugriff prüfen.“ Nenne genauere Schaltflächen nur, wenn sie für den aktuellen Client verifiziert sind. Installiere nichts ungefragt und bitte nie um Tokens, Passwörter oder Sitzungscookies im Chat.
- Unterscheide fehlende Anmeldung, fehlende Berechtigung, nicht gefundenes Ticket und einen vorübergehenden Abruffehler, soweit der Fehler das belegt. Bei uneindeutigem Fehler keine Ursache erfinden. Nenne genau den nächsten sinnvollen Schritt, statt den gleichen Abruf wiederholt zu starten.
- Möchte der Nutzer Jira später verbinden, setze den Spec-Teil fort und markiere Jira als offen.

### Rewrite-Specs

- Ein vorhandener bekannter Produktpfad wird direkt geprüft. Ist nur der Standardkandidat gefunden, kläre knapp, ob dies das gewünschte Rewrite-Repo ist, sofern der aktuelle Kontext es nicht bereits bestätigt.
- Fehlt ein Pfad, frage: „Hast du das Rewrite-Repo bereits auf deinem Rechner? Wenn ja, nenne mir den Ordner; sonst hilft der interne Repo-Link.“ Erkläre bei Bedarf: „Dort liegen die fachlichen Beschreibungen, mit denen ich die Tickets abgleiche.“
- Bei vorhandenem Ordner lies `docs/specs/features/README.md` und eine passende Original-Spec. Prüfe Repo-Identität und aktuellen lokalen Stand. Ein Verzeichnisname allein belegt nicht das richtige Produktrepo. Fehlt der Einstieg, suche begrenzt im bestätigten Dokumentationsordner nach den Specs und benenne die tatsächliche Fundstelle oder Lücke.
- Bei bloßem Repo-Link verwende verfügbaren freigegebenen Lesezugriff, wenn damit die Originaldateien erreichbar sind. Wenn ein lokaler Checkout erforderlich ist, erkläre den Zweck und kläre Zielordner und den Auftrag zum Herunterladen. Überschreibe keinen vorhandenen Ordner. Keine Produktinstallation, keine Container, keine Migrationen und keine Hintergrunddienste für das PM-Setup.
- Ist keine Kopie und kein Remote-Lesezugriff vorhanden, erkläre, welcher Repo-Zugang fehlt. Berechtigungen erteilt der zuständige interne Ansprechpartner. Fahre mit nutzbarem Jira-Zugriff fort, ohne Spec-Abgleich zu behaupten.

## 3. Lokal merken und fortsetzen können

Beim beauftragten Setup speichere die bestätigten Quellen unter `.local/sources.md`, sobald sie feststehen. Prüfe vorher, dass `.local/` von Git ignoriert wird und nicht bereits getrackt ist; wenn das nicht gilt, behalte die Angaben vorerst im Chat. Bestehende Angaben gezielt aktualisieren und andere Inhalte erhalten. Kein Commit und kein Upload dieser Datei.

Speichere nur: gewähltes Profil, bestätigten Produktrepo-Pfad oder Repo-Link, Jira-Site ohne Zugangsdaten, Zeitpunkt und Umfang der tatsächlich durchgeführten Zugriffsprüfungen sowie noch offene Setup-Schritte. Keine Tickettexte, Namen anderer Personen, Zugangsdaten oder Anhänge. Markiere alte Prüfungen als datierte Beobachtungen, nicht als dauerhafte Zugriffsfreigabe.

Wenn Speichern nicht möglich ist, sage kurz, dass die Angaben nur im laufenden Chat verfügbar bleiben. Bei „Setup weiter“ lies den gespeicherten Stand bzw. den aktuellen Kontext und setze bei der offenen Stelle fort. Nach Anmeldung oder korrigiertem Pfad wiederhole nur die betroffene Prüfung. Ein Abbruch ist kein Anlass, alles erneut abzufragen.

## 4. Verständlicher Abschluss und erste Nutzung

Zeige für Jira, Specs und lokale Speicherung jeweils **geprüft**, **offen** oder **nicht verfügbar**, ergänzt um einen kurzen verständlichen Grund. „Geprüft“ beim Quellenzugriff verlangt eine erfolgreiche aktuelle Leseprüfung; das Vorhandensein einer Datei oder eines Tools reicht nicht. Ein erreichbarer Spec-Ordner allein belegt noch keinen erfolgreichen Ticket-Spec-Abgleich.

Bei beiden zugänglichen Quellen fahre mit dem bereits genannten Ticket fort: finde die passende Spec, fasse die fachliche Anforderung verständlich zusammen und benenne einen offenen Punkt oder sinnvollen Abnahmeschritt, sofern vorhanden. Wird keine passende Spec gefunden, melde diese Lücke. Erfinde keine Zuordnung, nur um den ersten Durchlauf abzuschließen.

Beispiel für einen teilweisen Abschluss:

> Die Rewrite-Specs kann ich lesen. Für Jira fehlt noch die Anmeldung. Deinen Repo-Pfad habe ich lokal gespeichert. Du kannst bereits Produktfragen stellen; den Abgleich mit einem Ticket prüfen wir nach der Anmeldung.

Beispiel nach erfolgreichem ersten Durchlauf:

> Jira und Rewrite-Specs sind erreichbar. Das genannte Ticket habe ich mit der passenden Spec abgeglichen und die Quellen lokal eingerichtet. Du kannst jetzt zum Beispiel fragen: „Was fehlt für die Abnahme?“

Verwende solche Erfolgsaussagen nur bei tatsächlich erfolgten Prüfungen. Behaupte weder allgemeine Teamfreigabe noch korrekte Produktumsetzung. Ein Setup-Abschluss beschreibt den aktuellen Zugriff und die erprobte Nutzung.
