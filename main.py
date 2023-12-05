import requests
from bs4 import BeautifulSoup


def extract(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.magicbricks.com/'
    }

    with requests.Session() as session:
        session.headers.update(headers)
        url = f'https://www.magicbricks.com/property-for-sale/residential-commercial-agricultural-real-estate?bedroom=1,4,5,%3E5,%3E5,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot,Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Warehouse-Godown,Industrial-Building,Industrial-Shed,Agricultural-Land,Farm-House&cityName={city}'
        # Add code to capture and include cookies if needed
        r = session.get(url)
        #return r.status_code
        soup = BeautifulSoup(r.content,'html.parser')
        return(soup)

def transform(soup):

    divs = soup.find_all('div', class_ = "mb-srp__card__info")
    for item in divs:
        place = item.find('h2').text.strip()

        Developer_element = item.find('span', class_ = 'mb-srp__card__developer--name--highlight')
        Developer = Developer_element.text.strip() if Developer_element else "N/a"

        Total_area_element = item.find('div',class_ = 'mb-srp__card__summary--value')
        Total_area = Total_area_element.text.strip() if Total_area_element else "N/a"

        Summary = item.find('p', class_='two-line-truncated').text.strip()
        print(place)
        print(Developer)
        print(Total_area)
        print(Summary)
        print("\n")
    print("================================================")
    divs = soup.find_all('div', class_="mb-srp__card__estimate")
    for item in divs:

        price_element = item.find('div', class_='mb-srp__card__price--amount')
        price = price_element.text.strip() if price_element else "N/a"

        pricepersqft_element = item.find('div', class_='mb-srp__card__price--size')
        pricepersqft = pricepersqft_element.text.strip() if pricepersqft_element else "N/a"

        buildername_element = item.find('div', class_ ='mb-srp__card__ads--name')
        buildername = buildername_element.text.strip() if buildername_element else "N/a"

        Operations_since_element = item.find('div', class_ ='mb-srp__card__ads--since')
        Operations_since = Operations_since_element.text.strip() if Operations_since_element else "N/a"
        print(price)
        print(pricepersqft)
        print(buildername)
        print(Operations_since)
        print("\n")
    print("================================================")
    # Extract and print essential information
    divs = soup.find_all('div', class_="mb-srp__card__summary__list summary-luxury")

    for item in divs:
        # Extract Super Area
        super_area_element = item.find('div', {'data-summary': 'super-area'})
        super_area = super_area_element.find('div',class_='mb-srp__card__summary--value').text.strip() if super_area_element else "N/A"

        # Extract Status
        status_element = item.find('div', {'data-summary': 'status'})
        status = status_element.find('div',class_='mb-srp__card__summary--value').text.strip() if status_element else "N/A"

        # Extract Floor
        floor_element = item.find('div', {'data-summary': 'floor'})
        floor = floor_element.find('div',class_='mb-srp__card__summary--value').text.strip() if floor_element else "N/A"

        # Extract Transaction
        transaction_element = item.find('div', {'data-summary': 'transaction'})
        transaction = transaction_element.find('div',class_='mb-srp__card__summary--value').text.strip() if transaction_element else "N/A"

        # Extract Furnishing
        furnishing_element = item.find('div', {'data-summary': 'furnishing'})
        furnishing = furnishing_element.find('div',class_='mb-srp__card__summary--value').text.strip() if furnishing_element else "N/A"

        # Extract Bathroom
        bathroom_element = item.find('div', {'data-summary': 'bathroom'})
        bathroom = bathroom_element.find('div',class_='mb-srp__card__summary--value').text.strip() if bathroom_element else "N/A"

        # Extract Parking
        carparking_element = item.find('div', {'data-summary': 'parking'})
        carparking = carparking_element.find('div',class_='mb-srp__card__summary--value').text.strip() if carparking_element else "N/A"

        # Print the extracted information
        print(f"Super Area: {super_area}")
        print(f"Status: {status}")
        print(f"Floor: {floor}")
        print(f"Transaction: {transaction}")
        print(f"Furnishing: {furnishing}")
        print(f"Bathroom: {bathroom}")
        print(f"Parking: {carparking}")
        print("\n")

    return

data=extract('chennai')
transform(data)
