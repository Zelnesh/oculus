from flask import Flask,render_template,request
from forms import DNSForm
from fetch import DNSLookup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyberpunk-key'

@app.route('/')
def main():
    return render_template('main.html')

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

if __name__ == '__main__':
    app.run(debug=True)
