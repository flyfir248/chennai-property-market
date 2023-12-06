import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

def extract_with_selenium(country):
    driver = webdriver.Chrome()  # Use the appropriate driver for your browser
    driver.get(f'https://www.imdb.com/search/title/?title_type=feature&countries={country}&languages=hi')

    # Scroll down to load more entries
    for _ in range(5):  # Adjust the number of scrolls based on your needs
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Allow time for content to load

    while True:
        try:
            # Click the "50 more" button
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'ipc-see-more__button'))
            )

            load_more_button.click()

            # Wait for the new content to load
            time.sleep(5)  # Adjust this based on your needs

        except Exception as e:
            # If the "50 more" button is not found or not clickable, exit the loop
            print(f"Exception: {e}")
            break

    # Get the updated page source after clicking "50 more" multiple times
    updated_page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(updated_page_source, 'html.parser')
    return soup


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


def main():
    page_number = 1

    while True:
        data = extract_with_selenium('IN')
        movie_data = transform(data)

        if not movie_data:
            break

        save_to_csv(movie_data)

        page_number += 1

if __name__ == "__main__":
    main()