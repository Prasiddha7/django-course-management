# coursemanagemnt
1. Clone this repo from github
    https://github.com/Prasiddha7/django-course-management.git

2. Create a virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Apply database migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Create SuperUser to access admin pannel.
    python manage.py createsuperuser

6. Run the development server:
    python manage.py runserver

7. Access the application.
    Open a browser and navigate to http://localhost:8000.

    To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

    To access the dashboard, go to http://127.0.0.1:8000/dashboard/ 

