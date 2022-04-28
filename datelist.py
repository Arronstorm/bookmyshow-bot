from scraperbase import Movienamescraper
from constants import monthslist

def Datelist(location, theatername, date, num):
    temp = []
    movielist = []
    monthname = monthslist[num]
    datetocheck = date.replace('-', '')
    soup = Movienamescraper(location, theatername, datetocheck)
    movie_list_finder = soup.find_all('div', {'class': 'date-numeric'})
   
    for liElement in movie_list_finder:
        temp.append(liElement.text)

    for i in range(len(temp)):
        temp1 = temp[i].replace('\t', '')
        temp2 = temp1.replace('\n', '')
        if temp2 == '01':
            monthname = monthslist[num + 1]
        movielist.append(temp2 +" "+ monthname)

    return movielist