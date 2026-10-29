# Django User Login Project

A beginner-friendly Django login project with a separate CSS file.

## Requirements
- Python 3.10+
- pip

## Setup on Windows PowerShell

Open PowerShell in this folder and run:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and log in with the user credentials you created.

## Notes
- The project uses Django's built-in authentication.
- Passwords are stored using Django's password hashing, not as plain text.
- `DEBUG = True` and the sample secret key are for local development only.
- Do not deploy this configuration publicly without setting a secure secret key and `DEBUG = False`.
