#!/usr/local/bin/python3 
import requests
from bs4 import BeautifulSoup
import os
import sys

# TODO
# show results on a webserver (flask)
# add speech recognition feature
# add UI

infected_countries = []
# main setup
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# get all infected countries
result = soup.find('tbody')
trs = result.find_all('tr')
for tr in trs:
    td = tr.find('td')
    infected_country = td.text.strip()
    infected_countries.append(infected_country.lower())

def main():
    print("* Type A to check the general status for corona virus")
    print("* Enter a country's name to check its current status")
    print("* Use q to exit the program", end='\n'*2)

    inp = input("> ")
    print('', end='\n'*3)

    if inp in ['A', 'a']:
        get_general_status()
    elif inp.lower() in infected_countries:
        data = get_status(inp.lower())
        for key in data:
            print(key, data[key], sep=": ", end='\n'*2)
    elif inp in ['Q', 'q']:
        print('exiting...')
        clear_screen()
        exit(0)

# get general data of corona virus
def get_general_status():
    maincounters = soup.find_all('div', id='maincounter-wrap')
    for counter in maincounters:
        title = counter.find('h1')
        count = counter.find('span')
        if None in (count, title):
            continue   
        print(title.text.strip(), count.text.strip(), sep="  ")
    print('', end='\n'*3)

def get_status(country):
    result = soup.find('tbody')
    trs = result.find_all('tr')
    col = ["Country","Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases", "Serious/Critical", "Tot Cases/1Mpop"]
    for tr in trs:
        td = tr.find('td')
        # print(td.text.strip(), end='\n'*2)
        if country == td.text.strip().lower():
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

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]

def clear_screen():
    operating_system = get_platform()
    print(operating_system)
    if operating_system == "Windows":
        os.system("cls")
    elif operating_system in ["Linux", "OS X"]:
        os.system("clear")
# run program
if __name__ == "__main__":
    clear_screen()
    while True:
        main()
        input("ENTER TO CONTINUE...")
        clear_screen()