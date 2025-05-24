import requests

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
