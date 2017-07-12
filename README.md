MONTAGE
=======

To install:
1. First create an rsa key pair:
    ```
    ssh-keygen -t rsa -b 4096 -f private.pem 
    openssl rsa -in private.pem -outform PEM -pubout -out public.pem
    ```
2. Start a virtual environment
3. Then run: 
    ```
    pip install -r requirements.txt
    ```  
4. Apply these migrations with:
    ```
    python manage.py migrate
    ```
5. Then you can start the server with:
    ```
    python manage.py runserver
    ```

You should also make a superuser `admin` with `python manage.py createsuperuser`.  This will allow for administrator account approval.
