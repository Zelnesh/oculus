import requests
import asyncio

# Class for the DNS Lookup
class DNSLookup():
    def __init__(self, domain):
        self.domain = domain

    def fetch_info(self):
        url = f"https://dns.google/resolve?name={self.domain}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

# Class for the IP Geolocation
class IPGlocation():
    def __init__(self, ip):
        self.ip = ip

    def fetch_info(self):
        url = f"https://ipwhois.app/json/{self.ip}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

# Class for the Port scanner
class PortScanner():
    def __init__(self, host: str, ports, timeout=1.0, concurrency=100):
        self.host = host
        self.ports = ports
        self.timeout = timeout
        self.open_ports = []
        self.semaphore = asyncio.Semaphore(concurrency)

    async def scan_port(self, port: int):
        async with self.semaphore:
            try:
                await asyncio.wait_for(asyncio.open_connection(self.host, port),timeout=self.timeout)
                self.open_ports.append(port)
            except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
                pass

    async def scan_ports(self):
        self.open_ports = []
        tasks = [self.scan_port(port) for port in range(self.ports)]
        await asyncio.gather(*tasks)
        return self.open_ports
        
