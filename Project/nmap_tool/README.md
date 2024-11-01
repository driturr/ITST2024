# Scanning tool with Nmap  
`nmap_tool.py` is simple tool for performing various network scans using Nmap. This tool allows users to scan multiple IP addresses for open ports, service/version information, and potential vulnerabilities.  

## Features
- **Scan Multiple IPs**: Enter one or multiple IPs separated by commas.
- **Scan Options**: Choose from 4 scan types:
  - Service/version detection
  - Scanning the 100 most common ports
  - TCP SYN port scan
  - Vulnerability scanning
- **Error Handling**: Continue scanning even if one IP fails.
- **Save Results**: Option to save the scan results to a file.
<hr>  

## Installation
### Prerequisites
Install Nmap: [Nmap's official site](https://nmap.org/download.html).

### Required Python Packages
This script runs in Python3, therefore make sure you have Python installed. You will need the `python-nmap` package. You can install the required package using pip:
```bash
pip3 install python-nmap
```
### Clone the repository  
1. Clone this repo to your local machine
`git clone https://github.com/driturr/ITST2024/tree/main/Project/nmap_tool`  

2. Install the required libraries:  
`pip3 install -r requirements.txt`

3. Run the script:  
**Interactive mode:**
`python3 nmap_tool.py`  
or **Command-line mode:** `python3 nmap_tool.py --ip 127.0.0.1,192.168.0.1 --option 1`

## Usage
The tool can be run in two modes: **command-line mode** and **interactive mode**.

### Command-line mode:
Use `nmap_tool.py` to scan specific IPs.

**Command**
```bash
python3 nmap_tool.py --ip <IP,IP,IP> --option <option_number> --file <file_name>
```

**Arguments**  
If you choose command-line mode, some arguments need to be specified.

- `--ip`: The IP or IPs that is going to be scanned (separated by commas).
- `--option>`: The type of scan to perform.
- `--file`: Optional file name in which the results are to be saved. If not specified when running the script, the option will be offered again after the scan has finished.

Example:
```bash
python3 nmap_tool.py --ip 127.0.0.1,192.168.0.1 --option 1 --file results.txt
```

### Interactive mode:
Simply run the script without any arguments, and it will guide you through the input process. Example:  
```bash
python3 nmap_tool.py
```

<hr>  

## Scan Options
- `1` Check open ports to determine service/version info
- `2` Scan 100 most common ports
- `3` TCP SYN port scan
- `4` Vulnerability scan: check for possible vulnerabilities

### Command-line mode:
When running on command-line mode, select the option number as an argument before running the script.  

1, 2, 3 or 4 corresponding with the type of scan:
`--option <number>`  


### Interactive mode:
When prompted, choose from the scan types: `1`, `2`, `3`, `4`


## Saving Results (Optional)
You can save the scan results either by:

- Choosing to save the results after the scan is completed.
- Providing a file name in the command line using the `--file` option. Example: `--file filename.txt`

## Known Limitations
- Requires Nmap to be installed on your system and accessible via command line.
- Requires root privileges to run option 3 (TCP SYN port scan).
- The script may not handle all types of exceptions. It's recommended to review error messages for any unexpected behavior.
- Formatting missing in saved results.

## Contributing
To contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request when done.

Contributions welcome!