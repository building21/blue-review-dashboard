import csv

from django.core.exceptions import ValidationError

from application.models import Application

def handle_application_csv(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        try:
            email = row[0]
            date_commitment = True if row[1] == "1" else False
            name = row[2]
            faculty = row[3]
            other_faculty = row[4]
            project_name = row[5]
            idea = row[6]
            fit_for_blue = row[7]
            media_link = row[8]
            country = row[9]
            year = row[10]
            valid = True
            application = Application(email=email,
                    date_commitment=date_commitment,
                    name=name,
                    faculty=faculty,
                    other_faculty=other_faculty,
                    project_name=project_name,
                    idea=idea,
                    fit_for_blue=fit_for_blue,
                    media_link=media_link,
                    country=country,
                    year=year,
                    valid=valid)
            application.full_clean()
        except ValidationError as e:
            """Fields are not valid."""
            return True, "The csv fields are not valid."
        else:
            application.save()

    return False, "Uploaded applications"
