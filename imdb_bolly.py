import requests
from bs4 import BeautifulSoup
import csv

def extract(country):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.magicbricks.com/'
    }

    with requests.Session() as session:
        session.headers.update(headers)
        url = f'https://www.imdb.com/search/title/?title_type=feature&countries={country}&languages=hi'
        # Add code to capture and include cookies if needed
        r = session.get(url)
        #return r.status_code
        soup = BeautifulSoup(r.content,'html.parser')
        return(soup)

def transform(soup):
    movie_data = []
    divs = soup.find_all('li', class_ = "ipc-metadata-list-summary-item")
    for item in divs:

        Film_element = item.find('h3', class_ = 'ipc-title__text')
        Film = Film_element.text.strip() if Film_element else "N/a"

        element = item.find('div',class_ = 'sc-479faa3c-7 jXgjdT dli-title-metadata')
        E = element.text.strip() if element else "N/a"

        Year=E[:4]
        Duration=E[4:]

        element = item.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
        E = element.text.strip() if element else "N/a"

        Ratings = E[:3]
        Rators  = E[3:]

        element = item.find('div',class_='ipc-html-content-inner-div')
        Summary = element.text.strip() if element else "N/a"

        element = item.find('div', class_='sc-21df249b-0 jmcDPS')
        Votes = element.text.strip('Votes') if element else "N/a"
        #Votes = Votes[7:]

        print(f"Film name : {Film}")
        print(f"Film year release : {Year}")
        print(f"Film duration : {Duration}")
        print(f"Film ratings : {Ratings}")
        print(f"Film no. of rators : {Rators}")
        print(f"Film Summary : {Summary}")
        print(f"Film Votes : {Votes}")
        print("\n")

        # Append the extracted data to the list
        movie_data.append([Film, Year, Duration, Ratings, Rators, Summary, Votes])

    return movie_data


def save_to_csv(data, filename='movies.csv'):
    # Specify the header for the CSV file
    header = ['Film Name', 'Year', 'Duration', 'Ratings', 'Number of Rators', 'Summary', 'Votes']

    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write the header
        csv_writer.writerow(header)

        # Write the data
        csv_writer.writerows(data)

data = extract('IN')
movie_data = transform(data)
save_to_csv(movie_data)