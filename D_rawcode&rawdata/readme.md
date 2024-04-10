# D Report

## Introduction

In this project, our aim was to collect China stock market data and analyze it to gain insights into the economy. Due to the unavailability of easily accessible free APIs for A-shares, we opted to use Tencent and Sina APIs for data retrieval.

### Overall Architecture

**Part 1: Collecting Data**

The data collection process involves two main scripts:

1. `Ashare.py`: This script retrieves stock price data from Tencent and Sina APIs based on specified parameters such as frequency and stock code.
2. `stockCode_scrapper.ipynb`: This notebook performs web scraping on 'https://www.wkzk.com/gegu/' to extract stock codes.

**Part 2: Index Analysis**

This section involves analyzing key indices of the Chinese equity market, including SH00001, 399001, 000905, and 000300. Analysis includes data ingestion, preprocessing, analysis, visualization, and conclusion.

## Part 1: Collecting Data

### Ashare.py

#### Notes:

- The script is designed to fetch stock price data from Tencent and Sina APIs.
- Error handling is implemented for handling potential API request issues.
- Pandas DataFrames are used to structure and manipulate the data.
- The script can be run directly to execute specific functions.

#### Functions Overview:

1. `get_price_day_tx(code, end_date='', count=10, frequency='1d')`: Fetches daily stock price data from Tencent API.
2. `get_price_min_tx(code, end_date=None, count=10, frequency='1d')`: Fetches minute-level stock price data from Tencent API.
3. `get_price_sina(code, end_date='', count=10, frequency='60m')`: Fetches stock price data from Sina API.
4. `get_price(code, end_date='',count=10, frequency='1d', fields=[]): Fetches stock price data based on the provided frequency and source.

### stockCode_scrapper.ipynb

#### Overview:

This notebook performs web scraping on 'https://www.wkzk.com/gegu/' to extract stock codes.

#### Code Analysis:

1. URL Retrieval: Defines the URL of the webpage to scrape.
2. Sending HTTP Request: Sends an HTTP GET request to the URL using the requests library.
3. Response Status Code: Prints the status code of the HTTP response for verification.
4. HTML Parsing: Utilizes BeautifulSoup to parse the HTML content of the webpage.
5. Finding Stock List: Identifies the `<div>` element with the class 'stock_list', which contains the list of stock codes.
6. Extracting Stock Codes: Iterates through all `<a>` elements within the stock list and extracts the stock numbers.
7. Output Confirmation: Prints a message indicating that the stock codes have been saved to a text file.

#### Conclusion:

The code successfully scrapes stock codes from the webpage and saves them to a text file. It effectively utilizes BeautifulSoup and requests libraries for web scraping and HTTP requests, respectively.

### A_share_Price_His.ipynb

#### Overview:

This script automates the retrieval of historical stock price data for multiple stock codes listed in a text file.

#### Code Analysis:

1. Importing Required Modules: Imports the Ashare module for data retrieval.
2. Setting Up Stock Code and Retrieval Parameters: Specifies parameters for data retrieval.
3. Data Retrieval for Specific Stock: Calls the `get_price` function to retrieve stock price data for each stock code.
4. Iterating Through Stock Codes in File: Reads stock codes from 'stock_code.txt' and fetches stock data for each code.
5. Saving Data to CSV: Saves retrieved data to individual CSV files.

#### Conclusion:

The script automates the retrieval of historical stock price data but lacks stability. Error handling and optimization could enhance its performance.

## Part 2: Index Analysis

### Architecture

1. Data Ingestion: Importing dataset from a CSV file.
2. Preprocessing: Data cleaning, transformation, and calculation of basic statistics.
3. Analysis: Calculating financial indicators and performing transformations.
4. Visualization: Plotting data for analysis.
5. Conclusion: Deriving insights from analysis and visualizations.

### Results

The analysis of main Chinese equity market indices provides insights into performance and volatility over different periods.

### Summary

- SH00001: Experienced significant drawdowns and growth periods, reflecting economic cycles.
- 399001: Similar pattern to SH00001, indicating market trends.
- 000905: Demonstrated drawdowns and growth, reflecting market fluctuations.
- 000300: Showed similar trends to other indices, reflecting economic cycles.

Overall, understanding these patterns helps assess the Chinese economy's health and direction.

## Fake Checks

Brief overview of notable recessions in China's recent history:

1. Asian Financial Crisis (Late 1990s)
2. Global Financial Crisis (2007-2008)
3. COVID-19 Pandemic (2020)

These events impacted China's economy, leading to slowdowns and challenges.

### Conclusion

The project aimed to analyze China's stock market data for economic insights. While facing challenges, the analysis provides valuable information for understanding economic trends and making informed decisions. Further improvements can enhance stability and accuracy in future analyses.# D Report

## Introduction

In this project, our aim was to collect China stock market data and analyze it to gain insights into the economy. Due to the unavailability of easily accessible free APIs for A-shares, we opted to use Tencent and Sina APIs for data retrieval.

### Overall Architecture

**Part 1: Collecting Data**

The data collection process involves two main scripts:

1. `Ashare.py`: This script retrieves stock price data from Tencent and Sina APIs based on specified parameters such as frequency and stock code.
2. `stockCode_scrapper.ipynb`: This notebook performs web scraping on 'https://www.wkzk.com/gegu/' to extract stock codes.

**Part 2: Index Analysis**

This section involves analyzing key indices of the Chinese equity market, including SH00001, 399001, 000905, and 000300. Analysis includes data ingestion, preprocessing, analysis, visualization, and conclusion.

## Part 1: Collecting Data

### Ashare.py

#### Notes:

- The script is designed to fetch stock price data from Tencent and Sina APIs.
- Error handling is implemented for handling potential API request issues.
- Pandas DataFrames are used to structure and manipulate the data.
- The script can be run directly to execute specific functions.

#### Functions Overview:

1. `get_price_day_tx(code, end_date='', count=10, frequency='1d')`: Fetches daily stock price data from Tencent API.
2. `get_price_min_tx(code, end_date=None, count=10, frequency='1d')`: Fetches minute-level stock price data from Tencent API.
3. `get_price_sina(code, end_date='', count=10, frequency='60m')`: Fetches stock price data from Sina API.
4. `get_price(code, end_date='',count=10, frequency='1d', fields=[]): Fetches stock price data based on the provided frequency and source.

### stockCode_scrapper.ipynb

#### Overview:

This notebook performs web scraping on 'https://www.wkzk.com/gegu/' to extract stock codes.

#### Code Analysis:

1. URL Retrieval: Defines the URL of the webpage to scrape.
2. Sending HTTP Request: Sends an HTTP GET request to the URL using the requests library.
3. Response Status Code: Prints the status code of the HTTP response for verification.
4. HTML Parsing: Utilizes BeautifulSoup to parse the HTML content of the webpage.
5. Finding Stock List: Identifies the `<div>` element with the class 'stock_list', which contains the list of stock codes.
6. Extracting Stock Codes: Iterates through all `<a>` elements within the stock list and extracts the stock numbers.
7. Output Confirmation: Prints a message indicating that the stock codes have been saved to a text file.

#### Conclusion:

The code successfully scrapes stock codes from the webpage and saves them to a text file. It effectively utilizes BeautifulSoup and requests libraries for web scraping and HTTP requests, respectively.

### A_share_Price_His.ipynb

#### Overview:

This script automates the retrieval of historical stock price data for multiple stock codes listed in a text file.

#### Code Analysis:

1. Importing Required Modules: Imports the Ashare module for data retrieval.
2. Setting Up Stock Code and Retrieval Parameters: Specifies parameters for data retrieval.
3. Data Retrieval for Specific Stock: Calls the `get_price` function to retrieve stock price data for each stock code.
4. Iterating Through Stock Codes in File: Reads stock codes from 'stock_code.txt' and fetches stock data for each code.
5. Saving Data to CSV: Saves retrieved data to individual CSV files.

#### Conclusion:

The script automates the retrieval of historical stock price data but lacks stability. Error handling and optimization could enhance its performance.

## Part 2: Index Analysis

### Architecture

1. Data Ingestion: Importing dataset from a CSV file.
2. Preprocessing: Data cleaning, transformation, and calculation of basic statistics.
3. Analysis: Calculating financial indicators and performing transformations.
4. Visualization: Plotting data for analysis.
5. Conclusion: Deriving insights from analysis and visualizations.

### Results

The analysis of main Chinese equity market indices provides insights into performance and volatility over different periods.

### Summary

- SH00001: Experienced significant drawdowns and growth periods, reflecting economic cycles.
- 399001: Similar pattern to SH00001, indicating market trends.
- 000905: Demonstrated drawdowns and growth, reflecting market fluctuations.
- 000300: Showed similar trends to other indices, reflecting economic cycles.

Overall, understanding these patterns helps assess the Chinese economy's health and direction.

## Fake Checks

Brief overview of notable recessions in China's recent history:

1. Asian Financial Crisis (Late 1990s)
2. Global Financial Crisis (2007-2008)
3. COVID-19 Pandemic (2020)

These events impacted China's economy, leading to slowdowns and challenges.

### Conclusion

The project aimed to analyze China's stock market data for economic insights. While facing challenges, the analysis provides valuable information for understanding economic trends and making informed decisions. Further improvements can enhance stability and accuracy in future analyses.