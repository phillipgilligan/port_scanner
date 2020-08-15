import pyfiglet 
import sys 
import socket 
from datetime import datetime
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.progress import track
import json

ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font='block')
ascii_author = pyfiglet.figlet_format("By Binary Fallen", font='cybersmall')
rprint(ascii_banner) 
rprint(ascii_author)

# port = "80"
data = json.load(open("port-db.json"))
# for key, value in data.items():
#     if key == port:
#         rprint(key, value) # example usage


host = input("Please enter the IP you want to scan: ")

def portScanner():
    portstart = int(input("start: "))
    portstop = int(input("stop: "))
    portlist = []
    portlist.extend(range(portstart, portstop))
    table = Table(title=f"Port Scan for Host: {host}")
    table.add_column("Port Number", justify="center", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Service", justify="left", style="yellow")
    
    for port in portlist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.05)
        
        try:
            s.connect((host, port))
            s.close()
            x = data.get(str(port), "Unknown")
            table.add_row(f"{port}", "[bold green]Open[/bold green]", f"{x}")
            
        except (socket.timeout, socket.error):
            pass
            # table.add_row(f"{port}", "[bold red]Closed[/bold red]", "Unknown")

    
    rprint ("Scanning Completed")
    console = Console()
    console.print(table)

portScanner()

hold = input("Scanning completed, press any key to exit")