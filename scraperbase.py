from bs4 import BeautifulSoup
import requests


def Movienamescraper(location, theatername, date):
    # url = "https://in.bookmyshow.com/"+ location +"/" + theatername + "/" + date
    url = 'https://in.bookmyshow.com/trivandrum/cinemas/pvr-kripa-trivandrum/SPIT/20220428'
    response = requests.get(url)

    return BeautifulSoup(response.text, 'lxml')

def Theaterlistscraper(location):
    url = "https://in.bookmyshow.com/"+location+"/cinemas"
    response = requests.get(url)

    return BeautifulSoup(response.text, 'html.parser')