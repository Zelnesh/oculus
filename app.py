from flask import Flask,render_template,request
from forms import DNSForm,IPGForm,PortScannerForm
from fetch import DNSLookup,IPGlocation,PortScanner
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyberpunk-key'

# Main page
@app.route('/')
def main():
    return render_template('main.html')

# DNS Lookup page
@app.route('/dns_lookup', methods = ['GET', 'POST'])
def dns_lookup():
    form = DNSForm()
    result = None

    if form.validate_on_submit():
        dns = form.dns_name.data
        dns_record  = DNSLookup(dns)
        result = dns_record.fetch_info()
        return render_template('dns_lookup_result.html', data=result)
    return render_template('dns_lookup.html', form=form)

# IP Geolocation page
@app.route('/ipg_location', methods = ['GET', 'POST'])
def ipg_location():
    form = IPGForm()
    result = None

    if form.validate_on_submit():
        ip = form.ip_address.data
        ip_record = IPGlocation(ip)
        result = ip_record.fetch_info()
        return render_template('ip_geolocation_result.html', data=result)
    return render_template('ip_geolocation.html', form=form)

# Port Scanner page
@app.route('/port_scanner', methods=['GET', 'POST'])
def port_scanner():
    form = PortScannerForm()
    reult = None

    if form.validate_on_submit():
        ip = form.ip_address.data
        ports = int(form.ports.data)
        scanner = PortScanner(ip, ports)
        open_ports = asyncio.run(scanner.scan_ports())
        return render_template('port_scanner_result.html', open_ports=open_ports)
    return render_template('port_scanner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
