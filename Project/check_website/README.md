# Website Checker
`check_website.py` is a command-line tool for checking the reachability of a specified website by making an HTTP request to the provided URL. It helps determine if a website is accessible and identifies common HTTP status codes, such as redirection, authorization issues, or server errors.

## Features
- **Check Website Reachability**: Send an HTTP request to any URL and receive feedback on the status code.  
- **Detailed HTTP Status Code Interpretation**:  
  - **200 OK**: The website is reachable.
  - **301/302 Redirect**: The website redirects to another URL.
  - **403 Forbidden**: Access to the website is restricted.
  - **404 Not Found**: The URL is not found on the server.
  - **500 Internal Server Error**: The server encountered an error.
- **Error Handling**: Provides clear output if the URL is unreachable or an error occurs.

<hr>

## Installation
### Prerequisites
This script requires Python3 and the `requests` library to function.

Install `requests` via pip if it’s not already installed:
```bash
pip3 install requests
```
### Clone the repository  
1. Clone this repo to your local machine
`git clone https://github.com/driturr/ITST2024/tree/main/Project/check_website`  

2. Install the required libraries:  
`pip3 install -r requirements.txt`

3. Run the script: 
`python3 check_website.py <url>`

## Usage
To check the reachability of a website, simply run the script with the desired URL as an argument.

**Command:**
```bash
python3 check_website.py <url>
```
**Example:**
To check the reachability of `https://www.example.com`, run:
```bash
python3 check_website.py https://www.example.com
```
## Output
Depending on the HTTP response, the output will indicate the URL's reachability or provide details on the specific HTTP status encountered. Example outputs:
- `'https://www.example.com' is reachable (Status Code: 200 OK).`
- `'https://www.example.com' was not found (Status Code: 404 Not Found).`
- `'https://www.example.com' returned status code 403. Permission missing (Status Code: 403 Forbidden).`

## Error Handling
The `check_website.py` script includes error handling for various scenarios, providing informative messages for the following conditions:
- **Network or Connection Issues**: If the network is down or the URL is incorrect, a `requests.exceptions.RequestException` is raised, and the output displays an error message with details.
- **Unreachable or Non-responsive URLs**: If the URL does not respond or times out, the error message indicates that the URL is unreachable.
- **Invalid URLs**: If the URL format is incorrect or invalid, the script will indicate that the URL could not be reached.

## Known Limitations
- Only checks HTTP(S) reachability; does not support protocols like FTP or WebSocket.
- Provides feedback based only on HTTP status codes; more complex issues (e.g., server load times or DNS errors) are not covered.

## Contributing
To contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request when done.

Contributions welcome!