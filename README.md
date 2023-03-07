# Web Scraping 

This repository contains examples of web scraping scripts written in Python. The scripts demonstrate how to extract data from different websites using various Python libraries, such as BeautifulSoup, Requests, and Selenium.

## Installation

1. Clone the repository: `git clone https://github.com/Adebowale-Morakinyo/web-scrapping.git`
2. Install the required libraries: `pip install -r requirements.txt`

## Usage

To run the scripts, navigate to the directory of the script and run it using the Python interpreter. For example, to run the `google_search_results.py` script:

1. Open a terminal or command prompt.
2. Navigate to the `web-scrapping` directory: `cd web-scrapping`
3. Navigate to the directory containing the script: `cd Google-Search-Opener`
4. Run the script: `python google_search_results.py <search_terms>`

Replace `<search_terms>` with the search terms you want to search for. The script will open the top 5 search results in your default web browser.

## Scripts

### Google Search Results

The `google_search_results.py` script opens the top 5 search results from Google search in your default web browser. To use the script, provide the search terms as command line arguments.

## Warning

n this implementation, if we get a 429 status code, indicating that we've sent too many requests, we wait for 10 seconds before retrying the request. This should help avoid hitting Google's rate limit. However, it's important to note that even with a delay, using web scraping to get search results from Google is against their terms of service and could potentially lead to your IP being banned. This is just for educational purpose.

## Contributing

Contributions are welcome! If you have any suggestions or ideas for new web scraping scripts, please feel free to submit a pull request.
