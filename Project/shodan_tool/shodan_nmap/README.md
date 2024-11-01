# Shodan - Nmap Tool
This tool uses the Shodan API to retrieve information on IP addresses or HTTP services and allows optional vulnerability checking using Nmap. It offers two main modes: IP lookup and HTTP service search.

This tool was created to be able to check for vulnerabilities even if you lack a Shodan membership. For this reason, checking vulnerabilities for "search HTTP services" is not possible.

## Features
- IP Lookup: Retrieve details about a specific IP address, including open ports, operating system, and organization details.
- HTTP Service Search: Search for HTTP services by query (e.g., "apache") and receive service details such as IP, port, and product information.
- Vulnerability Check: Optionally check for known vulnerabilities related to IP addresses using Nmap vulnerability script.
- Report Generation: Save results in JSON format, including all retrieved data and vulnerability details.

## Installation
### Prerequisites
Install Nmap: [Nmap's official site](https://nmap.org/download.html).

### Required Python Packages
This script runs in Python3, therefore make sure you have Python installed.

To run this script you need to install `python-dotenv`, `shodan`, and `python-nmap` packages:

- `python-dotenv` package:
```bash
pip3 install python-dotenv
```
- `shodan` package:
```bash
pip3 install shodan
```
- `python-nmap` package:
```bash
pip3 install python-nmap
```

### Clone the repository  
1. Clone this repo to your local machine
`git clone https://github.com/driturr/ITST2024/tree/main/Project/shodan_tool/shodan_nmap`  

2. Install the required libraries:  
`pip3 install -r requirements.txt`

3. Set up your Shodan API key:
- Create a `.env` file in the root of the project:
`SHODAN_API_KEY=shodan_api_key_here`
- Replace `your_shodan_api_key_here` with your actual Shodan API key.

### Optional but recommended:
Activate a virtual environment and add the `.env` within this environment to keep it isolated.

1. Create the virtual environment: 
`python3 -m venv myvenv`

2. Activate the virtual environment:  
On Linux/Mac:
`source myvenv/bin/activate`

On Windows:
`myvenv\Scripts\activate`

## Usage
Run the tool with an IP address or a search term for HTTP services. You can also add optional flags for vulnerability checks (only for IP addresses) and report generation.

### Basic Commands
1. Lookup IP Information:
```bash
python3 shodan_nmap.py --ip <IP_ADDRESS>
```
Example:
```bash
python3 shodan_nmap.py --ip 8.8.8.8
```
You can aslo add more than one IP, comma-separated:
```bash
python3 shodan_nmap.py --ip 8.8.8.8,192.168.0.1
```
You can also specify a port:
```bash
python3 shodan_nmap.py --ip 8.8.8.8,192.168.0.1:80
```

2. Search for HTTP Services:
```bash
python3 shodan_nmap.py --search <query>
```
    Example:
```bash
python3 shodan_nmap.py --search "apache"
```
You can aslo add more than one query:
```bash
python3 shodan_nmap.py --search "apache" "nginx"
```

3. Check Vulnerabilities: Add `--nmap-vuln` to `--ip` command to perform a vulnerability check.
Example:
```bash
python3 shodan_nmap.py --ip 8.8.8.8 --nmap-vuln
```
4. Generate a Report: Use `--report` to save the results in JSON format.
```bash
python3 shodan_nmap.py --ip 8.8.8.8 --report
```

### Combined Commands
Combine arguments to check for vulnerabilities and generate a report  in JSON format.

Example:
```bash
python3 shodan_nmap.py --ip 8.8.8.8 --nmap-vuln --report
```

### Parameters
- `--ip <IP>`: Specify an IP address. You can add multiple IPs separated by commas. (Avoid Spaces)
- `--search <query>`: Search for HTTP services using a query string (e.g., "apache").
- `--nmap-vuln`: Perform a vulnerability check on the IP. (Optional)
- `--report`: Save results as JSON reports in the current directory. (Optional)

## Saving Results (Report)
You can specify the `--report` option and generate a JSON report for either IP addresses or HTTP services.

The reports are saved in the same directory with the following names:

- IP Report: `report_<IP>.json` (e.g., report_8.8.8.8.json)
- Search Report: `report_search_results.json`

## Make sure to have a valid API-KEY
1. Log in to Shodan
2. Locate your API Key in your Account Overview
3. Copy the API Key to authenticate your request to the Shodan API
4. In the same path where the shodan_tool.py is, create a `.env` file and store the API key there. Example in the `.env` file: `SHODAN_API_KEY=this_is_my_api_key`
5. Check the file to confirm that it contains the key:`cat .env`. Make sure there's nothing else but the key in this specific format (no extra spaces, etc.).

## Logging
The tool logs actions, including successful Shodan queries, errors, and any exceptions encountered during the execution. Logs are saved in a shodan_tool.log file located in the same directory as the tool.

## Known Limitations
- You need a Shodan account to check for IPs.
- You might need a Shodan account with membership to search for HTTP services.
- The Shodan API has rate limits based on the type of account. You may encounter restrictions on the number or type of queries you can make.
- Checking vulnerabilities on "search HTTP services" mode is not possible.
- The tool handles common API errors but may not cover all edge cases.
- Shodan API can't always retrieve all the information. Therefore, some IP details might lack information about the organization, product version, or OS, leaving the output data empty.
- Lacks multithreading. IP addresses or search queries are processed one by one. For large lists of IPs or multiple queries, the tool may take significant time to complete.
- The tool requires a `.env` file with a valid API key for authentication. Missing or incorrect API key configuration will raise an error.

## Contributing
To contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request when done.

Contributions welcome!