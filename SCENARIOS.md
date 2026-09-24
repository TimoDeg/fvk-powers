# Abnahme mit der Scenario-Engine (optional)

Die Journey-Scenario-Engine im Rewrite-Repo fährt die Kundenstrecke im echten Browser: Eingabe, Vergleich, Tarifdetail, Checkout, optional Testbestellung und Kundenbereich. Sie schreibt ein Manifest mit dem, was der Browser tatsächlich angezeigt hat. Damit wird aus einer Prüfsituation etwas Ausführbares, und das Ergebnis ist eine Beobachtung mit eigener Herkunft. Dieses Modul ist optional; die geführte Abnahme aus dem [PM-Profil](profiles/pm.md#geführte-abnahme-und-bug-entwurf) funktioniert ohne sie.

**Originale, vor dem ersten Entwurf lesen:** `docs/end2end/scenario-engine/scenario-engine.md` (Felder, Befehle, Sicherheit) und `deployables/frontend-journey/e2e-scenario-engine/schema/scenario.schema.json`, dazu ein vorhandenes Szenario unter `scenarios/` im selben Paket als Muster. Kopiere die Doku nicht hierher; Felder können sich ändern.

## Passt das Ticket?

Die Engine deckt nur die Kundenstrecke ab. Tickets zu Tarifverwaltung, Versichererverwaltung, CRM oder reinen Texten und Layouts lassen sich nicht als Szenario ausdrücken; sag das in einem Satz und biete die geführte Abnahme an. Auch innerhalb der Strecke prüft `expect` nur Ergebnisanzahl, Versicherer und Preisspanne. Alles andere aus den Akzeptanzkriterien (Hinweistexte, Layout, Fehlermeldungen) bleibt ein manueller Prüffall und wird so benannt.

## Stufe 1: Szenario entwerfen und prüfen

1. Übersetze die Akzeptanzkriterien in ein Szenario-Dokument nach dem Schema: Eingaben (`entry`), Verfeinerungen, Tarifauswahl (`selection`) und Erwartung (`expect`). Relative Daten wie `{ "age": 35 }` statt fester Daten. **`mode` ist immer `dry-run`**; dann stoppt die Engine vor der Bestellung.
2. Werte, die Ticket und Spec nicht vorgeben, übernimmst du aus den Engine-Standards oder einem vorhandenen Szenario und listest sie als **Annahmen**. Erfinde keine fachlichen Erwartungen.
3. Speichere den Entwurf als JSON unter `.local/scenarios/<TICKET>-<kurzname>.json` (Zielprüfung wie bei [Stand speichern](CONTEXT.md#stand-speichern)). Nichts davon kommt ins Produktrepo.
4. Prüfe ihn ohne Browser und ohne Zugangsdaten, wenn `tools/doctor.py` die Engine als installiert meldet: im Engine-Ordner `npm run scenario -- --scenario <absoluter Pfad> --plan-only`. Zeig dem PM den aufgelösten Plan in fachlichen Worten. Ist die Engine nicht installiert, sag das: Die einmalige Installation (`npm ci` und `npx playwright install chromium` im Engine-Ordner) braucht einen ausdrücklichen Auftrag oder übernimmt ein Entwickler. Den Entwurf und den Prüfbefehl lieferst du trotzdem.

Die Antwort nennt: was das Szenario prüft, was manuell bleibt, die Annahmen und den nächsten Schritt.

## Stufe 2: Lauf auf test oder preview

Nur auf ausdrücklichen Auftrag („Führe das Szenario aus“), nur mit `--env test` oder `--env preview`.

- **Testkonto:** Jede Person nutzt ihr eigenes Testkonto, erkennbar als Testkunde an einer CHECK24-Plus-Adresse (etwa `vorname.nachname+fvk-e2e@check24.de`). Die Person trägt E-Mail und Passwort selbst in die von Git ausgeschlossene `.env.local` im Engine-Ordner ein. Du fragst nie nach dem Passwort, liest es nicht aus und schreibst es nirgends hin. Im [Profil](CONTEXT.md#profil) steht höchstens der Alias.
- **Harte Grenzen:** Wird eine Live-Bestellung verlangt, lehnst du ab und bietest einen Dry-Run auf test oder preview an. Kein `--env live` für Bestellungen, nie `--allow-live-convert`, keine `.env`-Änderung durch dich. `mode: convert` nur auf ausdrücklichen Wunsch, nur auf test oder preview; die Engine prüft dann selbst die Testidentität und bricht sonst ab.
- **Auswerten:** Lies danach `test-results/scenario-engine/latest-manifest.json` und bei Fehlern das Fehlerbündel. Jede Beobachtung bekommt die Herkunft „Engine-Lauf <run-id>, <Umgebung>, <Zeit>“. Werte jeden Fall wie in der geführten Abnahme als **bestanden**, **abweichend** oder **offen**; was das Manifest nicht zeigt, bleibt offen. Eine Abweichung wird ein Bug-Entwurf mit run-id, nicht erstellt.

Ein grüner Lauf ist eine Beobachtung auf einem Stand, keine Abnahme und keine Freigabe.
