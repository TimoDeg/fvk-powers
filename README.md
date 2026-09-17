# fvk-powers

Ein Rewrite-Assistent für Produktmanager: Jira und passende Specs verstehen, Anforderungen abgleichen, Abnahmen vorbereiten und sinnvolle Ideen entwickeln. Die Antworten bleiben verständlich; technische Begriffe erscheinen nur, wenn sie bei einer Entscheidung helfen.

## Einstieg

1. Dieses private Repo lokal klonen und als Projekt in Codex öffnen.
2. Einen freigegebenen Jira-Connector im eigenen Client verbinden. Zugriff auf das Rewrite-Produktrepo bereitstellen, zum Beispiel als lokalen Checkout neben diesem Repo. Zugangsdaten bleiben im Connector bzw. im vorgesehenen Zugangssystem.
3. Im Chat schreiben: **„Richte fvk-powers für mich als PM ein. Prüfe meine Quellen und erkläre mir, was noch fehlt.“** Der Assistent klärt den Produktrepo-Pfad und die Jira-Quelle und prüft die tatsächlich verfügbaren Lesezugriffe. Für den Jira-Test ein konkretes Ticket nennen. Das Produkt muss dafür nicht lokal laufen.
4. Danach eine Frage stellen, zum Beispiel:
   - „Erkläre mir dieses Ticket und gleiche es mit den passenden Specs ab: [Ticketlink].“
   - „Welche fachlichen Entscheidungen fehlen noch?“
   - „Wie kann ich dieses Feature als PM abnehmen?“
   - „Welche kleinen Verbesserungen wären sinnvoll? Trenne Ideen von Anforderungen.“

Wenn der Produktcheckout anders heißt oder woanders liegt, genügt sein Pfad im Chat. Lokale Quellenangaben können bei der beauftragten Einrichtung unter `.local/sources.md` gespeichert werden. Dieser Ordner wird nicht veröffentlicht. Kein Token und kein Passwort gehört in diese Datei.

## So arbeitet der Assistent

**Frage → Jira und relevante Original-Specs → Abgleich → verständliche Antwort mit Quellen und nächsten Schritten.**

Die [Arbeitsregeln](AGENTS.md) steuern die Recherche. Das [PM-Profil](profiles/pm.md) bestimmt die Ausgabe. Die [Beispiele](examples/pm.md) zeigen den gewünschten Stil und dienen als einfache Abnahmefälle.

PM bedeutet eine verständliche Erklärung bei gründlicher Recherche. Der Assistent unterscheidet zwischen Anforderung, dokumentiertem Verhalten, tatsächlich geprüftem Verhalten und eigenen Vorschlägen. Eine Spec oder ein Jira-Status allein beweist keine fertige Umsetzung.

Die fachlichen Specs bleiben im Produktrepo gepflegt. Dieses Repo verteilt den Arbeitsablauf und die Antwortregeln. Es enthält keine privaten Ticketkopien, Produktquellen oder persönlichen Arbeitsverläufe.

## Stand und Grenzen

Erste Version als Anweisungspaket für einen Assistenten mit Dateizugriff und Jira-Werkzeugen. Sie installiert keinen Connector und verleiht keine Zugriffsrechte. Der erste Zielclient ist Codex; andere Clients müssen die Arbeitsregeln ausdrücklich laden und separat erprobt werden.

Der Ablauf ist standardmäßig lesend. Ticketentwürfe und Abnahmepläne können im Chat entstehen; Jira-Einträge, Produktänderungen und Veröffentlichungen brauchen einen entsprechenden ausdrücklichen Auftrag.

Vor dem Einsatz im Team auf einem frischen PM-Setup prüfen: ein echtes Ticket erklären, mit seiner Spec abgleichen und einen Abnahmeplan ableiten. Fehlende Zugriffe und widersprüchliche Quellen ebenfalls prüfen. Diese Erprobung ist noch offen; vorhandene Beispiele sind kein Nachweis einer funktionierenden Jira-Anbindung.
