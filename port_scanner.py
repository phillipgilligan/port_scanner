import pyfiglet 
import sys 
import socket 
from datetime import datetime
from rich import print as rprint #We don't want to replace print.
from rich.console import Console
from rich.table import Table
from rich.progress import track
import json

#Loading in our json file to be read from for service matching.
data = json.load(open("port-db.json"))


#This functions only purpose is to make a banner for the port scanner, how
#else would people know how cool you are?
def banner():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font='block')
    ascii_author = pyfiglet.figlet_format("By Binary Fallen", font='cybersmall')
    rprint(ascii_banner) 
    rprint(ascii_author)

#This grabs user input and stores them in vars to work with.
def get_host():
    host = input("Please enter the IP you want to scan: ")
    return host

def get_portlist():
    portstart = int(input("start: "))
    portstop = int(input("stop: "))
    portlist = []
    portlist.extend(range(portstart, portstop))
    return portlist

#This creates our basic table along with some styling applied to it for console output.
def table_constructor(host):
    table = Table(title=f"Port Scan for Host: {host}")
    table.add_column("Port Number", justify="center", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Service", justify="left", style="yellow")
    return table
    
#The bread and butter port scan function, takes the port list, and for each port tries to connect
#to the host with the port number. If it connects, closes said connection, logs it, then adds a row
#in this row, we search for the port and then sub in the services that could be running on it according
#to the json file.
def port_scanner():
    host = get_host()
    portlist = get_portlist()
    table = table_constructor(host)
    for port in portlist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.05)      
        try:
            s.connect((host, port))
            s.close()
            services = data.get(str(port), "Unknown")
            services = str(services)
            services = services.translate({ord(i): None for i in '\'[]'})
            table.add_row(f"{port}", "[bold green]Open[/bold green]", f"{services}")
            
        except (socket.timeout, socket.error):
            pass
            # If you wanted to have instead it detect dead ports use the code below.
            # table.add_row(f"{port}", "[bold red]Closed[/bold red]", "Unknown")

    
    rprint ("Scanning Completed")
    console = Console()
    console.print(table)
    input("Scanning completed, press any key to exit")

def main():
    banner()
    port_scanner()
    
main()