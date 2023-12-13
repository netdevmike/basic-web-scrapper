# Basic Web Scraper

## Description
This project is a simple web scraper that extracts information from websites. It fetches and parses HTML content to extract data such as article titles, links, paragraphs, and images.

## Requirements
- Python
- BeautifulSoup4
- aiohttp

## Installation
Before running the scraper, you need to install the required Python libraries. You can install them using pip:
```bash
pip install beautifulsoup4 aiohttp
```

## Usage
To use the scraper, follow these steps:
1. Run the script using Python.
2. When prompted, enter the URL of the website you want to scrape.
3. Next, enter the type of information you want to extract. Options include:
   - `titles` for extracting titles (found in `<h2>` tags).
   - `links` for extracting all hyperlinks.
   - `paragraphs` for extracting text from paragraph tags.
   - `images` for extracting image URLs.

The scraper will fetch data from the provided URL and output it to the terminal. Additionally, it will save the data in a file named `scraped_data.json` in the same directory as the script.

## Features
- Asynchronous HTTP requests for efficient web scraping.
- User input for URL and data type to extract.
- Error handling for invalid URLs or unexpected website structures.
- Supports basic pagination for websites with multiple pages.
- Extracted data is both printed to the console and saved as a JSON file.

## Customization
You can customize the script for different websites by modifying the `extract_info` function. Adjust the range in the pagination section of the `main` function as needed for different websites.

## Author
Michael Charara