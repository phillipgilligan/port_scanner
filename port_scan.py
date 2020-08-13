import pyfiglet 
import sys 
import socket 
from datetime import datetime
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.progress import track

ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font='block')
ascii_author = pyfiglet.figlet_format("By Binary Fallen", font='cybersmall')
rprint(ascii_banner) 
rprint(ascii_author) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
portstart = int(input("Starting Port: "))
portend = int(input("Ending Port: "))
portlist = []
portlist.extend(range(portstart, portend+1))


def portScanner(portlist):
    table = Table(title=f"Port Scan for Host: {host}")
    table.add_column("Port Number", justify="left", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Service", justify="right", style="green")
    
    for port in track(range(portend), description="Processing..."):
        if s.connect_ex((host, port)):
            table.add_row(f"{port}", "[bold red]Closed[/bold red]", "Unknown")
        else:
            table.add_row(f"{port}", "[bold green]Open[/bold green]", "Unknown")
    
    rprint ("Scanning Completed")
    console = Console()
    console.print(table)

portScanner(portlist)

#for n in track(range(n), description="Processing..."):