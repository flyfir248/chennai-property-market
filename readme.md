# Magicbricks Property Data Scraper

This Python script allows you to scrape property data from Magicbricks for a specific city. It uses Selenium and BeautifulSoup to extract information about properties, including place, developer, summary, price, and square footage.

## Prerequisites

- Make sure you have [GeckoDriver](https://github.com/mozilla/geckodriver/releases) installed. GeckoDriver is the WebDriver for Firefox. Download the appropriate version for your operating system and add the executable to your system's PATH.

- Install the required Python packages using the following command:

  ```bash
  pip install selenium beautifulsoup4
  ```

- Ensure you have Mozilla Firefox installed on your machine.

## Usage

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/magicbricks-scraper.git
   cd magicbricks-scraper
   ```

2. Open the `magicbricks_scraper.py` file and adjust the following parameters:

   - `city`: Specify the city for which you want to scrape property data.
   - `num_pages`: Set the number of pages to scrape. Increase this value to gather more data.

3. Run the script using the following command:

   ```bash
   python magicbricks_scraper.py
   ```

4. The script will launch Firefox, navigate to Magicbricks, and start scraping property data. It simulates scrolling to load more results dynamically. Please be patient as it may take some time to complete.

5. Once the scraping is finished, the data will be saved to a CSV file named `output2.csv` in the same directory.

## Disclaimer

This script is for educational purposes only. Use it responsibly, adhere to the terms of service of the website you are scraping, and ensure that your actions comply with relevant laws and regulations. The author is not responsible for any misuse or legal consequences arising from the use of this script.