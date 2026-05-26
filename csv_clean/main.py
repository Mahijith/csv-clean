import typer
import pandas as pd
from pathlib import Path
from csv_clean.logger import get_logger
from csv_clean.transforms import (
    normalize_headers, strip_whitespace, drop_empty_rows
)

app = typer.Typer()
logger = get_logger(__name__)

@app.command()
def clean(
    input_file: Path = typer.Argument(..., help="Input CSV path"),
    output: Path = typer.Option("clean_output.csv", help="Output path"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Clean a messy CSV file."""
    if verbose:
        logger.setLevel("DEBUG")

    # --- validate input ---
    if not input_file.exists():
        logger.error(f"File not found: {input_file}")
        raise typer.Exit(code=1)

    if input_file.suffix.lower() != ".csv":
        logger.error(f"Expected a .csv file, got: {input_file.suffix}")
        raise typer.Exit(code=1)

    try:
        logger.info(f"Reading {input_file}")
        df = pd.read_csv(input_file)

        if df.empty:
            logger.error("CSV file is empty — nothing to clean")
            raise typer.Exit(code=1)

        logger.debug(f"Loaded {len(df)} rows, {len(df.columns)} columns")

        df = normalize_headers(df)
        logger.debug("Headers normalized")

        df = strip_whitespace(df)
        logger.debug("Whitespace stripped")

        before = len(df)
        df = drop_empty_rows(df)
        logger.debug(f"Dropped {before - len(df)} empty rows")

        df.to_csv(output, index=False)
        logger.info(f"Done — saved {len(df)} rows → {output}")

    except pd.errors.ParserError as e:
        logger.error(f"Could not parse CSV: {e}")
        raise typer.Exit(code=1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()