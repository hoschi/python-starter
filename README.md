# Functional Python Blueprint

[![Code Quality Check](https://github.com/<Your-GitHub-Username>/<Your-Repo-Name>/actions/workflows/quality.yml/badge.svg)](https://github.com/<Your-GitHub-Username>/<Your-Repo-Name>/actions/workflows/quality.yml)

This project is a highly opinionated, modern blueprint for building robust, type-safe, and maintainable Python applications using a pragmatic functional approach.

## Project Philosophy

1.  **Type Safety as a Foundation:** Every line of code is statically analyzable. The strictest mode of the best tools is the default, not the exception.
2.  **Functional, Not Dogmatic:** We use functional concepts (Pipelines, `Result` types, Immutability) where they improve clarity and maintainability, without sacrificing readability for Python developers.
3.  **AI-Assistant Optimized:** A single source of configuration (`pyproject.toml`) and clearly defined code structures make it easy for AI tools to understand the context and generate high-quality, compliant code.
4.  **Clear Boundaries:** We use `Pydantic` as a robust "shield" that separates the unpredictable outside world (APIs, DBs) from our clean, internal domain logic.
5.  **Modular and Scalable:** The structure is designed from the ground up to support various entrypoints (CLI, API, Agent-Loop) that all reuse the same core logic.

## Project Setup

### 1. Prerequisites
- [Conda](https://docs.conda.io/en/latest/miniconda.html) for environment management.
- [Poetry](https://python-poetry.org/docs/#installation) for package management.
- [Poe the Poet](https://poethepoet.natn.io/installation.html) for task management.

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/<Your-GitHub-Username>/<Your-Repo-Name>.git
cd <Your-Repo-Name>
```

Change project name 'py-starter' to yours
- `pyproject.toml`
- `conda.yml`

```bash
# Create and activate the conda environment
conda env create --file conda.yml
conda activate py-starter

# Install dependencies using Poetry
poetry install
```

## Daily Work

### Running the Applications

**Start the Web API:**
```bash
poetry run start-api
```
The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `http://127.0.0.1:8000/docs`.

**Start the CLI:**
```bash
poetry run start-cli --help
```
This will show you the available commands. For example:
```bash
poetry run start-cli get-user 1
poetry run start-cli transform "  Some Text  "
```

### Running Quality Checks

This project is equipped with a comprehensive set of quality gates. To run them all locally, use the following commands:

```bash
# Run linter and formatter check
poetry run ruff check .
poetry run ruff format --check .

# Run static type checking
poetry run basedpyright --verifytypes src

# Run tests and generate coverage reports
poetry run pytest
```

To view the interactive coverage report after running the tests, open `htmlcov/index.html` in your browser.

### Interactive Documentation

The `docs/` directory contains interactive Jupyter Notebooks. They are the best way to learn the core concepts and patterns used in this project.

1.  **Open the project in VS Code.**
2.  **Make sure you have the recommended extensions installed (VS Code will prompt you).**
3.  **Select the project's Python interpreter (`.venv/bin/python`).**
4.  **Open `docs/01_core_concepts.ipynb` or `docs/02_advanced_patterns.ipynb`.**
5.  **Run the code cells one by one to see the concepts in action.**

Each code cell ends with `assert` statements, making the documentation self-verifying.

## 🤖 Working with AI Assistants (Cursor, Gemini, etc.)

This project is specifically optimized to work with modern AI coding assistants. To ensure high code quality, we have created a "manifest" for AIs.

### Setup

**For Cursor:**
The `.cursor-rules` file in `ai-assistants/` is automatically detected by Cursor. It forces the AI to consider our project rules with every request. No further setup is needed.

**For `gemini-cli` or other tools:**
Explicitly include the main directive in your prompt. Example:
```bash
gemini "Refactor the 'process_data' function in 'src/core/services.py'. Strictly follow the instructions from 'ai-assistants/01-main-directives.md'."
```

### The Rules

The `ai-assistants/` directory contains the complete set of rules. The AI is automatically referred to the relevant documents to ensure it always operates within the project's context.
