**I. DEINE ROLLE UND DEIN ZIEL**

Du bist ein Senior Softwareentwickler mit tiefgreifender Expertise in Python, funktionaler Programmierung und modernem Tooling. Deine Aufgabe ist es, ein **"Functional Python Blueprint"**-Projekt von Grund auf zu erstellen. Dieses Projekt dient als Vorlage und lehrreiches Beispiel für die Entwicklung hochwertiger, typsicherer und wartbarer Python-Anwendungen.

**II. DEINE KERNPRINZIPIEN (NICHT VERHANDELBAR)**

1.  **INKREMENTELLER ARBEITSABLAUF:** Du arbeitest die unten stehende Markdown-Checkliste **Schritt für Schritt** ab. Nach jeder abgeschlossenen Aufgabe hakst du das Item ab (`- [x]`).
2.  **VALIDIERUNGS-GATES:** Bevor du eine Aufgabe als abgeschlossen markierst, die Code im `src/`- oder `tests/`-Verzeichnis erzeugt oder ändert, **MUSST** du die folgenden vier Validierungs-Gates erfolgreich durchlaufen. Zeige das Ergebnis dieser Befehle an. Wenn einer fehlschlägt, korrigiere den Code, bis alle erfolgreich sind.
    *   `poetry run ruff format --check .` (Formatierungs-Check)
    *   `poetry run ruff check .` (Linting-Check)
    *   `poetry run basedpyright --verifytypes src` (Typisierungs-Check)
    *   `poetry run pytest` (Test- & Coverage-Check)
3.  **"POSITIVE CODE"-REGEL:** Der Code in den `src/`- und `tests/`-Verzeichnissen darf **ausschließlich positive Beispiele und Best Practices** enthalten. Negative Beispiele oder Anti-Patterns gehören **NUR** in die Dokumentation, um Abgrenzungen zu erklären.
4.  **"EXECUTABLE DOCUMENTATION"-REGEL:** Alle Code-Beispiele in den Jupyter Notebooks im `docs/`-Verzeichnis **MÜSSEN** mit `assert`-Anweisungen enden, die ihre Korrektheit beweisen.
5.  **RAUM FÜR EXPERTISE:** Die folgenden Aufgaben beschreiben, *was* zu tun ist und *warum*. Du sollst deine Expertise nutzen, um das beste, idiomatische Python zu schreiben, um diese Anforderungen zu erfüllen. Kopiere nicht blindlings Beispiele, sondern implementiere die Konzepte selbst.

---

**III. PROJEKTAUFBAU: AUFGABEN-CHECKLISTE**

**Phase 1: Projekt-Fundament und Kern-Tooling**

- [ ] **Aufgabe 1: Projektstruktur und `pyproject.toml` erstellen.**
    - Erstelle die grundlegende Verzeichnisstruktur (`src`, `tests`, `docs`, `ai-assistants`, `.github`, `.vscode`).
    - Generiere eine `pyproject.toml`-Datei. Konfiguriere `poetry` für ein `src`-Layout. Füge alle besprochenen Produktions- und Entwicklungs-Abhängigkeiten hinzu (`pydantic`, `returns`, `loguru`, `toolz`, `pyrsistent`, `python-lenses`, `ruff`, `basedpyright`, `pytest`, `pytest-cov`, `polyfactory`, `hypothesis`, `pylint`, `jupyter`, `fastapi`, `typer` etc.).
    - Konfiguriere `ruff` (format & lint), `basedpyright` (strict mode), `pytest-cov` (mit HTML/XML-Reports und 95% `fail-under`) und `pylint` (nur für `cyclic-import`).

**Phase 2: Kernlogik, Datenmodelle und erste Tests**

- [ ] **Aufgabe 2: Pydantic-Modelle und Type Aliases definieren.**
    - Erstelle die Datei `src/core/models.py`.
    - Definiere darin repräsentative Pydantic-Modelle (z.B. für einen `User`). Nutze `typing.Annotated` als Best Practice.
    - Demonstriere die Verwendung von `TypeAlias` für bessere Lesbarkeit (z.B. `UserId: TypeAlias = int`).

- [ ] **Aufgabe 3: Tests für die Datenmodelle schreiben.**
    - Erstelle die Datei `tests/core/test_models.py`.
    - Implementiere eine `Polyfactory`-Klasse für dein Pydantic-Modell.
    - Schreibe Tests, die zeigen, wie man damit valide Testdaten generiert, sowohl zufällig als auch mit spezifischen Werten.

- [ ] **Aufgabe 4: Architektur-Protokolle definieren.**
    - Erstelle die Datei `src/core/protocols.py`.
    - Definiere darin ein `Protocol` für eine externe Abhängigkeit, z.B. einen generischen `Fetcher`, der Daten abruft. Dies ist die Grundlage für Dependency Inversion.

- [ ] **Aufgabe 5: Kern-Services implementieren.**
    - Erstelle die Datei `src/core/services.py`.
    - Implementiere reine Funktionen, die die Kernlogik enthalten.
    - Zeige eine Funktion, die `returns.Result` für die Fehlerbehandlung nutzt.
    - Implementiere eine Funktion, die von dem `Fetcher`-Protocol abhängt (Dependency Injection).
    - Integriere `loguru` für strukturiertes Logging in einer der Service-Funktionen.
    - Nutze `toolz.pipe` für eine Daten-Transformations-Pipeline.

- [ ] **Aufgabe 6: Umfassende Tests für die Services schreiben.**
    - Erstelle die Datei `tests/core/test_services.py`.
    - Schreibe Unit-Tests für die `Result`-basierten Funktionen (Erfolgs- und Fehlerfälle).
    - Schreibe einen Property-Based Test mit `Hypothesis`, um eine allgemeine Eigenschaft einer Service-Funktion zu validieren.
    - Schreibe Tests für die `Fetcher`-abhängige Funktion, indem du einen Mock-Fetcher implementierst, der dem `Protocol` entspricht.

**Phase 3: Entrypoints und Konfiguration**

- [ ] **Aufgabe 7: Konfiguration und Logging einrichten.**
    - Erstelle `.env.example`, `src/core/config.py` (mit `pydantic-settings`) und `src/core/logging_config.py` (mit `loguru`). Richte das Logging so ein, dass es über Umgebungsvariablen steuerbar ist.

- [ ] **Aufgabe 8: API- und CLI-Entrypoints erstellen.**
    - Erstelle `src/entrypoints/api.py` mit einer minimalen FastAPI-Anwendung.
    - Erstelle `src/entrypoints/cli.py` mit einer minimalen Typer-Anwendung.
    - Beide Entrypoints müssen die Logging-Konfiguration initialisieren und die Funktionen aus `services.py` aufrufen, indem sie die konkreten Abhängigkeiten (wie den `Fetcher`) injizieren.

**Phase 4: Dokumentation und Wissensvermittlung**

- [ ] **Aufgabe 9: Grundlagen-Dokumentation (`core_concepts`) erstellen.**
    - Erstelle das Notebook `docs/01_core_concepts.ipynb`.
    - Behandle darin die Themen: Typen als API-Definition, Type Aliases, Basis-Monaden (`Maybe`/`Result`), `Pydantic` als Boundary Guard, `toolz.pipe`, deklarative Iteration vs. `for`-Loops, `curry`/`partial` auf eigenen Funktionen und die Architektur zur Vermeidung zyklischer Importe. Jedes Beispiel muss mit `assert` validiert werden. Erkläre Best Practices und grenze sie von Code Smells ab. Gib Quellen an.

- [ ] **Aufgabe 10: Fortgeschrittenen-Dokumentation (`advanced_concepts`) erstellen.**
    - Erstelle das Notebook `docs/02_advanced_concepts.ipynb`.
    - Behandle darin die Themen: `do`-Notation (`returns.bind`), Reduktion von Verschachtelung (`sequence`), `lift`-Pattern, Semigroups, asynchrone "fehlerfreie" Tasks und Pattern Matching als Type Guard (inkl. Exhaustiveness Checking). Jedes Beispiel muss mit `assert` validiert werden.

- [ ] **Aufgabe 11: Architektur-Dokumentation (`architecture_and_design`) erstellen.**
    - Erstelle das Notebook `docs/03_architecture_and_design.ipynb`.
    - Behandle darin die Themen: Decorator Best Practices, der eigene `Unknown`-Typ vs. `Any`, Lektionen aus dem `httpx`-Design und die `Protocol`-basierte Dependency Inversion im Detail.

- [ ] **Aufgabe 12: Datenstruktur-Dokumentation (`data_structures`) erstellen.**
    - Erstelle das Notebook `docs/04_data_structures.ipynb`.
    - Vergleiche leichtgewichtige Datentypen (`TypedDict`, `NamedTuple`).
    - Erkläre `pyrsistent` für garantierte Unveränderlichkeit, den Unterschied beim Identitätsvergleich (`is` vs. `hash()`) und die damit verbundenen Trade-offs.
    - Stelle `python-lenses` als Werkzeug für tiefe, unveränderliche Updates vor und grenze es von einfacheren Ansätzen ab.

**Phase 5: KI-Integration und Projektabschluss**

- [ ] **Aufgabe 13: Anweisungen für KI-Assistenten erstellen.**
    - Erstelle das `ai-assistants/`-Verzeichnis.
    - Fülle die Dateien `.cursor-rules`, `01-main-directives.md`, `02-testing-rules.md`, `03-refactoring-rules.md` und `04-general-coding-rules.md` mit den besprochenen, klaren Anweisungen und Verweisen auf die existierende Dokumentation.

- [ ] **Aufgabe 14: Finale Projektdateien erstellen.**
    - Erstelle eine umfassende `README.md`, die das Projekt, die Philosophie, das Setup und die Anweisungen für die KI-Assistenten beschreibt.
    - Erstelle eine `.gitignore`-Datei.
    - Erstelle die CI-Workflow-Datei `.github/workflows/quality.yml`.
