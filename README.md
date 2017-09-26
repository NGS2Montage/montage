# MONTAGE

To install:

1. First create an rsa key pair:
    ```
    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out private.pem
    openssl rsa -in private.pem -outform PEM -pubout -out public.pem
    ```
2. Start a virtual environment

  a.
  ```
  apt-get install python3-venv
  ```
  b.
  ```
  python3 -m venv env
  ```
  c. open a new terminal into /montage/env/bin
  d. . ./env/bin/activate
  ```
  source activate
  ```
3. From the other terminal, run:
    ```
    pip3 install -r requirements.txt
    ```  
4. Apply these migrations with:
    ```
    python3 manage.py migrate
    ```
5. Now apply settings.  To do this
  * copy `django_montage/local_settings.py.example` to
   `django_montage/local_settings.py`.
   * Now, add any configuration settings to
   `local_settings.py`.
   * If not connecting to the database, delete that entire section from file.

6. Then you can start the server with:
    ```
    python3 manage.py runserver
    ```

You should also make a superuser `admin` with `python manage.py createsuperuser`.  This will allow for administrator account approval.

## API

[Read about the API here](https://github.com/NGS2Montage/montage/blob/master/rafter_user_service/models/README.md).

It might be convenient for development to load some initial model data with `./manage.py loaddata rafter_user_service/initial_data.json`


## Configuration
Configuration is described in [`/django_montage/README.md`](https://github.com/NGS2Montage/montage/blob/master/django_montage/README.md).
