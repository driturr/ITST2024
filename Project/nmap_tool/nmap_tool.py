#Self-Note 1: Remember to activate virtual environment to find nmap:
    #In Terminal, in path to "venv" folder, type: source venv/bin/activate 


#This script can run both through the command line or interactive mode (user input)

import argparse
from nmap_sV import scan as scan_sV
from nmap_sS import scan as scan_sS
from nmap_top_ports import scan as scan_top_ports
from nmap_vuln import scan as scan_vuln

def get_ip(ip_input=None): #collects IPs
    if ip_input: #command line mode
        ip_list = [ip.strip() for ip in ip_input.split(",")]
        print(f"You will scan the IPs: {ip_list}")
        return ip_list
    else: #interactive mode
        while True:
                ip = input("""********************
            Welcome to the nmap tool!
            What IP or IPs will you be scanning today?
            (Separate more than one IP using commas ',' between each IP)
                    """)    

                ip_list = [ip.strip() for ip in ip.split(",")]

                print("\n********************\nConfirm IPs: \nAre you sure you want to continue?")
                check_ip_correct = input("\nPress 'y' to continue or any other key to start over: ")
                if check_ip_correct.lower() == "y":
                    print(f"You will scan the IPs: {ip_list}")
                    return ip_list
                else:
                        print("\n********************\nRestarting the program...")


def choose_scan_type(ip_list, option=None):#collects scanning option & performs scan. Saves results
    scan_performed = False
    results = {}

    if option is None: #interactive mode
        print("""\n********************
        Now let's choose what type of scan you want to perform.
        \nSelect from below (1, 2, 3 or 4):""")
        option = input("""
        1: Check open ports to determine service/version info
        2: Scan 100 most common ports
        3: TCP SYN port scan
        4: Vulnerability scan: check for possible vulnerabilities
                    """)
    
    #handles scans based on the chosen option
    if option == "1":
        selected_option = "Check open ports to determine service/version info"
        print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
        for ip in ip_list:
            print(f"\n\nScanning... {ip}")
            try:
                results[ip] = scan_sV(ip)
                print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
                scan_performed = True
            except Exception as e:
                print(f"Error while scanning {ip}: {e}")
                results[ip] = None #indicates failure if an IP scan fails


    elif option == "2":
        selected_option = "Scan 100 most common ports"
        print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
        for ip in ip_list:
            print(f"\n\nScanning... {ip}")
            try:
                results[ip] = scan_top_ports(ip)
                print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
                scan_performed = True
            except Exception as e:
                print(f"Error while scanning {ip}: {e}")
                results[ip] = None

    elif option == "3":
        selected_option = "TCP SYN port scan"
        print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
        for ip in ip_list:
            print(f"\n\nScanning... {ip}")
            try:
                results[ip] = scan_sS(ip)
                print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
                scan_performed = True
            except Exception as e:
                print(f"Error while scanning {ip}: {e}")
                results[ip] = None

    elif option == "4":
        selected_option = "Vulnerability scan"
        print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
        for ip in ip_list:
            print(f"\n\nScanning... {ip}")
            try:
                results[ip] = scan_vuln(ip)
                print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
                scan_performed = True
            except Exception as e:
                print(f"Error while scanning {ip}: {e}")
                results[ip] = None

    else:
        selected_option = "Invalid option selected"
        print(f"\n{selected_option}: You will have to start over")
        
    return results, scan_performed

def choose_save_results(results, filename=None):
    if filename: #command line mode
        with open(filename, 'w') as file:
            file.write(str(results))
            print(f"\n\a\aThe results have been saved into '{filename}'.")
    
    else: #interactive mode. It continues here if no filename is given in command-line mode
        save_results = input("\n\nPress 'y' to save the results. Otherwise, press any other key.")
        if save_results.lower() == "y":
            filename = input("Please enter the filename to save the results (.txt extension). Example: 'results_nmap.txt':")
            with open(filename, 'w') as file:
                file.write(str(results))
                print("\n\a\aThe results have been saved into {filename}")
        else:
            print("\nResults not saved. \n\n**************** \nExiting program \n****************")

def main():
    parser = argparse.ArgumentParser(description="""Nmap Scanning Tool.
                                     \nRequirement: [--ip] + [--option]. ||
                                     \nOptional: [--file] to save results
                                     \nExample: --ip 127.0.0.1, 192.168.0.1 --option 1 --file results_nmap.txt
                                     """)
    parser.add_argument("--ip", type=str, help="One IP or several IPs separated by comma.")
    parser.add_argument("--option", type=str, help="""Scan type option (1, 2, 3 or 4):
    \n1 for 'Check open ports to determine service/version info'.
    \n2 for 'Scan 100 most common ports'.
    \n3 for 'TCP SYN port scan'.
    \n4 for 'Vulnerability scan: check for possible vulnerabilities'
    """)
    parser.add_argument("--file", type=str, help="Optional filename to save results.")

    args = parser.parse_args()

    ip_list = get_ip(args.ip) #Collect IPs from command line mode or interactive mode
    results, scan_performed = choose_scan_type(ip_list, args.option) # Choose scan type from command line mode or interactive mode

    # If scans were performed, ask to save results
    if scan_performed:
        choose_save_results(results, args.file)
    else:
        print("\n No performed scans.")

if __name__ == "__main__":
    main()