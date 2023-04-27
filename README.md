# Recipe App API (v2) Source Code

This is the code for the second edition of the course that was released in 2022.

Course code for: [Build a Backend REST API with Python &amp; Django - Advanced](https://londonapp.dev/c2)


# Setting github action job
https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment


# Add SimpleJWT token
```
  curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "member1@gmail.com", "password": "12345"}' \
  http://localhost:8880/api/token/
```


# Log changed DB
https://django-auditlog.readthedocs.io/en/latest/usage.html

# Move data
Create a new PostgreSQL database and update the DATABASES configuration in your settings.py file to use the new database.

Use Django's inspectdb management command to generate models for your existing MSSQL database. This will create a new set of models that are compatible with the PostgreSQL database.


``` python manage.py inspectdb > models.py```
Update the generated models to fix any issues with data types or other incompatibilities between MSSQL and PostgreSQL. For example, PostgreSQL uses serial fields instead of IDENTITY columns for auto-incrementing primary keys.

Run the Django migration tool to create the tables in the new PostgreSQL database:


``` python manage.py makemigrations```
``` python manage.py migrate ```
This will create all the necessary tables in the new PostgreSQL database, based on the updated models.

Use Django's dumpdata management command to export the data from the old MSSQL database in a format that can be imported into the new PostgreSQL database:


``` python manage.py dumpdata --natural-primary --database=himalaya --exclude admin.LogEntry --exclude auth.Permission --exclude contenttypes --exclude auth.Group --exclude sessions.Session --exclude authtoken.Token > data.json```
This command will export all the data from the MSSQL database to a JSON file named data.json, excluding the contenttypes and auth.Permission tables which can cause issues.

Use Django's loaddata management command to import the data from the JSON file into the new PostgreSQL database:

``` python manage.py loaddata data.json ```
This command will import all the data from the JSON file into the new PostgreSQL database.

Finally, test your application thoroughly to ensure that everything is working as expected.


SysQuyen
Sysdiagrams