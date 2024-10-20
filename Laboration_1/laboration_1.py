#Self-Note 1: Remember to activate virtual environment to find nmap:
    #In Terminal, in path to "venv" folder, type: source venv/bin/activate 
#Note 2: If run in Visual Studio Code, option 3 will not work since it requires root privileges.
    #Not recommended to run Visual Code as root. Exposed to vulnerabilities from any extensions within Visual Code

from nmap_sV import scan as scan_sV
from nmap_sS import scan as scan_sS
from nmap_top_ports import scan as scan_top_ports


while True:
    ip = input("""********************
Welcome to the nmap tool!
What IP or IPs will you be scanning today?
(Separate more than one IP using comas ',' between each IP)
        """)    

    ip_list = [ip.strip() for ip in ip.split(",")]

    print("\n********************\nConfirm IPs: \nAre you sure you want to continue?")
    check_ip_correct = input("\nPress 'Y' to continue or any other key to start over: ")
    if check_ip_correct == "Y":
        break
    else:
            print("\n********************\nRestarting the program...")

print(f"You will scan the IPs: {ip_list}")

print("""\n********************
Now let's choose what type of scan you want to perform.
\nSelect from below (1, 2 or 3):""")

option = input("""
1: Check open ports to determine service/version info
2: Scan 100 most common ports
3: TCP SYN port scan
               """)

scan_performed = False
results = {}

if option == "1":
    selected_option = "Check open ports to determine service/version info"
    print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
    for ip in ip_list:
        print(f"\n\nScanning... {ip}")
        results[ip] = scan_sV(ip)
        print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
        scan_performed = True


elif option == "2":
    selected_option = "Scan 100 most common ports"
    print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
    for ip in ip_list:
        print(f"\n\nScanning... {ip}")
        results[ip] = scan_top_ports(ip)
        print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
        scan_performed = True

elif option == "3":
    selected_option = "TCP SYN port scan"
    print(f"\nCool! \nYou selected '{selected_option}' on IPs: ")
    for ip in ip_list:
        print(f"\n\nScanning... {ip}")
        results[ip] = scan_sS(ip)
        print(f"\a\n************\nScan results for {ip}:\n\a{results[ip]}")
        scan_performed = True

else:
    selected_option = "Invalid option selected"
    print(f"\n{selected_option}: You will have to start over")



if scan_performed == True:
    save_results = input("\n\nPress 'Y' to save the results. Otherwise, press any other key.")
    if save_results == "Y":
        with open("results_nmap.txt", 'w') as file:
            file.write(str(results))
            print("\n\a\aThe results have been saved into 'results_nmap.txt'")
    else:
        print("\nResults not saved. \n\n**************** \nExiting program \n****************")
else:
    print("\n No performed scans.") 
