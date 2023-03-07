import requests
import sys
import webbrowser
import bs4
import time

# check if command line arguments are provided
if len(sys.argv) < 2:
    print('Usage: python search.py <search terms>')
    sys.exit()

# join the search terms to form the search query
search_query = ' '.join(sys.argv[1:])

# make the request to Google search
print('Searching for {}...'.format(search_query))
res = requests.get('http://google.com/search?q=' + search_query)
res.raise_for_status()

# parse the HTML using BeautifulSoup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# extract the links to the search results
link_elems = soup.select('.r a')
num_links = min(5, len(link_elems))  # open only the top 5 search results

# open each link in a new tab using the default web browser
for i in range(num_links):
    url = 'http://google.com' + link_elems[i].get('href')
    print('Opening:', url)
    webbrowser.open(url)
    time.sleep(1)  # add a delay of 1 second between requests to prevent rate limiting
