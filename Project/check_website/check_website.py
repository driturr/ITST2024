import argparse
import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"'{url}' is reachable (Status Code: {response.status_code} OK).")
        elif response.status_code in (301, 302):
            print(f"'{url}' was redirected to another URL (Status Code: {response.status_code} Redirect).")
        elif response.status_code == 403:
            print(f"'{url}' didn't authorize the request. Permission missing (Status Code: {response.status_code} Forbidden).")
        elif response.status_code == 404:
            print(f"'{url}' was not found (Status Code: {response.status_code} Not Found).")
        elif response.status_code == 500:
            print(f"Internal server error on '{url}' (Status Code: {response.status_code} Internal Server Error).")
        else:
            print(f"'{url}' returned status code {response.status_code}. It may not be reachable.")
    except requests.exceptions.RequestException as e:
        print(f"Error:'{url}' not reachable. Details: {e}")

def main():
    parser = argparse.ArgumentParser(description="Check if a website is reachable by making an HTTP request.")
    parser.add_argument("url", help="The URL of the website to check (e.g., https://www.example.com).")
    
    args = parser.parse_args()
    
    check_website(args.url)

if __name__ == "__main__":
    main()