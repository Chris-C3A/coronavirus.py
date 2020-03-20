#!/usr/local/bin/python3 
import requests
from bs4 import BeautifulSoup

# TODO
# add speech recognition feature
# add UI

infected_countries = []
# main setup
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

def main():
    # get all infected countries
    result = soup.find('tbody')
    trs = result.find_all('tr')
    for tr in trs:
        td = tr.find('td')
        # print(td.text.strip(), end='\n'*2)
        infected_countries.append(td.text.strip())
    print("Type A to check the general status for corona virus")
    print("Or Enter a country name to check its status", end='\n'*2)

    inp = input("> ")
    print('', end='\n'*3)

    if inp == 'A' or inp == 'a':
        get_general_status()
    elif inp in infected_countries or inp[0].upper() + inp[1::] in infected_countries:
        # change first letter to upercase
        inp = inp[0].upper() + inp[1::]
        data = get_status(inp)
        for key in data:
            print(key, data[key], sep=": ", end='\n'*2)


# get general data of corona virus
def get_general_status():
    maincounters = soup.find_all('div', id='maincounter-wrap')
    for counter in maincounters:
        title = counter.find('h1')
        count = counter.find('span')
        if None in (count, title):
            continue   
        print(title.text.strip(), count.text.strip(), sep="  ")

def get_status(country):
    result = soup.find('tbody')
    trs = result.find_all('tr')
    for tr in trs:
        td = tr.find('td')
        # print(td.text.strip(), end='\n'*2)
        col = ["Country","Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases", "Serious/Critical", "Tot Cases/1Mpop"]
        if country == td.text.strip():
            tds = tr.find_all('td')
            data = {}
            for td in tds:
                if td.text.strip() == '':
                    data[col[tds.index(td)]] = '0'
                else:
                    data[col[tds.index(td)]] = td.text.strip()
                
                # Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered, Active Cases, serious
    return data

    # return t_cases.text.strip()

# run program
if __name__ == "__main__":
    main()