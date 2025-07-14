import datetime
import re
from calendar import Calendar
from unicodedata import east_asian_width

from dateutil import parser as dt_parser

WS = re.compile(r"\s+", flags=re.UNICODE)

def _remove_ws(s: str) -> str:
    return re.sub(WS, " ", s.strip())

def _fix_width(string: str, width: int) -> str:

    string_width = 0
    for s in string:
        if east_asian_width(s) in ["F", "W", "A"]:
            string_width += 2
        else:
            string_width += 1

    margin = max(width - string_width, 0)
    return string + " " * margin

def _normalize_timestr(
        timestr: str | datetime.datetime | None, 
        default: datetime.datetime = datetime.datetime.today()
    ) -> datetime.datetime:
    if timestr is None:
        return default
    elif isinstance(timestr, datetime.datetime):
        return timestr
    
    return dt_parser.parse(timestr)


def _month_calendar(year: int, month: int) -> str:
    """
    Generate a string representation of a month calendar with Rich markup:
    - Today's date is underlined.
    - Saturdays are colored cyan.
    - Sundays are colored magenta.

    Returns:
        A multi-line string with Rich markup tags.
    """
    sat_color = "cyan"
    sun_color = "magenta"

    cal = Calendar()
    today = datetime.date.today()
    
    # Header
    header_text = f"{year}年{month}月"
    padding = max((20 - len(header_text)) // 2, 0)
    # Underlined and bold header
    ym_header = "\n" + " " * padding + f"[underline][bold]{header_text}[/bold][/underline]\n"
    
    headers = ["Mo", "Tu", "We", "Th", "Fr", f"[{sat_color}]Sa[/{sat_color}]", f"[{sun_color}]Su[/{sun_color}]"]
    lines = [ym_header, " ".join(headers)]
    
    # Weeks
    for week in cal.monthdayscalendar(year, month):
        parts = []
        for idx, day in enumerate(week):
            if day == 0:
                part = "  "
            else:
                day_str = f"{day:2}"
                # underline today
                if year == today.year and month == today.month and day == today.day:
                    day_str = f"[underline]{day_str}[/underline]"
                # Saturday
                if idx == 5:
                    day_str = f"[{sat_color}]{day_str}[/{sat_color}]"
                # Sunday
                elif idx == 6:
                    day_str = f"[{sun_color}]{day_str}[/{sun_color}]"
                part = day_str
            parts.append(part)
        lines.append(" ".join(parts))
    
    return "\n".join(lines)