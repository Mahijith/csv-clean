import typer
import pandas as pd
from pathlib import Path
from rich.console import Console
from csv_clean.transforms import (
    normalize_headers, strip_whitespace, drop_empty_rows
)

app = typer.Typer()
console = Console()

@app.command()
def clean(
    input_file: Path = typer.Argument(..., help="Input CSV path"),
    output: Path = typer.Option("clean_output.csv", help="Output path"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Clean a messy CSV file."""
    df = pd.read_csv(input_file)
    if verbose:
        console.print(f"[bold]Loaded:[/bold] {len(df)} rows")

    df = normalize_headers(df)
    df = strip_whitespace(df)
    before = len(df)
    df = drop_empty_rows(df)

    if verbose:
        console.print(f"[green]Dropped {before - len(df)} empty rows[/green]")

    df.to_csv(output, index=False)
    console.print(f"[bold green]✓ Saved {len(df)} rows → {output}[/bold green]")

if __name__ == "__main__":
    app()