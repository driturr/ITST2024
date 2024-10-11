# Lägg till IP-adresser från tailscale-miljön i en text fil (en ip-adress per rad).
# Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen och till en fil.
import os

file_path = "ip.txt"

with open(file_path, "r") as file:
    ip_addresses = file.read().splitlines()

with open("ping.txt", 'w') as result_file:
    for ip_address in ip_addresses:
        response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
        print(response)