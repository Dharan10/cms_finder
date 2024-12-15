CmoSS Scanner
CmoSS Scanner is a powerful and easy-to-use terminal tool designed to detect the CMS (Content Management System) and its version from any given website. The tool analyzes the HTML and headers of the website to identify popular CMS platforms such as WordPress, Joomla, Drupal, Magento, Shopify, and more. It then outputs the CMS name and version information in different colors for improved readability.

Features
Detects popular CMS platforms (WordPress, Joomla, Drupal, Magento, Shopify, Wix, Squarespace, etc.).
Extracts and displays CMS version information where available.
Displays results in a color-coded format for better readability.
Simple and user-friendly command-line interface.
Fast and lightweight, ideal for security professionals and developers.
Technologies Used
Python
requests for making HTTP requests.
BeautifulSoup for parsing HTML.
termcolor for colorizing output.
Installation
Clone this repository:

git clone https://github.com/yourusername/cmoss-scanner.git
Install dependencies:

pip install -r requirements.txt
Run the tool:

python cms_scanner.py http://example.com
Example Output

WordPress version: 5.8.3  [Displayed in Blue]
Usage
To use the tool, simply run it with the URL of the website you want to scan:

python cms_scanner.py http://example.com
