import requests
from bs4 import BeautifulSoup
import csv
import time

file = open('formula1.csv', 'w', encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['Name', 'Surname', 'Country', 'Points', 'Year'])


year = 2015
while year < 2024:
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    all_year = soup.tbody
    all_driver = all_year.find_all('tr')

    for driver in all_driver:
        driver_name = driver.a.find('span', class_='hide-for-tablet').text
        driver_surname = driver.a.find('span', class_='hide-for-mobile').text
        driver_country = driver.find('td', class_='dark semi-bold uppercase').text
        driver_points = driver.find('td', class_='dark bold').text
        write_obj.writerow([driver_name, driver_surname, driver_country, driver_points, year])
    year += 1
    time.sleep(16)



