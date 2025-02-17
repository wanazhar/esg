# esg.py
import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
import asyncio
from pathlib import Path
from typing import List, Optional

from esg.global_core import GlobalESGSystem
from models.esg_metrics import RefinitivESGScores
from reporting.global_reports import generate_refinitiv_table

app = typer.Typer(help="Global ESG Analysis System")
console = Console()

def create_layout() -> Layout:
    """Create a pretty layout for the terminal"""
    layout = Layout()
    layout.split_column(
        Layout(name="header"),
        Layout(name="body"),
        Layout(name="footer")
    )
    return layout

def display_header():
    console.print(Panel(
        "[bold cyan]Global ESG Analysis System[/bold cyan]\n"
        "[yellow]✦ 150+ Global Exchanges[/yellow]\n"
        "[yellow]✦ Real-time ESG Monitoring[/yellow]\n"
        "[yellow]✦ Refinitiv-based Scoring[/yellow]",
        border_style="blue"
    ))

def main_menu() -> str:
    display_header()
    
    console.print("\n[bold green]Available Options:[/bold green]")
    console.print("1. [cyan]View Detailed ESG Analysis[/cyan]")
    console.print("2. [cyan]View & Export to Excel[/cyan]")
    console.print("3. [cyan]AI-Assisted Report Retrieval[/cyan]")
    console.print("4. [cyan]Exit[/cyan]\n")
    
    return Prompt.ask(
        "Select option",
        choices=["1", "2", "3", "4"],
        default="1"
    )

async def process_analysis(
    symbols: List[str],
    system: GlobalESGSystem,
    export: bool = False,
    filename: Optional[str] = None
):
    try:
        with console.status("[bold green]Analyzing global ESG data...") as status:
            results = await system.analyze(symbols)
            
            if export and filename:
                results.save(filename)
                console.print(f"\n[bold green]✓ Report exported to {filename}[/bold green]")
            
            # Display detailed Refinitiv scores
            for symbol, data in results.items():
                console.print(f"\n[bold cyan]Analysis for {symbol}[/bold cyan]")
                console.print(generate_refinitiv_table(data))
                
    except Exception as e:
        console.print(f"\n[bold red]Error: {str(e)}[/bold red]")
        console.print("[dim]Tip: Check symbol format or try fewer symbols[/dim]")

@app.command()
def start():
    """Start the interactive ESG analysis interface"""
    system = GlobalESGSystem()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            symbols = Prompt.ask(
                "\nEnter ticker symbols (comma-separated)",
                default="AAPL.US,MSFT.US"
            ).split(",")
            asyncio.run(process_analysis(symbols, system))
            
        elif choice == "2":
            symbols = Prompt.ask(
                "\nEnter ticker symbols (comma-separated)",
                default="AAPL.US,MSFT.US"
            ).split(",")
            filename = Prompt.ask(
                "Export filename",
                default="esg_analysis.xlsx"
            )
            asyncio.run(process_analysis(symbols, system, export=True, filename=filename))
            
        elif choice == "3":
            query = Prompt.ask("\nEnter high-level query for AI-assisted report retrieval")
            reports = system.ai_assisted_report_retrieval(query)
            console.print("\n[bold cyan]AI-Assisted Report Retrieval Results:[/bold cyan]")
            for report in reports:
                console.print(f"- {report['name']}: {report['url']}")
            
        elif choice == "4":
            console.print("\n[yellow]Exiting ESG Analysis System...[/yellow]")
            break
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    app()