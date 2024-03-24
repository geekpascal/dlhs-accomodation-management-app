from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
import os

app = Flask(__name__)
app.static_folder = 'static'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vipascal@localhost:5432/dlccdb'
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('POSTGRES_URL')
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)

# Database model class
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    campus = db.Column(db.String(50), nullable=False)
    areYouAworker = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text, nullable=False)
    emailAddress = db.Column(db.Text, nullable=False)
    whatsapp = db.Column(db.String(12), nullable=False)
    participant_type = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    ageBracket = db.Column(db.String(20), nullable=False)
    hostel = db.Column(db.String(250), nullable=True)

# Create the database tables if they don't exist
app.app_context().push()
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')



def determine_accommodation(gender, campus, category):
    # Gender check
    if gender.lower() == 'male':
        gender_key = 'Boys'
        girls_hostel = False
    elif gender.lower() == 'female':
        gender_key = 'Sisters'
        girls_hostel = True
    else:
        return "Invalid gender provided"
    
    # if gender == 'Male' and category == 'Choir':
    #     accomodation = "testing"
    #     if category == 'Planning Committe':
    #         accomodation = 'White House'
    #     elif category == 'Associate Coordinator':
    #         accomodation = 'Bethel 4'
    #     elif category == 'Choir':
    #         accomodation = 'Right wing 2nd floor of the boys Hostel'
    #     elif category == 'Staff':
    #         accomodation = 'Left wing 2nd floor of the boys Hostel'
    #     elif category == 'Corpers':
    #         accomodation = 'Left wing 2nd floor of the boys Hostel' 
    #     elif category == 'Principal Officer':
    #         accomodation = 'White House'
    #     elif category == 'Others':
    #         accomodation = 'Common Room'            
    # else:
    #     if category == 'Planning Committe':
    #         accomodation = 'White House'
    #     elif category == 'Associate Coordinator':
    #         accomodation = 'Bethel 4'
    #     elif category == 'Choir':
    #         accomodation = 'Right wing 2nd floor of the girls Hostel'
    #     elif category == 'Staff':
    #         accomodation = 'Left wing 2nd floor of the girls Hostel'
    #     elif category == 'Corpers':
    #         accomodation = 'Left wing 2nd floor of the girls Hostel'
    #     elif category == 'Principal Officer':
    #         accomodation = 'White House' 
    #     elif category == 'Others':
    #         accomodation = 'Common Room'

    # Campus and group check
    schools = {
        'LASU IKEJA': 'LASU IKEJA',
        'LASU EPE': 'LASU EPE',
        'LASU OJO': 'LASU OJO',
        'UNILAG': 'UNILAG',
        'AFRICAN CHURCH': 'AFRICAN CHURCH',
        'AOCOED': 'AOCOED',
        'ANCHOR UNIVERSITY': 'ANCHOR UNIVERSITY',
        'CALEB UNIVERSITY': 'CALEB UNIVERSITY',
        'CISM CAMPUS': 'CISM CAMPUS',
        'CORPERS': 'CORPERS',
        'FCE (TECH) AKOKA': 'FCE (TECH) AKOKA',
        'FISHERIES': 'FISHERIES',
        'FRENCH VILLAGE': 'FRENCH VILLAGE',
        'FSTC': 'FSTC',
        'LASUSTECH': 'LASUSTECH',
        'LAW SCHOOL': 'LAW SCHOOL',
        'LUTH': 'LUTH',
        'NOUN': 'NOUN',
        'ORTHOPADIC IGBOBI': 'ORTHOPADIC IGBOBI',
        'PROJECTIME': 'PROJECTIME',
        'RADIOGRAPHY': 'RADIOGRAPHY',
        'YABATECH': 'YABATECH',
        'YABATECH EPE': 'YABATECH EPE',
        "SON, IGANDO": "SON, IGANDO",
        "NOIC": "NOIC",
        "NASFA": "NASFA",
        "LCP": "LCP",
        "CORPER": "CORPER"
    }

    categories = {
        'Corper': 'Corper',
        'Student': 'Student',
        'Choir': 'Choir',
        'Staff': 'Staff',
        'Planning Committe': 'Planning Committe',
        'Associate Coordinator': 'Associate Coordinator',
        'Principal Officer': 'Principal Officer',
        'Others (Graduate, Postgraduate, etc.)': 'Others (Graduate, Postgraduate, etc.)'
    }
    

    if campus in schools.keys():
        school_key = schools[campus]
    # else:
    #     return "Invalid campus provided"

    if category in categories.keys():
        category_key = categories[category]
    # else:
    #     category_key = None

    # Accommodation determination
    accommodation = "Unknown"
    
    # if school_key and category_key == 'Choir' and gender == 'Female':
    #     accommodation = "Right wing 2nd floor of the girls Hostel"
    
    # if category_key == 'Choir' and gender == 'Male':
    #     accommodation = "Right wing 2nd floor of the boys Hostel"
    
    
    
      

#working code
    
    # if categories == "Student" and school_key not in categories:    
    #     if school_key in ['UNILAG', 'LUTH', 'YABATECH', 'LASU OJO']:
    #         accommodation = "Chalet 3 beside MHA after the GS lodge"
    #     elif school_key == 'ANCHOR UNIVERSITY':
    #         accommodation = "1st part of junior dormitory i.e the bungalow building"
    #     elif school_key in ['FRENCH VILLAGE', "LASUED IJANIKIN"] and not girls_hostel:
    #         accommodation = "Ground floor of boys hostel to the right"
    #     elif school_key in ['LASUSTECH', "LASU EPE"] and not girls_hostel:
    #         accommodation = "Ground floor of boys hostel to the left"
    #     elif school_key in ['YABATECH EPE', 'LASUTH', 'LASUED EPE'] and not girls_hostel:
    #         accommodation = "1st floor of the boys hostel to the right"
    #     elif school_key in ['FCE (TECH) AKOKA', 'SON, IGANDO', 'PROJECTIME', 'RADIOGRAPHY', "NOIC", "ORTHOPADIC IGBOBI", "FISHERIES", "LCP", "LAW SCHOOL"] and not girls_hostel and not categories:
    #         accommodation = "1st floor of the boys hostel to the left"
    #     elif category_key == 'Corper' or school_key == 'Noun' or school_key == 'NASFA' or school_key == 'FSTC':
    #         accommodation = "Left wing 2nd floor of the boys hostel"
    #     elif category_key == 'Choir' and gender == 'Male':
    #         accommodation = "Right wing 2nd floor of the boys hostel"
    #     elif category_key == 'Planning Committe':
    #         accommodation = "White House"
    #     elif category_key == 'Principal Officer':
    #         accommodation = "White House"
    #     elif category_key == 'Associate Coordinator':
    #         accommodation = "Bethel 4"
    #     elif category_key == 'Others (Graduate, Postgraduate, etc.)':
    #         accommodation = "Common Room"
#working code     
    

    if school_key in ['UNILAG', 'LUTH', 'YABATECH', 'LASU OJO'] and not categories:
        accommodation = "Chalet 3 beside MHA after the GS lodge"
    elif school_key == 'ANCHOR UNIVERSITY' and not categories:
        accommodation = "1st part of junior dormitory i.e the bungalow building"
    elif school_key in ['FRENCH VILLAGE', "LASUED IJANIKIN"] and not girls_hostel and not categories:
        accommodation = "Ground floor of boys hostel to the right"
    elif school_key in ['LASUSTECH', "LASU EPE"] and not girls_hostel and not categories:
        accommodation = "Ground floor of boys hostel to the left"
    elif school_key in ['YABATECH EPE', 'LASUTH', 'LASUED EPE'] and not girls_hostel and not categories:
        accommodation = "1st floor of the boys hostel to the right"
    elif school_key in ['FCE (TECH) AKOKA', 'SON, IGANDO', 'PROJECTIME', 'RADIOGRAPHY', "NOIC", "ORTHOPADIC IGBOBI", "FISHERIES", "LCP", "LAW SCHOOL"] and not girls_hostel and not categories:
        accommodation = "1st floor of the boys hostel to the left"
    elif category_key == 'Student' or school_key == 'Noun' or school_key == 'NASFA' or school_key == 'FSTC':
        accommodation = "Left wing 2nd floor of the boys hostel"
    elif category_key == 'Choir' and gender == 'Male':
        accommodation = "Right wing 2nd floor of the boys hostel"
    elif category_key == 'Corper' and gender == 'Male':
        accommodation = "Left wing 2nd floor of the boys hostel"
    elif category_key == 'Planning Committe':
        accommodation = "White House"
    elif category_key == 'Principal Officer':
        accommodation = "White House"
    elif category_key == 'Associate Coordinator':
        accommodation = "Bethel 4"
    elif category_key == 'Others (Graduate, Postgraduate, etc.)':
        accommodation = "Common Room"
    elif category_key == 'Student' and school_key in ['UNILAG', 'LUTH', 'YABATECH', 'LASU OJO'] and not girls_hostel:
        accommodation = "Chalet 3 beside MHA after the GS lodge"
    elif category_key == 'Student' and school_key == 'ANCHOR UNIVERSITY' and not girls_hostel:
        accommodation = "1st part of junior dormitory i.e the bungalow building"
    elif category_key == 'Student' and school_key in ['FRENCH VILLAGE', "LASUED IJANIKIN"]and not girls_hostel:
        accommodation = "Ground floor of boys hostel to the right"
    elif category_key == 'Student' and school_key in ['LASUSTECH', "LASU EPE"] and not girls_hostel:
        accommodation = "Ground floor of boys hostel to the left"
    elif category_key == 'Student' and school_key in ['YABATECH EPE', 'LASUTH', 'LASUED EPE'] and not girls_hostel:
        accommodation = "1st floor of the boys hostel to the right"
    elif category_key == 'Student' and school_key in ['FCE (TECH) AKOKA', 'SON, IGANDO', 'PROJECTIME', 'RADIOGRAPHY', "NOIC", "ORTHOPADIC IGBOBI", "FISHERIES", "LCP", "LAW SCHOOL"] and not girls_hostel:
        accommodation = "1st floor of the boys hostel to the left"
    elif category_key == 'Student' and school_key == 'Noun' and school_key == 'NASFA' and school_key == 'FSTC':
        accommodation = "Left wing 2nd floor of the boys hostel"

     
        
 #working code   
    elif girls_hostel:
        if school_key in ['UNILAG', 'LUTH', 'YABATECH', 'LASU OJO'] and not categories:
            accommodation = "Ground floor of the girl's hostel to the left"
        elif school_key in ['ANCHOR UNIVERSITY', 'LASUED IJANIKIN', "LASUSTECH", "FRENCH VILLAGE"] and not categories:
            accommodation = "Ground floor of the girls hostel to the right"
        elif school_key in ['LASU EPE', 'YABATECH EPE', 'LASUTH', 'LASUED EPE'] and not categories:
            accommodation = "1st floor of girls hostel to the left"
        elif school_key in ['FCE (TECH) AKOKA', 'SON, IGANDO', 'PROJECTIME', 'RADIOGRAPHY', "NOIC", "ORTHOPADIC IGBOBI", "FISHERIES", "LCP", "LAW SCHOOL"] and not categories:
            accommodation == "1st floor of the girls hostel to the right"
        elif school_key == 'NOUN' or school_key == 'FSTC':
            accommodation = "Left wing 2nd floor of the girls hostel"
        elif category_key == 'Choir' and gender == 'Female':
            accommodation = "Right wing 2nd floor of the girls hostel"
        elif category_key == 'Corper' and gender == 'Female':
            accommodation = "Left wing 2nd floor of the girls hostel"
        elif category_key == 'Planning Committe':
            accommodation = "White House"
        elif category_key == 'Principal Officer':
            accommodation = "White House"
        elif category_key == 'Associate Coordinator':
            accommodation = "Bethel 4"
        elif category_key == 'Others (Graduate, Postgraduate, etc.)':
            accommodation = "Common Room"
        elif category_key == 'Student' and school_key in ['UNILAG', 'LUTH', 'YABATECH', 'LASU OJO']:
            accommodation = "Ground floor of the girl's hostel to the left"
        elif category_key == 'Student' and school_key in ['ANCHOR UNIVERSITY', 'LASUED IJANIKIN', "LASUSTECH", "FRENCH VILLAGE"]:
            accommodation = "Ground floor of the girls hostel to the right"
        elif category_key == 'Student' and school_key in ['LASU EPE', 'YABATECH EPE', 'LASUTH', 'LASUED EPE']:
            accommodation = "1st floor of girls hostel to the left"
        elif category_key == 'Student' and school_key in ['FCE (TECH) AKOKA', 'SON, IGANDO', 'PROJECTIME', 'RADIOGRAPHY', "NOIC", "ORTHOPADIC IGBOBI", "FISHERIES", "LCP", "LAW SCHOOL"] and not categories:
            accommodation == "1st floor of the girls hostel to the right"           
            

    return accommodation
#working code


# def assign_hostel(participant):
#     # Define your hostel assignment logic here
#     # For example, you can use if-else statements or a switch-case based on the participant's category, group, campus, and gender

#     if participant.category == 'Planning Committe':
#         participant.hostel = 'Hostel A'
#     elif participant.category == 'Associate Coordinator':
#         participant.hostel = 'Hostel B'
#     # Add more conditions or cases as needed
#         accommodation = "Unknown"

#     if participant.campus in ['Unilag', 'LUTH', 'Yabatech', 'LASU Ojo']:
#         accommodation = "Chalet 3 beside MHA after the GS lodge"
#     elif participant.campus == 'ANCHOR':
#         accommodation = "1st part of junior dormitory i.e the bungalow building"
#     elif participant.campus in ['LASUED Ijanikin', 'French village'] and not girls_hostel:
#         accommodation = "Ground floor of boys Hostel to the right"
#     elif participant.campus in ['LASUSTECH', 'LASU Epe'] and not girls_hostel:
#         accommodation = "Ground floor of boys Hostel to the left"
#     elif participant.campus in ['Yabatech Epe', 'LASUTH', 'LASUED Epe'] and not girls_hostel:
#         accommodation = "1st floor of the boys Hostel to the right"
#     elif participant.campus in ['FCE(T)', 'SON', 'Igando', 'Projectime', 'Radiography', 'NOIC', 'Orthopaedic', 'LCP', 'law school Fisheries'] and not girls_hostel:
#         accommodation = "1st floor of the boys Hostel to the left"
#     elif participant.campus == 'Corpers' or group_key == 'Staff of tertiary institutions' or group_key == 'Noun' or group_key == 'NASFA' or group_key == 'FSTC':
#         accommodation = "Left wing 2nd floor of the boys Hostel"
#     elif participant.campus == 'Choir':
#         accommodation = "Right wing 2nd floor of the boys Hostel"
#     elif participant.campus == "Female":
#         if participant.campus in ['Unilag', 'LUTH', 'Yabatech', 'LASU Ojo']:
#             accommodation = "Ground floor of the girl's hostel to the left"
#         elif participant.campus in ['ANCHOR', 'LASUED Ijanikin', 'French village']:
#             accommodation = "Ground floor of the girls hostel to the right"
#         elif participant.campus in ['LASU Epe', 'Yabatech Epe', 'LASUTH', 'LASUED Epe']:
#             accommodation = "1st floor of girls Hostel to the left"
#         elif participant.campus in ['FCE(T)', 'SON', 'Igando', 'Projectime', 'Radiography', 'NOIC', 'Orthopaedic', 'LCP', 'law school Fisheries']:
#             accommodation = "1st floor of the girls Hostel to the right"
#         elif participant.campus == 'Corpers' or participant.campus == 'Staff of tertiary institutions' or group_key == 'Noun' or group_key == 'NASFA' or group_key == 'FSTC':
#             accommodation = "Left wing 2nd floor of the girls Hostel"
#         elif participant.campus == 'Choir':
#             accommodation = "Right wing 2nd floor of the girls Hostel"

#     return accommodation

#     # Save the assigned hostel to the database
#     db.session.commit()

#     return participant.hostel


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        surname = request.form['surname']
        category = request.form['category']
        group = request.form['group']
        if group == 'other':
            group = request.form['other_group']
            
        campus = request.form['campus']
        if campus == 'other':
            campus = request.form['other_campus']        
        
        areYouAworker = request.form['areYouAworker']
        address = request.form['address']
        emailAddress = request.form['emailAddress']
        whatsapp = request.form['whatsapp']
        participant_type = request.form['participant_type']
        gender = request.form['gender']
        ageBracket = request.form['ageBracket']

        # Save the form data to the Participant table
        new_participant = Participant(
            title=title,
            first_name=first_name,
            surname=surname,
            category=category,
            group=group,
            campus=campus,
            areYouAworker=areYouAworker,
            address=address,
            emailAddress=emailAddress,
            whatsapp=whatsapp,
            participant_type=participant_type,
            gender=gender,
            ageBracket=ageBracket
        )

        db.session.add(new_participant)
        db.session.commit()

        return redirect(url_for('view_hostel', participant_id=new_participant.id))

    return render_template('form.html')


@app.route('/view-hostel/', methods=['GET', 'POST'])
def view_hostel():
    participant_id = request.args.get('participant_id')
    
    if participant_id:
        participant = Participant.query.get(participant_id)
        if participant:
            # Determine accommodation based on gender, school, and group
            accommodation = determine_accommodation(participant.gender, participant.campus, participant.category)
            # Update participant's hostel with the determined accommodation
            print(participant.gender, participant.campus, participant.category)
            participant.hostel = accommodation
            db.session.commit()
            
            return render_template('view_hostel.html', participant=participant)
      
    return redirect(url_for('index'))




# @app.route('/view-hostel/', methods=['GET', 'POST'])
# def view_hostel():
#     participant_id = request.args.get('participant_id')
    
#     if participant_id:
#         participant = Participant.query.get(participant_id)
#         if participant:
#             return render_template('view_hostel.html', participant=participant)
      
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)