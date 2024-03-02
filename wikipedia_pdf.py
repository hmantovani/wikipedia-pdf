import asyncio
import csv
import pdfkit
import urllib.parse
from pyppeteer import launch

async def save_pdf(url, file_name):
    try:
        browser = await launch(headless=True, executablePath=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'networkidle0'})
        await page.pdf({'path': file_name})
        await browser.close()
        print(f"PDF saved as {file_name}")
    except Exception as e:
        print(f"Error saving PDF for {url}: {e}")

async def read_urls_from_csv(file_path):
    urls = []
    with open(file_path, 'r', newline='', encoding='latin-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = row.get("URL")
            if url:
                urls.append(url)
            else:
                print("Warning: Empty URL found in CSV file.")
        await asyncio.sleep(1)  # Introduce an asynchronous delay
    return urls

async def main():
    urls_file = "url.csv"  # Change this to the path of your CSV file
    urls = await read_urls_from_csv(urls_file)
    
    tasks = []
    for url in urls:
        # Decode URL and extract page title
        decoded_url = urllib.parse.unquote(url)
        page_title = decoded_url.split("/")[-1].replace("_", " ")  # Replace underscores with spaces
        file_name = f"{page_title}.pdf"  # Use page title as filename
        tasks.append(save_pdf(url, file_name))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
