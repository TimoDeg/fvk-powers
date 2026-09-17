# PM-Beispiele und Abnahme

Alle folgenden Inhalte sind erfunden. Sie sind Stilbeispiele und keine Aussagen über das Rewrite-Produkt. In echten Antworten werden die tatsächlich gelesenen Originalquellen verlinkt; hier gibt es bewusst keine erfundenen Jira-URLs.

## 1. Ticket und passende Spec erklären

**Beispielquellen:** Ein Ticket fordert, Favoriten auf einer Vergleichsseite zu markieren. Die zugehörige Spec begrenzt die Auswahl auf drei Favoriten und verlangt bei einer vierten Auswahl einen Hinweis, ohne eine bestehende Auswahl zu entfernen. Speicherung über das Schließen der Seite hinaus ist nicht beschrieben.

**Frage:** „Was soll passieren und was fehlt noch?“

**Beispielantwort:**

Kunden sollen bis zu drei Angebote als Favoriten markieren können. Wählen sie ein viertes aus, erscheint laut Spec ein Hinweis; die drei bisherigen Favoriten bleiben erhalten.

Offen ist, ob die Auswahl nach dem Schließen und erneuten Öffnen der Seite noch vorhanden sein soll. Das sollten wir vor der Abnahme klären. Aus Ticket und Spec allein lässt sich nicht ableiten, ob die Funktion schon umgesetzt ist.

**Prüfpunkt:** Die Antwort erhält das Limit, den vierten Auswahlversuch und das Verhalten der bisherigen Auswahl. Sie erfindet keine dauerhafte Speicherung und keine Umsetzung.

## 2. Widerspruch sichtbar machen

**Beispielquellen:** Das Ticket verlangt drei Favoriten. Die Spec erlaubt fünf. Es gibt keinen Hinweis, dass eine Quelle die andere ersetzt.

**Frage:** „Kann ich das so abnehmen?“

**Beispielantwort:**

Die erlaubte Anzahl ist noch nicht eindeutig: Das Ticket nennt drei Favoriten, die Spec fünf. Für diesen Punkt fehlt daher ein verbindliches Abnahmekriterium.

Klärt zuerst, welches Limit gelten soll. Danach lässt sich gezielt prüfen, was beim nächsten Auswahlversuch passiert. Die widersprüchlichen Angaben allein sagen noch nicht, dass die Anwendung fehlerhaft ist.

**Prüfpunkt:** Die Antwort entscheidet den Konflikt nicht eigenmächtig und verwechselt ihn nicht mit einem nachgewiesenen Fehler.

## 3. Abnahme und Idee trennen

**Beispielquellen:** Die Anforderungen aus Beispiel 1 gelten, das Limit drei ist bestätigt. Es gibt keine Vorgabe für einen Zähler.

**Frage:** „Was sollte ich testen? Hast du eine Idee zur Verbesserung?“

**Beispielantwort:**

Für die Abnahme würde ich diese Fälle prüfen; die Prüfungen sind noch nicht ausgeführt:

| Ausgangslage | Handlung | Erwartung laut Beispiel-Spec |
| --- | --- | --- |
| Zwei Favoriten ausgewählt | Ein drittes Angebot markieren | Alle drei bleiben ausgewählt. |
| Drei Favoriten ausgewählt | Ein viertes Angebot markieren | Ein Hinweis erscheint; die ursprünglichen drei bleiben ausgewählt. |

**Idee:** Ein Zähler wie „2 von 3 ausgewählt“ könnte das Limit vor dem nächsten Klick erklären. Das ist ein zusätzlicher Vorschlag. Vor einer Aufnahme in den Umfang sollten wir prüfen, ob Kunden das Limit mit dem bisherigen Hinweis bereits verstehen.

**Prüfpunkt:** Der Zähler erscheint nicht als verbindliche Anforderung. Die Antwort behauptet weder bestandene Tests noch gemessenen Nutzen.

## 4. Fehlende Quelle

**Beispielquellen:** Das Ticket ist lesbar; das Produktrepo ist nicht zugänglich.

**Frage:** „Passt das Ticket zur Spec?“

**Beispielantwort:**

Ich kann die Anforderung aus dem Ticket erklären, aber den Abgleich mit der Spec noch nicht bestätigen: Mir fehlt Zugriff auf das Produktrepo. Sobald der Repo-Pfad mit Lesezugriff verfügbar ist, lässt sich prüfen, ob beide dasselbe Verhalten beschreiben.

**Prüfpunkt:** Die Antwort erfindet weder eine Spec noch das Ergebnis des Abgleichs. Umgekehrt gilt: Ohne Jira-Zugriff dürfen Specs erklärt, aber kein aktueller Ticketstatus behauptet werden.

## Erprobung mit einem PM

Für einen Vergleich dieselben Quellen und dieselbe Frage verwenden. Ein PM beurteilt: Ist die Antwort fachlich richtig, ohne Entwicklerwissen verständlich, mit Quellen nachvollziehbar und für den nächsten Schritt hilfreich? Ausgelassene Bedingungen und erfundene Fakten sind Fehler, auch bei angenehm lesbarer Sprache.

Auf einem frischen Setup mit echten zugänglichen Quellen zusätzlich prüfen: exaktes Ticket gelesen, passende Original-Spec gefunden, Quellenkonflikt offengelegt, Zugriffsfehler klar benannt. Ergebnisse lokal halten; keine privaten Ticketinhalte in diese Beispielsammlung übernehmen.

## Setup-Dialog prüfen

Diese Fälle dienen zur manuellen Abnahme des [Setup-Dialogs](../SETUP.md); sie sind noch kein Nachweis eines ausgeführten Erststarts.

| Ausgangslage | Eingabe | Erwartetes Verhalten |
| --- | --- | --- |
| Keine Quellen gespeichert | „Setup“ | Erklärt das Ziel, prüft vorhandene Werkzeuge und Pfade, fragt nur nach der nächsten fehlenden Angabe. |
| Jira-Werkzeug fehlt, Specs sind lesbar | „Richte es ein“ | Erklärt den nötigen Verbindungsschritt ohne erfundene UI-Anleitung; Spec-Fragen bleiben möglich. |
| Jira verbunden, Ticketzugriff verweigert | Ticketlink | Meldet den belegten Zugriffsfehler, fordert keine Geheimnisse an und behauptet keinen erfolgreichen Jira-Test. |
| Bestätigter Repo-Pfad existiert nicht | „Weiter“ | Fragt nach dem korrigierten Ordner oder internen Repo-Link; installiert keine Produktumgebung. |
| Einrichtung unterbrochen, Angaben lokal gespeichert | „Setup weiter“ | Nutzt bekannte Angaben, setzt den offenen Schritt fort und behandelt frühere Prüfungen als datiert. |
| Beide Quellen zugänglich, Ticket bekannt | „Loslegen“ | Prüft die Zugriffe und führt den ersten Ticket-Spec-Abgleich aus; fehlende Zuordnung wird offen benannt. |
| Lokaler Speicher schreibgeschützt oder nicht ignoriert | „Setup“ | Behält Quellenangaben im Chat und erklärt die fehlende dauerhafte Speicherung; veröffentlicht keine lokalen Angaben. |
| Vollständige Quellen, direkte Produktfrage | „Was muss ich bei diesem Ticket abnehmen?“ | Bearbeitet die Frage ohne unnötigen vollständigen Setup-Dialog. |
