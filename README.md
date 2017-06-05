MONTAGE
=======

To install, start a virtual environment, then run `pip install -r
requirements.txt`.  Then create migrations with `python manage.py
makemigrations`.  Apply these migrations with `python manage.py migrate`.  Then
you can start the server with `python manage.py runserver`.  You should also
make a superuser `admin` with `python manage.py createsuperuser`.  This will
allow for administrator accont approval.
