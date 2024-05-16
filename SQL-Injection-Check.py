import requests
from bs4 import BeautifulSoup
import urllib.parse

def scan_for_sql_injection(url):
    # Send a request to the website with a test payload
    payload = "' OR 1=1 --"
    params = {"search": payload}
    encoded_params = urllib.parse.urlencode(params)
    test_url = f"{url}?{encoded_params}"

    response = requests.get(test_url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the response contains any error messages
    error_messages = ["error", "warning", "syntax", "mysql", "sql"]
    for error_message in error_messages:
        if error_message in soup.text.lower():
            print(f"Potential SQL injection vulnerability found: {test_url}")
            return True

    print(f"No SQL injection vulnerability found: {test_url}")
    return False

# Example usage:
url = "http://testphp.vulnweb.com"
scan_for_sql_injection(url)
