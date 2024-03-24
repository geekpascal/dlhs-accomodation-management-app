from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    group = SelectField('Group', choices=[('group1', 'AGEGE'), ('group2', 'AJEGUNLE'), ('group3', 'ALIMOSHO'), ('group4', 'BAGAGRY'), ('group5', 'EPE'), ('group6', 'FESTAC'), ('group7', 'GBAGADA'), ('group8', 'IKEJA'), ('group9', 'IKORODU'), ('group10', 'ISOLO'), ('group11', 'KETU'), ('group12', 'LAGOS ISLAND'), ('group13', 'MUSHIN'), ('group14', 'ORILE'), ('group15', 'OSHODI'), ('group16', 'SOMOLU'), ('group17', 'SURULERE'), ('group18','YABA')], validators=[DataRequired()])
    category = SelectField('Category', choices=[('', 'AGEGE'), ('group2', 'AJEGUNLE'), ('group3', 'ALIMOSHO'), ('group4', 'BAGAGRY'), ('group5', 'EPE'), ('group6', 'FESTAC'), ('group7', 'GBAGADA'), ('group8', 'IKEJA'), ('group9', 'IKORODU'), ('group10', 'ISOLO'), ('group11', 'KETU'), ('group12', 'LAGOS ISLAND'), ('group13', 'MUSHIN'), ('group14', 'ORILE'), ('group15', 'OSHODI'), ('group16', 'SOMOLU'), ('group17', 'SURULERE'), ('group18','YABA')], validators=[DataRequired()])
    campus = SelectField('Campus', choices=[('lasu', 'LASU IKEJA'), ('lasu', 'LASU EPE'), ('lasu', 'LASU OJO'), ('unilag', 'University of Lagos (UNILAG)'), ('other', 'OTHERS')], validators=[DataRequired()])
    address = TextAreaField('Home Address', validators=[DataRequired()])
    whatsapp = StringField('WhatsApp Number', validators=[DataRequired()])
    participant_type = SelectField('Participant Type', choices=[('invitee', 'Invitee'), ('first_timer', 'First Time attendee'), ('regular', 'Regular attendee')], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    ageBracket = SelectField('Age bracket', choices=[('16-19', '16-19'), ('20-23', '20-23'), ('24-26', '24-26'), ('27-30', '27-30'), ('above_31', 'Above 31')], validators=[DataRequired()])
    submit = SubmitField('Register')