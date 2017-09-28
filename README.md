# MONTAGE

## Initial Setup

1. git clone --recursive https://github.com/NGS2Montage/montage.git

2. Navigate into the project folder, then create an rsa key pair:
    ```
    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out private.pem
    openssl rsa -in private.pem -outform PEM -pubout -out public.pem
    ```
3. Start a virtual environment

  a.
  ```
  apt-get install python3-venv
  ```
  b.
  ```
  python3 -m venv env
  ```
  c.
  ```
   . ./env/bin/activate
  ```

4. You should see (env) at prompt, then run:
    ```
    pip3 install -r requirements.txt
    ```  
5. Now apply settings.  To do this
    ```
    - Copy `django_montage/local_settings.py.example` to
       `django_montage/local_settings.py`.
    - Add any configuration settings to
       `local_settings.py`.
    - If not connecting to Postgres, comment out that entire section from this file.
    ```
6. Apply these migrations with:
    ```
    python3 manage.py migrate
    ```

7. Start the server with:
    ```
    python3 manage.py runserver
    ```

8. Create a superuser `admin` with `python manage.py createsuperuser`.  This will allow for administrator account approval.

## API

[Read about the API here](https://github.com/NGS2Montage/montage/blob/master/rafter_user_service/models/README.md).

It might be convenient for development to load some initial model data with `./manage.py loaddata rafter_user_service/initial_data.json`


## Configuration
Configuration is described in [`/django_montage/README.md`](https://github.com/NGS2Montage/montage/blob/master/django_montage/README.md).


## Ongoing development

1. . ./env/bin/activate
2. python3 manage.py runserver

## If db KeyError Occurs

1. Delete the db.sqlite3 file
2. `git status` and make sure that nothing in rafter_user_service/migrations<br>
has changed. If so, remove/replace.   
2. `. ./env/bin/activate`
3. `python3 manage.py migrate`
4. `python3 manage.py runserver`
5. Recreate your super admin account.
