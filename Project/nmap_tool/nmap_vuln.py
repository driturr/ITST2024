import nmap
def scan(ip):
    try:
        nmap_vuln_scan = nmap.PortScanner()
        nmap_vuln_scan.scan(ip, arguments="--script vuln")
        results = nmap_vuln_scan[ip]
        return results

    except Exception as e:
        print(f"An error ocurred while scaninng {ip}: {e}")