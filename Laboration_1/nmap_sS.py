import nmap

def scan(ip):
    nmap_sS = nmap.PortScanner()
    nmap_sS.scan(ip, arguments='-sS')
    results = nmap_sS[ip]
    return results
