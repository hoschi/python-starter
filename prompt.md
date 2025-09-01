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
5.  **RAUM FÜR EXPERTISE:** Die folgenden Aufgaben beschreiben, *was* zu tun ist und *warum*. Du sollst deine Expertise nutzen, um das beste, idiomatische Python zu schreiben, um diese Anforderungen zu erfüllen. Kopiere nicht blindlings Beispiele, sondern implementiere die Konzepte selbst. Verwende deine Funktion im Internet nach Details zu suchen. Benutze Context7.

---

**III. PROJEKTAUFBAU: AUFGABEN-CHECKLISTE**

- [ ] **Aufgabe 1: Projektstruktur und `pyproject.toml` erstellen.**
    - Erstelle die Verzeichnisstruktur: `src`, `tests`, `docs`, `ai-assistants`, `.github/workflows`, `.vscode`.
    - Generiere eine `pyproject.toml`-Datei mit den folgenden Inhalten:
        - **`[tool.poetry]`**: Konfiguriere `poetry` für Python `^3.12` und ein `src`-Layout (`packages = [{include = "src"}]`).
        - **`[tool.poetry.dependencies]`**: Füge hinzu: `pydantic`, `pydantic-settings`, `returns`, `loguru`, `toolz`, `pyrsistent`, `python-lenses`.
        - **`[tool.poetry.extras]`**: Erstelle Extras für `api` (`fastapi`, `uvicorn`) und `cli` (`typer`).
        - **`[tool.poetry.group.dev.dependencies]`**: Füge hinzu: `ruff`, `basedpyright`, `pytest`, `pytest-cov`, `polyfactory`, `hypothesis`, `pylint`, `jupyter`.
        - **`[tool.poetry.scripts]`**: Füge Skripte hinzu: `start-api = "src.entrypoints.api:main"` und `start-cli = "src.entrypoints.cli:main"`.
        - **`[tool.ruff]`**: Konfiguriere `ruff format` und `ruff lint` mit den Regeln `E, F, W, I, UP, B, SIM, ARG`.
        - **`[tool.basedpyright]`**: Konfiguriere den `strict` mode, den `stubPath = "stubs"` und aktiviere alle `reportUnknown... = "error"`-Regeln.
        - **`[tool.pytest.ini_options]`**: Konfiguriere `pytest-cov` für HTML- und XML-Reports und ein `--cov-fail-under=95`-Limit.
        - **`[tool.pylint.main]`**: Deaktiviere alle Regeln (`disable=all`) und aktiviere nur `cyclic-import`.

**Phase 2: Kernlogik, Datenmodelle und erste Tests**

- [ ] **Aufgabe 2: Pydantic-Modelle und Type Aliases definieren.**
    - Erstelle `src/core/models.py`.
    - Definiere ein Pydantic-Modell `User` mit Feldern wie `id: int`, `name: str`, `age: int`. Verwende `typing.Annotated` und `pydantic.Field` für Constraints (z.B. `min_length=2`).
    - Definiere einen `TypeAlias` `UserId: TypeAlias = int`.

- [ ] **Aufgabe 3: Tests für die Datenmodelle schreiben.**
    - Erstelle `tests/core/test_models.py`.
    - Implementiere eine `UserFactory(ModelFactory[User])` mit `Polyfactory`.
    - Schreibe einen Test, der `UserFactory.build()` verwendet, um eine valide Instanz zu erstellen.
    - Schreibe einen zweiten Test, der `UserFactory.build(name="Specific Name")` verwendet, um Felder zu überschreiben.

- [ ] **Aufgabe 4: Architektur-Protokolle definieren.**
    - Erstelle `src/core/protocols.py`.
    - Definiere ein generisches `Fetcher(Protocol[KeyType, ReturnType])` mit einer Methode `async def fetch_by_id(self, key: KeyType) -> ReturnType | None: ...`.

- [ ] **Aufgabe 5: Kern-Services implementieren.**
    - Erstelle `src/core/services.py`.
    - Implementiere eine Funktion `get_user_details(user_fetcher: Fetcher[int, User], user_id: int) -> Result[User, str]`, die von dem `Fetcher`-Protocol abhängt.
    - Implementiere eine zweite, einfache Funktion, die `toolz.pipe` nutzt, um einen String zu transformieren (z.B. `strip` und `lower`).
    - Importiere `loguru.logger` und füge Log-Nachrichten in beiden Funktionen hinzu.

- [ ] **Aufgabe 6: Umfassende Tests für die Services schreiben.**
    - Erstelle `tests/core/test_services.py`.
    - Schreibe Unit-Tests für `get_user_details`, die einen `MockUserFetcher` verwenden, der das `Fetcher`-Protocol implementiert. Teste den Erfolgs- und den Fehlerfall.
    - Schreibe einen Property-Based Test mit `@given(st.text())` von `Hypothesis` für die String-Transformations-Funktion.

**Phase 3: Entrypoints und Konfiguration**

- [ ] **Aufgabe 7: Konfiguration und Logging einrichten.**
    - Erstelle eine `.env.example`-Datei mit den Variablen `LOG_LEVEL` und `LOG_TO_FILE`.
    - Erstelle `src/core/config.py` mit einer `pydantic_settings.BaseSettings`-Klasse, um diese Variablen zu laden.
    - Erstelle `src/core/logging_config.py` mit einer `setup_logging()`-Funktion, die `loguru` basierend auf der Konfiguration einrichtet.

- [ ] **Aufgabe 8: API- und CLI-Entrypoints erstellen.**
    - Erstelle `src/entrypoints/api.py` mit einer FastAPI-Anwendung.
    - Erstelle `src/entrypoints/cli.py` mit einer Typer-Anwendung.
    - Beide müssen `setup_logging()` aufrufen und eine konkrete Implementierung des `Fetcher`-Protocols instanziieren und an die Service-Funktionen übergeben.

**Phase 4: Dokumentation und Wissensvermittlung**

- [ ] **Aufgabe 9: Grundlagen-Dokumentation (`core_concepts`) erstellen.**
    - Erstelle `docs/01_core_concepts.ipynb`.
    - Erkläre und demonstriere darin:
        - Typen als API-Definition (FastAPI/Pydantic).
        - Lesbarkeit durch `TypeAlias`.
        - Basis-Monaden `Maybe`/`Result` (Railway Oriented Programming vs. `try/except`).
        - `Pydantic` als Boundary Guard (vs. "Primitive Obsession").
        - `toolz.pipe` für funktionale Pipelines.
    - Jedes Beispiel muss mit `assert` validiert werden. Gib Quellen an.

- [ ] **Aufgabe 10: Funktionale Muster (`functional_patterns`) erstellen.**
    - Erstelle `docs/02_functional_patterns.ipynb`.
    - Erkläre und demonstriere darin:
        - Deklarative Iteration (Comprehensions, `toolz.map/filter` vs. `for`-Loops).
        - Partielle Anwendung mit `toolz.curry` auf selbstgeschriebenen Funktionen.
        - Logische Operationen (`allPass`, `anyPass`) mit `toolz` und Lambdas.
    - Jedes Beispiel muss mit `assert` validiert werden.

- [ ] **Aufgabe 11: Fortgeschrittenen-Dokumentation (`advanced_concepts`) erstellen.**
    - Erstelle `docs/03_advanced_concepts.ipynb`.
    - Erkläre und demonstriere darin:
        - `returns.do` als `do`-Notation.
        - Reduktion von Verschachtelung mit `returns.iterables.sequence`.
        - Das `lift`-Pattern mit `.map` und `.apply`.
        - Semigroups (am Beispiel von Konfigurations-Merges).
        - Asynchrone, fehlerfreie Tasks mit `returns.Future`.
    - Jedes Beispiel muss mit `assert` validiert werden.

- [ ] **Aufgabe 12: Architektur-Dokumentation (`architecture_and_design`) erstellen.**
    - Erstelle `docs/04_architecture_and_design.ipynb`.
    - Erkläre und demonstriere darin:
        - `match/case` als Type Guard mit Exhaustiveness Checking.
        - Decorator Best Practices (`functools.wraps`, `ParamSpec`).
        - Implementierung eines eigenen, sicheren `Unknown`-Typs als Alternative zu `Any`.
        - Design-Lektionen von `httpx` (z.B. Async-First Design).

- [ ] **Aufgabe 13: Datenstruktur-Dokumentation (`data_structures`) erstellen.**
    - Erstelle `docs/05_data_structures.ipynb`.
    - Vergleiche leichtgewichtige Datentypen (`TypedDict`, `NamedTuple`, `frozen dataclass`).
    - Erkläre `pyrsistent` für garantierte Unveränderlichkeit und den Unterschied zwischen `is` und `hash()`-basierten Vergleichen.
    - Stelle `python-lenses` für tiefe Updates vor und grenze es von einfacheren Ansätzen ab.

**Phase 5: KI-Integration und Projektabschluss**

- [ ] **Aufgabe 14: Anweisungen für KI-Assistenten erstellen.**
    - Erstelle das `ai-assistants/`-Verzeichnis mit den Dateien `.cursor-rules`, `01-main-directives.md`, `02-testing-rules.md`, `03-refactoring-rules.md` und `04-general-coding-rules.md`.
    - Fülle diese Dateien mit expliziten Anweisungen und Verweisen auf die erstellte Dokumentation, um die Einhaltung der Projekt-Standards zu gewährleisten.

- [ ] **Aufgabe 15: Finale Projektdateien erstellen.**
    - Erstelle eine umfassende `README.md`, die das Projekt, die Philosophie, das Setup, die Startbefehle für API/CLI und die Anweisungen für die KI-Assistenten beschreibt (inklusive der "Troubleshooting"-Sektion für zyklische Importe).
    - Erstelle eine passende `.gitignore`-Datei.
    - Erstelle die CI-Workflow-Datei `.github/workflows/quality.yml`.
