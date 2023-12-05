import requests
from bs4 import BeautifulSoup


def extract(city, num_pages=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.magicbricks.com/'
    }

    results = []

    with requests.Session() as session:
        session.headers.update(headers)

        for page in range(1, num_pages + 1):
            url = f'https://www.magicbricks.com/property-for-sale/residential-commercial-agricultural-real-estate?bedroom=1,4,5,%3E5,%3E5,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot,Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Warehouse-Godown,Industrial-Building,Industrial-Shed,Agricultural-Land,Farm-House&cityName={city}&page={page}'
            r = session.get(url)

            if r.status_code != 200:
                print(f"Failed to fetch page {page}. Status code: {r.status_code}")
                continue

            soup = BeautifulSoup(r.content, 'html.parser')
            results.append(soup)

    return results


def transform(pages):
    for soup in pages:
        divs_info = soup.find_all('div', class_="mb-srp__card__info mb-srp__card__info-withoutburger")

        for item in divs_info:
            place = item.find('h2').text.strip()

            Developer_element = item.find('div', class_='mb-srp__card__society')
            Developer = Developer_element.text.strip() if Developer_element else "N/a"

            Summary_element = item.find('div', class_='mb-srp__card--desc--text')
            Summary = Summary_element.text.strip() if Summary_element else "N/a"

            print(place)
            print(Developer)
            print(Summary)
            print("\n")

        print("================================================")

        divs_estimate = soup.find_all('div', class_="mb-srp__card__estimate")
        for item in divs_estimate:
            Price_element = item.find('div', class_='mb-srp__card__price--amount')
            Price = Price_element.text.strip() if Price_element else "N/a"

            Sqft_element = item.find('div', class_='mb-srp__card__price--size')
            Sqft = Sqft_element.text.strip() if Sqft_element else "N/a"

            print(Price)
            print(Sqft)
            print("\n")

        print("================================================")


# Assuming the 'extract' function is defined elsewhere
pages = extract('chennai', num_pages=3)
transform(pages)
