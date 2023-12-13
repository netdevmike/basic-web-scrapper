import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json

async def fetch_html(session, url):
    """Fetch the HTML content of a given URL asynchronously."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Check for HTTP request errors
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def extract_info(html, info_type):
    """Extract information from HTML based on the specified info type."""
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')

    try:
        if info_type == 'titles':
            # Extracting and returning titles
            titles = [title.text for title in soup.find_all('h2')]
            return titles
        elif info_type == 'links':
            # Extracting and returning links
            links = [{'text': link.text, 'href': link.get('href')} for link in soup.find_all('a')]
            return links
        elif info_type == 'paragraphs':
            # Extracting and returning paragraphs
            paragraphs = [paragraph.text for paragraph in soup.find_all('p')]
            return paragraphs
        elif info_type == 'images':
            # Extracting and returning image sources
            images = [img.get('src') for img in soup.find_all('img')]
            return images
    except Exception as e:
        print(f"Error processing HTML: {e}")
        return []

    return None

async def main():
    """Main function to run the web scraper."""
    url = input("Enter the URL to scrape: ")
    info_type = input("Enter the type of information to extract (e.g., 'titles'): ")

    # Prepare URLs for pagination (adjust the range as needed)
    urls = [f"{url}?page={i}" for i in range(1, 4)]

    data = []
    async with aiohttp.ClientSession() as session:
        # Creating tasks for each URL
        tasks = [fetch_html(session, url) for url in urls]
        # Gathering HTML content from all URLs
        html_pages = await asyncio.gather(*tasks)

        # Processing each HTML page
        for html in html_pages:
            if html:
                extracted_data = extract_info(html, info_type)
                if extracted_data:
                    data.extend(extracted_data)
                    print(data)  # Print each page's data to the terminal

    # Saving extracted data to a JSON file if any data was extracted
    if data:
        with open('scraped_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Data saved to scraped_data.json")
    else:
        print("No data extracted.")

if __name__ == "__main__":
    asyncio.run(main())