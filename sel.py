import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def extract(city, num_pages=500):
    results = []

    # Using Firefox WebDriver. You can use other drivers as well.
    driver = webdriver.Firefox()

    try:
        for page in range(1, num_pages + 1):
            url = f'https://www.magicbricks.com/property-for-sale/residential-commercial-agricultural-real-estate?bedroom=1,4,5,%3E5,%3E5,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot,Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Warehouse-Godown,Industrial-Building,Industrial-Shed,Agricultural-Land,Farm-House&cityName={city}&page={page}'

            driver.get(url)
            time.sleep(2)  # Wait for the page to load

            # Simulate scrolling to trigger dynamic loading of content
            for _ in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results.append(soup)

            # Add a delay between requests to avoid potential issues
            time.sleep(1)

    finally:
        driver.quit()

    return results

def transform(pages):
    entries = []

    for soup in pages:
        divs_info = soup.find_all('div', class_="mb-srp__card__info mb-srp__card__info-withoutburger")
        divs_estimate = soup.find_all('div', class_="mb-srp__card__estimate")

        for info, estimate in zip(divs_info, divs_estimate):
            place = info.find('h2').text.strip()
            Developer_element = info.find('div', class_='mb-srp__card__society')
            Developer = Developer_element.text.strip() if Developer_element else "N/a"
            Summary_element = info.find('div', class_='mb-srp__card--desc--text')
            Summary = Summary_element.text.strip() if Summary_element else "N/a"

            Price_element = estimate.find('div', class_='mb-srp__card__price--amount')
            Price = Price_element.text.strip() if Price_element else "N/a"

            Sqft_element = estimate.find('div', class_='mb-srp__card__price--size')
            Sqft = Sqft_element.text.strip() if Sqft_element else "N/a"

            entries.append([place, Developer, Summary, Price, Sqft])

    return entries

def save_to_csv(entries, filename='output2.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Place', 'Developer', 'Summary', 'Price', 'Sqft'])
        csv_writer.writerows(entries)

# Assuming the 'extract' function is defined elsewhere
pages = extract('chennai', num_pages=3)
entries = transform(pages)
save_to_csv(entries)