## Employee

Simple Django Web App to implement CRUD operations referenced from [Django CRUD](https://www.youtube.com/watch?v=N6jzspc2kds) while extending it to implement charting using [HighCharts](https://www.highcharts.com).

### Setting Environment

1. Install and setup python with paths.
2. Open terminal(command prompt) and run the following commands:
    1. pip install django.
    2. pip install django-crispy-forms.
3. The database is set in SQLite, which is default for Django.
4. Database setup:
    1. Download and install [SqLite DB Browser](https://sqlitebrowser.org/).
    2. Tables present:
        1. *register_employee* - Entries inserted using the app.
        2. *register_position* - Inserted with dummy entries to be referenced with *register_employee*.
    3. Open the DB Browser and open connection to *db.sqlite3* database in the project to refer to the tables.

### Usage

1. Open terminal and go to the project location.
2. Run command: python manage.py runserver.
3. Open browser and hit **localhost:8000/employee** to use the app.
