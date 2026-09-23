# Geführtes Setup im Chat

Diese Anleitung richtet sich an den Assistenten. Ziel: Nach dem Setup kann der PM ein echtes Ticket mit der passenden Spec abgleichen. Führe die Schritte selbst aus, soweit Werkzeuge und Auftrag es erlauben. Der Nutzer übernimmt nur Angaben, Anmeldungen und Zugriffsentscheidungen, die du nicht selbst erledigen kannst. Ein Link auf diese Datei erfüllt keinen Setup-Auftrag.

## 1. Vorhandenes prüfen

Beginne etwa so:

> Ich richte fvk-powers für dich ein. Dafür prüfe ich den Zugriff auf Jira und auf die Rewrite-Specs. Ich schaue zuerst, was schon da ist, und führe dich dann durch die fehlenden Schritte. Eine Entwicklerumgebung brauchst du nicht.

Frage nicht nach Rolle, Modell oder Antwortlänge; Deutsch und das PM-Profil sind Standard. Prüfe dann ohne Rückfrage:

- `.local/sources.md` und den laufenden Chat auf bereits bekannte Angaben. Ein gespeicherter Erfolg ist eine alte Beobachtung und wird frisch geprüft.
- Welche Datei- und Jira-Werkzeuge der Client tatsächlich anbietet. Erfinde keine Toolnamen.
- Den bekannten Produktpfad oder den Kandidaten `../fvk` auf lesbare Specs. Suche nicht auf dem ganzen Rechner.
- Beim lokalen Git-Weg `git --version`. Fehlt eine Grundvoraussetzung, führe mit dem passenden Abschnitt aus [Einrichtung von Anfang an](docs/DEPENDENCIES.md#einrichtung-von-anfang-an) durch genau den nächsten Schritt; Betriebssystem und Client ermittelst du aus verfügbaren Angaben und fragst nur, wenn die Anleitung davon abhängt.

Kündige Schritte kurz mit ihrem Zweck an und zeige Ergebnisse, keine Befehlsausgaben. Verlange für die PM-Nutzung keine Entwicklerpakete, Produktinstallation, Container oder Datenbank.

## 2. Fehlendes nacheinander klären

Stelle eine kurze Frage auf einmal, sag, wofür du die Angabe brauchst, und arbeite an unabhängigen Prüfungen weiter, während die Antwort aussteht. Bereits beantwortete Fragen stellst du nicht erneut.

### Jira

- Ist ein Ticketlink bekannt, übernimm Site und Schlüssel daraus. Sonst: „Schick mir einen Link zu einem Rewrite-Ticket, das du lesen kannst. Daran prüfe ich den Jira-Zugriff.“
- Lies das Ticket über den vorhandenen Connector. Geprüft ist Jira erst, wenn das zurückgegebene Ticket übereinstimmt und Beschreibung und Status lesbar sind; notiere die Abrufzeit. Ein installiertes Werkzeug allein ist kein Zugriff.
- Fehlt der Connector, nenne sofort den konkreten nächsten Schritt aus [Jira verbinden](docs/DEPENDENCIES.md#jira-verbinden) für den erkennbaren Client. Ist der Client nicht erkennbar, frag nicht erst danach: Nenne den Schritt für die Desktop-App (**Plugins** öffnen, **Atlassian** suchen, installieren und anmelden) und einen Satz, wo die Anleitung für andere Clients steht. Weichen Menüs ab, orientiere dich an den tatsächlich sichtbaren Optionen oder der offiziellen Anleitung, statt Schaltflächen zu raten. Installiere nichts ungefragt und bitte nie um Passwörter, Tokens oder Sitzungscookies. Nach einer Plugin-Installation ist oft ein neuer Chat nötig: Weise auf „Setup weiter“ hin.
- Unterscheide, soweit der Fehler es belegt: fehlende Anmeldung, fehlende Berechtigung, Ticket nicht gefunden, vorübergehender Fehler. Ist er uneindeutig, erfinde keine Ursache. Nenne den nächsten sinnvollen Schritt, statt denselben Abruf zu wiederholen. Fehlende Plugin-Freigabe klärt der Workspace-Administrator, fehlende Ticketrechte das Team.
- Möchte der Nutzer Jira später verbinden, mach mit den Specs weiter und markiere Jira als offen.

### Rewrite-Specs

- Einen bekannten Pfad prüfst du direkt. Ist nur der Kandidat `../fvk` gefunden, frag knapp, ob das das gewünschte Rewrite-Repo ist, sofern der Kontext es nicht bestätigt.
- Fehlt ein Pfad: „Hast du das Rewrite-Repo schon auf deinem Rechner? Dann nenne mir den Ordner, sonst hilft der interne Repo-Link. Dort liegen die fachlichen Beschreibungen, mit denen ich Tickets abgleiche.“
- Bei einem Ordner lies `docs/specs/features/README.md` und eine passende Spec. Prüfe Identität und Stand im Produktordner selbst: `git -C <produktrepo> rev-parse --show-toplevel HEAD` und `git -C <produktrepo> status --short`. Ein im übergeordneten Arbeitsrepo ungetrackter Ordner kann ein eigenes Repo mit gültigem Commit sein; ein Ordnername allein belegt nicht das richtige Repo.
- Bei einem Repo-Link nutzt du freigegebenen Lesezugriff, wenn er die Originaldateien erreicht. Ist ein Download nötig, klärst du Zielordner und Auftrag; einen vorhandenen Ordner überschreibst du nie.
- Ohne Kopie und Remote-Zugriff erklärst du, welcher Repo-Zugang fehlt und wer ihn intern freischaltet. Mit Jira geht es weiter, ohne einen Spec-Abgleich zu behaupten.

### Gemeinsames Wissen (optional)

Möchte der Nutzer eine Wissensbasis anbinden, frag nach ihrem Einstieg (Datei oder interne URL), lies ihn und einen zur aktuellen Frage passenden Kapitelverweis. Halte fest, was lesbar ist und welche verlinkten Originale fehlen. Speichere ihn als `Wissenseinstieg` mit Themenbereich, gelesenem Kapitel und Prüfzeit; relative Pfade beziehen sich auf das fvk-powers-Root. Ohne Wissensbasis bleibt alles andere nutzbar. Details: [Gemeinsames Wissen](CONTEXT.md#gemeinsames-wissen).

## 3. Lokal merken

Sobald Quellen feststehen, speicherst du sie in `.local/sources.md`, nachdem du geprüft hast, dass `.local/` von Git ignoriert und nicht getrackt ist; sonst bleiben die Angaben im Chat. Aktualisiere gezielt und erhalte andere Inhalte. Kein Commit, kein Upload.

Gespeichert werden nur: Profil, Produktrepo-Pfad oder -Link, Jira-Site ohne Zugangsdaten, optionaler Wissenseinstieg, Zeitpunkt und Umfang der tatsächlich durchgeführten Zugriffsprüfungen und offene Setup-Schritte. Keine Tickettexte, Namen anderer Personen, Zugangsdaten oder Anhänge.

Bei „Setup weiter“ liest du den gespeicherten Stand und den Chat und setzt an der offenen Stelle fort. Links, Pfade und Tickets, die im Chat oder in `.local/sources.md` schon stehen, verwendest du weiter, statt erneut danach zu fragen. Meldet der Nutzer eine Anmeldung, ist der nächste Schritt der Abruf des bereits genannten Tickets; nach einem korrigierten Pfad die Leseprüfung dieses Pfads. Wiederhole nur die betroffene Prüfung.

## 4. Abschluss und erste Nutzung

Zeige für **Jira**, **Specs** und **lokale Speicherung** jeweils **geprüft**, **offen** oder **nicht verfügbar** mit kurzem Grund. „Geprüft“ heißt: aktuell erfolgreich gelesen bzw. geschrieben und zurückgelesen.

- **Setup offen:** Die Antwort endet mit genau einem direkt ausführbaren nächsten Schritt: dem konkreten Bedien- oder Anmeldeschritt aus [Jira verbinden](docs/DEPENDENCIES.md#jira-verbinden) oder der Frage nach dem richtigen Ordner bzw. Repo-Link. „Zugriff offen“ allein hilft nicht weiter. Was schon geht, sagst du ausdrücklich, etwa „Du kannst bereits Fragen zu den Specs stellen.“
- **Beide Quellen erreichbar:** Mach mit dem genannten Ticket weiter: passende Spec finden, Anforderung verständlich zusammenfassen, einen offenen Punkt oder Abnahmeschritt nennen. Findest du keine passende Spec, sag das; erfinde keine Zuordnung.

Beispiele, nur bei tatsächlich erfolgten Prüfungen:

> Die Rewrite-Specs kann ich lesen, deinen Repo-Pfad habe ich lokal gespeichert. Für Jira fehlt noch die Anmeldung: Öffne in der App **Plugins**, suche nach **Atlassian** und installiere es. Fragen zu den Specs kannst du schon jetzt stellen.

> Jira und Rewrite-Specs sind erreichbar. Dein Ticket habe ich mit der passenden Spec abgeglichen. Frag zum Beispiel: „Was fehlt für die Abnahme?“

Ein Setup-Abschluss beschreibt den aktuellen Zugriff, keine Teamfreigabe und keine korrekte Produktumsetzung.
