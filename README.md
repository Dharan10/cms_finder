CmoSS Scanner

CmoSS Scanner is a powerful and easy-to-use terminal tool designed to detect the CMS (Content Management System) and its version from any given website. The tool analyzes the HTML and headers of the website to identify popular CMS platforms such as WordPress, Joomla, Drupal, Magento, Shopify, and more. It then outputs the CMS name and version information in different colors for improved readability.

➡Features

Detects popular CMS platforms (WordPress, Joomla, Drupal, Magento, Shopify, Wix, Squarespace, etc.).
Extracts and displays CMS version information where available.
Displays results in a color-coded format for better readability.
Simple and user-friendly command-line interface.
Fast and lightweight, ideal for security professionals and developers.

➡Technologies Used:

⚫Python

⚫requests for making HTTP requests.

⚫BeautifulSoup for parsing HTML.

⚫termcolor for colorizing output.

➡Installation

1.Clone this repository:

git clone https://github.com/Dharan10/cms_finder.git

2.Install dependencies:

pip install -r requirements.txt

3.Run the tool:

python cms_scanner.py http://example.com

➡Example Output

WordPress version: 5.8.3  [Displayed in Blue]

➡Usage:

To use the tool, simply run it with the URL of the website you want to scan:

python cms_scanner.py http://example.com


MIT License

Copyright (c) 2024 Cy-sec-dharan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

If you encounter any errors or need advice, feel free to reach out to me at:
- LinkedIn: www.linkedin.com/in/cy-sec-dharan
- Gmail: dharanragunathan@gmail.com
