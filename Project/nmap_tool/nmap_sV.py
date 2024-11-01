import nmap

def scan(ip):
    nmap_sV = nmap.PortScanner()
    nmap_sV.scan(ip, arguments = '-sV')
    results = nmap_sV[ip]
    return results

