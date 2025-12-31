import requests
from bs4 import BeautifulSoup

print("Web Scraper")

while True:
    url = input("Enter URL to scrape\n>> ")

    url2 = "https://" + url

    # Send GET request
    data = requests.get(url2)

    # Check if the request was successful
    if data.status_code == 200:
        # Create a BeautifulSoup object with the HTML content
        soup = BeautifulSoup(data.text, 'html.parser')
        
        # Print the title of the page
        print("Title of the page:", soup.title.string if soup.title else "No title found")
        
        # Print the first <h1> tag
        print("First H1 tag:", soup.h1.string if soup.h1 else "No H1 tag found")
        
        # Print the first <li> tag
        print("First LI tag:", soup.li.string if soup.li else "No LI tag found")
    else:
        print(f"Sorry! It looks like it doesn't work! Status Code: {data.status_code}")