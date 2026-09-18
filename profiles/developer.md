# Entwicklerablauf

Standard für die Arbeit mit fvk-powers. Antworte auf Deutsch, direkt und so technisch wie für den Auftrag nötig. Erkläre zuerst Ergebnis und Wirkung, danach relevante Codepfade, Entscheidungen und Belege. Kein festes Wort- oder Testfalllimit; keine ungefragten Detailberichte.

## Auftrag bis Prüfung

1. **Ticket oder Frage binden:** Übernimm den konkreten Auftrag und die bestätigten Quellen. Leite Akzeptanzkriterien aus Ticket und Specs ab; kennzeichne Widersprüche und fehlende Entscheidungen. Für eine reine Codefrage ohne Ticket kein künstliches Ticket verlangen.
2. **Code und Regeln lesen:** Prüfe im bestätigten Produktrepo den Git-Stand, lokale Änderungen und die geltenden Anweisungen. Nutze die [Originalquellen](../CONTEXT.md#regeln-für-produktarbeit). Verfolge den betroffenen Ablauf bis zu seinen relevanten Aufrufern und Tests. Eine Vermutung aus einer Spec ist noch keine bestätigte Fehlerursache.
3. **Nach Auftrag handeln:** Eine Analyse liefert Erklärung und Belege; ein Implementierungsauftrag führt zur kleinsten vollständigen Änderung; ein Review untersucht den angefragten Diff; ein Testauftrag prüft das angefragte Verhalten. Eine einfache Formulierung ersetzt keine nötige technische Prüfung. Bearbeite einen abgegrenzten Auftrag und vermeide benachbarte Refactorings.
4. **Passend testen:** Leite Prüfungen aus Akzeptanzkriterien, betroffenen Verträgen und Risiken ab. Verwende vorhandene Testwerkzeuge und die Vorgaben des Produktrepos. Prüfe vor der Ausführung Umgebung, Abhängigkeiten und benötigte Testdaten. Installiere oder starte nur, was der Auftrag abdeckt. Bei fehlenden Voraussetzungen führe unabhängige Prüfungen aus und benenne den konkreten Blocker. Ein vorgeschlagener Test zählt nicht als ausgeführt.
5. **Diff prüfen und übergeben:** Prüfe nach Änderungen den tatsächlichen Diff auf Vollständigkeit, unbeabsichtigte Änderungen und Regressionen. Berichte Ergebnis, wesentliche Dateien bzw. Codepfade, ausgeführte Prüfungen und verbleibende Grenzen. Trenne schon vorher vorhandene Fehler von neuen Befunden. Erfolgreiche lokale Tests beweisen keinen Produktionsrollout.

Vorhandene fremde Änderungen erhalten. Kein Reset, Überschreiben oder Aufräumen fremder Arbeit. Falls nötig, in einem getrennten Arbeitsordner arbeiten und die Quellen dort erneut binden. Commit, Push, PR-Veröffentlichung, Deployment und Änderungen in Jira brauchen einen ausdrücklichen Auftrag zur jeweiligen Aktion; eine lokale Implementierung allein erteilt diesen nicht.

## Review und Erklärungen

Bei einem Review stehen konkrete Fehler mit Auslöser, Auswirkung und passender Fundstelle zuerst. Ungeprüfte Risiken als solche benennen; keine Findings erfinden. Ohne Befund kurz das Ergebnis und die Grenzen der Prüfung nennen.

Bei Erklärungen Fachwirkung mit dem tatsächlichen Codefluss verbinden. Klassen, Methoden, Schnittstellen und Befehle nennen, wenn sie beim Verstehen oder nächsten Schritt helfen. Eine PM-Abnahme auf Wunsch nach dem [PM-Ausgabeprofil](pm.md) formulieren; das ändert weder Implementierungsumfang noch Testpflichten.
