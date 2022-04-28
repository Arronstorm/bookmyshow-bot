from scraperbase import Movienamescraper


def Movielist(location, theatername, date):
    movielist = []
    datetocheck = date.replace('-', '')
    soup = Movienamescraper(location, theatername, datetocheck)
    movie_list_finder = soup.find('ul', {'id': 'showEvents'})
    for liElement in movie_list_finder.find_all('a', {'class', 'nameSpan'}):
        screenName = liElement.get('href')
        if screenName != 0:
            lenofstr = len(screenName)
            name = screenName[8:lenofstr - 11]
            temp3 = name.replace('-', ' ')
            movielist.append(temp3.title())
    return movielist