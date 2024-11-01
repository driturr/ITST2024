import shodan
import argparse
import os
from dotenv import load_dotenv
import json
import logging
import re #used in validate_ip_format() function
import nmap_vuln


#load the shodan API key from environment
load_dotenv()

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY") #get the API key from environment

if not SHODAN_API_KEY:
    raise ValueError("Shodan API key not found. Set the SHODAN_API_KEY in a .env file.")

api = shodan.Shodan(SHODAN_API_KEY)

logging.basicConfig(filename='shodan_tool.log', level=logging.INFO, filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

# Check if the IP address matches the correct format
def validate_ip_format(ip_address):
    ip_pattern = re.compile(
        r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'
        r'(?::([0-5]?[0-9]{1,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?$'
    )
    if not ip_pattern.match(ip_address):
        raise ValueError(f"Invalid IP address format: {ip_address}")
    
# ip_addresses Mode --> Get info about an IP from Shodan & print info
def lookup_ip(ip_address, check_nmap=False):
    vulnerabilities = []
    try:
        # extract port if provided
        ip_parts = ip_address.split(':') # splits the string based on ':' as delimiter
        ip = ip_parts[0]
        port = ip_parts[1] if len(ip_parts) > 1 else None # checks if the list 'ip_parts' has more than one element
                                                          # if the condition is True, it means the input includes a port number and assigns the second element (index 1) to the variable "port"
                                                          # if no port provided, it assigns "None" to "port"
        validate_ip_format(ip_address)
        host_info = api.host(ip)

        logging.info(f"Successfully retrieved data for {ip}")
        print(f"\nInformation for IP: {ip_address}")
        print(f"Organization: {host_info.get('org', 'Not Available')}")
        print(f"Operating System: {host_info.get('os', 'Not Available')}")

        open_ports = []
        # port_found = False # track if the specified port was found

        # Print "open ports" only if no specific port was provided
        if not port:
            print("\nOpen Ports:")
        for item in host_info['data']:
            item_port = item['port']
            if port and item_port != port: # skip other ports if a specific port was provided
                continue
            port_info = {"Port": item['port'], "Service": item.get('product', 'Not Available')}
            open_ports.append(port_info)
            print(f"Port: {item['port']}, Service: {item.get('product', 'Not Available')}")
        

        # Look for vulnerabilties if requested
        if check_nmap and (port or open_ports):
            print("\nChecking for vulnerabilities with Nmap...")
            nmap_results = nmap_vuln.scan(ip)
            if nmap_results:
                vulnerabilities.append({"Tool": "Nmap", "Findings": nmap_results})
                print(f"Nmap results for {ip}: {nmap_results}")
                for vuln in nmap_results:
                    print(f" - {vuln}")

        results = {
            "IP Address": ip,
            "Organization": host_info.get('org', 'Not Available'),
            "Operating System": host_info.get('os', 'Not Available'),
            "Open Ports": open_ports,
            "Vulnerabilities": vulnerabilities if vulnerabilities else []
        }
        return results
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print(f"Error: {e}")
    except shodan.APIError as e:
        logging.error(f"Shodan APIError for {ip}: {e}")
        print(f"Error querying Shodan: {e}")
    except Exception as e:
        logging.error(f"Unexpected error for {ip}: {e}")
        print(f"Unexpected error: {e}")

# search mode --> search for HTTP services, print results & vulnerabilities
def search_http_services(queries):
    all_results = [] # all results from each query
    
    for query in queries:
        print(f"\nSearching for HTTP services related to '{query}'...")
        try:
            # search query on Shodan
            results = api.search(f"http {query}")
            logging.info(f"Successfully retrieved search results for HTTP services related to '{query}'. Found {len(results['matches'])} matches.")
            print(f"\nSearch results for HTTP services related to '{query}':")

            # Go through each match in the results
            for match in results['matches']:
                ip = match['ip_str']
                port = match['port']
                organization = match.get('org', 'Not Available')
                product = match.get('product', 'Not Available')
                version = match.get('version', 'Not Available')

                # service info
                print(f"\nIP: {ip}, Port: {port}, Organization: {organization}")
                print(f"Product: {product}, Version: {version}")

                all_results.append({
                    "IP": ip,
                    "Port": port,
                    "Organization": organization,
                    "Product": product,
                    "Version": version,
                })
        
        except shodan.APIError as e:
            logging.error(f"Shodan APIError during HTTP service search: {e}")
            print(f"Error searching Shodan: {e}")
        except Exception as e:
            logging.error(f"Unexpected error for {query}: {e}")
            print(f"Unexpected error: {e}")
    
    return all_results

# save a report in JSON format: valid for IP info or Search Results
def generate_report(data, report_name):
    with open(report_name, 'w') as report_file:
        json.dump(data, report_file, indent=4)
    print(f"Report generated: {report_name}")


def main():
    parser = argparse.ArgumentParser(description="""Shodan IP Tool: Query Shodan for information about IP addresses or search for HTTP services.
                                     \n|| 2 modes: "IP addresses" or "HTTP services".
                                     \n|| If "IP addresses mode", optional check for vulnerabilities using Nmap.
                                     \n|| Requirement: If "IP addresses mode", then --ip <ip> or --ip <ip:port>. Example: 127.0.0.1,192.168.0.1:80
                                     \n|| Requirement: If "HTTP services mode", then --search <query>. Example: --search "apache". Example: --search "apache" "nginx"
                                     \n\n|| Optional: --report --> Example: 192.168.0.1 --report
                                     \n|| Optional: --nmap-vuln --> Example: 192.168.0.1 --nmap-vuln
                                     \n\n|| Example: IPs combined: --ip 192.168.0.0.1,8.8.8.8 --nmap-vuln --report
                                     \n|| Example HTTP service combined: --search "apache" --report
                                     \n|| OBS!: The --search function doesn't allow checking for vulnerabilities.
                                     \n\n
                                     """)
    parser.add_argument("--ip", help="""IP address or comma-separated list of IP addresses (e.g., 192.168.0.1,8.8.8.8).
                        Optionally include port followed by ':' (e.g., 192.168.0.1:80). AVOID SPACES\n
                        """)
    parser.add_argument("--search", type=str, nargs='*', help="Search for HTTP services using specified queries.\n")
    parser.add_argument('--nmap-vuln', action='store_true', help='Check for vulnerabilities using Nmap. (Optional)\n')
    parser.add_argument("--report", action='store_true', help="Generate a report for each IP address or HTTP service search results. (Optional)")

    args = parser.parse_args()

    try:
        api.info() # verify key is valid
    except shodan.APIError as e:
        print(f"Invalid API key: {e}")
        logging.error(f"Invalid Shodan API key: {e}")
        return

    # If IP addresses provided, run lookup on each IP
    if args.ip:
        if args.nmap_vuln:
            print("Vulnerability check is enabled.")
        else:
            print("Vulnerability check is disabled.")

        ip_list = [ip.strip() for ip in args.ip.split(',')]
        for ip in ip_list:
            print(f"Processing IP: {ip}...")
            ip_info = lookup_ip(ip, check_nmap=args.nmap_vuln)
            if args.report and ip_info:
                generate_report(ip_info, f"report_{ip.replace(':', '_')}.json")

    # If search query is provided, run HTTP service search
    if args.search:
        print(f"Searching for HTTP services related to '{args.search}'...")
        search_results = search_http_services(args.search)
        if args.report and search_results:
            generate_report(search_results, "report_search_results.json")
    
    # Check that at least one mode is specified
    if not args.ip and not args.search:
        parser.print_help()
        print(f"\n\nAttention!! Please specify either --ip for IP lookup or --search for HTTP service search.")
        exit(1) # exists if no arguments provided

if __name__ == "__main__":
    main()
    



#other pattern matches that I tried:
    
    # (r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
    #                         r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
    #                         r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
    #                         r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)(:[0-9]{1,5})?$')
    
    #(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})?$') #pattern to match exactly "xxx.xxx.xxx.xxx" each segmenet is 1-3 digits, with optional :port