# Rules for Writing Tests

- **Vollständige Abdeckung:** Jede neue Funktion in `src/core/services.py` benötigt mindestens einen Unit-Test in `tests/core/test_services.py`.
- **Test Data Generation:** Erstelle **IMMER** Testdaten für Pydantic-Modelle mit `Polyfactory`. Schreibe keine manuellen Dictionaries.
  - *Zweck & Beispiel:* Um Boilerplate zu reduzieren und sicherzustellen, dass Testdaten immer valide sind. Siehe `tests/core/test_models.py`.
- **Property-Based Testing:** Für jede Kern-Business-Logik-Funktion, füge mindestens einen Property-Based Test mit `Hypothesis` hinzu, um allgemeine Eigenschaften zu validieren.
  - *Zweck & Beispiel:* Um die Robustheit über tausende von Fällen zu beweisen, nicht nur Einzelfälle. Siehe die `@given`-Tests in `tests/core/test_services.py`.
- **Mocking:** Verwende **IMMER** Test-Doubles, die dem `Protocol` der Abhängigkeit entsprechen. Nutze keine Magie-Mocks ohne Spezifikation.
  - *Zweck & Beispiel:* Um sicherzustellen, dass Mocks und echter Code synchron bleiben. Siehe `MockUserFetcher` in `tests/core/test_services.py`.
