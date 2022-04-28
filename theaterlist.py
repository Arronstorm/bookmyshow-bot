import re

from scraperbase import Theaterlistscraper


def Location(location):
    theaterlist = []
    
    soup = Theaterlistscraper(location)
    theaters_div_finder = soup.find('div', {'class': 'cinema-brand-list row'})
    for link in theaters_div_finder.find_all("a", attrs={"href": re.compile("^/cinemas/")}):
        if (link.get("href") not in theaterlist):
            theaterlist.append(link.get("href"))

    return theaterlist
