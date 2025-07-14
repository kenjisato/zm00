import datetime
from typing import Optional
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from .util import _remove_ws, _normalize_timestr

def fetch_release_schedule(
    start: Optional[datetime.datetime | str] = None, 
    end: Optional[datetime.datetime | str] = None,
    period: Optional[str] = None
):
    """
    period:  
    """
    base_url = "https://www.e-stat.go.jp"

    start = _normalize_timestr(start)
    end = _normalize_timestr(end, start + datetime.timedelta(days=7))

    query_params = {
        'startYear': start.year,
        'startMonth': start.month,
        'startDay': start.day,
        'endYear': end.year,
        'endMonth': end.month,
        'endDay': end.day
    }
    
    with requests.Session() as session:  
        res = session.get(f"{base_url}/release-calendar", params=urlencode(query_params))
        url = res.url

    soup = BeautifulSoup(res.text, features="lxml")
    stat_rows = soup.find_all("li", class_="stat-list-row")

    result = []
    for row in stat_rows:
        cols = row.find_all("span") # type: ignore
        date, dept, comment = [_remove_ws(col.get_text()) for col in cols]
        code = cols[2].attrs["data-toukei_cd"] # type: ignore
        link1 = base_url + cols[2].a.attrs["href"].replace(".", "") # type: ignore
        link2 = base_url + "/statistics/" + code # type: ignore
        result.append((date, dept, comment, code, link1, link2))
    
    return (url, result)
    

if __name__ == "__main__":

    print(fetch_release_schedule())
