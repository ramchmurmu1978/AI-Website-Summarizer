import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/155.0 Safari/537.36"
    }
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    #Get page title
    title = soup.title.get_text(strip=True) if soup.title else "Untitled Page"

    #Remove elements that don't contain useful article text
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    #Extract text
    text = soup.get_text(separator=" ", strip=True)

    return title, text[:12000]

if __name__=="__main__":
    url = input("Enter website URL: ")

    title, text = scrape_website(url)

    print("\n---Page Title---")
    print(title)

    print("\n---Extracted Website Text---\n")
    print(text[:5000])

