
# Wikipedia PDF Downloader

## Overview

The Wikipedia PDF Downloader is a Python-based tool designed to automate the process of downloading Wikipedia articles as PDF files. Utilizing modern web scraping techniques, this tool offers a convenient way to save and archive valuable information from Wikipedia.

## Features

- **Asynchronous Downloading**: Leverages Python's `asyncio` for efficient downloading of multiple articles.
- **CSV Input Support**: Reads URLs from a CSV file, allowing batch processing of multiple Wikipedia articles.
- **Browser Automation**: Uses `pyppeteer`, a headless browser, for accurate rendering of web pages.
- **PDF Generation**: Converts web pages to PDF format with `pdfkit`, ensuring high-fidelity document preservation.

## Installation

Before using the Wikipedia PDF Downloader, ensure that Python 3.x is installed on your system. Additionally, you'll need to install the required dependencies:

```bash
pip install pyppeteer pdfkit asyncio csv urllib.parse
```

## Usage

1. **Prepare a CSV File**: Create a CSV file with a column named "URL" containing the Wikipedia URLs you wish to download.

2. **Run the Script**: Execute the script with the path to your CSV file:

   ```python
   python wikipedia_pdf.py your_file.csv
   ```

   The script will read each URL and save the corresponding Wikipedia article as a PDF file.

3. **Check Output**: The downloaded PDFs will be saved in the same directory as the script.

## Contributing

Contributions to the Wikipedia PDF Downloader are welcome! Whether it's bug fixes, feature enhancements, or documentation improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the LICENSE file for details.
