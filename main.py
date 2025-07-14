import typer
from src.financeManager import FinanceManager
from colorama import Fore, Style
from tabulate import tabulate
import csv

app = typer.Typer()
fm = FinanceManager()

# 🎯 DEFAULT ENTRY (Just run `python main.py`)
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(Fore.CYAN + "\n📊 Finance Summary\n" + Style.RESET_ALL)

        tags = fm.get_all_tags()
        typer.echo(Fore.YELLOW + "📌 Tags: " + ", ".join(t[0] for t in tags) + Style.RESET_ALL)

        total = fm.get_total_expense()[0] or 0
        typer.echo(Fore.GREEN + f"💰 Total Expense: ₹{total}\n" + Style.RESET_ALL)

        data = fm.get_all_data()
        if data:
            headers = ["ID", "Tag", "Amount", "Date"]
            typer.echo(tabulate(data, headers, tablefmt="fancy_grid"))
        else:
            typer.echo(Fore.RED + "No expenses found." + Style.RESET_ALL)

# ➕ Add Expense
@app.command()
def add(tag: str, amount: float, date: str):
    fm.add_data(tag, amount, date)
    typer.echo(Fore.GREEN + f"✅ Added ₹{amount} for '{tag}' on {date}" + Style.RESET_ALL)

# 📋 View All
@app.command()
def view_all():
    data = fm.get_all_data()
    if data:
        typer.echo(tabulate(data, headers=["ID", "Tag", "Amount", "Date"], tablefmt="grid"))
    else:
        typer.echo(Fore.RED + "No data available." + Style.RESET_ALL)

# 🔍 Filter by Date
@app.command()
def filter_date(date: str):
    data = fm.filter_by_date(date)
    if data:
        typer.echo(tabulate(data, headers=["ID", "Tag", "Amount", "Date"], tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + "No expenses on this date." + Style.RESET_ALL)

# 📅 Filter by Month
@app.command()
def filter_month(month: str = typer.Argument(..., help="Format: YYYY-MM")):
    data = fm.filter_by_month(month)
    if data:
        typer.echo(tabulate(data, headers=["ID", "Tag", "Amount", "Date"], tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + "No expenses in this month." + Style.RESET_ALL)

# ❌ Delete by ID
@app.command()
def delete(id: int):
    fm.delete_data(id)
    typer.echo(Fore.RED + f"🗑️ Deleted expense with ID {id}" + Style.RESET_ALL)

# ✏️ Update Expense
@app.command()
def update(id: int, tag: str, amount: float, date: str):
    fm.update_data(id, tag, amount, date)
    typer.echo(Fore.BLUE + f"✏️ Updated ID {id} to {tag}, ₹{amount} on {date}" + Style.RESET_ALL)

# 🏷️ Summary by Tag
@app.command()
def summary_tag(tag: str):
    data = fm.summary_by_tag(tag)
    if data:
        typer.echo(tabulate(data, headers=["ID", "Tag", "Amount", "Date"], tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + f"No expenses with tag '{tag}'" + Style.RESET_ALL)

# 💾 Export to CSV
@app.command()
def export(path: str):
    data = fm.get_all_data()
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Tag", "Amount", "Date","Desc"])
        writer.writerows(data)
    typer.echo(Fore.GREEN + f"✅ Exported data to {path}" + Style.RESET_ALL)

# 📥 Import Bank Statement
@app.command()
def import_statement(file: str = typer.Argument(..., help="Path to bank CSV file"),
                     bank: str = typer.Argument(..., help="Bank name (e.g., pnb)")):
    """
    Imports a bank statement and stores tagged transactions in the database.
    """
    fm.extract_bank_statement_to_db(file, bank)
    typer.echo(Fore.GREEN + f"📥 Imported and categorized transactions from {file} ({bank.upper()})" + Style.RESET_ALL)


if __name__ == "__main__":
    app()