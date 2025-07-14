from datetime import datetime, timedelta
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from . import estat
from . import util
from . import mathtools 

app = typer.Typer()
console = Console()

@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))

@app.command(name="is-prime")
def is_prime(x: int):
    """
    Prime number?
    """
    typer.echo(mathtools.is_prime(x))

@app.command()
def c(
        year: Annotated[int | None, typer.Argument(help="Year to display (defaults to current year)", show_default=False)] = None,
        month: Annotated[int | None, typer.Argument(help="Month to display (defaults to current month)", show_default=False)] = None
    ):

    if year is None:
        year = datetime.today().year
    
    if month is None:
        month = datetime.today().month

    cal = util._month_calendar(year, month)
    console.print(cal, highlight=False)

@app.command()
def r(
    days_before: Annotated[int, typer.Option("-b", "--days-before", help="From X days before today")] = 0,
    days_after: Annotated[int, typer.Option("-a", "--days-after", help="By X days after today")] = 7
):
    """
    e-stat.go.jp から政府統計の公表スケジュールを取得する。検索期間のデフォルトは今日の0日前から7日後まで。
    期間は days_before, days_after 引数で変更できる。

    Example:\n
    - zm stat\n
    - zm stat -b 4 -a 7
    """

    td = datetime.today()
    start = td - timedelta(days=days_before)
    end = td + timedelta(days=days_after)
    url, schedule = estat.fetch_release_schedule(start, end)

    table = Table(title=f"[link={url}]直近の政府統計公表スケジュール[/link]")

    table.add_column("日付", style="cyan", no_wrap=True)
    table.add_column("所管", style="magenta")
    table.add_column("統計")
    table.add_column("統計コード")

    for item in schedule:
        row = (item[0], 
               item[1], 
               f"[link={item[4]}]{item[2]}[/link]", 
               f"[link={item[5]}]{item[3]}[/link]")
        table.add_row(*row)

    console.print(table)

