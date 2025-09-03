# General Coding Rules

- **Functional First:** Schreibe reine Funktionen, wann immer möglich. Vermeide Klassen für reine Datenstrukturen.
- **Strict Typing:** Jeder Code muss vollständig mit `BasedPyright` im `strict`-Modus validieren. Vermeide `Any`.
- **Error Handling:** Verwende **IMMER** `returns.Result` für Operationen, die fehlschlagen können. Wirf keine Exceptions für erwartbare Fehler.
  - *Zweck & Beispiel:* Um sicherzustellen, dass alle Fehlerfälle im Typsystem abgebildet und behandelt werden müssen. Siehe die lauffähigen Beispiele in `docs/01_core_concepts.ipynb`.
- **Data Boundaries:** Validiere **ALLE** externen Daten (API-Responses, DB-Queries, User-Input) mit `Pydantic`-Modellen an den Rändern der Anwendung.
  - *Zweck & Beispiel:* Um eine typsichere Domäne im Inneren der Anwendung zu garantieren. Siehe die Pydantic-Beispiele in `docs/01_core_concepts.ipynb`.
- **Don't Repeat Yourself (DRY):** Vermeide Code-Duplizierung durch die Nutzung von wiederverwendbaren Service-Funktionen und Protokollen.
  - *Zweck & Beispiel:* Um die Wartbarkeit zu erhöhen. Das `Fetcher`-Protocol in `src/core/protocols.py` ist ein Beispiel für eine wiederverwendbare Abstraktion.
