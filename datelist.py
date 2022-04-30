from scraperbase import Movienamescraper
from constants import monthslist


def Datelist(location, theatername, date, num):
    tempDateArray = []
    dateListArray = []
    monthName = monthslist[num]
    
    datetocheck = date.replace('-', '')
    
    soup = Movienamescraper(location, theatername, datetocheck)
    date_list_finder = soup.find_all('div', {'class': 'date-numeric'})

    for divElement in date_list_finder:
        tempDateArray.append(divElement.text)

    for temporaryDateFormatPointer in range(len(tempDateArray)):
        tempDate = tempDateArray[temporaryDateFormatPointer].replace('\t', '').replace('\n', '')
        
        if tempDate == '01':
            monthName = monthslist[num + 1]
        dateListArray.append(tempDate + " " + monthName)

    return dateListArray
