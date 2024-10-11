import nmap

def scan(ip):
    nmap_top_ports = nmap.PortScanner()
    nmap_top_ports.scan(ip, arguments='--top-ports 100')
    results = nmap_top_ports[ip]
    return results