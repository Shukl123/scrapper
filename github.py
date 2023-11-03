import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = 'https://www.divyahimachal.com/category/himachal-latest-news/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text content within the <p> and <h1> to <h6> tags
    text_content = ""
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text_content += tag.get_text() + "\n"

    # Save the extracted text content to a text file
    with open('extracted_text.txt', 'w', encoding='utf-8') as file:
        file.write(text_content)

    print("Text content has been saved to 'extracted_text.txt'.")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
