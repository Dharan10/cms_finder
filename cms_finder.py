import requests
from bs4 import BeautifulSoup
import re
import argparse
import sys
from termcolor import colored

def find_cms_version(url):
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10, verify=False)  # Disable SSL verification (for self-signed certs)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check meta tags for CMS identification
        meta_generator = soup.find('meta', attrs={'name': 'generator'})
        if meta_generator and 'content' in meta_generator.attrs:
            cms_info = meta_generator['content']
            return colored(f"CMS identified: {cms_info}", 'green')

        # Check for WordPress version
        if 'wp-' in response.text or 'wordpress' in response.text.lower():
            match = re.search(r'content=\"WordPress (\d+\.\d+(\.\d+)?)\"', response.text)
            if match:
                return colored(f"WordPress version: {match.group(1)}", 'blue')
            return colored("WordPress detected, version not found.", 'yellow')

        # Check for Joomla version
        if 'joomla' in response.text.lower():
            match = re.search(r'content=\"Joomla\! (\d+\.\d+(\.\d+)?)\"', response.text)
            if match:
                return colored(f"Joomla version: {match.group(1)}", 'cyan')
            return colored("Joomla detected, version not found.", 'yellow')

        # Check for Drupal version
        if 'drupal' in response.text.lower():
            match = re.search(r'Drupal (\d+\.\d+(\.\d+)?)', response.text)
            if match:
                return colored(f"Drupal version: {match.group(1)}", 'magenta')
            return colored("Drupal detected, version not found.", 'yellow')

        # Check for Magento version in headers
        if 'magento' in response.text.lower():
            match = re.search(r'Magento/(\d+\.\d+(\.\d+)?)', response.headers.get('X-Magento-Vary', ''))
            if match:
                return colored(f"Magento version: {match.group(1)}", 'red')
            return colored("Magento detected, version not found.", 'yellow')

        # Check for Shopify version information
        if 'shopify' in response.text.lower():
            return colored("Shopify detected, version information not available.", 'yellow')

        # Check for Wix and Squarespace
        if 'wix.com' in response.text.lower():
            return colored("Wix detected, version information not available.", 'yellow')
        if 'squarespace' in response.text.lower():
            return colored("Squarespace detected, version information not available.", 'yellow')

        # Additional CMS detection can be added here

        return colored("CMS not identified. The website may use a custom CMS or obfuscate this information.", 'red')

    except requests.exceptions.HTTPError as e:
        return colored(f"HTTP error occurred: {e}", 'red')
    except requests.exceptions.ConnectionError as e:
        return colored(f"Connection error occurred: {e}", 'red')
    except requests.exceptions.Timeout as e:
        return colored(f"Timeout error occurred: {e}", 'red')
    except requests.exceptions.RequestException as e:
        return colored(f"An error occurred: {e}", 'red')
    except requests.exceptions.SSLError as e:
        return colored(f"SSL error occurred: {e}", 'red')
    except Exception as e:
        return colored(f"Unexpected error: {e}", 'red')

def main():
    banner = """
   ██████╗ ███╗   ███╗ ██████╗ ███████╗
  ██╔════╝ ████╗ ████║██╔═══██╗██╔════╝ 
  ██║  ███╗ ██╔████╔██║██║   ██║███████╗ 
  ██║   ██║ ██║╚██╔╝██║██║   ██║╚════██║  
  ╚██████╔╝ ██║ ╚═╝ ██║╚██████╔╝███████║
   ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚══════╝ 

                  CmoSS Scanner
             Author: A!Z3N(Dharan) | Made with Power
    Detect CMS and version information with ease
    """
    print(banner)

    # Argument parsing
    parser = argparse.ArgumentParser(description="CmoSS Scanner - Detect CMS and version")
    parser.add_argument("url", help="Enter the website URL (include http/https)")
    args = parser.parse_args()

    if not args.url:
        print(colored("Error: No URL provided. Please enter a valid URL.", 'red'))
        sys.exit(1)

    result = find_cms_version(args.url)
    print(result)

if __name__ == "__main__":
    main()
