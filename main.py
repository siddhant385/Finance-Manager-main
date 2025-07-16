
import typer
from src.financeManager import FinanceManager
from colorama import Fore, Style
from tabulate import tabulate
import csv

app = typer.Typer()
fm = FinanceManager()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(Fore.CYAN + "\n📊 Full Financial Summary\n" + Style.RESET_ALL)

        total_income = fm.get_total_income()
        total_expense = fm.get_total_expense()
        savings = fm.get_savings()
        avg_income = fm.get_average_monthly_income()
        avg_expense = fm.get_average_monthly_expense()
        top_tags = fm.get_top_expense_tags()
        trend = fm.get_last_n_months_trend()
        large_expenses = fm.get_large_expenses()

        typer.echo(Fore.GREEN + f"💰 Total Income: ₹{total_income}")
        typer.echo(Fore.RED + f"💸 Total Expense: ₹{total_expense}")
        typer.echo(Fore.YELLOW + f"💼 Savings: ₹{savings}" + Style.RESET_ALL)

        typer.echo(Fore.BLUE + f"\n📈 Avg Monthly Income: ₹{round(avg_income,2)}")
        typer.echo(f"📉 Avg Monthly Expense: ₹{round(avg_expense,2)}" + Style.RESET_ALL)

        typer.echo(Fore.MAGENTA + "\n🔝 Top Expense Categories:")
        for item in top_tags:
            typer.echo(f"   • {item['tag']}: ₹{item['total']}")
        
        typer.echo(Fore.CYAN + "\n📊 Monthly Trend (Recent):")
        if trend:
            typer.echo(tabulate(trend, headers="keys", tablefmt="grid"))
        else:
            typer.echo("No monthly trend data available.")

        if large_expenses:
            typer.echo(Fore.RED + "\n⚠️ Large Transactions (₹10k+):")
            typer.echo(tabulate(large_expenses, headers="keys", tablefmt="grid"))
        else:
            typer.echo(Fore.GREEN + "\n✅ No large expenses detected.")

        typer.echo(Style.RESET_ALL)

@app.command()
def add(tag: str, amount: float, date: str, desc: str, transaction_type: str = typer.Option("expense", help="Type: income/expense")):
    fm.add_data(tag, amount, date, desc, transaction_type)
    typer.echo(Fore.GREEN + f"✅ Added ₹{amount} for '{tag}' on {date} ({transaction_type})" + Style.RESET_ALL)

@app.command()
def view_all():
    data = fm.get_all_data()
    if data:
        typer.echo(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    else:
        typer.echo(Fore.RED + "No data available." + Style.RESET_ALL)

@app.command()
def filter_date(date: str):
    data = fm.filter_by_date(date)
    if data:
        typer.echo(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + "No entries found on this date." + Style.RESET_ALL)

@app.command()
def filter_month(month: str = typer.Argument(..., help="Format: YYYY-MM")):
    data = fm.filter_by_month(month)
    if data:
        typer.echo(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + "No entries in this month." + Style.RESET_ALL)

@app.command()
def delete(id: int):
    fm.delete_data(id)
    typer.echo(Fore.RED + f"🗑️ Deleted entry with ID {id}" + Style.RESET_ALL)

@app.command()
def update(id: int, tag: str, amount: float, date: str, desc: str, transaction_type: str):
    fm.update_data(id, tag, amount, date, desc, transaction_type)
    typer.echo(Fore.BLUE + f"✏️ Updated ID {id} -> {tag}, ₹{amount}, {desc}, {transaction_type}" + Style.RESET_ALL)

@app.command()
def summary_tag(tag: str):
    data = fm.summary_by_tag(tag)
    if data:
        typer.echo(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        typer.echo(Fore.YELLOW + f"No entries with tag '{tag}'" + Style.RESET_ALL)

@app.command()
def export(path: str):
    data = fm.get_all_data()
    if not data:
        typer.echo(Fore.YELLOW + "No data available to export." + Style.RESET_ALL)
        return
        
    with open(path, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    typer.echo(Fore.GREEN + f"✅ Exported data to {path}" + Style.RESET_ALL)

@app.command()
def import_statement(file: str = typer.Argument(..., help="Path to bank CSV file"),
                     bank: str = typer.Argument(..., help="Bank name (e.g., pnb)")):
    fm.extract_bank_statement_to_db(file, bank)
    typer.echo(Fore.GREEN + f"📥 Imported and categorized transactions from {file} ({bank.upper()})" + Style.RESET_ALL)


if __name__ == "__main__":
    app()
