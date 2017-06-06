MONTAGE
=======

To install:
1. Start a virtual environment
2. Then run: 
    ```
    pip install -r requirements.txt
    ```  
3. Apply these migrations with:
    ```
    python manage.py migrate
    ```
4. Then you can start the server with:
    ```
    python manage.py runserver
    ```

You should also make a superuser `admin` with `python manage.py createsuperuser`.  This will allow for administrator account approval.
