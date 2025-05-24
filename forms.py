from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, IPAddress

# Form for the DNS Lookup 
class DNSForm(FlaskForm):
    dns_name = StringField('DNS Name', validators=[DataRequired()], render_kw={"placeholder": "Enter DNS Name"})
    submit = SubmitField('Lookup')

# Form for the IP geo location
class IPGForm(FlaskForm):
    ip_address = StringField('IP Address', validators=[DataRequired()], render_kw={"placeholder": "Enter IP address"})
    submit = SubmitField('IPGlocation')
