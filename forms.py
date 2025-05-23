from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, IPAddress

class DNSForm(FlaskForm):
    dns_name = StringField('DNS Name', validators=[DataRequired()], render_kw={"placeholder": "Enter DNS Name"})
    submit = SubmitField('Lookup')
