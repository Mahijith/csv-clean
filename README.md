# csv-clean

![CI](https://github.com/Mahijith/csv-clean/actions/workflows/ci.yml/badge.svg)

A production-grade CLI tool for cleaning messy CSV files.
Normalizes headers, strips whitespace, and drops empty rows.

## Features
- Snake_case header normalization
- Whitespace stripping from all string columns
- Empty row removal
- Structured logging with configurable verbosity
- Graceful error handling with clear messages

## Installation
```bash
pip install git+https://github.com/Mahijith/csv-clean.git
```

## Usage
```bash
# Basic usage
csv-clean input.csv

# With custom output path
csv-clean input.csv --output cleaned.csv

# Verbose mode — shows detailed log output
csv-clean input.csv --verbose
```

## Example
Input `messy.csv`:
```
First Name , Last Name ,  Email
  Alice ,  Smith , alice@email.com
Bob,Jones,
  ,  ,
```

Output `clean.csv`:
```
first_name,last_name,email
Alice,Smith,alice@email.com
Bob,Jones,
```

## Development
```bash
# Clone and install in editable mode
git clone https://github.com/Mahijith/csv-clean.git
cd csv-clean
uv pip install -e .

# Run tests
uv run pytest tests/ -v
```

## Tech stack
- Python 3.14
- typer — CLI framework
- pandas — data processing
- rich — terminal output
- pytest — testing
- GitHub Actions — CI
